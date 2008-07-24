# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Wed Jul 23 16:06:36 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(QtCore.QSize(QtCore.QRect(0,0,598,223).size()).expandedTo(SelectFishery.minimumSizeHint()))

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

        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.hboxlayout1.addWidget(self.fishery_comboBox)
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

        self.widget_4 = QtGui.QWidget(SelectFishery)
        self.widget_4.setObjectName("widget_4")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.widget_4)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label_2 = QtGui.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(300,0))
        self.label_2.setMaximumSize(QtCore.QSize(300,16777215))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.hboxlayout4.addWidget(self.label_2)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem2)

        self.perc_trip_land_line = QtGui.QLineEdit(self.widget_4)
        self.perc_trip_land_line.setMinimumSize(QtCore.QSize(40,0))
        self.perc_trip_land_line.setMaximumSize(QtCore.QSize(40,16777215))
        self.perc_trip_land_line.setObjectName("perc_trip_land_line")
        self.hboxlayout4.addWidget(self.perc_trip_land_line)
        self.vboxlayout.addWidget(self.widget_4)

        spacerItem3 = QtGui.QSpacerItem(580,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem3)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setMargin(9)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem4)

        self.pbnFisheryFinished = QtGui.QPushButton(self.widget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFisheryFinished.setFont(font)
        self.pbnFisheryFinished.setObjectName("pbnFisheryFinished")
        self.hboxlayout6.addWidget(self.pbnFisheryFinished)

        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnStartShapes.setFont(font)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout6.addWidget(self.pbnStartShapes)
        self.hboxlayout5.addWidget(self.widget_2)
        self.vboxlayout.addLayout(self.hboxlayout5)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Abalone", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Barracuda", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Bonita", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Calico Bass", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "California Halibut", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Clams", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Croaker", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Dorado (Mahi Mahi)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Jack Smelt", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Lobster", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Mackerel", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Mako Shark", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Marlin (Swordfish)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Mussels", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Rays/Skates", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Rock Crab", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Rockfish/Lingcod", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Sand Crab", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Salmon", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Sand Bass", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Scallops", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Sharks (Other)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Sheephead", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Squid", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Surfperch", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Thresher Shark", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Tuna", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "White Sea Bass", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Yellowtail", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Urchin", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Other (Note the species)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectFishery", "What percentage of your trips (annually) are associated with this fishery (on average)?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SelectFishery", "What percentage of your total landings (annually) are associated with this fishery (on average)", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

