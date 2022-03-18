import sys
from enum import Enum
from typing import Optional, List

import mysql.connector
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QFileDialog
from gui.main_widget.ui_to_py.wsl_analytics_ui import Ui_MainWindow
from gui.common_widget.dialog_widget.simple_lineedit import SimpleLineEdit

########################################################################################################################
# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="Heather",
  password="#LAwaItly19"
)

# mycursor = mydb.cursor()
# mycursor.execute("select * from wsl.continents")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)


########################################################################################################################
# Define Places
class Places:
    @staticmethod
    def Continent():
        mycursor = mydb.cursor()
        mycursor.execute("select continent from wsl.continents")
        result = mycursor.fetchall()

        cont_lst = []
        for x in result:
            cont_lst.append(x)

        return cont_lst

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
# Add Location Button
class AddLocation:
    @staticmethod
    def addlocation(Continent='', Country='', Region='', City=''):
        dialog = SimpleLineEdit(title="Title")
        if dialog.exec() == QDialog.Accepted:
            # Error if any piece is blank
            try:
                if Country == '':
                    raise Exception("Empty Country, Dummy Bunny!")
                if Region == '':
                    raise Exception("Empty Region, Dummy Bunny!")
                if City == '':
                    raise Exception("Empty City, Dummy Bunny!")
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

########################################################################################################################
class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    # This defines the event handlers for everything.
    def connect_slots(self):
        # Slots for Break Tab
        self.BreakContCb.currentIndexChanged.connect(self.slot_breakcontcb_on_index_change)
        self.BreakCountryCb.currentIndexChanged.connect(self.slot_breakcountrycb_on_index_change)
        self.BreakRegionCb.currentIndexChanged.connect(self.slot_breakregioncb_on_index_change)
        self.addlocationbutton.clicked.connect(self.slot_addloc_on_clicked)
        self.BreakSubmit.clicked.connect(self.slot_breaksubmit_on_clicked)

        # Slots for Bio Tab
        self.BioAddlocbutton.clicked.connect(self.slot_bioaddlocbut_on_clicked)
        self.BioAddimagebut.clicked.connect(self.slot_bioaddimage_on_clicked)
        self.BioSubmitBut.clicked.connect(self.slot_biosubmit_on_clicked)

    ####################################################################################################################
    # Event Handlers for Breaks Tab

    # This setups up everything at the first startup.
    def on_startup(self):
        # Add Continents to the combobox.
        self.BreakContCb.addItems(
            [item[0] for item in Places.Continent()]
        )

    # This is the event handler (slot) for the combobox "breakcontcb" changing index.
    def slot_breakcontcb_on_index_change(self):
        if self.BreakContCb.currentText() == "Africa":
            # Clear the Countries Combobox.
            self.BreakCountryCb.clear()
            # Add the countries.
            self.BreakCountryCb.addItems(
                [item.name for item in Places.Africa]
            )
        elif self.BreakContCb.currentText() == "North_America":
            # Clear the Countries Combobox.
            self.BreakCountryCb.clear()
            # Add the countries.
            self.BreakCountryCb.addItems(
                [item.name for item in Places.NorthAmerica]
            )

    # This is the event handler (slot) for the combobox "breakcountrycb" changing index.
    def slot_breakcountrycb_on_index_change(self):
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
    def slot_breakregioncb_on_index_change(self):
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

    # Event Handler for clicking add location buttun on break tab
    def slot_addloc_on_clicked(self):
        AddLocation.addlocation()

    # This is the event handler (slot) for the submit button being clicked.
    def slot_breaksubmit_on_clicked(self):
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
    # Event Handlers for Bio Tab


    # Event Handler for clicking add location button on bio tab
    def slot_bioaddlocbut_on_clicked(self):
        AddLocation.addlocation()

    # Event Handler for opeing images
    def slot_bioaddimage_on_clicked(self):
        pass

    # Bio Tab Submit
    def slot_biosubmit_on_clicked(self):
        pass



########################################################################################################################
if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())