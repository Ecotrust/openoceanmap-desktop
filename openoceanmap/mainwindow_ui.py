# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jun 13 23:16:20 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,931,639).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frameMap = QtGui.QFrame(self.centralwidget)
        self.frameMap.setGeometry(QtCore.QRect(9,9,911,541))
        self.frameMap.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMap.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMap.setObjectName("frameMap")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,931,24))
        self.menubar.setObjectName("menubar")

        self.menuInterview = QtGui.QMenu(self.menubar)
        self.menuInterview.setObjectName("menuInterview")

        self.menuMap = QtGui.QMenu(self.menubar)
        self.menuMap.setObjectName("menuMap")

        self.menuUtilities = QtGui.QMenu(self.menubar)
        self.menuUtilities.setObjectName("menuUtilities")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mpActionZoomOut = QtGui.QAction(MainWindow)
        self.mpActionZoomOut.setIcon(QtGui.QIcon(":/images/mActionZoomOut.png"))
        self.mpActionZoomOut.setObjectName("mpActionZoomOut")

        self.mpActionPan = QtGui.QAction(MainWindow)
        self.mpActionPan.setIcon(QtGui.QIcon(":/images/mActionPan.png"))
        self.mpActionPan.setObjectName("mpActionPan")

        self.mpActionAddRasterLayer = QtGui.QAction(MainWindow)
        self.mpActionAddRasterLayer.setIcon(QtGui.QIcon(":/images/mActionAddRasterLayer.png"))
        self.mpActionAddRasterLayer.setObjectName("mpActionAddRasterLayer")

        self.actionStart_Interview = QtGui.QAction(MainWindow)
        self.actionStart_Interview.setIcon(QtGui.QIcon(":/images/mActionStartEditing.png"))
        self.actionStart_Interview.setObjectName("actionStart_Interview")

        self.actionRegion_Tool = QtGui.QAction(MainWindow)
        self.actionRegion_Tool.setIcon(QtGui.QIcon(":/images/mActionMeasureArea.png"))
        self.actionRegion_Tool.setObjectName("actionRegion_Tool")

        self.actionPolygon_Tool = QtGui.QAction(MainWindow)
        self.actionPolygon_Tool.setIcon(QtGui.QIcon(":/images/mActionCapturePolygon.png"))
        self.actionPolygon_Tool.setObjectName("actionPolygon_Tool")

        self.mpActionZoomIn = QtGui.QAction(MainWindow)
        self.mpActionZoomIn.setIcon(QtGui.QIcon(":/images/mActionZoomIn.png"))
        self.mpActionZoomIn.setObjectName("mpActionZoomIn")

        self.mpActionAddVectorLayer = QtGui.QAction(MainWindow)
        self.mpActionAddVectorLayer.setIcon(QtGui.QIcon(":/images/mActionAddLayer.png"))
        self.mpActionAddVectorLayer.setObjectName("mpActionAddVectorLayer")

        self.actionPython_Console = QtGui.QAction(MainWindow)
        self.actionPython_Console.setIcon(QtGui.QIcon(":/images/mIconProperties.png"))
        self.actionPython_Console.setObjectName("actionPython_Console")
        self.menuInterview.addAction(self.actionStart_Interview)
        self.menuMap.addAction(self.mpActionAddRasterLayer)
        self.menuMap.addAction(self.mpActionAddVectorLayer)
        self.menuMap.addSeparator()
        self.menuMap.addAction(self.mpActionZoomIn)
        self.menuMap.addAction(self.mpActionZoomOut)
        self.menuMap.addAction(self.mpActionPan)
        self.menuMap.addAction(self.actionRegion_Tool)
        self.menuUtilities.addAction(self.actionPython_Console)
        self.menubar.addAction(self.menuMap.menuAction())
        self.menubar.addAction(self.menuInterview.menuAction())
        self.menubar.addAction(self.menuUtilities.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInterview.setTitle(QtGui.QApplication.translate("MainWindow", "Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMap.setTitle(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUtilities.setTitle(QtGui.QApplication.translate("MainWindow", "Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionAddRasterLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setText(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setIconText(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setToolTip(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegion_Tool.setText(QtGui.QApplication.translate("MainWindow", "Region Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPolygon_Tool.setText(QtGui.QApplication.translate("MainWindow", "Polygon Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionAddVectorLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython_Console.setText(QtGui.QApplication.translate("MainWindow", "Python Console", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
