# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectgear.ui'
#
# Created: Thu Jul 17 17:08:16 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectGear(object):
    def setupUi(self, SelectGear):
        SelectGear.setObjectName("SelectGear")
        SelectGear.resize(QtCore.QSize(QtCore.QRect(0,0,448,279).size()).expandedTo(SelectGear.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectGear)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox = QtGui.QGroupBox(SelectGear)
        self.groupBox.setMinimumSize(QtCore.QSize(0,60))
        self.groupBox.setObjectName("groupBox")

        self.fishery_sector_label = QtGui.QLabel(self.groupBox)
        self.fishery_sector_label.setGeometry(QtCore.QRect(0,10,408,40))
        self.fishery_sector_label.setMinimumSize(QtCore.QSize(0,40))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.fishery_sector_label.setFont(font)
        self.fishery_sector_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fishery_sector_label.setObjectName("fishery_sector_label")
        self.vboxlayout.addWidget(self.groupBox)

        self.widget = QtGui.QWidget(SelectGear)
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.gear_comboBox = QtGui.QComboBox(self.widget)
        self.gear_comboBox.setMaximumSize(QtCore.QSize(300,16777215))
        self.gear_comboBox.setObjectName("gear_comboBox")
        self.gear_comboBox.addItem("")
        self.hboxlayout.addWidget(self.gear_comboBox)
        self.vboxlayout.addWidget(self.widget)

        self.widget_3 = QtGui.QWidget(SelectGear)
        self.widget_3.setObjectName("widget_3")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_3)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.fishery_text_3 = QtGui.QLabel(self.widget_3)
        self.fishery_text_3.setObjectName("fishery_text_3")
        self.hboxlayout1.addWidget(self.fishery_text_3)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.gear_perc_income = QtGui.QLineEdit(self.widget_3)
        self.gear_perc_income.setEnabled(True)
        self.gear_perc_income.setMinimumSize(QtCore.QSize(50,0))
        self.gear_perc_income.setMaximumSize(QtCore.QSize(50,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.gear_perc_income.setFont(font)
        self.gear_perc_income.setObjectName("gear_perc_income")
        self.hboxlayout1.addWidget(self.gear_perc_income)
        self.vboxlayout.addWidget(self.widget_3)

        self.widget_2 = QtGui.QWidget(SelectGear)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)

        self.pbnStepFinished = QtGui.QPushButton(self.widget_2)
        self.pbnStepFinished.setMinimumSize(QtCore.QSize(200,0))
        self.pbnStepFinished.setObjectName("pbnStepFinished")
        self.hboxlayout2.addWidget(self.pbnStepFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setMinimumSize(QtCore.QSize(200,0))
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout2.addWidget(self.pbnStartShapes)
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
        self.fishery_text_3.setText(QtGui.QApplication.translate("SelectGear", "For what % of income/interest/stake (for \n"
        " current fishery sector) do you use this gear type?", None, QtGui.QApplication.UnicodeUTF8))
        self.gear_perc_income.setText(QtGui.QApplication.translate("SelectGear", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectGear", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

