# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectconsscience.ui'
#
# Created: Fri Jun 27 16:23:31 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectConsScience(object):
    def setupUi(self, SelectConsScience):
        SelectConsScience.setObjectName("SelectConsScience")
        SelectConsScience.resize(QtCore.QSize(QtCore.QRect(0,0,578,180).size()).expandedTo(SelectConsScience.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectConsScience)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectConsScience)
        self.widget.setObjectName("widget")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.vboxlayout1.addWidget(self.fishery_text)

        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setMaximumSize(QtCore.QSize(700,16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.vboxlayout1.addWidget(self.comboBox)
        self.vboxlayout.addWidget(self.widget)

        self.widget_2 = QtGui.QWidget(SelectConsScience)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.pbnFinished = QtGui.QPushButton(self.widget_2)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout.addWidget(self.pbnFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout.addWidget(self.pbnStartShapes)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(SelectConsScience)
        QtCore.QMetaObject.connectSlotsByName(SelectConsScience)

    def retranslateUi(self, SelectConsScience):
        SelectConsScience.setWindowTitle(QtGui.QApplication.translate("SelectConsScience", "OpenOceanMap - Select Conservation / Science", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectConsScience", "Select species/ecosystem of expertise/concern:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Coastal reef ecosystem (all finfish and invertebrates assoc. with coastal reef)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Deep Sea reefs (all finfish and invertebrates assoc. with reef seamounts)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Soft bottom (sand, mud, etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Small pelagics (sardines, anchovy, etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Migratory fish (tuna, swordfish, sailfish, yellowtail, etc)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Sea turtles", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Sea lions", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "Dolphins or whales", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("SelectConsScience", "None of the above", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("SelectConsScience", "Exit Conservationist / Scientist Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectConsScience", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

