# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpolygon.ui'
#
# Created: Tue Jun 26 10:14:03 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NextPolygon(object):
    def setupUi(self, NextPolygon):
        NextPolygon.setObjectName("NextPolygon")
        NextPolygon.resize(QtCore.QSize(QtCore.QRect(0,0,549,147).size()).expandedTo(NextPolygon.minimumSizeHint()))

        self.label_1 = QtGui.QLabel(NextPolygon)
        self.label_1.setGeometry(QtCore.QRect(20,20,191,21))
        self.label_1.setObjectName("label_1")

        self.line_1 = QtGui.QLineEdit(NextPolygon)
        self.line_1.setEnabled(True)
        self.line_1.setGeometry(QtCore.QRect(230,20,281,29))
        self.line_1.setObjectName("line_1")

        self.pbnFinished = QtGui.QPushButton(NextPolygon)
        self.pbnFinished.setGeometry(QtCore.QRect(280,70,83,28))
        self.pbnFinished.setObjectName("pbnFinished")

        self.pbnMoreShapes = QtGui.QPushButton(NextPolygon)
        self.pbnMoreShapes.setGeometry(QtCore.QRect(370,70,151,28))
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")

        self.retranslateUi(NextPolygon)
        QtCore.QMetaObject.connectSlotsByName(NextPolygon)

    def retranslateUi(self, NextPolygon):
        NextPolygon.setWindowTitle(QtGui.QApplication.translate("NextPolygon", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("NextPolygon", "Weighting (Pennies)", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("NextPolygon", "Finished", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("NextPolygon", "More Shapes...", None, QtGui.QApplication.UnicodeUTF8))

