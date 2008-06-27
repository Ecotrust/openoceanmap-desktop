# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectgear.ui'
#
# Created: Fri Jun 27 00:52:40 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectGear(object):
    def setupUi(self, SelectGear):
        SelectGear.setObjectName("SelectGear")
        SelectGear.resize(QtCore.QSize(QtCore.QRect(0,0,668,301).size()).expandedTo(SelectGear.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectGear)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(SelectGear)
        self.groupBox.setMinimumSize(QtCore.QSize(0,40))
        self.groupBox.setObjectName("groupBox")

        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")

        self.fishery_sector_label = QtGui.QLabel(self.groupBox)
        self.fishery_sector_label.setMinimumSize(QtCore.QSize(0,40))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.fishery_sector_label.setFont(font)
        self.fishery_sector_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fishery_sector_label.setObjectName("fishery_sector_label")
        self.gridlayout.addWidget(self.fishery_sector_label,0,0,1,1)
        self.vboxlayout.addWidget(self.groupBox)

        self.widget = QtGui.QWidget(SelectGear)
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)

        self.gear_comboBox = QtGui.QComboBox(self.widget)
        self.gear_comboBox.setMaximumSize(QtCore.QSize(200,16777215))
        self.gear_comboBox.setObjectName("gear_comboBox")
        self.gear_comboBox.addItem("")
        self.hboxlayout.addWidget(self.gear_comboBox)
        self.vboxlayout.addWidget(self.widget)

        self.widget_2 = QtGui.QWidget(SelectGear)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.pbnStepFinished = QtGui.QPushButton(self.widget_2)
        self.pbnStepFinished.setObjectName("pbnStepFinished")
        self.hboxlayout1.addWidget(self.pbnStepFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(SelectGear)
        QtCore.QMetaObject.connectSlotsByName(SelectGear)

    def retranslateUi(self, SelectGear):
        SelectGear.setWindowTitle(QtGui.QApplication.translate("SelectGear", "OpenOceanMap - Select Gear", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SelectGear", "Fishery Sector", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectGear", "Select Gear Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Hook and Line", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Gillnets", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Hooka (compressor)", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Traps", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Trawling", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Purse Seine", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_comboBox.addItem(QtGui.QApplication.translate("SelectGear", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectGear", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

