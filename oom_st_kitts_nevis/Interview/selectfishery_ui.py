# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Fri Feb 05 17:58:56 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(682, 426)
        self.verticalLayout = QtGui.QVBoxLayout(SelectFishery)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setContentsMargins(9, 9, 9, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setMinimumSize(QtCore.QSize(100, 0))
        self.fishery_text.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setMinimumSize(QtCore.QSize(450, 0))
        self.fishery_comboBox.setMaximumSize(QtCore.QSize(450, 16777215))
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.setItemText(0, "")
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_4 = QtGui.QWidget(SelectFishery)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.fish_yrs_partic = QtGui.QLineEdit(self.widget_4)
        self.fish_yrs_partic.setMinimumSize(QtCore.QSize(100, 0))
        self.fish_yrs_partic.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fish_yrs_partic.setObjectName("fish_yrs_partic")
        self.horizontalLayout_8.addWidget(self.fish_yrs_partic)
        self.horizontalLayout_7.addWidget(self.widget_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtGui.QWidget(SelectFishery)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.fish_seasonality = QtGui.QLineEdit(self.widget_3)
        self.fish_seasonality.setMinimumSize(QtCore.QSize(450, 0))
        self.fish_seasonality.setMaximumSize(QtCore.QSize(450, 16777215))
        self.fish_seasonality.setObjectName("fish_seasonality")
        self.horizontalLayout_4.addWidget(self.fish_seasonality)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_7 = QtGui.QWidget(SelectFishery)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_6 = QtGui.QLabel(self.widget_7)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        self.label_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.fish_num_gear = QtGui.QLineEdit(self.widget_7)
        self.fish_num_gear.setMinimumSize(QtCore.QSize(100, 0))
        self.fish_num_gear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fish_num_gear.setObjectName("fish_num_gear")
        self.horizontalLayout_14.addWidget(self.fish_num_gear)
        self.horizontalLayout_13.addWidget(self.widget_7)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_5 = QtGui.QWidget(SelectFishery)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtGui.QLabel(self.widget_5)
        self.label_4.setMinimumSize(QtCore.QSize(160, 0))
        self.label_4.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.fish_gear_length = QtGui.QLineEdit(self.widget_5)
        self.fish_gear_length.setMinimumSize(QtCore.QSize(100, 0))
        self.fish_gear_length.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fish_gear_length.setObjectName("fish_gear_length")
        self.horizontalLayout_10.addWidget(self.fish_gear_length)
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_8 = QtGui.QWidget(SelectFishery)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_7 = QtGui.QLabel(self.widget_8)
        self.label_7.setMinimumSize(QtCore.QSize(160, 0))
        self.label_7.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.fish_price = QtGui.QLineEdit(self.widget_8)
        self.fish_price.setMinimumSize(QtCore.QSize(100, 0))
        self.fish_price.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fish_price.setObjectName("fish_price")
        self.horizontalLayout_16.addWidget(self.fish_price)
        self.horizontalLayout_15.addWidget(self.widget_8)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget_9 = QtGui.QWidget(SelectFishery)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_8 = QtGui.QLabel(self.widget_9)
        self.label_8.setMinimumSize(QtCore.QSize(160, 0))
        self.label_8.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_18.addWidget(self.label_8)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.fish_port = QtGui.QLineEdit(self.widget_9)
        self.fish_port.setMinimumSize(QtCore.QSize(450, 0))
        self.fish_port.setMaximumSize(QtCore.QSize(450, 16777215))
        self.fish_port.setObjectName("fish_port")
        self.horizontalLayout_18.addWidget(self.fish_port)
        self.horizontalLayout_17.addWidget(self.widget_9)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem7)
        self.pbnFisheryFinished = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFisheryFinished.setFont(font)
        self.pbnFisheryFinished.setObjectName("pbnFisheryFinished")
        self.hboxlayout1.addWidget(self.pbnFisheryFinished)
        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnStartShapes.setFont(font)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)
        SelectFishery.setTabOrder(self.fishery_comboBox, self.fish_yrs_partic)
        SelectFishery.setTabOrder(self.fish_yrs_partic, self.fish_seasonality)
        SelectFishery.setTabOrder(self.fish_seasonality, self.fish_num_gear)
        SelectFishery.setTabOrder(self.fish_num_gear, self.fish_gear_length)
        SelectFishery.setTabOrder(self.fish_gear_length, self.fish_price)
        SelectFishery.setTabOrder(self.fish_price, self.fish_port)
        SelectFishery.setTabOrder(self.fish_port, self.pbnStartShapes)
        SelectFishery.setTabOrder(self.pbnStartShapes, self.pbnFisheryFinished)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(1, QtGui.QApplication.translate("SelectFishery", "Coastal Pelagics or Net Fishery (Coastal Pealgics - Beach Seine)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(2, QtGui.QApplication.translate("SelectFishery", "Tuna & Bonito with Handline (Coastal Pelagics - Troll/Handline)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(3, QtGui.QApplication.translate("SelectFishery", "Large Offshore Pelagics (Ocean Pelagics - Troll/Handline)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(4, QtGui.QApplication.translate("SelectFishery", "Nearshore Trap/Pot (Coastal Demersals - Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(5, QtGui.QApplication.translate("SelectFishery", "Nearshore Handline/Banking (Coastal Demersals - Pole/Handline)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(6, QtGui.QApplication.translate("SelectFishery", "Nearshore Spear (Coastal Demersals - Spear Gun)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(7, QtGui.QApplication.translate("SelectFishery", "Nearshore Gillnets (Coastal Demersals - Gillnets)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(8, QtGui.QApplication.translate("SelectFishery", "Deep Slope/Bank Trap/Pot Fishery (Demersal Shelf/Deep Slope - Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(9, QtGui.QApplication.translate("SelectFishery", "Deep Slope/Bank Handline/Banking Fishery (Demersal Shelf/Deep Slope - Pole/Handline)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(10, QtGui.QApplication.translate("SelectFishery", "Lobster - Trap", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(11, QtGui.QApplication.translate("SelectFishery", "Lobster - Dive (SCUBA)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(12, QtGui.QApplication.translate("SelectFishery", "Lobster - Dive (Free)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(13, QtGui.QApplication.translate("SelectFishery", "Conch - Dive (SCUBA)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(14, QtGui.QApplication.translate("SelectFishery", "Conch - Dive (Free)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(15, QtGui.QApplication.translate("SelectFishery", "Shark - Hook and Line", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(16, QtGui.QApplication.translate("SelectFishery", "Shark - Gillnets", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(17, QtGui.QApplication.translate("SelectFishery", "Diamondback Squid - Light Stick (Hook and Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(18, QtGui.QApplication.translate("SelectFishery", "Turtle - Turtle Net", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SelectFishery", "Years experience in this fishery:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectFishery", "Fishing seasonality:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SelectFishery", "Average gear usage per trip:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SelectFishery", "Gear deployment length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SelectFishery", "Average price per pound:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SelectFishery", "Fishery-specific landing port:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Fisheries", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))
