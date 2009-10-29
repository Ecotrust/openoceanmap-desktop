#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
# Copyright (C) 2007  Aaron Racicot
# Copyright (C) 2009  Grant Gilron, Ecotrust Canada
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
# Custom Tools
from Tools.maptools import *
from Tools.legend import *
from Tools.mapcoords import *
from Tools.mapscale import *
# UI specific includes
from mainwindow_ui import Ui_MainWindow
# General system includes
import sys,string,time

# Main window used for housing the canvas, tool bars, and dialogs
class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self,splash):
    QMainWindow.__init__(self)

    # required by Qt4 to initialize the UI
    self.setupUi(self)
    self.splash = splash
       
    # create map canvas
    self.canvas = QgsMapCanvas(self)
    self.canvas.setCanvasColor(QColor(255,255,255))
    self.canvas.enableAntiAliasing(True)
    self.canvas.useQImageToRender(False)
    self.canvas.show()
    self.canvas.parentWin = self
    self.srs = None
    
    # lay our widgets out in the main window
    self.layout = QVBoxLayout(self.frameMap)
    self.layout.addWidget(self.canvas)

    # We need to initialize the window sizes
    self.splitter.setSizes([175,800])

    self.layers = []

    # Legend for displaying layers
    self.legend = Legend(self)
    
    # New Map Tools
    self.maptools = MapTools(self)
    
    # New Map Coords display in status bar
    self.mapcoords = MapCoords(self)
    
    self.mapscale = MapScale(self)

    # pre-load data
    self.loadBaseDataLayers()

    # give them some time to enjoy the splash screen
    time.sleep(2)
    
    self.splash.hide()

  def loadBaseDataLayers(self):

    # Set units to meters
    self.canvas.setMapUnits(QGis.units(0))
    self.canvas.updateScale()
    
    # compile list of tif files to use in the app
    # Note: the first one is the Open Sea Nautical Chart,
    # subsequent ones get added as Coastal Nautical Charts
    rasterList = [["Data/3000011.tif",0,50000000],
                  ["Data/north_coast_queen_charlotte.tif",0,50000000],    
                  ["Data/vancouver_island.tif",0,50000000],]    
    
    self.rasterBaseLayer = OOMLayer(self)
    self.openSeaRasterBaseLayer = OOMLayer(self)
    
    self.extent_raster = None

    for i in range(len(rasterList)):
      rasterSet = rasterList[i]
      
      raster = rasterSet[0]
      minScale = rasterSet[1]
      maxScale = rasterSet[2]
      
      info = QFileInfo(QString(raster))
      
      # create layer
      layer = QgsRasterLayer(info.filePath(), info.completeBaseName())

      # set the initial extent on the entire BC Coast
      if i == 0:
        self.extent_raster = layer        

      if self.srs == None:
        self.srs = layer.srs()
      
      # Set the scales
      layer.setScaleBasedVisibility(True)
      layer.setMinScale(minScale)
      layer.setMaxScale(maxScale)
      
      if not layer.isValid():
        capture_string = QString("ERROR reading file")
        self.statusbar.showMessage(capture_string)
        return
        
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      self.canvas.setLayerSet(self.layers)
      
      if i == 0:
        self.openSeaRasterBaseLayer.addLayerItem(layer,cl)
        cl.setVisible(True) # on by default
      else:
        self.rasterBaseLayer.addLayerItem(layer,cl)
            
    # Add base raster items to legend
    self.legend.addRasterLegendItem("BC Coast Chart 1:525,000",
                                    self.rasterBaseLayer.getCls())
    self.legend.addRasterLegendItem("BC Coast Chart 1:1,250,000",
                                    self.openSeaRasterBaseLayer.getCls())
    
    # now add the study region as a vector layer
    vectorList = []
    for vectorSet in vectorList:
      vector = vectorSet[0]
      
      info = QFileInfo(QString(vector))
      
      # create layer
      layer = QgsVectorLayer(info.filePath(), info.completeBaseName(), "ogr")
      
      if not layer.isValid():
        capture_string = QString("ERROR reading file")
        self.statusbar.showMessage(capture_string)
        return
      
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      layer.setTransparency(50)
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      cl.setVisible(False) # off by default
      self.canvas.setLayerSet(self.layers)
      
    self.canvas.setExtent(self.extent_raster.extent())    

class OOMLayer(object):
  def __init__(self, parent):
    # Get parent
    self.parent = parent
    self.layers = []
    
  # Add a data layer to this OOMLayer
  def addLayerItem(self, layer,cl):
    self.layers.insert(0,[layer,cl])

  # get layer
  def getLayerItem(self, index):
    return self.layers[index]

  # get cls
  def getCls(self):
    cls = []
    for layer in self.layers:
      cls.append(layer[1])
    return cls

  def turnLayersOff(self):
    # Here we can turn off the whole set of layers
    for layer in self.layers:
      # set the layer visibility to off
      layer[1].setVisible(False)
  
  def turnLayersOn(self):
    # Here we can turn off the whole set of layers
    for layer in self.layers:
      # set the layer visibility to on
      layer[1].setVisible(True)
  
    
