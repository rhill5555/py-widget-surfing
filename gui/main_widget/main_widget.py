import sys
from enum import Enum
from typing import Optional, List

import mysql.connector
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QFileDialog
from mysql.connector import MySQLConnection

from gui.main_widget.ui_to_py.wsl_analytics_ui import Ui_MainWindow
from gui.common_widget.dialog_widget.simple_lineedit import SimpleLineEdit

########################################################################################################################

# mycursor = mydb.cursor()
# mycursor.execute("select * from wsl.continents")
# myresult = mycursor.fetchall()

########################################################################################################################
# Define Places
class Places:
    @staticmethod
    def continent(mysql_connection: MySQLConnection):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select continent from wsl.continents")
        result = mycursor.fetchall()

        cont_lst = []
        for x in result:
            cont_lst.append(x)

        return cont_lst

    @staticmethod
    def countries(mysql_connection: MySQLConnection, continent: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select country.country
                         from wsl.countries country
                         join wsl.continents cont
                              on country.continent_id = cont.id
                         where cont.continent = '{continent}'""")
        result = mycursor.fetchall()

        country_lst = []
        for x in result:
            country_lst.append(x)

        return country_lst

    @staticmethod
    def region(mysql_connection: MySQLConnection, country: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select region from wsl.regions")
        result = mycursor.fetchall()

        region_lst = []
        for x in result:
            region_lst.append(x)

        return region_lst

    @staticmethod
    def city(mysql_connection: MySQLConnection, region: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select city from wsl.continents")
        result = mycursor.fetchall()

        city_lst = []
        for x in result:
            city_lst.append(x)

        return city_lst

    @staticmethod
    def surf_break(mysql_connection: MySQLConnection, city: str):
        pass

    class Africa(Enum):
        Eastern_Cape = ["Eastern_Cape"]

    class NorthAmerica(Enum):
        USA = ["Hawaii", "California"]
        Mexico = ["Ox"]

    class Hawaii(Enum):
        PipeLine = 1
        Sunset_Beach = 2

    class California(Enum):
        San_Clemente = 1
        Hunting_Beach = 2

    class Ox(Enum):
        Ox_beach = 1

    class Eastern_Cape(Enum):
        Jeffreys_Bay = 1


########################################################################################################################
class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, sql_host: str, sql_user: str, sql_password: str):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)


        # Sql Connection Info and mysql connection
        self.__sql_host: str = sql_host
        self.__sql_user: str = sql_user
        self.__sql_password: str = sql_password
        self.__mysql_connection: Optional[MySQLConnection] = None

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    @property
    def mysql(self) -> MySQLConnection:
        # Connect to MySQL
        if self.__mysql_connection is None:
            self.__mysql_connection = mysql.connector.connect(
                host=self.__sql_host,
                user=self.__sql_user,
                password=self.__sql_password
            )
        return self.__mysql_connection

    # This defines the event handlers for everything.
    def connect_slots(self):
        # Slots for Break Tab
        self.BreakContCb.currentIndexChanged.connect(self.slot_break_cont_cb_on_index_change)
        self.BreakCountryCb.currentIndexChanged.connect(self.slot_break_country_cb_on_index_change)
        self.BreakRegionCb.currentIndexChanged.connect(self.slot_break_region_cb_on_index_change)
        self.addlocationbutton.clicked.connect(self.slot_add_location_btn_on_clicked)
        self.BreakSubmit.clicked.connect(self.slot_break_submit_on_clicked)

        # Slots for Bio Tab
        self.BioAddlocbutton.clicked.connect(self.slot_add_location_btn_on_clicked)
        self.BioAddimagebut.clicked.connect(self.slot_bio_add_image_on_clicked)
        self.BioSubmitBut.clicked.connect(self.slot_bio_submit_on_clicked)

    # This setups up everything at the first startup.
    def on_startup(self):
        # Add Continents to the combobox.
        self.BreakContCb.addItems(
            [item[0] for item in Places.continent(mysql_connection=self.mysql)]
        )

    # Eventhandler for any button that adds a location to the database.
    @staticmethod
    def slot_add_location_btn_on_clicked():
        dialog = SimpleLineEdit(title="Add a location to the database.")
        if dialog.exec() == QDialog.Accepted:
            # Error if any piece is blank
            try:
                Continent = dialog.Cont_Cb.currentText()
                print(Continent)
                Country = dialog.Country_LineEdit.text()
                print(Country)
                Region = dialog.Region_LineEdit.text()
                print(Region)
                City = dialog.City_LineEdit.text()
                print(City)
            except Exception:
                print('Something was blank, dummy bunny!')

    ####################################################################################################################
    # Event Handlers for Breaks Tab

    # This is the event handler (slot) for the combobox "breakcontcb" changing index.
    def slot_break_cont_cb_on_index_change(self):
        self.BreakCountryCb.clear()
        self.BreakCountryCb.addItems([item[0] for item in Places.countries(mysql_connection=self.mysql, continent=self.BreakContCb.currentText())])

    # This is the event handler (slot) for the combobox "breakcountrycb" changing index.
    def slot_break_country_cb_on_index_change(self):
        if self.BreakCountryCb.currentText() == "Eastern_Cape":
            # Clear the Region Combobox.
            self.BreakRegionCb.clear()
            # Add the regions.
            self.BreakRegionCb.addItems(
                Places.Africa.Eastern_Cape.value
            )
        elif self.BreakCountryCb.currentText() == "USA":
            # Clear the Region Combobox.
            self.BreakRegionCb.clear()
            # Add the regions.
            self.BreakRegionCb.addItems(
                Places.NorthAmerica.USA.value
            )
        elif self.BreakCountryCb.currentText() == "Mexico":
            # Clear the Region Combobox.
            self.BreakRegionCb.clear()
            # Add the regions.
            self.BreakRegionCb.addItems(
                Places.NorthAmerica.Mexico.value
            )

    # This is the event handler (slot) for the combobox "breakregioncb" changing index.
    def slot_break_region_cb_on_index_change(self):
        if self.BreakRegionCb.currentText() == "Eastern_Cape":
            # Clear the City Combobox.
            self.BreakCityCb.clear()
            # Add the regions.
            self.BreakCityCb.addItems(
                [item.name for item in Places.Eastern_Cape]
            )
        elif self.BreakRegionCb.currentText() == "California":
            # Clear the City Combobox.
            self.BreakCityCb.clear()
            # Add the regions.
            self.BreakCityCb.addItems(
                [item.name for item in Places.California]
            )
        elif self.BreakRegionCb.currentText() == "Hawaii":
            # Clear the City Combobox.
            self.BreakCityCb.clear()
            # Add the regions.
            self.BreakCityCb.addItems(
                [item.name for item in Places.Hawaii]
            )
        elif self.BreakRegionCb.currentText() == "Ox":
            # Clear the City Combobox.
            self.BreakCityCb.clear()
            # Add the regions.
            self.BreakCityCb.addItems(
                [item.name for item in Places.Ox]
            )

    # This is the event handler (slot) for the submit button being clicked.
    def slot_break_submit_on_clicked(self):
        def breaktypelst(*args):
            tempbreaklst = []
            if self.BreakBeachBox.isChecked():
                tempbreaklst.append('Beach')
            if self.BreakPointBox.isChecked():
                tempbreaklst.append('Point')
            if self.BreakReefBox.isChecked():
                tempbreaklst.append('Reef')
            if self.BreakRiverBox.isChecked():
                tempbreaklst.append('River')
            if self.BreakEngBox.isChecked():
                tempbreaklst.append('Engineered')
            return tempbreaklst

        breakCont = self.BreakContCb.currentText()
        print(breakCont)

        breakCountry = self.BreakCountryCb.currentText()
        print(breakCountry)

        breakRegion = self.BreakRegionCb.currentText()
        print(breakRegion)

        breakCity = self.BreakCityCb.currentText()
        print(breakCity)

        breakName = self.BreakBreakEntry.text()
        print(breakName)

        breaktype = breaktypelst()
        print(breaktype)

        if self.BreakBurnLight.isChecked():
            breakburn = 'Light'
        elif self.BreakBurnMed.isChecked():
            breakburn = 'Medium'
        elif self.BreakBurnEx.isChecked():
            breakburn = 'Exhausting'
        print(breakburn)

    ####################################################################################################################

    # Event Handler for opening images
    def slot_bio_add_image_on_clicked(self):
        pass

    # Bio Tab Submit
    def slot_bio_submit_on_clicked(self):
        pass


########################################################################################################################
if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget(sql_host='localhost', sql_user='Heather', sql_password='#LAwaItly19')
    win.show()

    sys.exit(app.exec())