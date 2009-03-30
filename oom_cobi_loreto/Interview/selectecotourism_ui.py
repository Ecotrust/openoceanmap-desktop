# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectecotourism.ui'
#
# Created: Sun Mar 29 17:20:48 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectEcotourism(object):
    def setupUi(self, SelectEcotourism):
        SelectEcotourism.setObjectName("SelectEcotourism")
        SelectEcotourism.resize(281, 152)
        self.verticalLayout = QtGui.QVBoxLayout(SelectEcotourism)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(SelectEcotourism)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setObjectName("hboxlayout")
        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)
        self.comboActivity = QtGui.QComboBox(self.widget)
        self.comboActivity.setObjectName("comboActivity")
        self.comboActivity.addItem(QtCore.QString())
        self.comboActivity.setItemText(0, "")
        self.comboActivity.addItem(QtCore.QString())
        self.comboActivity.addItem(QtCore.QString())
        self.comboActivity.addItem(QtCore.QString())
        self.comboActivity.addItem(QtCore.QString())
        self.comboActivity.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.comboActivity)
        self.verticalLayout.addWidget(self.widget)
        self.other_wrap = QtGui.QWidget(SelectEcotourism)
        self.other_wrap.setEnabled(True)
        self.other_wrap.setObjectName("other_wrap")
        self._2 = QtGui.QHBoxLayout(self.other_wrap)
        self._2.setObjectName("_2")
        self.fishery_text_2 = QtGui.QLabel(self.other_wrap)
        self.fishery_text_2.setObjectName("fishery_text_2")
        self._2.addWidget(self.fishery_text_2)
        self.other_line = QtGui.QLineEdit(self.other_wrap)
        self.other_line.setEnabled(False)
        self.other_line.setMinimumSize(QtCore.QSize(50, 0))
        self.other_line.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.other_line.setFont(font)
        self.other_line.setObjectName("other_line")
        self._2.addWidget(self.other_line)
        self.verticalLayout.addWidget(self.other_wrap)
        self.widget_2 = QtGui.QWidget(SelectEcotourism)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.pbnFinished = QtGui.QPushButton(self.widget_2)
        self.pbnFinished.setObjectName("pbnFinished")
        self.hboxlayout1.addWidget(self.pbnFinished)
        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(SelectEcotourism)
        QtCore.QMetaObject.connectSlotsByName(SelectEcotourism)

    def retranslateUi(self, SelectEcotourism):
        SelectEcotourism.setWindowTitle(QtGui.QApplication.translate("SelectEcotourism", "OpenOceanMap - Select Ecotourism", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectEcotourism", "Select tourism activity type:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboActivity.setItemText(1, QtGui.QApplication.translate("SelectEcotourism", "Diving", None, QtGui.QApplication.UnicodeUTF8))
        self.comboActivity.setItemText(2, QtGui.QApplication.translate("SelectEcotourism", "Snorkeling", None, QtGui.QApplication.UnicodeUTF8))
        self.comboActivity.setItemText(3, QtGui.QApplication.translate("SelectEcotourism", "Kayaking", None, QtGui.QApplication.UnicodeUTF8))
        self.comboActivity.setItemText(4, QtGui.QApplication.translate("SelectEcotourism", "Marine Fauna Watching", None, QtGui.QApplication.UnicodeUTF8))
        self.comboActivity.setItemText(5, QtGui.QApplication.translate("SelectEcotourism", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text_2.setText(QtGui.QApplication.translate("SelectEcotourism", "    Other activity:", None, QtGui.QApplication.UnicodeUTF8))
        self.other_line.setText(QtGui.QApplication.translate("SelectEcotourism", "other activity", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("SelectEcotourism", "Exit Ecotourism Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectEcotourism", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

