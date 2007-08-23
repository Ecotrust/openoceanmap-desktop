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

from regiontool import *
from polygontool import *
from Interview.interviewstart import *
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
    self.toolbar = parent.addToolBar("File")
    self.toolbar.addAction(parent.mpActionAddVectorLayer)
    self.toolbar.addAction(parent.mpActionAddRasterLayer)
    self.toolbar.addAction(parent.mpActionZoomIn)
    self.toolbar.addAction(parent.mpActionZoomOut)
    self.toolbar.addAction(parent.mpActionPan)
    self.toolbar.addAction(parent.actionRegion_Tool)

    # create a little toolbar for interview tools
    self.toolbar2 = parent.addToolBar("File2")
    self.toolbar2.addAction(parent.actionStart_Interview)

    # create a little toolbar for utilities
    self.toolbar3 = parent.addToolBar("File3")
    self.toolbar3.addAction(parent.actionPython_Console)

    # create the map tools
    self.toolPan = QgsMapToolPan(self.canvas)
    self.toolPan.setAction(parent.mpActionPan)
    self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
    self.toolZoomIn.setAction(parent.mpActionZoomIn)
    self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
    self.toolZoomOut.setAction(parent.mpActionZoomOut)

  # Signal handeler for capturing rectangle
  def updateBoundsFromRegion(self):
    mc = self.canvas      
    self.r = RegionTool(mc)
    QObject.connect(self.r.o, SIGNAL("finished()"), self.doneRectangle)
    self.saveTool = mc.mapTool()
    mc.setMapTool(self.r)

  # Signal handeler for finishing capture of rectangle
  def doneRectangle(self):
    self.canvas.setMapTool(self.saveTool)
    capture_string = QString("Captured Rectangle - " +
                             str(self.r.bb.xMin()) + " " +
                             str(self.r.bb.yMax()) +
                             " :: " +
                             str(self.r.bb.xMax()) + " " +
                             str(self.r.bb.yMin()))
    #self.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)

  # Signal handeler for capturing polygon
  def updatePolygon(self):
    mc = self.canvas      
    self.p = PolygonTool(mc)
    QObject.connect(self.p.o, SIGNAL("finished()"), self.donePolygon)
    self.saveTool = mc.mapTool()
    mc.setMapTool(self.p)

  # Signal handeler for finishing capture of rectangle
  def donePolygon(self):
    self.canvas.setMapTool(self.saveTool)
    capture_string = QString("Captured Polygon")
    #self.outputWin.append(capture_string)
    self.statusbar.showMessage(capture_string)

  # Start Python Console
  def startPythonConsole(self):
      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
      wnd = PythonInterpGui(self.parent,flags)
      wnd.show()

  # Start interview dialog
  def interviewStart(self):
      capture_string = QString("Starting Interview Dialog...")
      #self.outputWin.append(capture_string)
      self.statusbar.showMessage(capture_string)
      # Reset previous polygons
      del self.parent.capturedPolygonsRub[:]
      del self.parent.capturedPolygons[:]
      del self.parent.capturedPolygonsPennies[:]
      del self.parent.interviewInfo[:]
      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
      wnd = InterviewStartGui(self,flags)
      wnd.show()

  # End interview dialog
  def interviewEnd(self):
      if len(self.parent.capturedPolygons) == 0:
          capture_string = QString("No Shapes to write...")
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)
      else:
          capture_string = QString("Writing shapefile...")
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)
          qd=QFileDialog()
          filter_str = QString("*.shp")
          f=qd.getSaveFileName(self.parent,QString(),QString(),filter_str)
          write_string = QString(f)
          # define fields for feature attributes
          fields = { 0 : QgsField("interviewer_name", QVariant.String),
                     1 : QgsField("participant_name", QVariant.String),
                     2 : QgsField("pennies", QVariant.Int) }
          
          # create an instance of vector file writer,
          # it will create the shapefile. Arguments:
          # 1. path to new shapefile (will fail if exists already)
          # 2. encoding of the attributes
          # 3. field map
          # 4. geometry type - from WKBTYPE enum
          # 5. layer's spatial reference (instance of QgsSpatialRefSys)
          writer = QgsVectorFileWriter(write_string, "UTF-8", fields,
                                       QGis.WKBPolygon, None)
          
          if writer.hasError() != QgsVectorFileWriter.NoError:
              print "Error when creating shapefile: ", writer.hasError()
              
          # add some features
          for capPolyInd, capPoly in enumerate(self.parent.capturedPolygons):
              fet = QgsFeature()
              ret_val = fet.setGeometry(QgsGeometry.fromWkt(capPoly))
              fet.addAttribute(0, QVariant(self.parent.interviewInfo[0]))
              fet.addAttribute(1, QVariant(self.parent.interviewInfo[1]))
              fet.addAttribute(2, QVariant(self.parent.capturedPolygonsPennies[capPolyInd]))
              writer.addFeature(fet)
          del writer
          capture_string = QString("Wrote Shapefile..." + write_string)
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)

          # add some features
          for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
          self.canvas.setMapTool(self.toolZoomIn)

  # Signal handeler for zoom in button
  def zoomIn(self):
    self.canvas.setMapTool(self.toolZoomIn)

  # Signal handeler for zoom out button
  def zoomOut(self):
    self.canvas.setMapTool(self.toolZoomOut)

  # Signal handeler for pan button
  def pan(self):
    self.canvas.setMapTool(self.toolPan)

  # Signal handeler for add layer button
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
        capture_string = QString("ERROR reading file")
        #self.canvas.parentWin.outputWin.append(capture_string)
        self.statusbar.showMessage(capture_string)
        return
    QgsMapLayerRegistry.instance().addMapLayer(layer)

    # set extent to the extent of our layer
    self.canvas.setExtent(layer.extent())

    # set the map canvas layer set
    cl = QgsMapCanvasLayer(layer)
    self.layers.insert(0,cl)
    self.canvas.setLayerSet(self.layers)

    #Add item to legend
    self.legend.addVectorLegendItem(info.completeBaseName(), layer)

  # Signal handeler for add layer button
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

    #Add item to legend
    self.legend.addRasterLegendItem(info.completeBaseName(), layer)
  

  # Geo-transform helper function
  def transform(self, x, y):
    return QgsPoint(self.canvas.getCoordinateTransform().toMapCoordinates(x,y))

  #def pythonInterpParse(self):
  #  capture_string = str(self.pythonInterp.text())
  #  #self.canvas.parentWin.outputWin.append(">>>" + capture_string)
  #  #self.sh.push(capture_string)
  #  capture_string = QString("--------")
  #  #self.canvas.parentWin.outputWin.append(capture_string)
  #  self.pythonInterp.clear()

    


  