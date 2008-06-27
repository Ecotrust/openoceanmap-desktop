# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecotourism.ui'
#
# Created: Thu Jun 26 23:51:08 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Ecotourism(object):
    def setupUi(self, Ecotourism):
        Ecotourism.setObjectName("Ecotourism")
        Ecotourism.resize(QtCore.QSize(QtCore.QRect(0,0,417,343).size()).expandedTo(Ecotourism.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Ecotourism)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vessel_info = QtGui.QGroupBox(Ecotourism)

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

        self.employee_text = QtGui.QLabel(self.home_port_5)
        self.employee_text.setMinimumSize(QtCore.QSize(150,0))
        self.employee_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.employee_text.setFont(font)
        self.employee_text.setObjectName("employee_text")
        self.hboxlayout1.addWidget(self.employee_text)

        self.employee_comboBox = QtGui.QComboBox(self.home_port_5)
        self.employee_comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.employee_comboBox.setObjectName("employee_comboBox")
        self.employee_comboBox.addItem("")
        self.hboxlayout1.addWidget(self.employee_comboBox)
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

        self.vboxlayout2 = QtGui.QVBoxLayout(self.home_port_4)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.workers_text = QtGui.QLabel(self.home_port_4)
        self.workers_text.setMinimumSize(QtCore.QSize(150,0))
        self.workers_text.setMaximumSize(QtCore.QSize(350,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.workers_text.setFont(font)
        self.workers_text.setObjectName("workers_text")
        self.vboxlayout2.addWidget(self.workers_text)

        self.workers_line = QtGui.QLineEdit(self.home_port_4)
        self.workers_line.setEnabled(True)
        self.workers_line.setMinimumSize(QtCore.QSize(200,0))
        self.workers_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.workers_line.setFont(font)
        self.workers_line.setObjectName("workers_line")
        self.vboxlayout2.addWidget(self.workers_line)
        self.vboxlayout1.addWidget(self.home_port_4)
        self.hboxlayout.addWidget(self.vessel_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(Ecotourism)
        self.button_box.setObjectName("button_box")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem)

        self.pbnCancel = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout6.addWidget(self.pbnCancel)

        self.pbnSelectEcotourism = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectEcotourism.setFont(font)
        self.pbnSelectEcotourism.setObjectName("pbnSelectEcotourism")
        self.hboxlayout6.addWidget(self.pbnSelectEcotourism)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(Ecotourism)
        QtCore.QMetaObject.connectSlotsByName(Ecotourism)

    def retranslateUi(self, Ecotourism):
        Ecotourism.setWindowTitle(QtGui.QApplication.translate("Ecotourism", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("Ecotourism", "Ecotourism Info", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_text.setText(QtGui.QApplication.translate("Ecotourism", "Type of Empolyee:", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_comboBox.addItem(QtGui.QApplication.translate("Ecotourism", "Owner", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_comboBox.addItem(QtGui.QApplication.translate("Ecotourism", "Captain of Boat", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_comboBox.addItem(QtGui.QApplication.translate("Ecotourism", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_length_text.setText(QtGui.QApplication.translate("Ecotourism", "Vessel length (meters) :", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_motor_text.setText(QtGui.QApplication.translate("Ecotourism", "Vessel motor (horsepower):", None, QtGui.QApplication.UnicodeUTF8))
        self.haul_capacity_text.setText(QtGui.QApplication.translate("Ecotourism", "Haul Capacity (kilograms):", None, QtGui.QApplication.UnicodeUTF8))
        self.home_port_text.setText(QtGui.QApplication.translate("Ecotourism", "Home Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.workers_text.setText(QtGui.QApplication.translate("Ecotourism", "How many work for the company?", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("Ecotourism", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectEcotourism.setText(QtGui.QApplication.translate("Ecotourism", "Select Ecotourism Type", None, QtGui.QApplication.UnicodeUTF8))

