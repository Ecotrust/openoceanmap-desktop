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
# Custom Tools
from Tools.maptools import *
from Tools.legend import *
from Tools.mapcoords import *
# UI specific includes
from mainwindow_ui import Ui_MainWindow
# General system includes
import sys,string

  
# Main window used for houseing the canvas, toolbars, and dialogs
class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self):
    QMainWindow.__init__(self)

    # required by Qt4 to initialize the UI
    self.setupUi(self)

    # create map canvas
    self.canvas = QgsMapCanvas(self)
    self.canvas.setCanvasColor(QColor(255,255,255))
    self.canvas.enableAntiAliasing(True)
    self.canvas.useQImageToRender(False)
    self.canvas.show()
    self.canvas.parentWin = self

    # lay our widgets out in the main window
    self.layout = QVBoxLayout(self.frameMap)
    self.layout.addWidget(self.canvas)
    # We need to initialize the window sizes
    self.splitter.setSizes([100,600])

    ## A place to store polygons we capture
    #self.capturedPolygons = []
    #self.capturedPolygonsPennies = []
    #self.capturedPolygonsRub = []
    #
    ## Interview info to write in shapefile
    #self.interviewInfo = []

    self.layers = []

    # Legend for displaying layers
    self.legend = Legend(self)
    
    # New Map Tools
    self.maptools = MapTools(self)
    
    # New Map Coords display in status bar
    self.mapcoords = MapCoords(self)

    self.loadDataLayers()

  def loadDataLayers(self):
    # Set units to meters
    self.canvas.setMapUnits(QGis.units(0))
    self.canvas.updateScale()
    rasterList = [["Data/noaa_7_albs34.tif",1500000,4000000],
                  ["Data/noaa_8_albs34.tif",500000,1500000],
                  ["Data/noaa_9_albs34.tif",250000,500000],
                  ["Data/noaa_10_albs34.tif",125000,250000],
                  ["Data/noaa_11_albs34.tif",85000,125000],
                  ["Data/noaa_12_albs34.tif",0,85000]]
    self.rasterBaseLayer = OOMLayer(self)
    for rasterSet in rasterList:
      raster = rasterSet[0]
      minScale = rasterSet[1]
      maxScale = rasterSet[2]
      
      info = QFileInfo(QString(raster))
      
      # create layer
      layer = QgsRasterLayer(info.filePath(), info.completeBaseName())

      # Set the scales
      layer.setScaleBasedVisibility(True)
      layer.setMinScale(minScale)
      layer.setMaxScale(maxScale)
      
      if not layer.isValid():
        capture_string = QString("ERROR reading file")
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      # set extent to the extent of our layer
      self.canvas.setExtent(layer.extent())
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      self.canvas.setLayerSet(self.layers)
      self.rasterBaseLayer.addLayerItem(layer,cl)
      
    #Add one base raster item to legend
    self.legend.addRasterLegendItem("NOAA ENC",
                                    self.rasterBaseLayer.getCls())

    vectorList = [["Data/NccKayakAccessPt.shp",0,125000]]
    #vectorList = ["Data/Ca_Counties_Simp.shp",
                  #"Data/NccDepthLineFa.shp",
                  #"Data/NccKayakAccessPt.shp"]
    for vectorSet in vectorList:
      vector = vectorSet[0]
      minScale = vectorSet[1]
      maxScale = vectorSet[2]
      
      info = QFileInfo(QString(vector))
      # create layer
      layer = QgsVectorLayer(info.filePath(), info.completeBaseName(), "ogr")
      if not layer.isValid():
        capture_string = QString("ERROR reading file")
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
      
      # Set the scales
      layer.setScaleBasedVisibility(True)
      layer.setMinScale(minScale)
      layer.setMaxScale(maxScale)

      layer.label().setLabelField(QgsLabel.Text, 1)
      layer.setLabelOn(True)
      label = layer.label()
      labelAt = label.layerAttributes()
      labelAt.setBold(True)
      labelAt.setBufferEnabled(True)
      labelAt.setOffset(0,-50,QgsLabelAttributes.Units(0))
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      # set extent to the extent of our layer
      #self.canvas.setExtent(layer.extent())
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      self.canvas.setLayerSet(self.layers)
      #Add item to legend
      self.legend.addVectorLegendItem(info.completeBaseName(), [cl])
      


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
  
    
