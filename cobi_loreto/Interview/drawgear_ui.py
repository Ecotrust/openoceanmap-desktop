# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawgear.ui'
#
# Created: Fri Jun 27 03:15:39 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawGear(object):
    def setupUi(self, DrawGear):
        DrawGear.setObjectName("DrawGear")
        DrawGear.resize(QtCore.QSize(QtCore.QRect(0,0,827,197).size()).expandedTo(DrawGear.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(DrawGear)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.widget_2 = QtGui.QWidget(DrawGear)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.type_label = QtGui.QLabel(self.widget_2)
        self.type_label.setMinimumSize(QtCore.QSize(200,0))
        self.type_label.setMaximumSize(QtCore.QSize(500,16777215))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.hboxlayout.addWidget(self.type_label)

        self.penny_label = QtGui.QLabel(self.widget_2)
        self.penny_label.setObjectName("penny_label")
        self.hboxlayout.addWidget(self.penny_label)

        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setMaximumSize(QtCore.QSize(200,16777215))
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)

        self.pl_label = QtGui.QLabel(self.widget_2)
        self.pl_label.setMinimumSize(QtCore.QSize(50,0))
        self.pl_label.setMaximumSize(QtCore.QSize(50,16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout.addWidget(self.pl_label)
        self.gridlayout.addWidget(self.widget_2,0,0,1,1)

        self.widget = QtGui.QWidget(DrawGear)
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
        self.gridlayout.addWidget(self.widget,2,0,1,1)

        self.groupBox = QtGui.QGroupBox(DrawGear)
        self.groupBox.setObjectName("groupBox")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.hboxlayout2.addWidget(self.checkBox)

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.hboxlayout2.addWidget(self.checkBox_2)

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.hboxlayout2.addWidget(self.checkBox_3)

        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.hboxlayout2.addWidget(self.checkBox_4)

        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.hboxlayout2.addWidget(self.checkBox_5)

        self.checkBox_6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.hboxlayout2.addWidget(self.checkBox_6)

        self.checkBox_7 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName("checkBox_7")
        self.hboxlayout2.addWidget(self.checkBox_7)
        self.gridlayout.addWidget(self.groupBox,1,0,1,1)

        self.retranslateUi(DrawGear)
        QtCore.QMetaObject.connectSlotsByName(DrawGear)

    def retranslateUi(self, DrawGear):
        DrawGear.setWindowTitle(QtGui.QApplication.translate("DrawGear", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.penny_label.setText(QtGui.QApplication.translate("DrawGear", "Weighting (pennies):", None, QtGui.QApplication.UnicodeUTF8))
        self.pl_label.setText(QtGui.QApplication.translate("DrawGear", "remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("DrawGear", "Finished With Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("DrawGear", "Discard Last Shape...", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("DrawGear", "Draw More Shapes...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DrawGear", "Choose any species types caught in this area:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("DrawGear", "Sharkes and Skates", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("DrawGear", "Coastal reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("DrawGear", "Deep reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("DrawGear", "Migratory fish", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("DrawGear", "Benthic fish", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setText(QtGui.QApplication.translate("DrawGear", "Shrimp", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setText(QtGui.QApplication.translate("DrawGear", "Other", None, QtGui.QApplication.UnicodeUTF8))

