# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythoninterp.ui'
#
# Created: Thu Nov 29 19:22:01 2007
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PythonWin(object):
    def setupUi(self, PythonWin):
        PythonWin.setObjectName("PythonWin")
        PythonWin.resize(QtCore.QSize(QtCore.QRect(0,0,600,476).size()).expandedTo(PythonWin.minimumSizeHint()))

        self.label_1 = QtGui.QLabel(PythonWin)
        self.label_1.setGeometry(QtCore.QRect(10,420,31,21))
        self.label_1.setObjectName("label_1")

        self.line_1 = QtGui.QLineEdit(PythonWin)
        self.line_1.setEnabled(True)
        self.line_1.setGeometry(QtCore.QRect(60,417,511,22))
        self.line_1.setObjectName("line_1")

        self.pbnFinished = QtGui.QPushButton(PythonWin)
        self.pbnFinished.setEnabled(False)
        self.pbnFinished.setGeometry(QtCore.QRect(490,440,83,28))
        self.pbnFinished.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pbnFinished.setObjectName("pbnFinished")

        self.retranslateUi(PythonWin)
        QtCore.QMetaObject.connectSlotsByName(PythonWin)

    def retranslateUi(self, PythonWin):
        PythonWin.setWindowTitle(QtGui.QApplication.translate("PythonWin", "OpenOceanMap - Python Console", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("PythonWin", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("PythonWin", "Close", None, QtGui.QApplication.UnicodeUTF8))

