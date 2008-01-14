# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Thu Nov 29 19:21:35 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(QtCore.QSize(QtCore.QRect(0,0,400,125).size()).expandedTo(SelectFishery.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectFishery)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)

        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.vboxlayout.addWidget(self.widget)

        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.pbnFisheryFinished = QtGui.QPushButton(self.widget_2)
        self.pbnFisheryFinished.setObjectName("pbnFisheryFinished")
        self.hboxlayout1.addWidget(self.pbnFisheryFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Chinook Salmon", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Rockfish/Lingcod Complex", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "California Halibut", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Dungeness Crab", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Abalone", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

