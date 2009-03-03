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
    
    self.phase = ["start","cpfv","shapes","clipped_shapes","finished"]
    
    self.resetInterview()
    
    # Reset previous polygons
    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    wnd = InterviewStartGui(self,flags)
    wnd.show()

  def nextStep(self):
      self.phase_index = self.phase_index + 1
      if self.phase[ self.phase_index ] == "cpfv":
          new_status = "Starting Charter Boat interview"
          self.parent.statusbar.showMessage(new_status)
          from rec_cpfv import RecCpfvGui
          wnd = RecCpfvGui(self)
          wnd.show()
          
      elif self.phase[ self.phase_index ] == "shapes":
          new_status = "Drawing full extent fisheries"
          self.parent.statusbar.showMessage(new_status)
          self.next_fishery()
          
      elif self.phase[ self.phase_index ] == "clipped_shapes":
          new_status = "Assigning pennies to clipped fishery shapes"
          self.parent.statusbar.showMessage(new_status)
          self.start_clipped_phase()

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
          fields[self.fisheryIndex] = QgsField("fishery", QVariant.String)          
          fields[self.penniesIndex] = QgsField("pennies", QVariant.Int)
          
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
          if self.phase[ self.phase_index ] == "shapes":
            new_layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")
            self.userLayers.append((str(f), new_layer))

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
          self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl])
          
      # Reset the rubberbands and then clear out the fishery related objects
      for capPolyRub in self.capturedPolygonsRub:
        capPolyRub.reset()
      self.capturedPolygons = []
      self.capturedPolygonsFishery = []
      self.capturedPolygonsPennies = []
      self.capturedPolygonsRub = []
      
      #Reset penny count
      self.pennies_left = 100
      
      self.next_fishery()

      
  def next_fishery(self): 
      if len(self.fisheries) > 0:
        (fishery,value) = self.fisheries.pop()
        wnd = SelectFisheryGui(self, fishery, value)
        wnd.show()
      else:
        self.nextStep()
        
  def start_clipped_phase(self):
      # load the study region shapefile to clip against
      study_region_layer = QgsVectorLayer("Data/study_region.shp", "study region", "ogr")
      if not study_region_layer.isValid(): 
        error_string = QString("ERROR reading study region file: could not load file Data/study_region.shp")
        QMessageBox.warning(self.mainwindow, "Error - interview aborted", error_string)
        self.parent.statusbar.showMessage(error_string)
        self.resetInterview()
        return
        
      study_region_provider = study_region_layer.getDataProvider()
      study_region_atts = study_region_provider.allAttributesList()
      study_region_provider.select( study_region_atts )
      study_region_feat = QgsFeature()
      
      if not study_region_provider.getNextFeature( study_region_feat ):
        error_string = QString("ERROR reading study region file Data/study_region.shp: no features found")
        QMessageBox.warning(self.mainwindow, "Error - interview aborted", error_string)
        self.parent.statusbar.showMessage(error_string)
        self.resetInterview()
        return
       
      # set up our field names for our new clipped shapefile
      fields = {}
      for index,value in enumerate(self.interviewInfo2):
        fields[index] = QgsField(value[0], QVariant.String) 
      fields[self.fisheryIndex] = QgsField("fishery", QVariant.String)          
      fields[self.penniesIndex] = QgsField("pennies", QVariant.Int)
      
      # iterate over the user fishery layers
      for (working_filename, working_layer) in self.userLayers:
      
        # set up new shapefile name (append "_c") to prev filename
        ext_index = working_filename.find( ".shp" )
        clip_filename = working_filename[0:ext_index]
        clip_filename = clip_filename + "_c.shp"
        
        # clip each shape in the layer to study region
        provider = working_layer.getDataProvider()
        allAttrs = provider.allAttributesList()
        provider.select(allAttrs)
        
        writer = QgsVectorFileWriter( clip_filename, "UTF-8", fields, QGis.WKBPolygon, self.mainwindow.srs)
        if writer.hasError() != QgsVectorFileWriter.NoError:
            print "Error when creating clip_temp shapefile: ", writer.hasError()

        feat = QgsFeature()
        while provider.getNextFeature(feat):
            clipped_feat = QgsFeature()
            clipped_feat.setAttributeMap( feat.attributeMap() )
            clipped_feat.setGeometry( study_region_feat.geometry().intersection( feat.geometry() )) 
            writer.addFeature( clipped_feat )
        del writer
        
        # display the clipped layer
        info = QFileInfo(QString(clip_filename))
        clip_layer = QgsVectorLayer( clip_filename, info.completeBaseName(), "ogr" )
                   
        clip_layer.setTransparency(190)
      
        QgsMapLayerRegistry.instance().addMapLayer(clip_layer)
      
        #set the map canvas layer set
        cl = QgsMapCanvasLayer(clip_layer)
        self.mainwindow.layers.insert(0,cl)
        self.canvas.setLayerSet(self.mainwindow.layers)
        
        clip_layer.label().setLabelField(QgsLabel.Text, self.penniesIndex)
        clip_layer.setLabelOn(True)
          
        #Add item to legend
        self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl])
        
        # keep a pointer to this layer where we can easily reference it later
        self.clipped_fisheries.append(( feat.attributeMap()[index+1].toString(), clip_layer ))
        #print "appending "+feat.attributeMap()[index+1].toString()
        
      # iterate over each remaining shape in each layer and assign pennies
      self.next_clipped_fishery()
      
      
  def next_clipped_fishery(self):
      if self.curr_clip_fishery < len(self.clipped_fisheries):
        (fishery,clipped_layer) = self.clipped_fisheries[self.curr_clip_fishery]
        self.curr_clip_fishery = self.curr_clip_fishery + 1
        if clipped_layer.featureCount() > 0:
            wnd = NextClippedPolygonGui(self, fishery, clipped_layer)
            wnd.show()
        else:
            QMessageBox.warning(None, "No shapes remaining", "None of the shapes in the "+fishery+" fishery were in the study region.")
            self.next_clipped_fishery()

      else:
        self.nextStep()
        
        
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
    
      self.pennies_left = 100
      self.phase_index = 0
      
      # Interview info to write in shapefile
      self.interviewInfo = []
      self.interviewInfo2 = []
    
      self.userLayers = []
      self.clipped_fisheries = []
      self.curr_clip_fishery = 0
      return
