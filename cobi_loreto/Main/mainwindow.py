#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer
# Copyright (C) 2008  Tim Welch
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
from PyQt4.QtGui import QApplication as QA
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
from Tools.maptools import *
from Tools.legend import *
from Tools.mapcoords import *
# UI specific includes
from mainwindow_ui import Ui_MainWindow
from language_dialog import LanguageDialog
# General system includes
import sys,string,time
import pdb
pyqtRemoveInputHook()

  
# Main window used for houseing the canvas, toolbars, and dialogs
class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self,splash):
    QMainWindow.__init__(self)

    # required by Qt4 to initialize the UI
    self.setupUi(self)
    self.splash = splash
    self.retranslate()
    
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

    #Uncomment to run the pre-load of data
    self.loadBaseDataLayers()

    time.sleep(2)
    self.splash.hide()

  def loadBaseDataLayers(self):

    # Set units to meters
    self.canvas.setMapUnits(QGis.units(0))
    self.canvas.updateScale()
    # set extent to the extent of our layer
    #self.canvas.setExtent(QgsRect(-340000,-70000,
    #                              -191000,52500))
    
    rasterList = [["Data/Loreto_base.tif",10000,5000000]]
    self.rasterBaseLayer = OOMLayer(self)
    
    first_raster = None
    for i in range(len(rasterList)):
      rasterSet = rasterList[i]

      raster = rasterSet[0]
      minScale = rasterSet[1]
      maxScale = rasterSet[2]
      
      info = QFileInfo(QString(raster))
      
      # create layer
      layer = QgsRasterLayer(info.filePath(), info.completeBaseName())
      # turn off contrast enhancement
      layer.setContrastEnhancementAlgorithm(QString("NO_STRETCH"))

      if i == 0:
        first_raster = layer        

      if self.srs == None:
        self.srs = layer.srs()
        #pdb.set_trace()
        print 'mainwindow: setting srs from layers.srs()...'
        print self.srs.epsg().__str__()
      
      # Set the scales
      layer.setScaleBasedVisibility(True)
      layer.setMinScale(minScale)
      layer.setMaxScale(maxScale)
      
      if not layer.isValid():
        capture_string = QString(self.file_error_str)
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      # set extent to the extent of our layer
      #self.canvas.setExtent(layer.extent())
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      self.canvas.setLayerSet(self.layers)
      self.rasterBaseLayer.addLayerItem(layer,cl)
      
    #Add one base raster item to legend
    self.legend.addRasterLegendItem(self.loreto_base_str,
                                    self.rasterBaseLayer.getCls())

    vectorList = [["Data/Aprov_Susten.shp",self.study_area_str, 0,5000000],
                  ["Data/Bathymetry.shp",self.bathymetry_str, 0,5000000],
                  ["Data/Zona_Restringido.shp",self.restricted_zone_str, 0,5000000],
                  ["Data/Zona_Proteccion.shp",self.protected_zone_str, 0,5000000],                                   
                  ["Data/Zona_Proteccion_Points.shp",self.protected_point_str, 0,5000000],
                  ["Data/Seamounts.shp",self.seamount_str, 0,5000000],
                  ["Data/Reference_Points.shp",self.ref_point_str, 0, 300000],
                  ]
    for vectorSet in vectorList:
      vector = vectorSet[0]
      minScale = vectorSet[2]
      maxScale = vectorSet[3]
      
      info = QFileInfo(QString(vector))
      # create layer
      layer = QgsVectorLayer(info.filePath(), info.completeBaseName(), "ogr")
      if not layer.isValid():
        capture_string = QString(self.file_error_str)
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
      
      # Set the scales
      layer.setScaleBasedVisibility(True)
      layer.setMinScale(minScale)
      layer.setMaxScale(maxScale)

      layer_on = Qt.Checked
      if vector == "Data/Aprov_Susten.shp":
        layer.renderer().symbols()[0].setColor(QColor('Black'))
        layer.renderer().symbols()[0].setFillStyle(Qt.NoBrush)          
      elif vector == 'Data/Zona_Proteccion_Points.shp':
        layer.renderer().symbols()[0].setPointSize(10)
        layer.renderer().symbols()[0].setNamedPointSymbol("hard:triangle")
        layer.renderer().symbols()[0].setFillColor(QColor("Red"))
      elif vector == 'Data/Seamounts.shp':
        layer.renderer().symbols()[0].setPointSize(9)
        layer.renderer().symbols()[0].setFillColor(QColor(200,84,232))
      elif vector == "Data/Zona_Restringido.shp":
        layer.renderer().symbols()[0].setColor(QColor(220,147,0))
        layer.renderer().symbols()[0].setFillColor(QColor(255,170,0))
        layer.renderer().symbols()[0].setFillStyle(Qt.FDiagPattern)
      elif vector == "Data/Zona_Proteccion.shp":
        layer.renderer().symbols()[0].setColor(QColor(192,0,0))
        layer.renderer().symbols()[0].setFillColor(QColor(221,48,18))
        layer.renderer().symbols()[0].setFillStyle(Qt.Dense7Pattern)
      elif vector == "Data/Bathymetry.shp":
        layer.renderer().symbols()[0].setPointSize(8)
        layer.renderer().symbols()[0].setLineWidth(1)
        layer.renderer().symbols()[0].setColor(QColor(8,83,137))
        layer_on = Qt.Unchecked
      elif vector == 'Data/Reference_Points.shp':
        layer.renderer().symbols()[0].setPointSize(9)
        layer.renderer().symbols()[0].setFillColor(QColor(255,170,0))
        layer.setLabelOn(True)
        layer.label().setLabelField(0,0)
        layer.label().layerAttributes().setSize(8,1)
        layer.label().layerAttributes().setAlignment(3)
        print layer.label().layerAttributes().offsetType()        
        layer.label().layerAttributes().setOffset(4,2,1)
        layer.label().layerAttributes().setBufferEnabled(True)
        layer.label().layerAttributes().setBufferColor(QColor(250,250,250))
      # add layer to the registry
      QgsMapLayerRegistry.instance().addMapLayer(layer)
      
      # set the map canvas layer set
      cl = QgsMapCanvasLayer(layer)
      self.layers.insert(0,cl)
      self.canvas.setLayerSet(self.layers)
      #Add item to legend
      self.legend.addVectorLegendItem(vectorSet[1],[cl],layer_on)
    self.canvas.setExtent(first_raster.extent())

  def retranslate(self):
    self.file_error_str = QA.translate("MainWindow", "ERROR reading file", "message when failing to load a map layer", QA.UnicodeUTF8)    
    self.loreto_base_str = QA.translate("MainWindow", "Loreto Base Map", "map legend text for base layer", QA.UnicodeUTF8)
    self.study_area_str = QA.translate("MainWindow", "Study Area", "", QA.UnicodeUTF8)
    self.bathymetry_str = QA.translate("MainWindow", "Bathymetry", "", QA.UnicodeUTF8)
    self.restricted_zone_str = QA.translate("MainWindow", "Restricted Zones", "", QA.UnicodeUTF8)
    self.protected_zone_str = QA.translate("MainWindow", "Protecteded Zones", "", QA.UnicodeUTF8)
    self.protected_point_str = QA.translate("MainWindow", "Protected Zones (pts)", "", QA.UnicodeUTF8)
    self.seamount_str = QA.translate("MainWindow", "Seamounts", "", QA.UnicodeUTF8)
    self.ref_point_str = QA.translate("MainWindow", "Reference Points", "", QA.UnicodeUTF8)

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
