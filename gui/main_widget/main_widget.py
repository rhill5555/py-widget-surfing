import sys
from src.place_hier import Places
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
    def slot_add_location_btn_on_clicked(self):
        dialog = SimpleLineEdit(title="Add a location to the database.", mysql_conn=self.mysql)
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

        # Add to continents table and raise exception if failed
        try:
            table = wsl.continents
            # Logic to add to table
        except Exception:
            print('Could not append data to wsl.continents')

    ####################################################################################################################
    # Event Handlers for Breaks Tab

    # This is the event handler (slot) for the combobox "breakcontcb" changing index.
    def slot_break_cont_cb_on_index_change(self):
        self.BreakCountryCb.clear()
        self.BreakCountryCb.addItems([item[0] for item in Places.countries(mysql_connection=self.mysql, continent=self.BreakContCb.currentText())])

    # This is the event handler (slot) for the combobox "breakcountrycb" changing index.
    def slot_break_country_cb_on_index_change(self):
        self.BreakRegionCb.clear()
        self.BreakRegionCb.addItems([item[0] for item in Places.region(mysql_connection=self.mysql,
                                                                          country=self.BreakCountryCb.currentText())])


    # This is the event handler (slot) for the combobox "breakregioncb" changing index.
    def slot_break_region_cb_on_index_change(self):
        self.BreakCityCb.clear()
        self.BreakCityCb.addItems([item[0] for item in Places.city(mysql_connection=self.mysql,
                                                                       region=self.BreakRegionCb.currentText())])

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