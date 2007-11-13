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



# Legend Check Box
class LegendCheckBox(QCheckBox):
  def __init__(self, parent, name, canvasLayers):
    QCheckBox.__init__(self, name)
    self.parent = parent
    self.name = name
    self.cls = canvasLayers
    self.app = qApp
    self.removeIcon = QIcon()
    self.removeIcon.addPixmap(self.app.style().standardPixmap(QStyle.SP_FileIcon))        
    self.act1 = QAction(self.removeIcon, "Remove Layer", self)
    QObject.connect(self.act1, SIGNAL("triggered()"), self.action1)
    self.setCheckState(Qt.Checked)
    QObject.connect(self, SIGNAL("refresh()"),
                    self.parent.parent.canvas, SLOT("layerStateChange()"))

  def mousePressEvent(self, event):
    if event.button() == Qt.RightButton:
      # custom menu for layer
      #print "right click"
      self.menu = QMenu(self)
      self.menu.addAction(self.act1)
      self.menu.exec_(QCursor.pos())
    else:
      QCheckBox.mousePressEvent(self,event)
    
  def action1(self):
    #print "Action1"
    self.hide()
    self.parent.removeLegendItem(self)
    for cl in self.cls:
      self.parent.parent.layers.remove(cl)
    self.parent.parent.canvas.setLayerSet(self.parent.parent.layers)

  # Update Layer status
  def updateLayerStatus(self, state):
    cls = self.cls
    for cl in cls:
      if state == Qt.Unchecked:
        cl.setVisible(False)
        #self.emit(SIGNAL("refresh()"))
        self.parent.parent.canvas.setLayerSet(self.parent.parent.layers)
      else:
        cl.setVisible(True)
        #self.emit(SIGNAL("refresh()"))
        self.parent.parent.canvas.setLayerSet(self.parent.parent.layers)
      # Debug
      capture_string = QString("Setting layer visibility for layer " +
                               cl.layer().name() + " " + str(cl.visible()))
      self.parent.parent.statusbar.showMessage(capture_string)
  


# Main window used for houseing the canvas, toolbars, and dialogs
class Legend(object):
  def __init__(self, parent):
    # Get List Widget
    #self.listWidget = parent.listWidget
    self.parent = parent
    # Get List Widget
    self.groupBox = parent.groupBox
    self.groupBoxLayout = QVBoxLayout()
    self.groupBoxLayout.setAlignment(Qt.AlignTop)
    self.groupBox.setLayout(self.groupBoxLayout)

  # Add Item To Legend
  def addRasterLegendItem(self, name, cls):
    item_new = LegendCheckBox(self, name, cls)
    QObject.connect(item_new, SIGNAL("stateChanged(int)"),
                 item_new.updateLayerStatus)
    pm = QPixmap(20,20)
    cls[0].layer().drawThumbnail(pm)
    icon = QIcon(pm)
    item_new.setIcon(icon)
    self.groupBoxLayout.addWidget(item_new)

  # Add Item To Legend
  def addVectorLegendItem(self, name, cls):
    item_new = LegendCheckBox(self, name, cls)
    QObject.connect(item_new, SIGNAL("stateChanged(int)"),
                 item_new.updateLayerStatus)    
    pm = QPixmap(20,20)
    pm.fill(cls[0].layer().renderer().symbols()[0].fillColor())
    icon = QIcon(pm)
    item_new.setIcon(icon)
    self.groupBoxLayout.addWidget(item_new)

  # Remove Item To Legend
  def removeLegendItem(self, widget):
    #Remove the item
    self.groupBoxLayout.removeWidget(widget)
  

