# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Thu Jun 26 01:23:53 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(QtCore.QSize(QtCore.QRect(0,0,667,122).size()).expandedTo(SelectFishery.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectFishery)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)

        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.fishery_comboBox.addItem("")
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.vboxlayout.addWidget(self.widget)

        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.pbnFisheryFinished = QtGui.QPushButton(self.widget_2)
        self.pbnFisheryFinished.setObjectName("pbnFisheryFinished")
        self.hboxlayout1.addWidget(self.pbnFisheryFinished)

        self.pbnTypeFinished = QtGui.QPushButton(self.widget_2)
        self.pbnTypeFinished.setObjectName("pbnTypeFinished")
        self.hboxlayout1.addWidget(self.pbnTypeFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Shark and Skates", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Coastal reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Deep reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Migratory fish", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Benthic invertebrate", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Shrimp", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Exit Fishery Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnTypeFinished.setText(QtGui.QApplication.translate("SelectFishery", "Switch Vessel / Gear Type", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

