# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectother.ui'
#
# Created: Fri Jun 27 00:52:42 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectOther(object):
    def setupUi(self, SelectOther):
        SelectOther.setObjectName("SelectOther")
        SelectOther.resize(QtCore.QSize(QtCore.QRect(0,0,485,194).size()).expandedTo(SelectOther.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectOther)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget = QtGui.QWidget(SelectOther)
        self.widget.setObjectName("widget")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.other_text = QtGui.QLabel(self.widget)
        self.other_text.setObjectName("other_text")
        self.hboxlayout.addWidget(self.other_text)

        self.other_line = QtGui.QTextEdit(self.widget)
        self.other_line.setObjectName("other_line")
        self.hboxlayout.addWidget(self.other_line)
        self.vboxlayout.addWidget(self.widget)

        self.widget_2 = QtGui.QWidget(SelectOther)
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

        self.retranslateUi(SelectOther)
        QtCore.QMetaObject.connectSlotsByName(SelectOther)

    def retranslateUi(self, SelectOther):
        SelectOther.setWindowTitle(QtGui.QApplication.translate("SelectOther", "OpenOceanMap - Select Other Income", None, QtGui.QApplication.UnicodeUTF8))
        self.other_text.setText(QtGui.QApplication.translate("SelectOther", "Describe Other Income:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("SelectOther", "Exit Other Income Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectOther", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

