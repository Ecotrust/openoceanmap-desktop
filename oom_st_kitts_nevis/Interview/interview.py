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
from interviewstart import *
from selectfishery import *
from nextclippedpolygon import *
#from Tools.polygontool import *
#from nextpolygon import *
# UI specific includes
from interviewstart_ui import Ui_InterviewStart
# General system includes
import sys

# Interview object for doing interviews
class Interview(QObject):
  def __init__(self, parent):
    self.parent = parent
    self.canvas = parent.canvas
    self.mainwindow = parent.parent
    
    self.phase = ["start","general","addtquestions","shapes","finished"]
    
    self.resetInterview()
    
    # Reset previous polygons
    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    wnd = InterviewStartGui(self,flags)
    wnd.show()

  def nextStep(self):
      self.phase_index = self.phase_index + 1
      if self.phase[ self.phase_index ] == "general":
          new_status = "General questions"
          self.parent.statusbar.showMessage(new_status)
          from rec_cpfv import RecCpfvGui
          wnd = RecCpfvGui(self)
          wnd.show()
          
      elif self.phase[ self.phase_index ] == "addtquestions":
          new_status = "Additional questions"
          self.parent.statusbar.showMessage(new_status)
          from addtquestions import AddtQuestionsGui
          wnd = AddtQuestionsGui(self)
          wnd.show()
          
      elif self.phase[ self.phase_index ] == "shapes":
          new_status = "Drawing fisheries"
          self.parent.statusbar.showMessage(new_status)
          self.next_fishery()

      else: # "finished"
          new_status = "Interview complete"
          self.parent.statusbar.showMessage(new_status)
          self.end_interview()
      

  # End interview dialog for current fishery, then start a new one
  def end_fishery(self):
      if len(self.capturedPolygons) == 0:
          capture_string = QString("No Shapes to write...")
          self.parent.statusbar.showMessage(capture_string)
      else:                              
          capture_string = QString("Writing shapefile...")
          self.parent.statusbar.showMessage(capture_string)
          qd=QFileDialog()
          filter_str = QString("*.shp")
          f2=qd.getSaveFileName(self.mainwindow,QString(),QString(),filter_str)
          if f2.count(".shp")==0:
            f = f2 + ".shp"
          else:
            f = f2
          write_string = QString(f)
          # define fields for feature attributes
          fields = {}
          #keySort = self.interviewInfo2.keys()
          #keySort.sort()
          #i = 0
          for index,value in enumerate(self.interviewInfo2):
            fields[index] = QgsField(value[0], QVariant.String)

          self.fisheryIndex = index+1
          self.penniesIndex = index+2
          #self.habitatIndex = index+3
          
          self.fisheryYrsParticIndex = index+3
          self.fisheryNumGearIndex = index+4
          self.fisheryGearLengthIndex = index+5
          self.fisherySeasonStartIndex = index+6
          self.fisherySeasonEndIndex = index+7
          self.fisherySeasonStartIndex2 = index+8
          self.fisherySeasonEndIndex2 = index+9
          self.fisheryPortIndex = index+10
          
          fields[self.fisheryIndex] = QgsField("fishery", QVariant.String)          
          fields[self.penniesIndex] = QgsField("pennies", QVariant.Int)
          #fields[self.habitatIndex] = QgsField("habitat", QVariant.String)
          
          fields[self.fisheryYrsParticIndex] = QgsField("fshy_yrs", QVariant.String)
          fields[self.fisheryNumGearIndex] = QgsField("fshy_gear", QVariant.String)
          fields[self.fisheryGearLengthIndex] = QgsField("fshy_glen", QVariant.String)
          fields[self.fisherySeasonStartIndex] = QgsField("f_seasn_s", QVariant.String)
          fields[self.fisherySeasonEndIndex] = QgsField("f_seasn_e", QVariant.String)
          fields[self.fisherySeasonStartIndex2] = QgsField("f_seas2_s", QVariant.String)
          fields[self.fisherySeasonEndIndex2] = QgsField("f_seas2_e", QVariant.String)
          fields[self.fisheryPortIndex] = QgsField("fshy_port", QVariant.String)
          
          #fields = { 0 : QgsField("interviewer_name", QVariant.String),
          #           1 : QgsField("participant_name", QVariant.String),
          #           2 : QgsField("pennies", QVariant.Int) }
          
          # create an instance of vector file writer,
          # it will create the shapefile. Arguments:
          # 1. path to new shapefile (will fail if exists already)
          # 2. encoding of the attributes
          # 3. field map
          # 4. geometry type - from WKBTYPE enum
          # 5. layer's spatial reference (instance of QgsSpatialRefSys)
          writer = QgsVectorFileWriter(write_string, "UTF-8", fields,
                                       QGis.WKBPolygon, self.mainwindow.srs)
          
          if writer.hasError() != QgsVectorFileWriter.NoError:
              print "Error when creating shapefile: ", writer.hasError()
              
          # add some features
          for capPolyInd, capPoly in enumerate(self.capturedPolygons):
              fet = QgsFeature()
              ret_val = fet.setGeometry(QgsGeometry.fromWkt(capPoly))
              #keySort = self.interviewInfo2.keys()
              #keySort.sort()
              #i = 0
              for index,value in enumerate(self.interviewInfo2):
                fet.addAttribute(index, QVariant(value[1]))
                
              fet.addAttribute(self.fisheryIndex, QVariant(self.capturedPolygonsFishery[capPolyInd]))
              fet.addAttribute(self.penniesIndex, QVariant(self.capturedPolygonsPennies[capPolyInd]))
              #fet.addAttribute(self.habitatIndex, QVariant(self.capturedPolygonsHabitat[capPolyInd]))
              
              fet.addAttribute(self.fisheryYrsParticIndex, QVariant(self.currentFisheryYearsPartic))
              fet.addAttribute(self.fisheryNumGearIndex, QVariant(self.currentFisheryNumGear))
              fet.addAttribute(self.fisheryGearLengthIndex, QVariant(self.currentFisheryGearLength))
              fet.addAttribute(self.fisherySeasonStartIndex, QVariant(self.currentFisherySeasonStart))
              fet.addAttribute(self.fisherySeasonEndIndex, QVariant(self.currentFisherySeasonEnd))
              fet.addAttribute(self.fisherySeasonStartIndex2, QVariant(self.currentFisherySeasonStart2))
              fet.addAttribute(self.fisherySeasonEndIndex2, QVariant(self.currentFisherySeasonEnd2))
              fet.addAttribute(self.fisheryPortIndex, QVariant(self.currentFisheryPort))
              
              writer.addFeature(fet)
          del writer
          capture_string = QString("Wrote Shapefile..." + write_string)
          self.parent.statusbar.showMessage(capture_string)

          # Now add the new layer back... but with styling...
          info = QFileInfo(QString(f))
          layer = QgsVectorLayer(f, info.completeBaseName(), "ogr")
          
          if not layer.isValid():            
            capture_string = QString("ERROR reading file, did it save correctly?  If not, do you have write permission in the save directory you chose?")
            self.parent.statusbar.showMessage(capture_string)
            #Restart save dialog
            self.interviewEnd()
            #Pull out
            return
            
          # track user-added layers for later clipping
          new_layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")

          #layer.label().setLabelField(QgsLabel.Text, self.penniesIndex)
          #layer.setLabelOn(True)
          
          # Set the transparency for the layer
          layer.setTransparency(190)
          
          QgsMapLayerRegistry.instance().addMapLayer(layer)
          
          # set the map canvas layer set
          cl = QgsMapCanvasLayer(layer)
          self.mainwindow.layers.insert(0,cl)
          self.canvas.setLayerSet(self.mainwindow.layers)
          
          #Add item to legend
          self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl], cl.layer().renderer().symbols()[0].fillColor())
          
      # Reset the rubberbands and then clear out the fishery related objects
      for capPolyRub in self.capturedPolygonsRub:
        capPolyRub.reset()
      self.capturedPolygons = []
      self.capturedPolygonsFishery = []
      self.capturedPolygonsPennies = []
      self.capturedPolygonsRub = []
      #self.capturedPolygonsHabitat = []

      #Reset penny count
      self.pennies_left = 100

      # EITHER create a shapefile clipped to the study region and reassign pennies # NO LONGER USED
      #self.create_clipped_layer( str(f), new_layer )
      
      # OR just proceed directly to the next fishery
      self.next_fishery()

      
  def next_fishery(self): 
      # turn any  newly-added layers off to avoid clutter
      self.parent.legend.setLayerCheckboxes(QgsMapLayer.VECTOR,Qt.Unchecked)
        
      wnd = SelectFisheryGui(self)
      wnd.show()
          
        
  def end_interview(self):
      QMessageBox.warning(self.mainwindow, "Completed", "Interview Completed")
      self.resetInterview()
      
      
  def resetInterview(self):
      self.currentFishery = None
        
      # A place to store polygons we capture
      self.capturedPolygons = []
      self.capturedPolygonsFishery = []
      self.capturedPolygonsPennies = []
      self.capturedPolygonsRub = []
      #self.capturedPolygonsHabitat = []
    
      self.pennies_left = 100
      self.phase_index = 0
      
      # Interview info to write in shapefile
      self.interviewInfo = []
      self.interviewInfo2 = []
    
      self.curr_clip_fishery = 0
      return
