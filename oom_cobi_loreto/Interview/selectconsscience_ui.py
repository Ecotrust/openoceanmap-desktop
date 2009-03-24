# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectconsscience.ui'
#
# Created: Mon Mar 23 14:38:45 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectConsScience(object):
    def setupUi(self, SelectConsScience):
        SelectConsScience.setObjectName("SelectConsScience")
        SelectConsScience.resize(590, 115)
        self.vboxlayout = QtGui.QVBoxLayout(SelectConsScience)
        self.vboxlayout.setObjectName("vboxlayout")
        self.widget = QtGui.QWidget(SelectConsScience)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")
        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setMaximumSize(QtCore.QSize(450, 16777215))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.comboBox)
        self.vboxlayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(SelectConsScience)
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

        self.retranslateUi(SelectConsScience)
        QtCore.QMetaObject.connectSlotsByName(SelectConsScience)

    def retranslateUi(self, SelectConsScience):
        SelectConsScience.setWindowTitle(QtGui.QApplication.translate("SelectConsScience", "OpenOceanMap - Select Conservation / Science", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectConsScience", "Select focus:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("SelectConsScience", "Coastal reef ecosystem - finfish and invertebrates", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("SelectConsScience", "Deep Sea reefs and seamounts - finfish and invertebrates", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("SelectConsScience", "Soft bottom - sand-mud-etc", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("SelectConsScience", "Small pelagics - sardines-anchovy-etc", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("SelectConsScience", "Migratory fish - tuna-swordfish-sailfish-yellowtail-etc", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("SelectConsScience", "Sea turtles", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("SelectConsScience", "Sea lions", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("SelectConsScience", "Dolphins or whales", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("SelectConsScience", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("SelectConsScience", "Exit Cons / Scientist Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectConsScience", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

