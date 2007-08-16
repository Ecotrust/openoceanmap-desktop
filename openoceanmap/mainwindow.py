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
from regiontool import *
from polygontool import *
from interviewstart import *
# Python Shell
from pythoninterp import *
# UI specific includes
from mainwindow_ui import Ui_MainWindow
from interviewstart_ui import Ui_InterviewStart
# General system includes
import sys,string
from code import *


  
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
    # A place to store polygons we capture
    self.capturedPolygons = []
    self.capturedPolygonsPennies = []
    self.capturedPolygonsRub = []
    # Interview info to write in shapefile
    self.interviewInfo = []
    
    self.layers = []
    
    # lay our widgets out in the main window
    self.layout = QVBoxLayout(self.frameMap)
    self.layout.addWidget(self.canvas)

    # We need to initialize the window sizes
    self.splitter.setSizes([100,600])

    # Set up the legend string list
    #self.model = QStringListModel()
    #self.stringList =  QStringList()
    #self.model.setStringList(self.stringList)
    #self.listView.setModel(self.model)
    #self.listWidget.addColumn("Layers")

    # Setup the Python interpreter
    #self.pythonInterp.setFocus(Qt.OtherFocusReason)
    #self.connect(self.pythonInterp, SIGNAL("returnPressed()"),
    #             self.pythonInterpParse)
    #self.sh = Shell(locals(),self.canvas)

    # create the actions behaviours
    self.connect(self.mpActionAddVectorLayer, SIGNAL("triggered()"),
                 self.addVectorLayer)
    self.connect(self.mpActionAddRasterLayer, SIGNAL("triggered()"),
                 self.addRasterLayer)
    self.connect(self.mpActionZoomIn, SIGNAL("triggered()"), self.zoomIn)
    self.connect(self.mpActionZoomOut, SIGNAL("triggered()"), self.zoomOut)
    self.connect(self.mpActionPan, SIGNAL("triggered()"), self.pan)
    self.connect(self.actionStart_Interview, SIGNAL("triggered()"),
                 self.interviewStart)
    self.connect(self.actionRegion_Tool, SIGNAL("triggered()"),
                 self.updateBoundsFromRegion)
    self.connect(self.actionPolygon_Tool, SIGNAL("triggered()"),
                 self.updatePolygon)
    self.connect(self.actionPython_Console, SIGNAL("triggered()"),
                 self.startPythonConsole)

    # create a little toolbar for map tools
    self.toolbar = self.addToolBar("File")
    self.toolbar.addAction(self.mpActionAddVectorLayer)
    self.toolbar.addAction(self.mpActionAddRasterLayer)
    self.toolbar.addAction(self.mpActionZoomIn)
    self.toolbar.addAction(self.mpActionZoomOut)
    self.toolbar.addAction(self.mpActionPan)
    self.toolbar.addAction(self.actionRegion_Tool)

    # create a little toolbar for interview tools
    self.toolbar2 = self.addToolBar("File2")
    self.toolbar2.addAction(self.actionStart_Interview)
    #self.toolbar2.addAction(self.actionPolygon_Tool)

    # create a little toolbar for utilities
    self.toolbar3 = self.addToolBar("File3")
    self.toolbar3.addAction(self.actionPython_Console)

    # create the map tools
    self.toolPan = QgsMapToolPan(self.canvas)
    self.toolPan.setAction(self.mpActionPan)
    self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
    self.toolZoomIn.setAction(self.mpActionZoomIn)
    self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
    self.toolZoomOut.setAction(self.mpActionZoomOut)


  # Signal handeler for capturing rectangle
  def updateBoundsFromRegion(self):
    mc = self.canvas      
    self.r = regionTool(mc)
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
    self.p = polygonTool(mc)
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
      wnd = PythonInterpGui(self,flags)
      wnd.show()

  # Start interview dialog
  def interviewStart(self):
      capture_string = QString("Starting Interview Dialog...")
      #self.outputWin.append(capture_string)
      self.statusbar.showMessage(capture_string)
      # Reset previous polygons
      del self.capturedPolygonsRub[:]
      del self.capturedPolygons[:]
      del self.capturedPolygonsPennies[:]
      del self.interviewInfo[:]
      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
      wnd = InterviewStartGui(self,flags)
      wnd.show()

  # End interview dialog
  def interviewEnd(self):
      if len(self.capturedPolygons) == 0:
          capture_string = QString("No Shapes to write...")
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)
      else:
          capture_string = QString("Writing shapefile...")
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)
          qd=QFileDialog()
          filter_str = QString("*.shp")
          f=qd.getSaveFileName(self,QString(),QString(),filter_str)
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
          for capPolyInd, capPoly in enumerate(self.capturedPolygons):
              fet = QgsFeature()
              ret_val = fet.setGeometry(QgsGeometry.fromWkt(capPoly))
              fet.addAttribute(0, QVariant(self.interviewInfo[0]))
              fet.addAttribute(1, QVariant(self.interviewInfo[1]))
              fet.addAttribute(2, QVariant(self.capturedPolygonsPennies[capPolyInd]))
              writer.addFeature(fet)
          del writer
          capture_string = QString("Wrote Shapefile..." + write_string)
          #self.outputWin.append(capture_string)
          self.statusbar.showMessage(capture_string)

          # add some features
          for capPolyRub in self.capturedPolygonsRub:
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
    f=qd.getOpenFileName(self,QString(),QString(),filter_str)
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
    #self.stringList.append(info.completeBaseName())
    #self.model.insertRows(self.stringList.count()-1, self.stringList.count())
    item_new = QListWidgetItem( info.completeBaseName(), self.listWidget)
    pm = QPixmap(10,10)
    pm.fill(layer.renderer().symbols()[0].fillColor())
    icon = QIcon(pm)
    item_new.setIcon(icon)

  # Signal handeler for add layer button
  def addRasterLayer(self):
    qd=QFileDialog()
    filter_str = QString("*.tif")
    f=qd.getOpenFileName(self,QString(),QString(),filter_str)
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
  

  # Geo-transform helper function
  def transform(self, x, y):
    return QgsPoint(self.canvas.getCoordinateTransform().toMapCoordinates(x,y))

  def pythonInterpParse(self):
    capture_string = str(self.pythonInterp.text())
    #self.canvas.parentWin.outputWin.append(">>>" + capture_string)
    #self.sh.push(capture_string)
    capture_string = QString("--------")
    #self.canvas.parentWin.outputWin.append(capture_string)
    self.pythonInterp.clear()
  
  def custPrint(self, obj):
    print ", ".join(map(str,obj))
