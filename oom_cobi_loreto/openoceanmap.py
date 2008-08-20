#!/usr/bin/python
#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer 
# Copyright (C) 2008  Tim Welch
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
from Main.language_dialog_ui import *
# General system includes
import sys
# Import OOM config
from config import *

class OpenOceanMap(QObject):

  def __init__(self, argv):
    self.app = QApplication(argv,True)

    self.appTranslator = QTranslator()
    #Get system locale
    #locale_name = QLocale.system().name()  
    #Start with spanish, this is hackish
    locale_name = 'es_MX'  
    if self.appTranslator.load("i18n/"+locale_name+".qm"):
      self.app.installTranslator(self.appTranslator)
      print 'translator installed'

    # Set the app style
    self.app.setStyle(QString("plastique"))
  
    mySplashPix = QPixmap(QString("Data/OCEAN.png"))
    mySplashPixScaled = mySplashPix.scaled(500,300,Qt.KeepAspectRatio)
    mySplash = QSplashScreen(mySplashPixScaled)
    mySplash.show()
    
    # initialize qgis libraries
    QgsApplication.setPrefixPath(qgis_prefix, True)
    QgsApplication.initQgis()

    # create main window
    self.win = MainWindow(mySplash)
    self.win.show()

    self.start_language_selection()

    # Create signal for app finish
    self.app.connect(self.app, SIGNAL("lastWindowClosed()"), self.app, SLOT("quit()"))
  
    # Start the app up
    retval = self.app.exec_()
  
    # We got an exit signal so time to clean up
    QgsApplication.exitQgis()

    sys.exit(retval)

  def start_language_selection(self):
    """Used for selecting language and translating if necessary"""
    self.language_dialog = LanguageDialog(self.win, self.finish_language_selection)
    QObject.connect(self.language_dialog, SIGNAL("language_selected"), self.finish_language_selection)
    self.language_dialog.show()
    
  def finish_language_selection(self, language):
    self.language = language
    self.language_dialog.hide()
    self.language_dialog.deleteLater()
    
    print language
    if language == 'english': 
      #Switch back to english, this is a hack
      self.app.removeTranslator(self.appTranslator)
      print "translator removed"
      self.win.retranslateUi(self.win)

#Start us off
if __name__ == "__main__":
  oom = OpenOceanMap(sys.argv)
