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
# set up for translateable strings
from PyQt4.QtGui import QApplication as QA
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
#from interviewstart import *
#from selectfishery import *
from interviewstart import InterviewStartGui
#from Tools.polygontool import *
#from nextpolygon import *
# UI specific includes
from interviewstart_ui import Ui_InterviewStart
# General system includes
import sys, os

#(QtGui.QApplication.translate("NextPolygon", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
#def _t(string, ui="Interview"):
#   u_string = string.encode("UTF-8")
#   translation_instance = QA.translate("Interview",u_string, None, QApplication.UnicodeUTF8)
#   return translation_instance

# Interview object for doing interviews
class Interview(object):
  def __init__(self, parent):
    self.parent = parent
    self.canvas = parent.canvas
    self.mainwindow = parent.parent
    

    self.currentStep = None
    self.shapeType = None
    
    self.currentFishery = None
    self.commFishIncome = None
    self.sportFishIncome = None
    self.privateFishIncome = None    
    self.ecotourismIncome = None
    self.consScienceIncome = None
    self.otherIncome = None

    # A place to store polygons we capture
    self.capturedText = ''
    self.capturedTextType = ''
    self.capturedPolygons = []
    self.capturedPolygonsType = []
    self.capturedPolygonsPennies = []
    self.capturedPolygonsRub = []
    
    self.pennies_left = 100

    # Interview info to write in shapefile
    self.interviewInfo = []
    self.interviewInfo2 = []
    
    # Reset previous polygons
    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    wnd = InterviewStartGui(self,flags)
    wnd.show()


  def resetInterview(self,msg="Canceling Interview... "):
        capture_string = QString(msg)
        self.parent.statusbar.showMessage(capture_string)
        self.parent.interviewInProgress = False
        self.parent.interviewSaveTool = None
        
        self.currentFishery = None
        
        self.commFishIncome = None
        self.sportFishIncome = None
        self.privateFishIncome = None    
        self.ecotourismIncome = None
        self.consScienceIncome = None
        self.otherIncome = None
        self.canvas.setMapTool(self.parent.toolZoomIn)
        
        
  def nextStep(self, previousGui, msg="Leaving Step"):
      sector_specific_vessel_port_info = False
      S = sector_specific_vessel_port_info
      
      capture_string = QString(msg)
      self.parent.statusbar.showMessage(capture_string)
      self.pennies_left = 100;
      self.shapeType = None
      for capPolyRub in self.capturedPolygonsRub:
          capPolyRub.reset()
      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
      if self.commFishIncome:
          capture_string = QString("Commericial Fishery Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Commercial Fishery'
          if S:          
              from fishery import FisheryGui
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          else:
              from selectgear import SelectGearGui
              wnd = SelectGearGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          
      elif self.sportFishIncome:
          capture_string = QString("Commercial Sport Fishery Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Sport Fishery'
          if S:          
              from fishery import FisheryGui
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          else:
              from selectgear import SelectGearGui
              wnd = SelectGearGui(self,flags,self.currentStep,previousGui)
              wnd.show()           
    
      elif self.privateFishIncome:
          capture_string = QString("Private Sport Fishery Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Private Fishery'
          if S:          
              from fishery import FisheryGui
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          else:
              from selectgear import SelectGearGui
              wnd = SelectGearGui(self,flags,self.currentStep,previousGui)
              wnd.show()
    
      elif self.ecotourismIncome:
          capture_string = QString("Ecotourism Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Ecotourism'
          from ecotourism import EcotourismGui
          flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
          wnd = EcotourismGui(self,flags,previousGui)
          wnd.show()
          
      elif self.consScienceIncome:
          capture_string = QString("Conservation / Scientist Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Conservationist Scientist'
          from consscience import ConsScienceGui
          flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
          wnd = ConsScienceGui(self,flags,previousGui)
          wnd.show()
          
      elif self.otherIncome:
          capture_string = QString("Other Income exists, starting that interview...")
          self.parent.statusbar.showMessage(capture_string)
          self.currentStep = 'Other'
          textType = "Income" #the type should be gathered
          # skip right to drawing...
          from other import OtherGui
          flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
          wnd = OtherGui(self,flags,self.currentStep,previousGui)
          wnd.show()
      else:
          self.resetInterview('Interview is finished!')
          print 'left interview fully...'
      
      self.parent.canvas.setMapTool(self.parent.toolZoomIn)
            

  # End interview dialog
  def saveText(self, textGui):
      textGui.close()
      
      if len(self.capturedText) == 0:
          # Finished a interview step without writing any text...
          capture_string = QString("No info to write, returning to previous choices...")
          self.parent.statusbar.showMessage(capture_string)
          # Fire up the previous gui again...
          textGui.show()
      else:
          file_prefix = (str(self.currentStep) + '_' + str(self.capturedTextType)).replace(' ','_').lower()
          file_prefix_obj = QString(file_prefix)
          file_name = QString("%s_" % file_prefix_obj)
          capture_string = QString("Writing text file...")
          self.parent.statusbar.showMessage(capture_string)
          qd=QFileDialog()
          qd.DontConfirmOverwrite = True
          file_type_filter = QString("Plain Text (*.txt)")
          f2=qd.getSaveFileName(self.mainwindow,QA.translate("Interview","Save Text as", None, QApplication.UnicodeUTF8),file_name,file_type_filter)
          
          # Check to see if the shapefile has been saved
          if f2.count(".txt")==0:
            # If the user cancels...
            print 'empty so it was cancelled'
            textGui.show()
            
          # check to see if the user tried to overwrite an txt file of the same name
          elif os.path.isfile(f2):
            # Currently we don't suport overwriting, so return to same dialog
            write_string = QString(f2)
            # this translation is not found perhaps due to line number or order of excution...
            msg = QA.translate("Interview","Overwriting existing text file is not supported: ", None, QApplication.UnicodeUTF8)
            capture_string = QString(msg + write_string)
            self.parent.statusbar.showMessage(capture_string)
            textGui.show()
          else:
              f = f2
              write_string = QString(f)
              file = open(write_string, 'w')
              file.write(self.capturedText)
              file.close()
              msg = QA.translate("Other Income Saved","Other income info successfully saved to: ", None, QApplication.UnicodeUTF8)
              capture_string = QString(msg + write_string)
              self.parent.statusbar.showMessage(capture_string)
              # reset values to prepare for another save...
              self.capturedText = []
              #self.capturedTextType = []
              textGui.show()


  # End interview dialog
  def saveShapes(self, drawGui):
      drawGui.close()
      
      if len(self.capturedPolygons) == 0:
          # Finished a interview step without writing any shapes...
          capture_string = QString("No Shapes to write, returning to previous choices...")
          self.parent.statusbar.showMessage(capture_string)
          
          # Fire up the previous gui again...
          drawGui.previousGui.show()
      else:
          file_prefix = (str(self.currentStep) + '_' + str(self.shapeType)).replace(' ','_').lower()
          file_prefix_obj = QString(file_prefix)
          file_name = QString("%s_" % file_prefix_obj)
          # self.parent.statusbar.showMessage(file_prefix)
          capture_string = QString("Writing shapefile...")
          self.parent.statusbar.showMessage(capture_string)
          qd=QFileDialog()
          qd.DontConfirmOverwrite = True
          file_type_filter = QString("Shapefiles (*.shp)")
          f2=qd.getSaveFileName(self.mainwindow,QA.translate("Interview","Save Shapes as", None, QApplication.UnicodeUTF8),file_name,file_type_filter)
          
          
          # Check to see if the shapefile has been saved
          if f2.count(".shp")==0:
            # If the user cancels...
            print 'cancelled'
            drawGui.previousGui.show()
          
          # check to see if the user tried to overwrite an existing shapefile
          elif os.path.isfile(f2):
            # Currently we don't suport overwriting, so return to same dialog
            write_string = QString(f2)
            # this translation is not found perhaps due to line number or order of excution...
            msg = QA.translate("Interview","Overwriting existing shapefile is not supported: ", None, QApplication.UnicodeUTF8)
            capture_string = QString(msg + write_string)
            self.parent.statusbar.showMessage(capture_string)
            drawGui.show()
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
              
            fields[index+1] = QgsField("income", QVariant.String)
            fields[index+2] = QgsField("pennies", QVariant.Int)
            
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
                  print index, value
                
                for index,value in enumerate(self.interviewInfo2):
                  fet.addAttribute(index, QVariant(value[1]))

                fet.addAttribute(index+1, QVariant(self.capturedPolygonsType[capPolyInd]))
                fet.addAttribute(index+2, QVariant(self.capturedPolygonsPennies[capPolyInd]))
                
                #fet.addAttribute(0, QVariant(self.interviewInfo[0]))
                #fet.addAttribute(1, QVariant(self.interviewInfo[1]))
                #fet.addAttribute(2, QVariant(self.capturedPolygonsPennies[capPolyInd]))
                writer.addFeature(fet)
            del writer
            capture_string = QString("Wrote Shapefile..." + write_string)
            self.parent.statusbar.showMessage(capture_string)
  
            # Now add the new layer back... but with styling...
            info = QFileInfo(QString(f))
            layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")
            
            if not layer.isValid():
              capture_string = QString("ERROR reading file, did it save correctly?  If not, do you have write permission in the save directory you chose?")
              self.statusbar.showMessage(capture_string)
              #Restart save dialog
              self.interviewEnd()
              #Pull out
              return
    
            layer.label().setLabelField(QgsLabel.Text, 23)
            layer.setLabelOn(True)
            
            # Set the transparency for the layer
            layer.setTransparency(190)
            
            QgsMapLayerRegistry.instance().addMapLayer(layer)
            
            # set the map canvas layer set
            cl = QgsMapCanvasLayer(layer)
            self.mainwindow.layers.insert(0,cl)
            self.canvas.setLayerSet(self.mainwindow.layers)
            
            #Add item to legend
            self.mainwindow.legend.addVectorLegendItem(info.completeBaseName(), [cl])

            ## Reset the rubberbands and then clear out the  income type related objects
            for capPolyRub in self.capturedPolygonsRub:
              capPolyRub.reset()
            self.capturedPolygons = []
            self.capturedPolygonsType = []
            self.capturedPolygonsPennies = []
            self.capturedPolygonsRub = []
            
            # Fire up the select type gui again...
            #flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
            
            #Reset penny count
            self.pennies_left = 100
            
            drawGui.previousGui.show()

