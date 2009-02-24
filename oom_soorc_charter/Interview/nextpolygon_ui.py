# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpolygon.ui'
#
# Created: Thu Jul 31 16:19:22 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NextPolygon(object):
    def setupUi(self, NextPolygon):
        NextPolygon.setObjectName("NextPolygon")
        NextPolygon.resize(QtCore.QSize(QtCore.QRect(0,0,493,109).size()).expandedTo(NextPolygon.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(NextPolygon)
        self.hboxlayout.setObjectName("hboxlayout")

        self.groupBox = QtGui.QGroupBox(NextPolygon)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setContentsMargins(-1,0,-1,0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(0)
        self.hboxlayout1.setContentsMargins(-1,-1,-1,6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.label_1 = QtGui.QLabel(self.groupBox)
        self.label_1.setMinimumSize(QtCore.QSize(100,0))
        self.label_1.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.hboxlayout2.addWidget(self.label_1)

        self.line_1 = QtGui.QLineEdit(self.groupBox)
        self.line_1.setEnabled(True)
        self.line_1.setMinimumSize(QtCore.QSize(100,0))
        self.line_1.setMaximumSize(QtCore.QSize(100,16777215))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_1.setFont(font)
        self.line_1.setObjectName("line_1")
        self.hboxlayout2.addWidget(self.line_1)

        self.pl_label = QtGui.QLabel(self.groupBox)
        self.pl_label.setMinimumSize(QtCore.QSize(50,0))
        self.pl_label.setMaximumSize(QtCore.QSize(50,16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout2.addWidget(self.pl_label)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.hboxlayout1.addLayout(self.vboxlayout1)

        spacerItem = QtGui.QSpacerItem(88,30,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setObjectName("widget")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.pbnShapeFinished = QtGui.QPushButton(self.widget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnShapeFinished.setFont(font)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout3.addWidget(self.pbnShapeFinished)

        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnShapeDiscard.setFont(font)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout3.addWidget(self.pbnShapeDiscard)

        self.pbnMoreShapes = QtGui.QPushButton(self.widget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnMoreShapes.setFont(font)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout3.addWidget(self.pbnMoreShapes)
        self.vboxlayout.addWidget(self.widget)
        self.hboxlayout.addWidget(self.groupBox)

        self.retranslateUi(NextPolygon)
        QtCore.QMetaObject.connectSlotsByName(NextPolygon)

    def retranslateUi(self, NextPolygon):
        NextPolygon.setWindowTitle(QtGui.QApplication.translate("NextPolygon", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("NextPolygon", "Pennies:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("NextPolygon", "Finished With Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("NextPolygon", "Discard Last Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("NextPolygon", "More Shapes This Fishery", None, QtGui.QApplication.UnicodeUTF8))

