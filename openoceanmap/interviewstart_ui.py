# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewstart.ui'
#
# Created: Tue Jun 12 07:52:45 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InterviewStart(object):
    def setupUi(self, InterviewStart):
        InterviewStart.setObjectName("InterviewStart")
        InterviewStart.resize(QtCore.QSize(QtCore.QRect(0,0,549,230).size()).expandedTo(InterviewStart.minimumSizeHint()))

        self.label_2 = QtGui.QLabel(InterviewStart)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(20,60,191,21))
        self.label_2.setObjectName("label_2")

        self.label_1 = QtGui.QLabel(InterviewStart)
        self.label_1.setGeometry(QtCore.QRect(20,20,191,21))
        self.label_1.setObjectName("label_1")

        self.line_1 = QtGui.QLineEdit(InterviewStart)
        self.line_1.setEnabled(True)
        self.line_1.setGeometry(QtCore.QRect(230,20,281,29))
        self.line_1.setObjectName("line_1")

        self.line_2 = QtGui.QLineEdit(InterviewStart)
        self.line_2.setGeometry(QtCore.QRect(230,60,281,29))
        self.line_2.setObjectName("line_2")

        self.pbnCancel = QtGui.QPushButton(InterviewStart)
        self.pbnCancel.setGeometry(QtCore.QRect(280,170,83,28))
        self.pbnCancel.setObjectName("pbnCancel")

        self.pbnStartShapes = QtGui.QPushButton(InterviewStart)
        self.pbnStartShapes.setGeometry(QtCore.QRect(370,170,151,28))
        self.pbnStartShapes.setObjectName("pbnStartShapes")

        self.retranslateUi(InterviewStart)
        QtCore.QMetaObject.connectSlotsByName(InterviewStart)

    def retranslateUi(self, InterviewStart):
        InterviewStart.setWindowTitle(QtGui.QApplication.translate("InterviewStart", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("InterviewStart", "Person Conducting Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("InterviewStart", "Person Being Interviewed", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("InterviewStart", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("InterviewStart", "Start Making Shapes", None, QtGui.QApplication.UnicodeUTF8))

