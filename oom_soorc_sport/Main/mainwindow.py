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
from Tools.mapscale import *
# UI specific includes
from mainwindow_ui import Ui_MainWindow
# General system includes
import sys,string,time

  
# Main window used for houseing the canvas, toolbars, and dialogs
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

    # A place to store polygons we capture
    #self.capturedPolygons = []
    #self.capturedPolygonsPennies = []
    #self.capturedPolygonsRub = []
    #
    # Interview info to write in shapefile
    #self.interviewInfo = []

    self.layers = []

    # Legend for displaying layers
    self.legend = Legend(self)
    
    # New Map Tools
    self.maptools = MapTools(self)
    
    # New Map Coords display in status bar
    self.mapcoords = MapCoords(self)
    
    self.mapscale = MapScale(self)

    #Uncomment to run the pre-load of data
    self.loadBaseDataLayers()

    time.sleep(2)
    self.splash.hide()

  def loadBaseDataLayers(self):

    # Set units to meters
    self.canvas.setMapUnits(QGis.units(0))
    self.canvas.updateScale()
    
    rasterList = [["Data/Trin2Blanco.tif"], #,40000,1200000], # these are just the scale vals from the prev set -- we aren't using them here
                  ["Data/SwWash.tif"], #,800001,5000000],
                  ["Data/Yaq2Col.tif"], #,300001,800000],
                  ["Data/Blanco2Yaq.tif"] #,40000,300000]   
                  ]    
    
    self.rasterBaseLayer = OOMLayer(self)
    
    self.extent_raster = None
    for i in range(len(rasterList)):
      rasterSet = rasterList[i]
      
      raster = rasterSet[0]
      #minScale = rasterSet[1]
      #maxScale = rasterSet[2]
      
      info = QFileInfo(QString(raster))
      
      # create layer
      layer = QgsRasterLayer(info.filePath(), info.completeBaseName())

      if i == 3: # Cafe Blanco 2 Yaquino Head
        self.extent_raster = layer        

      if self.srs == None:
        self.srs = layer.srs()
      
      # Set the scales
      #layer.setScaleBasedVisibility(True)
      #layer.setMinScale(minScale)
      #layer.setMaxScale(maxScale)
      
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
      self.rasterBaseLayer.addLayerItem(layer,cl)
      
    #Add one base raster item to legend
    self.legend.addRasterLegendItem("Nautical Charts",
                                    self.rasterBaseLayer.getCls())
    

    # now add the study region as a vector layer
    vectorList = [["Data/Soorc_sr.shp"]] #,60000,1200000]]
    for vectorSet in vectorList:
      vector = vectorSet[0]
      #minScale = vectorSet[1]
      #maxScale = vectorSet[2]
      
      info = QFileInfo(QString(vector))
      # create layer
      layer = QgsVectorLayer(info.filePath(), info.completeBaseName(), "ogr")
      if not layer.isValid():
        capture_string = QString("ERROR reading file")
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
      
      # Set the scales
      #layer.setScaleBasedVisibility(True)
      #layer.setMinScale(minScale)
      #layer.setMaxScale(maxScale)
      
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      layer.setTransparency(50)
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      cl.setVisible(False) # off by default
      self.canvas.setLayerSet(self.layers)
      
      #Add item to legend
      self.legend.addVectorLegendItem("Study Region", [cl])
      
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
  
    
