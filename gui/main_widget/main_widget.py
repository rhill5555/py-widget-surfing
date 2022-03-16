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

    def connect_slots(self):
        #self.cont_entry.currentIndexChanged.connect(self.slot_cont_entry_on_selection_change)
        pass

   # def slot_cont_entry_on_selection_change(self):
        #print(self.cont_entry.currentText())


if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())