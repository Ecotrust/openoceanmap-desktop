# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawshapes.ui'
#
# Created: Thu Jun 26 01:23:53 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawShapes(object):
    def setupUi(self, DrawShapes):
        DrawShapes.setObjectName("DrawShapes")
        DrawShapes.resize(QtCore.QSize(QtCore.QRect(0,0,610,114).size()).expandedTo(DrawShapes.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(DrawShapes)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.widget_2 = QtGui.QWidget(DrawShapes)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_1 = QtGui.QLabel(self.widget_2)
        self.label_1.setObjectName("label_1")
        self.hboxlayout.addWidget(self.label_1)

        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)

        self.pl_label = QtGui.QLabel(self.widget_2)
        self.pl_label.setMinimumSize(QtCore.QSize(50,0))
        self.pl_label.setMaximumSize(QtCore.QSize(50,16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout.addWidget(self.pl_label)
        self.gridlayout.addWidget(self.widget_2,0,0,1,1)

        self.widget = QtGui.QWidget(DrawShapes)
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

        self.retranslateUi(DrawShapes)
        QtCore.QMetaObject.connectSlotsByName(DrawShapes)

    def retranslateUi(self, DrawShapes):
        DrawShapes.setWindowTitle(QtGui.QApplication.translate("DrawShapes", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("DrawShapes", "Weighting (Pennies)", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("DrawShapes", "Finished With Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("DrawShapes", "Discard Last Shape...", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("DrawShapes", "Draw More Shapes...", None, QtGui.QApplication.UnicodeUTF8))

