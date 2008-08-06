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
from PyQt4.QtGui import QApplication as QA
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# General system includes
import sys,string

from regiontool import *
from polygontool import *
#from Interview.interviewstart import *
from Interview.interview import *
# Python Shell
from Util.pythoninterp import *


  
# Main window used for houseing the canvas, toolbars, and dialogs
class MapTools(object):
  def __init__(self, parent):
    self.parent = parent
    self.canvas = parent.canvas
    self.statusbar = parent.statusbar
    self.legend = parent.legend
    self.layers = parent.layers
    self.retranslate()

    # create the actions behaviours
    QObject.connect(parent.mpActionAddVectorLayer, SIGNAL("triggered()"),
                 self.addVectorLayer)
    QObject.connect(parent.mpActionAddRasterLayer, SIGNAL("triggered()"),
                 self.addRasterLayer)
    QObject.connect(parent.mpActionZoomIn, SIGNAL("triggered()"), self.zoomIn)
    QObject.connect(parent.mpActionZoomOut, SIGNAL("triggered()"), self.zoomOut)
    QObject.connect(parent.mpActionPan, SIGNAL("triggered()"), self.pan)
    QObject.connect(parent.actionStart_Interview, SIGNAL("triggered()"),
                 self.interviewStart)
    QObject.connect(parent.actionRegion_Tool, SIGNAL("triggered()"),
                 self.updateBoundsFromRegion)
    QObject.connect(parent.actionPolygon_Tool, SIGNAL("triggered()"),
                 self.updatePolygon)
    QObject.connect(parent.actionPython_Console, SIGNAL("triggered()"),
                 self.startPythonConsole)

    # create a little toolbar for map tools
    self.toolbar = parent.addToolBar(self.file_bar_str)
    self.toolbar.addAction(parent.mpActionAddVectorLayer)
    self.toolbar.addAction(parent.mpActionAddRasterLayer)
    self.toolbar.addAction(parent.mpActionZoomIn)
    self.toolbar.addAction(parent.mpActionZoomOut)
    self.toolbar.addAction(parent.mpActionPan)
    self.toolbar.addAction(parent.actionRegion_Tool)

    # create a little toolbar for interview tools
    self.toolbar2 = parent.addToolBar(self.file_bar_2_str)
    self.toolbar2.addAction(parent.actionStart_Interview)

    # create a little toolbar for utilities
    #self.toolbar3 = parent.addToolBar("File3")
    #self.toolbar3.addAction(parent.actionPython_Console)

    # create the map tools
    self.toolPan = QgsMapToolPan(self.canvas)
    self.toolPan.setAction(parent.mpActionPan)
    self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
    self.toolZoomIn.setAction(parent.mpActionZoomIn)
    self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
    self.toolZoomOut.setAction(parent.mpActionZoomOut)
    
    # Default to zoom in tool
    self.canvas.setMapTool(self.toolZoomIn)
    
    # Default to not interviewing and no saved tool for interview
    self.interviewInProgress = False
    self.interviewSaveTool = None
    
  # Signal handler for capturing rectangle
  def updateBoundsFromRegion(self):
    mc = self.canvas      
    self.r = RegionTool(mc)
    QObject.connect(self.r.o, SIGNAL("finished()"), self.doneRectangle)
    self.saveTool = mc.mapTool()
    mc.setMapTool(self.r)

  # Signal handler for finishing capture of rectangle
  def doneRectangle(self):
    self.canvas.setMapTool(self.saveTool)
    capture_string = QString(self.capt_rect_str +
                             str(self.r.bb.xMin()) + " " +
                             str(self.r.bb.yMax()) +
                             " :: " +
                             str(self.r.bb.xMax()) + " " +
                             str(self.r.bb.yMin()))
    #self.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)

  # Signal handler for capturing polygon
  def updatePolygon(self):
    mc = self.canvas      
    self.p = PolygonTool(mc)
    QObject.connect(self.p.o, SIGNAL("finished()"), self.donePolygon)
    self.saveTool = mc.mapTool()
    mc.setMapTool(self.p)

  # Signal handler for finishing capture of rectangle
  def donePolygon(self):
    self.canvas.setMapTool(self.saveTool)
    capture_string = QString(self.poly_captured_str)
    #self.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)

  # Start Python Console
  def startPythonConsole(self):
      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
      wnd = PythonInterpGui(self.parent,flags)
      wnd.show()

  # Start interview dialog
  def interviewStart(self):
    #print "Interview start..."
    if self.interviewInProgress == True:
      # We need to continue
      self.canvas.setMapTool(self.interviewSaveTool)
      self.interviewSaveTool = None
    else:
      # Start up a new interview
      self.statusbar.showMessage(self.start_interview_str)
      self.interviewInProgress = True
      self.interview = Interview(self)


  # Signal handler for zoom in button
  def zoomIn(self):
    if self.interviewInProgress and self.interviewSaveTool == None:
      self.interviewSaveTool = self.canvas.mapTool()
    self.canvas.setMapTool(self.toolZoomIn)

  # Signal handler for zoom out button
  def zoomOut(self):
    if self.interviewInProgress and self.interviewSaveTool == None:
      self.interviewSaveTool = self.canvas.mapTool()
    self.canvas.setMapTool(self.toolZoomOut)

  # Signal handler for pan button
  def pan(self):
    if self.interviewInProgress and self.interviewSaveTool == None:
      self.interviewSaveTool = self.canvas.mapTool()
    self.canvas.setMapTool(self.toolPan)

  # Signal handler for add layer button
  def addVectorLayer(self):
    qd=QFileDialog()
    filter_str = QString("*.shp")
    f=qd.getOpenFileName(self.parent,QString(),QString(),filter_str)
    # Check for cancel
    if len(f) == 0:
      return
    capture_string = QString(f)
    #self.canvas.parentWin.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)

    info = QFileInfo(QString(f))

    # create layer
    layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")
    self.vec_layer = layer
    
    if not layer.isValid():
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(self.error_reading_str)
        return

    if self.parent.srs == None:
      self.parent.srs = layer.srs()
      print 'maptools.py srs setting...' + str(self.parent.srs)
      # set extent to the extent of our layer
      self.parent.canvas.setExtent(layer.extent())

    QgsMapLayerRegistry.instance().addMapLayer(layer)

    # set extent to the extent of our layer
    #self.canvas.setExtent(layer.extent())

    # Set the transparency for the layer
    layer.setTransparency(190)
    
    # set the map canvas layer set
    cl = QgsMapCanvasLayer(layer)
    self.layers.insert(0,cl)
    self.canvas.setLayerSet(self.layers)

    #Add item to legend
    self.legend.addVectorLegendItem(info.completeBaseName(), [cl])

  # Signal handler for add layer button
  def addRasterLayer(self):
    qd=QFileDialog()
    filter_str = QString("*.tif")
    f=qd.getOpenFileName(self.parent,QString(),QString(),filter_str)
    # Check for cancel
    if len(f) == 0:
      return
    capture_string = QString(f)
    #self.canvas.parentWin.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)
    
    info = QFileInfo(QString(f))

    # create layer
    layer = QgsRasterLayer(info.filePath(), info.completeBaseName())

    if not layer.isValid():
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(self.error_reading_str)
        return

    if self.parent.srs == None:
      self.parent.srs = layer.srs()
      # set extent to the extent of our layer
      self.parent.canvas.setExtent(layer.extent())

    # add layer to the registry
    QgsMapLayerRegistry.instance().addMapLayer(layer)

    # set extent to the extent of our layer
    #self.canvas.setExtent(layer.extent())

    # set the map canvas layer set
    cl = QgsMapCanvasLayer(layer)
    self.layers.insert(0,cl)
    self.canvas.setLayerSet(self.layers)

    #Add item to legend
    self.legend.addRasterLegendItem(info.completeBaseName(), [cl])
  

  # Geo-transform helper function
  def transform(self, x, y):
    return QgsPoint(self.canvas.getCoordinateTransform().toMapCoordinates(x,y))

  def retranslate(self):
    self.capt_rect_str = QA.translate("MapTools", "Captured Rectangle - ", "", QA.UnicodeUTF8)
    self.error_reading_str = QA.translate("MapTools", "Error reading file", "", QA.UnicodeUTF8)
    self.start_interview_str = QA.translate("MapTools", "Starting interview", "", QA.UnicodeUTF8)
    self.file_bar_str = QA.translate("MapTools", "File", "", QA.UnicodeUTF8)
    self.file_bar_2_str = QA.translate("MapTools", "File2", "Menu bar title", QA.UnicodeUTF8)
    self.poly_captured_str = QA.translate("MapTools", "Polygon captured", "Status message shown after user finished a polygon", QA.UnicodeUTF8)