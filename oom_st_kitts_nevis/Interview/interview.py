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
import os
import os.path

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
          
          cancel_save = False
          while not cancel_save:
              f2=qd.getSaveFileName(self.mainwindow,QString(),QString(),filter_str)
              if not f2: # user pressed cancel
                while not f2:
                  cancel_choice = QMessageBox.question(self.mainwindow, "Really discard this fishery?", "Are you sure you want to cancel and lose entered data for this fishery?", QMessageBox.Yes, QMessageBox.No)        
                  if cancel_choice == QMessageBox.Yes:
                    cancel_save = True
                    break
                  f2=qd.getSaveFileName(self.mainwindow,QString(),QString(),filter_str)
                if cancel_save:
                  break
              
              if f2.count(".shp")==0:
                f = f2 + ".shp"
              else:
                f = f2
                
              if os.path.isfile(str(f)): # handle overwrite
                try:
                  os.remove(str(f))
                except:
                  QMessageBox.warning(self.mainwindow, "Overwrite Error", "Cannot overwrite this file -- perhaps it is currently in use?")
                  continue # start loop again to reselect file
                  
              # test write a file with this name
              try:
                test_file = open(str(f), 'w')
                test_file.close()
                os.remove(str(f))
                break # exit retry loop
              except:
                QMessageBox.warning(self.mainwindow, "Write Error", "Cannot write this file -- do you have write permissions in the directory you selected?")
                # start loop again to reselect file
                
                
          if not cancel_save:
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
              self.habitatIndex = index+3
              
              self.fisheryYrsParticIndex = index+4
              self.fisheryNumGearIndex = index+5
              self.fisheryGearLengthIndex = index+6
              self.fisherySeasonStartIndex = index+7
              self.fisherySeasonEndIndex = index+8
              self.fisherySeasonStartIndex2 = index+9
              self.fisherySeasonEndIndex2 = index+10
              self.fisheryPortIndex = index+11
              
              fields[self.fisheryIndex] = QgsField("fishery", QVariant.String)          
              fields[self.penniesIndex] = QgsField("pennies", QVariant.Int)
              fields[self.habitatIndex] = QgsField("habitat", QVariant.String)
              
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
                  QMessageBox.warning(self.mainwindow, "Error when creating shapefile", str(writer.hasError()))
                
                  
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
                  fet.addAttribute(self.habitatIndex, QVariant(self.capturedPolygonsHabitat[capPolyInd]))
                  
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
                QMessageBox.warning(self.mainwindow, "ERROR saving file", "Your file was not saved, do you have write permission in the directory you chose?")
                #Restart save dialog
                self.interviewEnd()
                #Pull out
                return
                
              # track user-added layers for later clipping
              new_layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")

              # get the label instance associated with the layer
              label = layer.label()
              # and the label attributes associated with the label
              labelAttributes = label.layerAttributes()

              # use the Name field (specified by index 1) as the label field
              label.setLabelField(QgsLabel.Text,  self.penniesIndex)
        
              # set the colour of the label text
              labelAttributes.setColor(Qt.black)

              # create a 'halo' effect around each label so it
              # can still be read on dark backgrounds
              labelAttributes.setBufferEnabled(True)
              labelAttributes.setBufferColor(Qt.white)
              labelAttributes.setBufferSize(1, QgsLabelAttributes.PointUnits)
              
              layer.setLabelOn(True)
              
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
      self.capturedPolygonsHabitat = []

      #Reset penny count
      self.pennies_left = 100
      
      # just proceed directly to the next fishery
      self.next_fishery()

      
  def next_fishery(self): 
      # turn any  newly-added layers off to avoid clutter
      #self.parent.legend.setLayerCheckboxes(QgsMapLayer.VECTOR,Qt.Unchecked)
        
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
      self.capturedPolygonsHabitat = []
    
      self.pennies_left = 100
      self.phase_index = 0
      
      # Interview info to write in shapefile
      self.interviewInfo = []
      self.interviewInfo2 = []
    
      self.curr_clip_fishery = 0
      return
