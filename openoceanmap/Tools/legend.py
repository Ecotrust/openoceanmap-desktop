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
class Legend(object):
  def __init__(self, parent):
    # Get List Widget
    self.listWidget = parent.listWidget

  # Add Item To Legend
  def addRasterLegendItem(self, name, layer):
    item_new = QListWidgetItem( name, self.listWidget)
    pm = QPixmap(20,20)
    layer.drawThumbnail(pm)
    icon = QIcon(pm)
    item_new.setIcon(icon)

  # Add Item To Legend
  def addVectorLegendItem(self, name, layer):
    item_new = QListWidgetItem(name, self.listWidget)
    pm = QPixmap(20,20)
    pm.fill(layer.renderer().symbols()[0].fillColor())
    icon = QIcon(pm)
    item_new.setIcon(icon)

  # Remove Item To Legend
  def removeLegendItem(self, name):
    item_remove = self.listWidget.findItems(name, Qt.MatchExactly)
    #Remove the item

  
