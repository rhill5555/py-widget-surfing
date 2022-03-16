import sys
from enum import Enum

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from gui.main_widget.ui_to_py.wsl_analytics_ui import Ui_MainWindow


class Places:
    class Continent(Enum):
        Africa = 1
        North_America = 2

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
        self.BreakContCb.currentIndexChanged.connect(self.slot_breakcontcb_on_index_change)
        self.BreakCountryCb.currentIndexChanged.connect(self.slot_breakcountrycb_on_index_change)
        self.BreakRegionCb.currentIndexChanged.connect(self.slot_breakregioncb_on_index_change)
        self.BreakSubmit.clicked.connect(self.slot_breaksubmit_on_clicked)


    # This setups up everything at the first startup.
    def on_startup(self):
        # Add Continents to the combobox.
        self.BreakContCb.addItems(
            [item.name for item in Places.Continent]
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

    # This is the event handler (slot) for the submit button being clicked.
    def slot_breaksubmit_on_clicked(self):
        if self.BreakBurnLight.isChecked():
            print('Light')
        elif self.BreakBurnMed.isChecked():
            print('Medium')
        elif self.BreakBurnEx.isChecked():
            print('Exhausting')

        if self.

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())