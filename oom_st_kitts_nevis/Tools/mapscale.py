#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
# Copyright (C) 2007  Aaron Racicot
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
class MapScale(object):
  def __init__(self, parent):
    self.parent = parent
    # This one is to capture the mouse move for coordinate display
    QObject.connect(parent.canvas, SIGNAL("scaleChanged(double)"),
                    self.updateScaleDisplay)
    self.scale = QLabel("1:" + str( parent.canvas.getScale() ))
    self.scale.setFixedWidth(200)
    self.scale.setAlignment(Qt.AlignHCenter)
    self.scale.setFrameStyle(QFrame.StyledPanel)
    self.parent.statusbar.addPermanentWidget(self.scale)

  # Signal handeler for updating coord display
  def updateScaleDisplay(self, p):
    str_scale = str(p)
    str_parts = str_scale.split('.')
    if int(str_parts[0]) > 0:
        capture_string = QString("1:" + str_parts[0])
    else:
        capture_string = QString("1:" + str_scale)
        
    #self.statusbar.showMessage(capture_string)
    self.scale.setText(capture_string)



  
