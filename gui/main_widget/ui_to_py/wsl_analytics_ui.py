# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\py-widget-surfing\gui\main_widget\ui\wsl_analytics_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 900)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(3, 57, 108);\n"
"font: 10pt \"Verdana\";\n"
"border-color: rgb(1, 31, 75);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hLine4 = QtWidgets.QFrame(self.centralwidget)
        self.hLine4.setGeometry(QtCore.QRect(0, 0, 1100, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hLine4.sizePolicy().hasHeightForWidth())
        self.hLine4.setSizePolicy(sizePolicy)
        self.hLine4.setStyleSheet("background-color: rgb(1, 31, 75);")
        self.hLine4.setLineWidth(0)
        self.hLine4.setFrameShape(QtWidgets.QFrame.HLine)
        self.hLine4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hLine4.setObjectName("hLine4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"  background: #bae1ff;\n"
"  font-family: Papyrus;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: #c462fd;\n"
" }")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabSched = QtWidgets.QWidget()
        self.tabSched.setObjectName("tabSched")
        self.scheduleLabel = QtWidgets.QLabel(self.tabSched)
        self.scheduleLabel.setGeometry(QtCore.QRect(435, 60, 230, 71))
        self.scheduleLabel.setStyleSheet("font: 32pt Papyrus;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 98, 137);")
        self.scheduleLabel.setObjectName("scheduleLabel")
        self.SchedHLineYellow = QtWidgets.QFrame(self.tabSched)
        self.SchedHLineYellow.setGeometry(QtCore.QRect(0, 28, 1131, 4))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SchedHLineYellow.sizePolicy().hasHeightForWidth())
        self.SchedHLineYellow.setSizePolicy(sizePolicy)
        self.SchedHLineYellow.setStyleSheet("background-color: #bae1ff;")
        self.SchedHLineYellow.setLineWidth(0)
        self.SchedHLineYellow.setFrameShape(QtWidgets.QFrame.HLine)
        self.SchedHLineYellow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SchedHLineYellow.setObjectName("SchedHLineYellow")
        self.SchedHLinePurp = QtWidgets.QFrame(self.tabSched)
        self.SchedHLinePurp.setGeometry(QtCore.QRect(0, 16, 1131, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SchedHLinePurp.sizePolicy().hasHeightForWidth())
        self.SchedHLinePurp.setSizePolicy(sizePolicy)
        self.SchedHLinePurp.setStyleSheet("background-color: rgb(196, 98, 253);\n"
"color: rgb(196, 98, 253);")
        self.SchedHLinePurp.setLineWidth(0)
        self.SchedHLinePurp.setFrameShape(QtWidgets.QFrame.HLine)
        self.SchedHLinePurp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SchedHLinePurp.setObjectName("SchedHLinePurp")
        self.SchedHLinePink = QtWidgets.QFrame(self.tabSched)
        self.SchedHLinePink.setGeometry(QtCore.QRect(0, 0, 1131, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SchedHLinePink.sizePolicy().hasHeightForWidth())
        self.SchedHLinePink.setSizePolicy(sizePolicy)
        self.SchedHLinePink.setStyleSheet("background-color: rgb(255, 0, 129);")
        self.SchedHLinePink.setLineWidth(0)
        self.SchedHLinePink.setFrameShape(QtWidgets.QFrame.HLine)
        self.SchedHLinePink.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SchedHLinePink.setObjectName("SchedHLinePink")
        self.tabWidget.addTab(self.tabSched, "")
        self.tabSurfer = QtWidgets.QWidget()
        self.tabSurfer.setObjectName("tabSurfer")
        self.SurferHLinePink = QtWidgets.QFrame(self.tabSurfer)
        self.SurferHLinePink.setGeometry(QtCore.QRect(0, 0, 1131, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SurferHLinePink.sizePolicy().hasHeightForWidth())
        self.SurferHLinePink.setSizePolicy(sizePolicy)
        self.SurferHLinePink.setStyleSheet("background-color: rgb(255, 0, 129);")
        self.SurferHLinePink.setLineWidth(0)
        self.SurferHLinePink.setFrameShape(QtWidgets.QFrame.HLine)
        self.SurferHLinePink.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SurferHLinePink.setObjectName("SurferHLinePink")
        self.scheduleLabel_3 = QtWidgets.QLabel(self.tabSurfer)
        self.scheduleLabel_3.setGeometry(QtCore.QRect(459, 60, 182, 71))
        self.scheduleLabel_3.setStyleSheet("font: 32pt Papyrus;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 98, 137);")
        self.scheduleLabel_3.setObjectName("scheduleLabel_3")
        self.SurferHLineYellow = QtWidgets.QFrame(self.tabSurfer)
        self.SurferHLineYellow.setGeometry(QtCore.QRect(0, 28, 1131, 4))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SurferHLineYellow.sizePolicy().hasHeightForWidth())
        self.SurferHLineYellow.setSizePolicy(sizePolicy)
        self.SurferHLineYellow.setStyleSheet("background-color: #bae1ff;")
        self.SurferHLineYellow.setLineWidth(0)
        self.SurferHLineYellow.setFrameShape(QtWidgets.QFrame.HLine)
        self.SurferHLineYellow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SurferHLineYellow.setObjectName("SurferHLineYellow")
        self.SurferHLinePurp = QtWidgets.QFrame(self.tabSurfer)
        self.SurferHLinePurp.setGeometry(QtCore.QRect(0, 16, 1131, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SurferHLinePurp.sizePolicy().hasHeightForWidth())
        self.SurferHLinePurp.setSizePolicy(sizePolicy)
        self.SurferHLinePurp.setStyleSheet("background-color: rgb(196, 98, 253);\n"
"color: rgb(196, 98, 253);")
        self.SurferHLinePurp.setLineWidth(0)
        self.SurferHLinePurp.setFrameShape(QtWidgets.QFrame.HLine)
        self.SurferHLinePurp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SurferHLinePurp.setObjectName("SurferHLinePurp")
        self.tabWidget.addTab(self.tabSurfer, "")
        self.tabAna = QtWidgets.QWidget()
        self.tabAna.setObjectName("tabAna")
        self.AnaHLineYellow = QtWidgets.QFrame(self.tabAna)
        self.AnaHLineYellow.setGeometry(QtCore.QRect(0, 28, 1131, 4))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnaHLineYellow.sizePolicy().hasHeightForWidth())
        self.AnaHLineYellow.setSizePolicy(sizePolicy)
        self.AnaHLineYellow.setStyleSheet("background-color: #bae1ff;")
        self.AnaHLineYellow.setLineWidth(0)
        self.AnaHLineYellow.setFrameShape(QtWidgets.QFrame.HLine)
        self.AnaHLineYellow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AnaHLineYellow.setObjectName("AnaHLineYellow")
        self.AnaHLinePurp = QtWidgets.QFrame(self.tabAna)
        self.AnaHLinePurp.setGeometry(QtCore.QRect(0, 16, 1131, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnaHLinePurp.sizePolicy().hasHeightForWidth())
        self.AnaHLinePurp.setSizePolicy(sizePolicy)
        self.AnaHLinePurp.setStyleSheet("background-color: rgb(196, 98, 253);\n"
"color: rgb(196, 98, 253);")
        self.AnaHLinePurp.setLineWidth(0)
        self.AnaHLinePurp.setFrameShape(QtWidgets.QFrame.HLine)
        self.AnaHLinePurp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AnaHLinePurp.setObjectName("AnaHLinePurp")
        self.AnaHLinePink = QtWidgets.QFrame(self.tabAna)
        self.AnaHLinePink.setGeometry(QtCore.QRect(0, 0, 1131, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnaHLinePink.sizePolicy().hasHeightForWidth())
        self.AnaHLinePink.setSizePolicy(sizePolicy)
        self.AnaHLinePink.setStyleSheet("background-color: rgb(255, 0, 129);")
        self.AnaHLinePink.setLineWidth(0)
        self.AnaHLinePink.setFrameShape(QtWidgets.QFrame.HLine)
        self.AnaHLinePink.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AnaHLinePink.setObjectName("AnaHLinePink")
        self.scheduleLabel_4 = QtWidgets.QLabel(self.tabAna)
        self.scheduleLabel_4.setGeometry(QtCore.QRect(379, 60, 342, 71))
        self.scheduleLabel_4.setStyleSheet("font: 32pt Papyrus;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 98, 137);")
        self.scheduleLabel_4.setObjectName("scheduleLabel_4")
        self.tabWidget.addTab(self.tabAna, "")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.DataHLineYellow = QtWidgets.QFrame(self.tabData)
        self.DataHLineYellow.setGeometry(QtCore.QRect(0, 28, 1131, 4))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataHLineYellow.sizePolicy().hasHeightForWidth())
        self.DataHLineYellow.setSizePolicy(sizePolicy)
        self.DataHLineYellow.setStyleSheet("background-color: #bae1ff;")
        self.DataHLineYellow.setLineWidth(0)
        self.DataHLineYellow.setFrameShape(QtWidgets.QFrame.HLine)
        self.DataHLineYellow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DataHLineYellow.setObjectName("DataHLineYellow")
        self.DataHLinePurp = QtWidgets.QFrame(self.tabData)
        self.DataHLinePurp.setGeometry(QtCore.QRect(0, 16, 1131, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataHLinePurp.sizePolicy().hasHeightForWidth())
        self.DataHLinePurp.setSizePolicy(sizePolicy)
        self.DataHLinePurp.setStyleSheet("background-color: rgb(196, 98, 253);\n"
"color: rgb(196, 98, 253);")
        self.DataHLinePurp.setLineWidth(0)
        self.DataHLinePurp.setFrameShape(QtWidgets.QFrame.HLine)
        self.DataHLinePurp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DataHLinePurp.setObjectName("DataHLinePurp")
        self.DataHLinePink = QtWidgets.QFrame(self.tabData)
        self.DataHLinePink.setGeometry(QtCore.QRect(0, 0, 1131, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataHLinePink.sizePolicy().hasHeightForWidth())
        self.DataHLinePink.setSizePolicy(sizePolicy)
        self.DataHLinePink.setStyleSheet("background-color: rgb(255, 0, 129);")
        self.DataHLinePink.setLineWidth(0)
        self.DataHLinePink.setFrameShape(QtWidgets.QFrame.HLine)
        self.DataHLinePink.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DataHLinePink.setObjectName("DataHLinePink")
        self.scheduleLabel_5 = QtWidgets.QLabel(self.tabData)
        self.scheduleLabel_5.setGeometry(QtCore.QRect(410, 60, 280, 71))
        self.scheduleLabel_5.setStyleSheet("font: 32pt Papyrus;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 98, 137);")
        self.scheduleLabel_5.setObjectName("scheduleLabel_5")
        self.DatatabWidget = QtWidgets.QTabWidget(self.tabData)
        self.DatatabWidget.setGeometry(QtCore.QRect(100, 200, 900, 550))
        self.DatatabWidget.setStyleSheet("background-color: rgb(223, 227, 238);\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #005b96\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C4;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.DatatabWidget.setObjectName("DatatabWidget")
        self.breakformtab = QtWidgets.QWidget()
        self.breakformtab.setObjectName("breakformtab")
        self.formLayoutWidget = QtWidgets.QWidget(self.breakformtab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(67, 47, 391, 372))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.BreakForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.BreakForm.setContentsMargins(0, 0, 0, 0)
        self.BreakForm.setObjectName("BreakForm")
        self.BreakContLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakContLabel.setObjectName("BreakContLabel")
        self.BreakForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BreakContLabel)
        self.BreakRegionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakRegionLabel.setObjectName("BreakRegionLabel")
        self.BreakForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BreakRegionLabel)
        self.BreakCityLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakCityLabel.setObjectName("BreakCityLabel")
        self.BreakForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BreakCityLabel)
        self.BreakBreakLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakBreakLabel.setObjectName("BreakBreakLabel")
        self.BreakForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.BreakBreakLabel)
        self.BreakTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakTypeLabel.setObjectName("BreakTypeLabel")
        self.BreakForm.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.BreakTypeLabel)
        self.BreakBurnLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakBurnLabel.setObjectName("BreakBurnLabel")
        self.BreakForm.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.BreakBurnLabel)
        self.BreakContCb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.BreakContCb.setStyleSheet("background: #fcf4ff")
        self.BreakContCb.setObjectName("BreakContCb")
        self.BreakForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.BreakContCb)
        self.BreakRegionCb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.BreakRegionCb.setStyleSheet("background: #fcf4ff")
        self.BreakRegionCb.setObjectName("BreakRegionCb")
        self.BreakForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BreakRegionCb)
        self.BreakCityCb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.BreakCityCb.setStyleSheet("background: #fcf4ff")
        self.BreakCityCb.setObjectName("BreakCityCb")
        self.BreakForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BreakCityCb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BreakBeachBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.BreakBeachBox.setObjectName("BreakBeachBox")
        self.horizontalLayout.addWidget(self.BreakBeachBox)
        self.BreakPointBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.BreakPointBox.setObjectName("BreakPointBox")
        self.horizontalLayout.addWidget(self.BreakPointBox)
        self.BreakForm.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.BreakBreakEntry = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.BreakBreakEntry.setStyleSheet("background: #fcf4ff")
        self.BreakBreakEntry.setObjectName("BreakBreakEntry")
        self.BreakForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.BreakBreakEntry)
        self.BreakCountryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.BreakCountryLabel.setObjectName("BreakCountryLabel")
        self.BreakForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BreakCountryLabel)
        self.BreakCountryCb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.BreakCountryCb.setStyleSheet("background: #fcf4ff")
        self.BreakCountryCb.setObjectName("BreakCountryCb")
        self.BreakForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.BreakCountryCb)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.BreakForm.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BreakRiverBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.BreakRiverBox.setObjectName("BreakRiverBox")
        self.horizontalLayout_3.addWidget(self.BreakRiverBox)
        self.BreakReefBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.BreakReefBox.setObjectName("BreakReefBox")
        self.horizontalLayout_3.addWidget(self.BreakReefBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.BreakForm.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.BreakForm.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BreakForm.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BreakForm.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.BreakBurnLight = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.BreakBurnLight.setObjectName("BreakBurnLight")
        self.BreakForm.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.BreakBurnLight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BreakForm.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BreakForm.setItem(12, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.BreakBurnMed = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.BreakBurnMed.setObjectName("BreakBurnMed")
        self.BreakForm.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.BreakBurnMed)
        self.BreakBurnEx = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.BreakBurnEx.setObjectName("BreakBurnEx")
        self.BreakForm.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.BreakBurnEx)
        self.BreakEngBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.BreakEngBox.setObjectName("BreakEngBox")
        self.BreakForm.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.BreakEngBox)
        self.BreakSubmit = QtWidgets.QPushButton(self.breakformtab)
        self.BreakSubmit.setGeometry(QtCore.QRect(170, 460, 93, 28))
        self.BreakSubmit.setStyleSheet("background: #ff93ac;")
        self.BreakSubmit.setObjectName("BreakSubmit")
        self.addlocationbutton = QtWidgets.QPushButton(self.breakformtab)
        self.addlocationbutton.setGeometry(QtCore.QRect(620, 100, 150, 40))
        self.addlocationbutton.setStyleSheet("background: #dcb3ff;")
        self.addlocationbutton.setObjectName("addlocationbutton")
        self.DatatabWidget.addTab(self.breakformtab, "")
        self.breakbiotab = QtWidgets.QWidget()
        self.breakbiotab.setObjectName("breakbiotab")
        self.DatatabWidget.addTab(self.breakbiotab, "")
        self.breakschedtab = QtWidgets.QWidget()
        self.breakschedtab.setObjectName("breakschedtab")
        self.DatatabWidget.addTab(self.breakschedtab, "")
        self.breakheattab = QtWidgets.QWidget()
        self.breakheattab.setObjectName("breakheattab")
        self.DatatabWidget.addTab(self.breakheattab, "")
        self.breakheatrestab = QtWidgets.QWidget()
        self.breakheatrestab.setObjectName("breakheatrestab")
        self.DatatabWidget.addTab(self.breakheatrestab, "")
        self.tabWidget.addTab(self.tabData, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.DatatabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.BreakContCb)
        MainWindow.setTabOrder(self.BreakContCb, self.DatatabWidget)
        MainWindow.setTabOrder(self.DatatabWidget, self.BreakRegionCb)
        MainWindow.setTabOrder(self.BreakRegionCb, self.BreakCityCb)
        MainWindow.setTabOrder(self.BreakCityCb, self.BreakBeachBox)
        MainWindow.setTabOrder(self.BreakBeachBox, self.BreakPointBox)
        MainWindow.setTabOrder(self.BreakPointBox, self.BreakBreakEntry)
        MainWindow.setTabOrder(self.BreakBreakEntry, self.BreakCountryCb)
        MainWindow.setTabOrder(self.BreakCountryCb, self.BreakRiverBox)
        MainWindow.setTabOrder(self.BreakRiverBox, self.BreakReefBox)
        MainWindow.setTabOrder(self.BreakReefBox, self.BreakBurnLight)
        MainWindow.setTabOrder(self.BreakBurnLight, self.BreakBurnMed)
        MainWindow.setTabOrder(self.BreakBurnMed, self.BreakBurnEx)
        MainWindow.setTabOrder(self.BreakBurnEx, self.BreakEngBox)
        MainWindow.setTabOrder(self.BreakEngBox, self.BreakSubmit)
        MainWindow.setTabOrder(self.BreakSubmit, self.BreakContCb)
        MainWindow.setTabOrder(self.BreakContCb, self.BreakRegionCb)
        MainWindow.setTabOrder(self.BreakRegionCb, self.BreakCityCb)
        MainWindow.setTabOrder(self.BreakCityCb, self.BreakPointBox)
        MainWindow.setTabOrder(self.BreakPointBox, self.BreakBeachBox)
        MainWindow.setTabOrder(self.BreakBeachBox, self.BreakBreakEntry)
        MainWindow.setTabOrder(self.BreakBreakEntry, self.BreakCountryCb)
        MainWindow.setTabOrder(self.BreakCountryCb, self.BreakRiverBox)
        MainWindow.setTabOrder(self.BreakRiverBox, self.BreakReefBox)
        MainWindow.setTabOrder(self.BreakReefBox, self.BreakBurnLight)
        MainWindow.setTabOrder(self.BreakBurnLight, self.BreakBurnMed)
        MainWindow.setTabOrder(self.BreakBurnMed, self.BreakBurnEx)
        MainWindow.setTabOrder(self.BreakBurnEx, self.BreakEngBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WSL Analytics"))
        self.scheduleLabel.setText(_translate("MainWindow", "Schedule"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSched), _translate("MainWindow", "Schedule"))
        self.scheduleLabel_3.setText(_translate("MainWindow", "Surfers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSurfer), _translate("MainWindow", "Surfers"))
        self.scheduleLabel_4.setText(_translate("MainWindow", "Heat Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAna), _translate("MainWindow", "Analytics"))
        self.scheduleLabel_5.setText(_translate("MainWindow", "Data Entry"))
        self.BreakContLabel.setText(_translate("MainWindow", "Continent:"))
        self.BreakRegionLabel.setText(_translate("MainWindow", "Region/State:"))
        self.BreakCityLabel.setText(_translate("MainWindow", "City:"))
        self.BreakBreakLabel.setText(_translate("MainWindow", "Break:"))
        self.BreakTypeLabel.setText(_translate("MainWindow", "Break Type:"))
        self.BreakBurnLabel.setText(_translate("MainWindow", "Shoulder Burn:"))
        self.BreakBeachBox.setText(_translate("MainWindow", "Beach"))
        self.BreakPointBox.setText(_translate("MainWindow", "Point"))
        self.BreakCountryLabel.setText(_translate("MainWindow", "Country:"))
        self.BreakRiverBox.setText(_translate("MainWindow", "River         "))
        self.BreakReefBox.setText(_translate("MainWindow", "Reef"))
        self.BreakBurnLight.setText(_translate("MainWindow", "Light"))
        self.BreakBurnMed.setText(_translate("MainWindow", "Medium"))
        self.BreakBurnEx.setText(_translate("MainWindow", "Exhausting"))
        self.BreakEngBox.setText(_translate("MainWindow", "Engineered"))
        self.BreakSubmit.setText(_translate("MainWindow", "Submit"))
        self.addlocationbutton.setText(_translate("MainWindow", "Add Location"))
        self.DatatabWidget.setTabText(self.DatatabWidget.indexOf(self.breakformtab), _translate("MainWindow", "Breaks"))
        self.DatatabWidget.setTabText(self.DatatabWidget.indexOf(self.breakbiotab), _translate("MainWindow", "Bios"))
        self.DatatabWidget.setTabText(self.DatatabWidget.indexOf(self.breakschedtab), _translate("MainWindow", "Schedule"))
        self.DatatabWidget.setTabText(self.DatatabWidget.indexOf(self.breakheattab), _translate("MainWindow", "Heats"))
        self.DatatabWidget.setTabText(self.DatatabWidget.indexOf(self.breakheatrestab), _translate("MainWindow", "Heat Results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("MainWindow", "Data Entry"))
