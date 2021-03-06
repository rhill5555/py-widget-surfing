# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\py-widget-surfing\gui\main_widget\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 850)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("")
        self.top_message = QtWidgets.QLabel(Form)
        self.top_message.setGeometry(QtCore.QRect(140, 50, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.top_message.setFont(font)
        self.top_message.setStyleSheet("color: rgb(1, 94, 152);")
        self.top_message.setObjectName("top_message")
        self.cont_lbl = QtWidgets.QLabel(Form)
        self.cont_lbl.setGeometry(QtCore.QRect(50, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cont_lbl.setFont(font)
        self.cont_lbl.setStyleSheet("#cont_lbl{color: #3d4446}")
        self.cont_lbl.setObjectName("cont_lbl")
        self.count_lbl = QtWidgets.QLabel(Form)
        self.count_lbl.setGeometry(QtCore.QRect(50, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_lbl.setFont(font)
        self.count_lbl.setStyleSheet("#count_lbl{color: #3d4446}")
        self.count_lbl.setObjectName("count_lbl")
        self.cont_entry = QtWidgets.QComboBox(Form)
        self.cont_entry.setGeometry(QtCore.QRect(180, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cont_entry.setFont(font)
        self.cont_entry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(61, 68, 70);")
        self.cont_entry.setObjectName("cont_entry")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry.addItem("")
        self.cont_entry_2 = QtWidgets.QComboBox(Form)
        self.cont_entry_2.setGeometry(QtCore.QRect(180, 180, 181, 21))
        self.cont_entry_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(61, 68, 70);")
        self.cont_entry_2.setObjectName("cont_entry_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 700, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(1, 94, 152);\n"
"color: rgb(216, 243, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.top_message.setText(_translate("Form", "Enter Break Information"))
        self.cont_lbl.setText(_translate("Form", "Continent:"))
        self.count_lbl.setText(_translate("Form", "Country:"))
        self.cont_entry.setItemText(0, _translate("Form", "North America"))
        self.cont_entry.setItemText(1, _translate("Form", "South America"))
        self.cont_entry.setItemText(2, _translate("Form", "Africa"))
        self.cont_entry.setItemText(3, _translate("Form", "Europe"))
        self.cont_entry.setItemText(4, _translate("Form", "Asia"))
        self.cont_entry.setItemText(5, _translate("Form", "Australia"))
        self.cont_entry.setItemText(6, _translate("Form", "Oceania"))
        self.pushButton.setText(_translate("Form", "Submit!"))
