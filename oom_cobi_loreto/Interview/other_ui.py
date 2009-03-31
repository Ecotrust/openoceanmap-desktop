# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other.ui'
#
# Created: Mon Mar 30 13:25:11 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Other(object):
    def setupUi(self, Other):
        Other.setObjectName("Other")
        Other.resize(519, 127)
        self.vboxlayout = QtGui.QVBoxLayout(Other)
        self.vboxlayout.setObjectName("vboxlayout")
        self.widget = QtGui.QWidget(Other)
        self.widget.setObjectName("widget")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.other_text = QtGui.QLabel(self.widget)
        self.other_text.setObjectName("other_text")
        self.vboxlayout1.addWidget(self.other_text)
        self.other_line = QtGui.QLineEdit(self.widget)
        self.other_line.setObjectName("other_line")
        self.vboxlayout1.addWidget(self.other_line)
        self.vboxlayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(Other)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(246, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.pbnCancel = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.hboxlayout.addWidget(self.pbnCancel)
        self.pbnFinished = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFinished.setFont(font)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout.addWidget(self.pbnFinished)
        self.vboxlayout.addWidget(self.widget_2)

        self.retranslateUi(Other)
        QtCore.QMetaObject.connectSlotsByName(Other)

    def retranslateUi(self, Other):
        Other.setWindowTitle(QtGui.QApplication.translate("Other", "OpenOceanMap - Define Other Income", None, QtGui.QApplication.UnicodeUTF8))
        self.other_text.setText(QtGui.QApplication.translate("Other", "Describe Other Income:", None, QtGui.QApplication.UnicodeUTF8))
        self.other_line.setText(QtGui.QApplication.translate("Other", "other income", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("Other", "Exit Other Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("Other", "Save  to file", None, QtGui.QApplication.UnicodeUTF8))

