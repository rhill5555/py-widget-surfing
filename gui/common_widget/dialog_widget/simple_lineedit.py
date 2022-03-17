import sys
from enum import Enum

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QApplication, QDialogButtonBox

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

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Continent Label and Combobox
        self.layout.addWidget(QLabel("Continent"))
        self.Cont_Cb = PyQt5.QtWidgets.QComboBox()
        self.layout.addWidget(self.Cont_Cb)
        self.Cont_Cb.clear()
        self.Cont_Cb.addItems(cont_lst)

        # Country Label and Line Edit
        self.layout.addWidget(QLabel("Country"))
        self.Country_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.layout.addWidget(self.Country_LineEdit)

        # Region Label and Line Edit
        self.layout.addWidget(QLabel("Region"))
        self.Region_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.layout.addWidget(self.Region_LineEdit)

        # City Label and Line Edit
        self.layout.addWidget(QLabel("City"))
        self.City_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.layout.addWidget(self.City_LineEdit)

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