# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectecotourism.ui'
#
# Created: Thu Jun 26 17:47:07 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectEcotourism(object):
    def setupUi(self, SelectEcotourism):
        SelectEcotourism.setObjectName("SelectEcotourism")
        SelectEcotourism.resize(QtCore.QSize(QtCore.QRect(0,0,463,122).size()).expandedTo(SelectEcotourism.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectEcotourism)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectEcotourism)
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

        self.widget_2 = QtGui.QWidget(SelectEcotourism)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.pbnFinished = QtGui.QPushButton(self.widget_2)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout1.addWidget(self.pbnFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(SelectEcotourism)
        QtCore.QMetaObject.connectSlotsByName(SelectEcotourism)

    def retranslateUi(self, SelectEcotourism):
        SelectEcotourism.setWindowTitle(QtGui.QApplication.translate("SelectEcotourism", "OpenOceanMap - Select Ecotourism", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectEcotourism", "Select tourism activity type:", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectEcotourism", "Diving", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectEcotourism", "Snorkling", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectEcotourism", "Kayaking", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectEcotourism", "Whale Watching", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectEcotourism", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("SelectEcotourism", "Exit Ecotourism Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectEcotourism", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

