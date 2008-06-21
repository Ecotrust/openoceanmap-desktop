#!/usr/bin/python
#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer 
#---------------------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------


# PyQt4 includes for python bindings to QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
from Main.mainwindow import *
# General system includes
import sys

# Path to local QGIS install
qgis_prefix = "C:\Program Files\Quantum GIS"


# Main entry to program.  Set up the main app and create a new window.
def main(argv):
  
  # create Qt application
  app = QApplication(argv,True)
  #app = QgsApplication(argv,True)
  
  # Set the app style
  app.setStyle(QString("plastique"))
  
  mySplashPix = QPixmap(QString("Data/OCEAN.png"))
  mySplashPixScaled = mySplashPix.scaled(500,300,Qt.KeepAspectRatio)
  mySplash = QSplashScreen(mySplashPixScaled)
  mySplash.show()
  
  # initialize qgis libraries
  QgsApplication.setPrefixPath(qgis_prefix, True)
  QgsApplication.initQgis()
  #app.setPrefixPath(qgis_prefix, True)
  #app.initQgis()

  # create main window
  wnd = MainWindow(mySplash)
  wnd.show()

  # Create signal for app finish
  app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
  
  # Start the app up
  retval = app.exec_()
  
  # We got an exit signal so time to clean up
  QgsApplication.exitQgis()
  #app.exitQgis()
  
  sys.exit(retval)


if __name__ == "__main__":
  main(sys.argv)

