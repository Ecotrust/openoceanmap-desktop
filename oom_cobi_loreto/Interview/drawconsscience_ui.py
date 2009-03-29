# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawconsscience.ui'
#
# Created: Sun Mar 29 02:20:46 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawConsScience(object):
    def setupUi(self, DrawConsScience):
        DrawConsScience.setObjectName("DrawConsScience")
        DrawConsScience.resize(641, 142)
        self.gridlayout = QtGui.QGridLayout(DrawConsScience)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.widget_2 = QtGui.QWidget(DrawConsScience)
        self.widget_2.setObjectName("widget_2")
        self.gridlayout1 = QtGui.QGridLayout(self.widget_2)
        self.gridlayout1.setObjectName("gridlayout1")
        self.type_label = QtGui.QLabel(self.widget_2)
        self.type_label.setMinimumSize(QtCore.QSize(50, 0))
        self.type_label.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.type_label.setFont(font)
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_label.setObjectName("type_label")
        self.gridlayout1.addWidget(self.type_label, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.penny_label = QtGui.QLabel(self.widget_2)
        self.penny_label.setObjectName("penny_label")
        self.hboxlayout.addWidget(self.penny_label)
        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)
        self.pl_label = QtGui.QLabel(self.widget_2)
        self.pl_label.setMinimumSize(QtCore.QSize(200, 0))
        self.pl_label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout.addWidget(self.pl_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.gridlayout1.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(DrawConsScience)
        self.widget.setObjectName("widget")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem1 = QtGui.QSpacerItem(106, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.pbnShapeFinished = QtGui.QPushButton(self.widget)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout1.addWidget(self.pbnShapeFinished)
        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout1.addWidget(self.pbnShapeDiscard)
        self.pbnMoreShapes = QtGui.QPushButton(self.widget)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout1.addWidget(self.pbnMoreShapes)
        self.gridlayout.addWidget(self.widget, 1, 0, 2, 1)

        self.retranslateUi(DrawConsScience)
        QtCore.QMetaObject.connectSlotsByName(DrawConsScience)

    def retranslateUi(self, DrawConsScience):
        DrawConsScience.setWindowTitle(QtGui.QApplication.translate("DrawConsScience", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.type_label.setText(QtGui.QApplication.translate("DrawConsScience", "Coastal reef ecosystem (all finfish and invertebrates assoc. with coastal reef)", None, QtGui.QApplication.UnicodeUTF8))
        self.penny_label.setText(QtGui.QApplication.translate("DrawConsScience", "Weighting (pennies):", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("DrawConsScience", "Finished With Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("DrawConsScience", "Discard Last Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("DrawConsScience", "Draw More Shapes...", None, QtGui.QApplication.UnicodeUTF8))

