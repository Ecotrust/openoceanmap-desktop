#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer
# 
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
# General system includes
import sys,string


  
# Main window used for houseing the canvas, toolbars, and dialogs
class MapCoords(object):
  def __init__(self, parent):
    self.parent = parent
    # This one is to capture the mouse move for coordinate display
    QObject.connect(parent.canvas, SIGNAL("xyCoordinates(QgsPoint&)"),
                    self.updateCoordsDisplay)
    self.latlon = QLabel("0.0 , 0.0")
    self.latlon.setFixedWidth(200)
    self.latlon.setAlignment(Qt.AlignHCenter)
    self.latlon.setFrameStyle(QFrame.StyledPanel)
    self.parent.statusbar.addPermanentWidget(self.latlon)

  # Signal handeler for updating coord display
  def updateCoordsDisplay(self, p):
    capture_string = QString(str(p.x()) + " , " +
                             str(p.y()))
    #self.statusbar.showMessage(capture_string)
    self.latlon.setText(capture_string)



  
