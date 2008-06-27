# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fishery.ui'
#
# Created: Fri Jun 27 01:10:57 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Fishery(object):
    def setupUi(self, Fishery):
        Fishery.setObjectName("Fishery")
        Fishery.resize(QtCore.QSize(QtCore.QRect(0,0,448,433).size()).expandedTo(Fishery.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Fishery)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(Fishery)
        self.groupBox.setMinimumSize(QtCore.QSize(0,63))
        self.groupBox.setObjectName("groupBox")

        self.fishery_sector_label = QtGui.QLabel(self.groupBox)
        self.fishery_sector_label.setGeometry(QtCore.QRect(15,20,395,43))
        self.fishery_sector_label.setMinimumSize(QtCore.QSize(0,40))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.fishery_sector_label.setFont(font)
        self.fishery_sector_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fishery_sector_label.setObjectName("fishery_sector_label")
        self.vboxlayout.addWidget(self.groupBox)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vessel_info = QtGui.QGroupBox(Fishery)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.vessel_info)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vessel_length = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length.setFont(font)
        self.vessel_length.setObjectName("vessel_length")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.vessel_length)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vessel_length_text = QtGui.QLabel(self.vessel_length)
        self.vessel_length_text.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_length_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_text.setFont(font)
        self.vessel_length_text.setObjectName("vessel_length_text")
        self.hboxlayout1.addWidget(self.vessel_length_text)

        self.vessel_length_line = QtGui.QLineEdit(self.vessel_length)
        self.vessel_length_line.setEnabled(True)
        self.vessel_length_line.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_length_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_line.setFont(font)
        self.vessel_length_line.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.vessel_length_line.setObjectName("vessel_length_line")
        self.hboxlayout1.addWidget(self.vessel_length_line)
        self.vboxlayout1.addWidget(self.vessel_length)

        self.vessel_length_2 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_2.setFont(font)
        self.vessel_length_2.setObjectName("vessel_length_2")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.vessel_length_2)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.vessel_motor_text = QtGui.QLabel(self.vessel_length_2)
        self.vessel_motor_text.setMinimumSize(QtCore.QSize(150,0))
        self.vessel_motor_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_motor_text.setFont(font)
        self.vessel_motor_text.setObjectName("vessel_motor_text")
        self.hboxlayout2.addWidget(self.vessel_motor_text)

        self.vessel_motor_line = QtGui.QLineEdit(self.vessel_length_2)
        self.vessel_motor_line.setEnabled(True)
        self.vessel_motor_line.setMinimumSize(QtCore.QSize(200,0))
        self.vessel_motor_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_motor_line.setFont(font)
        self.vessel_motor_line.setObjectName("vessel_motor_line")
        self.hboxlayout2.addWidget(self.vessel_motor_line)
        self.vboxlayout1.addWidget(self.vessel_length_2)

        self.vessel_length_3 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length_3.setFont(font)
        self.vessel_length_3.setObjectName("vessel_length_3")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.vessel_length_3)
        self.hboxlayout3.setSpacing(4)
        self.hboxlayout3.setMargin(4)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.haul_capacity_text = QtGui.QLabel(self.vessel_length_3)
        self.haul_capacity_text.setMinimumSize(QtCore.QSize(150,0))
        self.haul_capacity_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.haul_capacity_text.setFont(font)
        self.haul_capacity_text.setObjectName("haul_capacity_text")
        self.hboxlayout3.addWidget(self.haul_capacity_text)

        self.haul_capacity_line = QtGui.QLineEdit(self.vessel_length_3)
        self.haul_capacity_line.setEnabled(True)
        self.haul_capacity_line.setMinimumSize(QtCore.QSize(200,0))
        self.haul_capacity_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.haul_capacity_line.setFont(font)
        self.haul_capacity_line.setObjectName("haul_capacity_line")
        self.hboxlayout3.addWidget(self.haul_capacity_line)
        self.vboxlayout1.addWidget(self.vessel_length_3)

        self.home_port = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port.setFont(font)
        self.home_port.setObjectName("home_port")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.home_port)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setMargin(4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.home_port_text = QtGui.QLabel(self.home_port)
        self.home_port_text.setMinimumSize(QtCore.QSize(150,0))
        self.home_port_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_text.setFont(font)
        self.home_port_text.setObjectName("home_port_text")
        self.hboxlayout4.addWidget(self.home_port_text)

        self.home_port_line = QtGui.QLineEdit(self.home_port)
        self.home_port_line.setEnabled(True)
        self.home_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.home_port_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_line.setFont(font)
        self.home_port_line.setObjectName("home_port_line")
        self.hboxlayout4.addWidget(self.home_port_line)
        self.vboxlayout1.addWidget(self.home_port)

        self.home_port_4 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_4.setFont(font)
        self.home_port_4.setObjectName("home_port_4")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.home_port_4)
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setMargin(4)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.landing_port_text = QtGui.QLabel(self.home_port_4)
        self.landing_port_text.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text.setFont(font)
        self.landing_port_text.setObjectName("landing_port_text")
        self.hboxlayout5.addWidget(self.landing_port_text)

        self.landing_port_line = QtGui.QLineEdit(self.home_port_4)
        self.landing_port_line.setEnabled(True)
        self.landing_port_line.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line.setFont(font)
        self.landing_port_line.setObjectName("landing_port_line")
        self.hboxlayout5.addWidget(self.landing_port_line)
        self.vboxlayout1.addWidget(self.home_port_4)

        self.home_port_7 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_7.setFont(font)
        self.home_port_7.setObjectName("home_port_7")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.home_port_7)
        self.hboxlayout6.setSpacing(4)
        self.hboxlayout6.setMargin(4)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.landing_port_text_2 = QtGui.QLabel(self.home_port_7)
        self.landing_port_text_2.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_2.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_2.setFont(font)
        self.landing_port_text_2.setObjectName("landing_port_text_2")
        self.hboxlayout6.addWidget(self.landing_port_text_2)

        self.landing_port_line_2 = QtGui.QLineEdit(self.home_port_7)
        self.landing_port_line_2.setEnabled(True)
        self.landing_port_line_2.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_2.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_2.setFont(font)
        self.landing_port_line_2.setObjectName("landing_port_line_2")
        self.hboxlayout6.addWidget(self.landing_port_line_2)
        self.vboxlayout1.addWidget(self.home_port_7)

        self.home_port_8 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_8.setFont(font)
        self.home_port_8.setObjectName("home_port_8")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.home_port_8)
        self.hboxlayout7.setSpacing(4)
        self.hboxlayout7.setMargin(4)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.landing_port_text_3 = QtGui.QLabel(self.home_port_8)
        self.landing_port_text_3.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_3.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_3.setFont(font)
        self.landing_port_text_3.setObjectName("landing_port_text_3")
        self.hboxlayout7.addWidget(self.landing_port_text_3)

        self.landing_port_line_3 = QtGui.QLineEdit(self.home_port_8)
        self.landing_port_line_3.setEnabled(True)
        self.landing_port_line_3.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_3.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_3.setFont(font)
        self.landing_port_line_3.setObjectName("landing_port_line_3")
        self.hboxlayout7.addWidget(self.landing_port_line_3)
        self.vboxlayout1.addWidget(self.home_port_8)

        self.home_port_9 = QtGui.QWidget(self.vessel_info)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_9.setFont(font)
        self.home_port_9.setObjectName("home_port_9")

        self.hboxlayout8 = QtGui.QHBoxLayout(self.home_port_9)
        self.hboxlayout8.setSpacing(4)
        self.hboxlayout8.setMargin(4)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.landing_port_text_4 = QtGui.QLabel(self.home_port_9)
        self.landing_port_text_4.setMinimumSize(QtCore.QSize(150,0))
        self.landing_port_text_4.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_text_4.setFont(font)
        self.landing_port_text_4.setObjectName("landing_port_text_4")
        self.hboxlayout8.addWidget(self.landing_port_text_4)

        self.landing_port_line_4 = QtGui.QLineEdit(self.home_port_9)
        self.landing_port_line_4.setEnabled(True)
        self.landing_port_line_4.setMinimumSize(QtCore.QSize(200,0))
        self.landing_port_line_4.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.landing_port_line_4.setFont(font)
        self.landing_port_line_4.setObjectName("landing_port_line_4")
        self.hboxlayout8.addWidget(self.landing_port_line_4)
        self.vboxlayout1.addWidget(self.home_port_9)
        self.hboxlayout.addWidget(self.vessel_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(Fishery)
        self.button_box.setObjectName("button_box")

        self.hboxlayout9 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout9.setObjectName("hboxlayout9")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout9.addWidget(self.pbnCancel)

        self.pbnBack = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnBack.setFont(font)
        self.pbnBack.setObjectName("pbnBack")
        self.hboxlayout9.addWidget(self.pbnBack)

        self.pbnSelectGear = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectGear.setFont(font)
        self.pbnSelectGear.setObjectName("pbnSelectGear")
        self.hboxlayout9.addWidget(self.pbnSelectGear)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(Fishery)
        QtCore.QMetaObject.connectSlotsByName(Fishery)

    def retranslateUi(self, Fishery):
        Fishery.setWindowTitle(QtGui.QApplication.translate("Fishery", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Fishery", "Fishery Sector", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_sector_label.setText(QtGui.QApplication.translate("Fishery", "Dynamic Fishery Sector Name", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("Fishery", "Fisher Information", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text.setText(QtGui.QApplication.translate("Fishery", "Vessel length (meters) :", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_motor_text.setText(QtGui.QApplication.translate("Fishery", "Vessel motor (horsepower):", None, QtGui.QApplication.UnicodeUTF8))
        self.haul_capacity_text.setText(QtGui.QApplication.translate("Fishery", "Haul Capacity (kilograms):", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text.setText(QtGui.QApplication.translate("Fishery", "Home Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text.setText(QtGui.QApplication.translate("Fishery", "Landing Port 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_2.setText(QtGui.QApplication.translate("Fishery", "Landing Port 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_3.setText(QtGui.QApplication.translate("Fishery", "Landing Port 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.landing_port_text_4.setText(QtGui.QApplication.translate("Fishery", "Landing Port 4:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("Fishery", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnBack.setText(QtGui.QApplication.translate("Fishery", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectGear.setText(QtGui.QApplication.translate("Fishery", "Select Gear Type", None, QtGui.QApplication.UnicodeUTF8))

