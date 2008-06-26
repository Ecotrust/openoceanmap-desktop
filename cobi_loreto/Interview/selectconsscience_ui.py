# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectconsscience.ui'
#
# Created: Thu Jun 26 01:23:54 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectConsScience(object):
    def setupUi(self, SelectConsScience):
        SelectConsScience.setObjectName("SelectConsScience")
        SelectConsScience.resize(QtCore.QSize(QtCore.QRect(0,0,667,122).size()).expandedTo(SelectConsScience.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectConsScience)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectConsScience)
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

        self.widget_2 = QtGui.QWidget(SelectConsScience)
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

        self.retranslateUi(SelectConsScience)
        QtCore.QMetaObject.connectSlotsByName(SelectConsScience)

    def retranslateUi(self, SelectConsScience):
        SelectConsScience.setWindowTitle(QtGui.QApplication.translate("SelectConsScience", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectConsScience", "Select species/ecosystem expertise/concern:", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Coastal reef ecosystem (all finfish and invertebrates assoc. with coastal reef)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Deep Sea reefs (all finfish and invertebrates assoc. with reef seamounts)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Soft bottom (sand, mud, etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Small pelagics (sardines, anchovy, etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Migratory fish (tuna, swordfish, sailfish, yellowtail, etc)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Sea turtles", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Sea lions", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Dolphins or whales", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "None of the above", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectConsScience", "Exit Fishery Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnTypeFinished.setText(QtGui.QApplication.translate("SelectConsScience", "Switch Type of Specialist", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectConsScience", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

