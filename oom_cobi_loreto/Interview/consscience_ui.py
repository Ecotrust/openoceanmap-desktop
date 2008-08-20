# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consscience.ui'
#
# Created: Mon Aug  4 16:27:25 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConsScience(object):
    def setupUi(self, ConsScience):
        ConsScience.setObjectName("ConsScience")
        ConsScience.resize(QtCore.QSize(QtCore.QRect(0,0,404,187).size()).expandedTo(ConsScience.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(ConsScience)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.vessel_info = QtGui.QGroupBox(ConsScience)

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

        self.comboBox = QtGui.QComboBox(self.home_port_5)
        self.comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.hboxlayout1.addWidget(self.comboBox)
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

        self.add_info_text = QtGui.QLabel(self.vessel_length)
        self.add_info_text.setMinimumSize(QtCore.QSize(150,0))
        self.add_info_text.setMaximumSize(QtCore.QSize(150,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_info_text.setFont(font)
        self.add_info_text.setObjectName("add_info_text")
        self.hboxlayout2.addWidget(self.add_info_text)

        self.add_info_line = QtGui.QLineEdit(self.vessel_length)
        self.add_info_line.setEnabled(True)
        self.add_info_line.setMinimumSize(QtCore.QSize(200,0))
        self.add_info_line.setMaximumSize(QtCore.QSize(200,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_info_line.setFont(font)
        self.add_info_line.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.add_info_line.setObjectName("add_info_line")
        self.hboxlayout2.addWidget(self.add_info_line)
        self.vboxlayout1.addWidget(self.vessel_length)
        self.hboxlayout.addWidget(self.vessel_info)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.button_box = QtGui.QWidget(ConsScience)
        self.button_box.setObjectName("button_box")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem)

        self.pbnSelectConsScience = QtGui.QPushButton(self.button_box)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectConsScience.setFont(font)
        self.pbnSelectConsScience.setObjectName("pbnSelectConsScience")
        self.hboxlayout3.addWidget(self.pbnSelectConsScience)
        self.vboxlayout.addWidget(self.button_box)

        self.retranslateUi(ConsScience)
        QtCore.QMetaObject.connectSlotsByName(ConsScience)

    def retranslateUi(self, ConsScience):
        ConsScience.setWindowTitle(QtGui.QApplication.translate("ConsScience", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("ConsScience", "Conservationist / Scientist Info", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_text.setText(QtGui.QApplication.translate("ConsScience", "Type of Specialist:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Academic", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Non-Governmental Organization", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Government (Municipal)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Government (State)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Government (Federal)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("ConsScience", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.add_info_text.setText(QtGui.QApplication.translate("ConsScience", "Additional info:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectConsScience.setText(QtGui.QApplication.translate("ConsScience", "Draw Shapes by Areas of Knowledge", None, QtGui.QApplication.UnicodeUTF8))

