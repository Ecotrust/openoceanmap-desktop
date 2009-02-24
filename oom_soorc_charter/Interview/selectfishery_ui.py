# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Thu Jul 31 16:19:22 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(QtCore.QSize(QtCore.QRect(0,0,550,166).size()).expandedTo(SelectFishery.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(SelectFishery)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setContentsMargins(9,9,9,0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setMinimumSize(QtCore.QSize(300,0))
        self.fishery_text.setMaximumSize(QtCore.QSize(300,16777215))
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout1.addWidget(self.fishery_text)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.fishery_line = QtGui.QLineEdit(self.widget)
        self.fishery_line.setMinimumSize(QtCore.QSize(200,0))
        self.fishery_line.setObjectName("fishery_line")
        self.hboxlayout1.addWidget(self.fishery_line)
        self.hboxlayout.addWidget(self.widget)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.widget_3 = QtGui.QWidget(SelectFishery)
        self.widget_3.setObjectName("widget_3")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.widget_3)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.label = QtGui.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(300,0))
        self.label.setMaximumSize(QtCore.QSize(300,16777215))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.hboxlayout3.addWidget(self.label)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem1)

        self.perc_trip_fish_line = QtGui.QLineEdit(self.widget_3)
        self.perc_trip_fish_line.setMinimumSize(QtCore.QSize(40,0))
        self.perc_trip_fish_line.setMaximumSize(QtCore.QSize(40,16777215))
        self.perc_trip_fish_line.setObjectName("perc_trip_fish_line")
        self.hboxlayout3.addWidget(self.perc_trip_fish_line)
        self.hboxlayout2.addWidget(self.widget_3)
        self.vboxlayout.addLayout(self.hboxlayout2)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout5 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setMargin(9)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem2)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnStartShapes.setFont(font)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout5.addWidget(self.pbnStartShapes)
        self.hboxlayout4.addWidget(self.widget_2)
        self.vboxlayout.addLayout(self.hboxlayout4)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Start Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Current Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectFishery", "Percentage of trips (annually) you said were associated with this fishery:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

