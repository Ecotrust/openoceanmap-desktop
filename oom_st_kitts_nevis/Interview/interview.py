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
    
    self.phase = ["start","general","shapes","finished"]
    
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
          self.habitatIndex = index+3
          
          self.fisheryYrsParticIndex = index+4
          self.fisheryNumGearIndex = index+5
          self.fisheryGearLengthIndex = index+6
          self.fisherySeasonalityIndex = index+7
          self.fisheryPriceIndex = index+8
          self.fisheryPortIndex = index+9
          
          fields[self.fisheryIndex] = QgsField("fishery", QVariant.String)          
          fields[self.penniesIndex] = QgsField("pennies", QVariant.Int)
          fields[self.habitatIndex] = QgsField("habitat", QVariant.String)
          
          fields[self.fisheryYrsParticIndex] = QgsField("fshy_yrs", QVariant.String)
          fields[self.fisheryNumGearIndex] = QgsField("fshy_gear", QVariant.String)
          fields[self.fisheryGearLengthIndex] = QgsField("fshy_glen", QVariant.String)
          fields[self.fisherySeasonalityIndex] = QgsField("fshy_sesn", QVariant.String)
          fields[self.fisheryPriceIndex] = QgsField("fshy_pric", QVariant.String)
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
              fet.addAttribute(self.habitatIndex, QVariant(self.capturedPolygonsHabitat[capPolyInd]))
              
              fet.addAttribute(self.fisheryYrsParticIndex, QVariant(self.currentFisheryYearsPartic))
              fet.addAttribute(self.fisheryNumGearIndex, QVariant(self.currentFisheryNumGear))
              fet.addAttribute(self.fisheryGearLengthIndex, QVariant(self.currentFisheryGearLength))
              fet.addAttribute(self.fisherySeasonalityIndex, QVariant(self.currentFisherySeasonality))
              fet.addAttribute(self.fisheryPriceIndex, QVariant(self.currentFisheryPrice))
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
          self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl])
          
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

      # EITHER create a shapefile clipped to the study region and reassign pennies # NO LONGER USED
      #self.create_clipped_layer( str(f), new_layer )
      
      # OR just proceed directly to the next fishery
      self.next_fishery()

      
  def next_fishery(self): 
      # turn any  newly-added layers off to avoid clutter
      self.parent.legend.setLayerCheckboxes(QgsMapLayer.VECTOR,Qt.Unchecked)
        
      wnd = SelectFisheryGui(self)
      wnd.show()
        
        
  # no longer used, but preserved for posterity  -- if you want to clip a layer against a shapefile, here's how:
  def create_clipped_layer(self, working_filename, working_layer):
      # load the study region shapefile to clip against
      study_region_layer = QgsVectorLayer("Data/Soorc_sr.shp", "study region", "ogr")
      if not study_region_layer.isValid(): 
        error_string = QString("ERROR reading study region file: could not load file Data/Soorc_sr.shp")
        QMessageBox.warning(self.mainwindow, "Error - interview aborted", error_string)
        self.parent.statusbar.showMessage(error_string)
        self.resetInterview()
        return
        
      study_region_provider = study_region_layer.getDataProvider()
      study_region_atts = study_region_provider.allAttributesList()
      study_region_provider.select( study_region_atts )
      study_region_feat = QgsFeature()
      
      if not study_region_provider.getNextFeature( study_region_feat ):
        error_string = QString("ERROR reading study region file Data/Soorc_sr.shp: no features found")
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
      fields[self.originalShapeIndex] = QgsField("orig_shp", QVariant.Int)
      fields[self.habitatIndex] = QgsField("habitat", QVariant.String)
      fields[self.fisheryIncIndex] = QgsField("finc_pct", QVariant.Int)
      
      
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
          clipped_feat.changeAttribute( self.originalShapeIndex, QVariant( feat.featureId() ))
          new_geometry = study_region_feat.geometry().intersection( feat.geometry() )
          if not new_geometry.isMultipart():
              clipped_feat.setGeometry( new_geometry ) 
              writer.addFeature( clipped_feat )
          else:
              for poly in new_geometry.asMultiPolygon():
                  sub_feat = QgsFeature()
                  sub_feat.setAttributeMap( feat.attributeMap() )
                  sub_feat.changeAttribute( self.originalShapeIndex, QVariant( feat.featureId() ))
                  sub_feat.setGeometry( QgsGeometry().fromPolygon(poly) ) 
                  writer.addFeature( sub_feat )
                    
      del writer
        
      # display the clipped layer
      info = QFileInfo(QString(clip_filename))
      clip_layer = QgsVectorLayer( clip_filename, info.completeBaseName(), "ogr" )
        
      #prov = clip_layer.getDataProvider()
      #allattr = prov.allAttributesList()
      #prov.select(allattr)
      #feat2 = QgsFeature()
      #print "just after save"
      #while prov.getNextFeature(feat2):
      #    print str(feat2.featureId())+": "+feat2.attributeMap()[45].toString()
        
                   
      clip_layer.setTransparency(190)
      
      QgsMapLayerRegistry.instance().addMapLayer(clip_layer)
      
      #set the map canvas layer set
      cl = QgsMapCanvasLayer(clip_layer)
      self.mainwindow.layers.insert(0,cl)
      self.canvas.setLayerSet(self.mainwindow.layers)
        
      clip_layer.label().setLabelField(QgsLabel.Text, self.penniesIndex)
      clip_layer.setLabelOn(True)
      clip_layer.renderer().setSelectionColor(QColor(0,255,100))
          
      #Add item to legend
      self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl])
        
      # reassign pennies to the shapes in this layer
      fishery = feat.attributeMap()[index+1].toString()
      if clip_layer.featureCount() > 0:
        wnd = NextClippedPolygonGui(self, fishery, clip_layer)
        wnd.show()
      else:
        QMessageBox.warning(None, "No shapes remaining", "None of the shapes in the "+fishery+" fishery were in the study region.")
        self.next_fishery()
          
        
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
