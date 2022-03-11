import sys

from PyQt5.QtWidgets import QWidget, QApplication

from gui.main_widget.ui_to_py.test import Ui_Form


class MainWidget(QWidget, Ui_Form):
    def __init__(self):
        # Call the constructor for the inherited QWidget class.
        QWidget.__init__(self)

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())