# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'language_dialog.ui'
#
# Created: Mon Mar 23 14:44:18 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LanguageDialog(object):
    def setupUi(self, LanguageDialog):
        LanguageDialog.setObjectName("LanguageDialog")
        LanguageDialog.resize(152, 112)
        self.hboxlayout = QtGui.QHBoxLayout(LanguageDialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.groupBox = QtGui.QGroupBox(LanguageDialog)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.english_button = QtGui.QPushButton(self.groupBox)
        self.english_button.setObjectName("english_button")
        self.vboxlayout.addWidget(self.english_button)
        self.spanish_button = QtGui.QPushButton(self.groupBox)
        self.spanish_button.setObjectName("spanish_button")
        self.vboxlayout.addWidget(self.spanish_button)
        self.hboxlayout.addWidget(self.groupBox)

        self.retranslateUi(LanguageDialog)
        QtCore.QMetaObject.connectSlotsByName(LanguageDialog)

    def retranslateUi(self, LanguageDialog):
        LanguageDialog.setWindowTitle(QtGui.QApplication.translate("LanguageDialog", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("LanguageDialog", "Select a Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.english_button.setText(QtGui.QApplication.translate("LanguageDialog", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.spanish_button.setText(QtGui.QApplication.translate("LanguageDialog", "Spanish", None, QtGui.QApplication.UnicodeUTF8))

