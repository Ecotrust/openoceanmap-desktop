# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fisherswindow.ui'
#
# Created: Tue Jun 24 22:35:10 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FishersWindow(object):
    def setupUi(self, FishersWindow):
        FishersWindow.setObjectName("FishersWindow")
        FishersWindow.resize(QtCore.QSize(QtCore.QRect(0,0,431,397).size()).expandedTo(FishersWindow.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(FishersWindow)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vessel_info = QtGui.QGroupBox(FishersWindow)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.home_port_5 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_5.setFont(font)
        self.home_port_5.setObjectName("home_port_5")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.home_port_5)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.gear_text = QtGui.QLabel(self.home_port_5)
        self.gear_text.setMinimumSize(QtCore.QSize(150,0))
        self.gear_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.gear_text.setFont(font)
        self.gear_text.setObjectName("gear_text")
        self.hboxlayout1.addWidget(self.gear_text)

        self.gear_comboBox = QtGui.QComboBox(self.home_port_5)
        self.gear_comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.gear_comboBox.setObjectName("gear_comboBox")
        self.hboxlayout1.addWidget(self.gear_comboBox)
        self.vboxlayout1.addWidget(self.home_port_5)

        self.vessel_length = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length.setFont(font)
        self.vessel_length.setObjectName("vessel_length")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.vessel_length)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.vessel_length_text = QtGui.QLabel(self.vessel_length)
        self.vessel_length_text.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_length_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_text.setFont(font)
        self.vessel_length_text.setObjectName("vessel_length_text")
        self.hboxlayout2.addWidget(self.vessel_length_text)

        self.vessel_length_line = QtGui.QLineEdit(self.vessel_length)
        self.vessel_length_line.setEnabled(True)
        self.vessel_length_line.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_length_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_line.setFont(font)
        self.vessel_length_line.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.vessel_length_line.setObjectName("vessel_length_line")
        self.hboxlayout2.addWidget(self.vessel_length_line)
        self.vboxlayout1.addWidget(self.vessel_length)

        self.vessel_length_2 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_2.setFont(font)
        self.vessel_length_2.setObjectName("vessel_length_2")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.vessel_length_2)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.vessel_motor_text = QtGui.QLabel(self.vessel_length_2)
        self.vessel_motor_text.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_motor_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_motor_text.setFont(font)
        self.vessel_motor_text.setObjectName("vessel_motor_text")
        self.hboxlayout3.addWidget(self.vessel_motor_text)

        self.vessel_motor_line = QtGui.QLineEdit(self.vessel_length_2)
        self.vessel_motor_line.setEnabled(True)
        self.vessel_motor_line.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_motor_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_motor_line.setFont(font)
        self.vessel_motor_line.setObjectName("vessel_motor_line")
        self.hboxlayout3.addWidget(self.vessel_motor_line)
        self.vboxlayout1.addWidget(self.vessel_length_2)

        self.vessel_length_3 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_3.setFont(font)
        self.vessel_length_3.setObjectName("vessel_length_3")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.vessel_length_3)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.haul_capacity_text = QtGui.QLabel(self.vessel_length_3)
        self.haul_capacity_text.setMinimumSize(QtCore.QSize(150,0))
        self.haul_capacity_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.haul_capacity_text.setFont(font)
        self.haul_capacity_text.setObjectName("haul_capacity_text")
        self.hboxlayout4.addWidget(self.haul_capacity_text)

        self.haul_capacity_line = QtGui.QLineEdit(self.vessel_length_3)
        self.haul_capacity_line.setEnabled(True)
        self.haul_capacity_line.setMinimumSize(QtCore.QSize(200,0))
        self.haul_capacity_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.haul_capacity_line.setFont(font)
        self.haul_capacity_line.setObjectName("haul_capacity_line")
        self.hboxlayout4.addWidget(self.haul_capacity_line)
        self.vboxlayout1.addWidget(self.vessel_length_3)

        self.home_port = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port.setFont(font)
        self.home_port.setObjectName("home_port")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.home_port)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.home_port_text = QtGui.QLabel(self.home_port)
        self.home_port_text.setMinimumSize(QtCore.QSize(150,0))
        self.home_port_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_text.setFont(font)
        self.home_port_text.setObjectName("home_port_text")
        self.hboxlayout5.addWidget(self.home_port_text)

        self.home_port_line = QtGui.QLineEdit(self.home_port)
        self.home_port_line.setEnabled(True)
        self.home_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.home_port_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_line.setFont(font)
        self.home_port_line.setObjectName("home_port_line")
        self.hboxlayout5.addWidget(self.home_port_line)
        self.vboxlayout1.addWidget(self.home_port)

        self.home_port_4 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_4.setFont(font)
        self.home_port_4.setObjectName("home_port_4")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.home_port_4)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.landing_port_text = QtGui.QLabel(self.home_port_4)
        self.landing_port_text.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text.setFont(font)
        self.landing_port_text.setObjectName("landing_port_text")
        self.hboxlayout6.addWidget(self.landing_port_text)

        self.landing_port_line = QtGui.QLineEdit(self.home_port_4)
        self.landing_port_line.setEnabled(True)
        self.landing_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line.setFont(font)
        self.landing_port_line.setObjectName("landing_port_line")
        self.hboxlayout6.addWidget(self.landing_port_line)
        self.vboxlayout1.addWidget(self.home_port_4)

        self.home_port_7 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_7.setFont(font)
        self.home_port_7.setObjectName("home_port_7")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.home_port_7)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.landing_port_text_2 = QtGui.QLabel(self.home_port_7)
        self.landing_port_text_2.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_2.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_2.setFont(font)
        self.landing_port_text_2.setObjectName("landing_port_text_2")
        self.hboxlayout7.addWidget(self.landing_port_text_2)

        self.landing_port_line_2 = QtGui.QLineEdit(self.home_port_7)
        self.landing_port_line_2.setEnabled(True)
        self.landing_port_line_2.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_2.setFont(font)
        self.landing_port_line_2.setObjectName("landing_port_line_2")
        self.hboxlayout7.addWidget(self.landing_port_line_2)
        self.vboxlayout1.addWidget(self.home_port_7)

        self.home_port_8 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_8.setFont(font)
        self.home_port_8.setObjectName("home_port_8")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.home_port_8)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.landing_port_text_3 = QtGui.QLabel(self.home_port_8)
        self.landing_port_text_3.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_3.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_3.setFont(font)
        self.landing_port_text_3.setObjectName("landing_port_text_3")
        self.hboxlayout8.addWidget(self.landing_port_text_3)

        self.landing_port_line_3 = QtGui.QLineEdit(self.home_port_8)
        self.landing_port_line_3.setEnabled(True)
        self.landing_port_line_3.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_3.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_3.setFont(font)
        self.landing_port_line_3.setObjectName("landing_port_line_3")
        self.hboxlayout8.addWidget(self.landing_port_line_3)
        self.vboxlayout1.addWidget(self.home_port_8)

        self.home_port_9 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_9.setFont(font)
        self.home_port_9.setObjectName("home_port_9")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.home_port_9)
        self.hboxlayout9.setSpacing(4)
        self.hboxlayout9.setMargin(4)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.landing_port_text_4 = QtGui.QLabel(self.home_port_9)
        self.landing_port_text_4.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_4.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_4.setFont(font)
        self.landing_port_text_4.setObjectName("landing_port_text_4")
        self.hboxlayout9.addWidget(self.landing_port_text_4)

        self.landing_port_line_4 = QtGui.QLineEdit(self.home_port_9)
        self.landing_port_line_4.setEnabled(True)
        self.landing_port_line_4.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_4.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_4.setFont(font)
        self.landing_port_line_4.setObjectName("landing_port_line_4")
        self.hboxlayout9.addWidget(self.landing_port_line_4)
        self.vboxlayout1.addWidget(self.home_port_9)
        self.hboxlayout.addWidget(self.vessel_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(FishersWindow)
        self.button_box.setObjectName("button_box")

        self.hboxlayout10 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout10.setObjectName("hboxlayout10")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout10.addItem(spacerItem)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout10.addWidget(self.pbnCancel)

        self.pbnBack = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnBack.setFont(font)
        self.pbnBack.setObjectName("pbnBack")
        self.hboxlayout10.addWidget(self.pbnBack)

        self.pbnSelectFishery = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectFishery.setFont(font)
        self.pbnSelectFishery.setObjectName("pbnSelectFishery")
        self.hboxlayout10.addWidget(self.pbnSelectFishery)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(FishersWindow)
        QtCore.QMetaObject.connectSlotsByName(FishersWindow)

    def retranslateUi(self, FishersWindow):
        FishersWindow.setWindowTitle(QtGui.QApplication.translate("FishersWindow", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("FishersWindow", "Fishery, Vessel and Port Information", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_text.setText(QtGui.QApplication.translate("FishersWindow", "Type of Fishing Gear:", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Hook and Line", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Gillnets", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Hooka (compressor)", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Traps", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Trawling", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Purse Seine", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("FishersWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text.setText(QtGui.QApplication.translate("FishersWindow", "Vessel length (meters) :", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_motor_text.setText(QtGui.QApplication.translate("FishersWindow", "Vessel motor (horsepower):", None, QtGui.QApplication.UnicodeUTF8))
        self.haul_capacity_text.setText(QtGui.QApplication.translate("FishersWindow", "Haul Capacity (kilograms):", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text.setText(QtGui.QApplication.translate("FishersWindow", "Home Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text.setText(QtGui.QApplication.translate("FishersWindow", "Landing Port 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_2.setText(QtGui.QApplication.translate("FishersWindow", "Landing Port 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_3.setText(QtGui.QApplication.translate("FishersWindow", "Landing Port 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_4.setText(QtGui.QApplication.translate("FishersWindow", "Landing Port 4:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("FishersWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnBack.setText(QtGui.QApplication.translate("FishersWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectFishery.setText(QtGui.QApplication.translate("FishersWindow", "Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
