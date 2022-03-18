import sys
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QApplication, QDialogButtonBox

cont_lst = ['Africa',
            'Asia',
            'Europe',
            'North America',
            'Oceania',
            'South America']

class SimpleLineEdit(QDialog):
    def __init__(self, title, left=10, top=10, width=520, height=400, parent=None):
        # Calls constructor for QDialog
        super().__init__(parent=parent)

        # Set Title
        self.setWindowTitle(title)

        # Set Geometry
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Set parent widget
        if not (parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts
        self.HLayoutCont = QHBoxLayout()
        self.HLayoutCountry = QHBoxLayout()
        self.HLayoutReg = QHBoxLayout()
        self.HLayoutCity = QHBoxLayout()

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Continent Label and Combobox
        self.HLayoutCont.addWidget(QLabel("Continent:"))

        self.Cont_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutCont.addWidget(self.Cont_Cb)
        self.Cont_Cb.clear()
        self.Cont_Cb.addItems(cont_lst)
        self.Cont_Cb.setFixedWidth(200)

        self.HLayoutCont.addWidget(QLabel(''))

        self.layout.addLayout(self.HLayoutCont)

        # Country Label and Line Edit
        self.HLayoutCountry.addWidget(QLabel("Country:"))

        self.Country_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutCountry.addWidget(self.Country_Cb)
        self.Country_Cb.clear()
        #self.Country_Cb.addItems()
        self.Country_Cb.setFixedWidth(200)

        self.Country_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutCountry.addWidget(self.Country_LineEdit)
        self.Country_LineEdit.setFixedWidth(200)

        self.layout.addLayout(self.HLayoutCountry)

        # Region Label and Line Edit
        self.HLayoutReg.addWidget(QLabel("Region:"))

        self.Region_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutReg.addWidget(self.Region_Cb)
        self.Region_Cb.clear()
        # self.Region_Cb.addItems()
        self.Region_Cb.setFixedWidth(200)

        self.Region_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutReg.addWidget(self.Region_LineEdit)
        self.Region_LineEdit.setFixedWidth(200)

        self.layout.addLayout(self.HLayoutReg)


        # City Label and Line Edit
        self.HLayoutCity.addWidget(QLabel("City:"))
        self.City_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutCity.addWidget(self.City_LineEdit)
        self.City_LineEdit.setFixedWidth(200)
        self.HLayoutCity.addWidget(QLabel(''))
        self.layout.addLayout(self.HLayoutCity)

        Q_Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(Q_Btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SimpleLineEdit(title="Title")
    win.show()
    if win.exec() == QDialog.Accepted:
        print('Hello Bitches!')