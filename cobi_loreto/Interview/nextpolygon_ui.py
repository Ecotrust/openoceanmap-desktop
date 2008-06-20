# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpolygon.ui'
#
# Created: Mon Jan 14 13:54:52 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NextPolygon(object):
    def setupUi(self, NextPolygon):
        NextPolygon.setObjectName("NextPolygon")
        NextPolygon.resize(QtCore.QSize(QtCore.QRect(0,0,484,106).size()).expandedTo(NextPolygon.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(NextPolygon)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.widget_2 = QtGui.QWidget(NextPolygon)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_1 = QtGui.QLabel(self.widget_2)
        self.label_1.setObjectName("label_1")
        self.hboxlayout.addWidget(self.label_1)

        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)
        self.gridlayout.addWidget(self.widget_2,0,0,1,1)

        self.widget = QtGui.QWidget(NextPolygon)
        self.widget.setObjectName("widget")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.pbnShapeFinished = QtGui.QPushButton(self.widget)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout1.addWidget(self.pbnShapeFinished)

        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout1.addWidget(self.pbnShapeDiscard)

        self.pbnMoreShapes = QtGui.QPushButton(self.widget)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout1.addWidget(self.pbnMoreShapes)
        self.gridlayout.addWidget(self.widget,1,0,1,1)

        self.retranslateUi(NextPolygon)
        QtCore.QMetaObject.connectSlotsByName(NextPolygon)

    def retranslateUi(self, NextPolygon):
        NextPolygon.setWindowTitle(QtGui.QApplication.translate("NextPolygon", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("NextPolygon", "Weighting (Pennies)", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("NextPolygon", "Finished With Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("NextPolygon", "Discard Last Shape...", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("NextPolygon", "More Shapes This Fishery...", None, QtGui.QApplication.UnicodeUTF8))

