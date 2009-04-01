#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer
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
# set up for translateable strings
from PyQt4.QtGui import QApplication as QA
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
from interviewstart import InterviewStartGui
# UI specific includes
from interviewstart_ui import Ui_InterviewStart
from resgroup import ResGroupGui
from fishery import FisheryGui
from ecotourism import EcotourismGui
from consscience import ConsScienceGui
from other import OtherGui
# General system includes
import sys, os

# Interview object for doing interviews
class Interview(object):
  def __init__(self, parent):
    self.parent = parent
    self.canvas = parent.canvas
    self.mainwindow = parent.parent

    self.currentStep = None
    self.shapeType = None
    self.res_groups = None
    self.commFishStarted= False    
    self.sportFishStarted = False
    self.privateFishStarted = False

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
    self.capturedPolygonsPennies = []
    self.capturedPolygonsRub = []
    
    #Ecotourism window
    self.eco_wnd = None
    self.consci_wnd = None
    
    self.pennies_left = 100

    # Interview info to write in shapefile
    self.interviewInfo = []
    self.interviewInfo2 = []

    self.fishery_attribs = [
      'emp_type',
      'v_len',
      'v_motor',                  
      'haul_cap',
      'v_homep',
      'landp_1',
      'landp_2',
      'landp_3',
      'landp_4',
      'resgrp',
      'resgrp_v',
      'gear',
      'main_sp'
    ]
    
    self.ecotourism_attribs = [
        'emp_type',
        'v_len',
        'v_motor',
        'v_cap',
        'v_homep',
        'workers',
        'act_type',
        'spe_type'
    ]
    
    self.consci_attribs = [
        'focus',
        'add_info',
        'spc_type'
    ]
    
    # Reset previous polygons
    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    
    self.retranslate()

    wnd = InterviewStartGui(self,flags)
    wnd.show()

  '''
  Reset interview state
  '''
  def resetInterview(self,msg=None):
        if not msg:
            msg = self.cancel_str
        capture_string = QString(msg)
        self.parent.statusbar.showMessage(capture_string)
        self.parent.interviewInProgress = False
        self.parent.interviewSaveTool = None        
        self.currentStep = None
        self.shapeType = None
        self.res_groups = None
        self.commFishIncome = None
        self.commFishStarted= False
        self.sportFishIncome = None
        self.sportFishStarted = False
        self.privateFishStarted = None
        self.privateFishIncome = False   
        self.ecotourismIncome = None
        self.consScienceIncome = None
        self.otherIncome = None
        self.interviewInfo2 = []
        self.canvas.setMapTool(self.parent.toolZoomIn)
  
  '''
  Add a key value pair to the set of attributes to be written
  out to shapefile.
  '''
  def add_attrib(self, b_name, b_value):
    found_group = False
    for i in range(len(self.interviewInfo2)):
      [a_name, a_value] = self.interviewInfo2[i]
      if a_name == b_name:
        found_group = True
        self.interviewInfo2[i] = [b_name,b_value]
    if not found_group:
      self.interviewInfo2.append([b_name,b_value])                  
        
  '''
  Remove items with the list of keys passed.  Useful for clearing user group specific attribs
  after you finish with a user group
  '''
  def remove_attribs(self, b_names):
    for b_name in b_names:
        for i in range(len(self.interviewInfo2)):
            #Length will shorten as we pop so short circuit as needed
            if i >= len(self.interviewInfo2):
                continue
            [a_name, a_value] = self.interviewInfo2[i]
            if a_name == b_name:
                self.interviewInfo2.pop(i)         
        
  '''
  Manages progress through the interview.  A state machine figures out what
  should be handled next.  Other dialogs are expected to set the appropriate
  state when steps wrap up before calling this function.
  '''
  def nextStep(self, previousGui=None, msg=None):
      if not msg:
          msg = self.leaving_step_str
      
      capture_string = QString(msg)
      self.parent.statusbar.showMessage(capture_string)

      #Reset some stuff
      self.pennies_left = 100;
      self.shapeType = None
      for capPolyRub in self.capturedPolygonsRub:
          capPolyRub.reset()

      flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint    
      
      if self.commFishIncome:
          self.parent.statusbar.showMessage(self.start_comm_fish_str)
          self.currentStep = self.comm_fish_str

          #Append user group name and income percent, overwrite if already exists          
          self.add_attrib(self.f_user_group_str,self.comm_fish_str)
          self.add_attrib(self.f_user_group_income_str, self.commFishIncome)
          
          #Get resource group information first time, then loop through resource groups
          #the second time
          if not self.res_groups:          
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          elif len(self.res_groups) > 0:
              self.startNextResGroup() 
                  
      elif self.sportFishIncome:
          self.parent.statusbar.showMessage(self.start_comm_sport_fish_str)
          self.currentStep = self.comm_sport_fish_str

          #Append user group name and income percent
          self.add_attrib(self.f_user_group_str,self.comm_sport_fish_str)
          self.add_attrib(self.f_user_group_income_str, self.sportFishIncome)

          if not self.res_groups:      
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          elif len(self.res_groups) > 0:
              self.startNextResGroup()
    
      elif self.privateFishIncome:
          self.parent.statusbar.showMessage(self.start_priv_fish_str)
          self.currentStep = self.priv_fish_str

          #Append user group name and income percent, overwrite if already exists          
          self.add_attrib(self.f_user_group_str,self.priv_fish_str)
          self.add_attrib(self.f_user_group_income_str, self.privateFishIncome)

          if not self.res_groups:         
              wnd = FisheryGui(self,flags,self.currentStep,previousGui)
              wnd.show()
          elif len(self.res_groups) > 0:
              self.startNextResGroup()
    
      elif self.ecotourismIncome:
          self.parent.statusbar.showMessage(self.start_eco_str)
          self.currentStep = self.eco_str
          #Append user group name and income percent
          self.add_attrib(self.f_user_group_str,self.eco_str)
          self.add_attrib(self.f_user_group_income_str, self.ecotourismIncome)

          if not self.eco_wnd:         
              flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
              self.eco_wnd = EcotourismGui(self,flags,previousGui)
              self.eco_wnd.show()
          else:
              self.eco_wnd.startNextActivity()
          
      elif self.consScienceIncome:
          self.parent.statusbar.showMessage(self.start_consci_str)
          self.currentStep = self.consci_str

          #Append user group name and income percent, overwrite if already exists          
          self.add_attrib(self.f_user_group_str,self.consci_str)
          self.add_attrib(self.f_user_group_income_str, self.consScienceIncome)

          if not self.consci_wnd:         
              flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
              self.consci_wnd = ConsScienceGui(self,flags,previousGui)
              self.consci_wnd.show()
          else:
              self.consci_wnd.startNextActivity()
          
      elif self.otherIncome:
          self.parent.statusbar.showMessage(self.start_other_str)
          self.currentStep = self.other_str

          #Append user group name and income percent, overwrite if already exists          
          self.add_attrib(self.f_user_group_str,self.other_str)
          self.add_attrib(self.f_user_group_income_str, self.otherIncome)
          
          textType = self.income_str #the type should be gathered
          # skip right to drawing...
          flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
          wnd = OtherGui(self,flags,self.currentStep,previousGui)
          wnd.show()
      else:
          self.resetInterview(self.int_finished_str)
          QMessageBox.information(self.mainwindow, self.success_str, self.int_comp_str)
      
      self.parent.canvas.setMapTool(self.parent.toolZoomIn)

  '''
  Pulls the next resource group and starts the dialog for collecting information
  about that group
  '''
  def startNextResGroup(self):        
      if len(self.res_groups) > 0:
          (res_group,value) = self.res_groups.pop()
          flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
          wnd = ResGroupGui(self,flags, self.currentStep, res_group, value)
          wnd.show()                                 

  # End interview dialog
  def saveText(self, textGui):
      textGui.close()
      if len(self.capturedText) == 0:
          # Finished a interview step without writing any text...
          capture_string = self.no_info_str
          self.parent.statusbar.showMessage(capture_string)
          # Fire up the previous gui again...
          textGui.show()
      else:                         
          file_prefix = self.first_name_str+'_'+ self.last_name_str+'_'+ QString(self.currentStep) + '_' + QString(self.capturedTextType).replace(' ','_').toLower()
          file_prefix_obj = QString(file_prefix)
          file_name = QString("%s" % file_prefix_obj)
          self.parent.statusbar.showMessage(self.writing_text_str)
          qd=QFileDialog()
          qd.DontConfirmOverwrite = True
          file_type_filter = QString("Plain Text (*.csv)")
          f2=qd.getSaveFileName(self.mainwindow, self.save_text_str, file_name, file_type_filter)

          #Check for correct extension and add if necessary
          if f2.count(".csv")==0:
            f2 = f2 + ".csv"              
            
          # check to see if the user tried to overwrite an csv file of the same name
          if os.path.isfile(f2):
            # Currently we don't suport overwriting, so return to same dialog
            write_string = QString(f2)
            capture_string = QString(self.overwrite_support_str + write_string)
            self.parent.statusbar.showMessage(capture_string)
            textGui.show()
          else:
              f = f2
              write_string = QString(f)
              file = open(write_string, 'w')
              line1 = []
              line2 = []

              for index,value in enumerate(self.interviewInfo2):
                line1.append(unicode(value[0]))
                line2.append(unicode(value[1]))
              
              line1.append(unicode('other_text'))
              line2.append(unicode(self.capturedText))

              #file.write(self.capturedText)
              str1 = u', '.join(line1)+u'\n'
              str2 = u', '.join(line2)
              
              file.write(str1.encode('iso-8859-1'))
              file.write(str2.encode('iso-8859-1'))

              file.close()
              capture_string = QString(self.other_info_save_str + write_string)
              self.parent.statusbar.showMessage(capture_string)
              # reset values to prepare for another save...
              self.capturedText = []
              #self.capturedTextType = []

  # End interview dialog
  def saveShapes(self, drawGui):
      drawGui.close()
      if len(self.capturedPolygons) == 0:
          # Finished a interview step without writing any shapes...
          self.parent.statusbar.showMessage(self.no_shapes_str)
          # Fire up the previous gui again...
          drawGui.previousGui.show()
      else:      
          file_prefix = (self.first_name_str+'_'+
                         self.last_name_str+'_'+
                         QString(self.currentStep) + '_' + 
                         QString(self.shapeType)).replace(' ','_').toLower()
          file_prefix_obj = QString(file_prefix)
          file_name = QString("%s_" % file_prefix_obj)
          # self.parent.statusbar.showMessage(file_prefix)
          self.parent.statusbar.showMessage(self.writing_shape_str)
          qd=QFileDialog()
          qd.DontConfirmOverwrite = True
          file_type_filter = QString("Shapefiles (*.shp)")
          f2=qd.getSaveFileName(self.mainwindow, self.save_shape_str, file_name, file_type_filter)
         
          # Check to see if the shapefile has been saved
          if f2 == "":
            drawGui.previousGui.show()              
          # check to see if the user tried to overwrite an existing shapefile
          elif os.path.isfile(f2):
            # Currently we don't suport overwriting, so return to same dialog
            write_string = QString(f2)
            # this translation is not found perhaps due to line number or order of excution...
            capture_string = QString(self.overwrite_support_str + write_string)
            self.parent.statusbar.showMessage(capture_string)
            drawGui.show()
          else:
            if f2.count(".shp")==0:
                # If user typed name but didn't end it with .shp
                f2 = f2 + ".shp"              
              
            f = f2
            write_string = QString(f)
            # define fields for feature attributes
            fields = {}
            #keySort = self.interviewInfo2.keys()
            #keySort.sort()
            #i = 0
            for index,value in enumerate(self.interviewInfo2):
              fields[index] = QgsField(value[0], QVariant.String)

            fields[index+1] = QgsField(self.f_pennies_str, QVariant.Int)

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
                for index,value in enumerate(self.interviewInfo2):
                  fet.addAttribute(index, QVariant(value[1]))

                fet.addAttribute(index+1, QVariant(self.capturedPolygonsPennies[capPolyInd]))                                       
                writer.addFeature(fet)                
                
            del writer
            capture_string = QString(self.wrote_shape_str + write_string)
            self.parent.statusbar.showMessage(capture_string)
  
            # Now add the new layer back... but with styling...
            info = QFileInfo(QString(f))
            layer = QgsVectorLayer(QString(f), info.completeBaseName(), "ogr")
            
            if not layer.isValid():
              self.statusbar.showMessage(self.save_error_str)
              #Restart save dialog
              self.saveShapes(drawGui)
              #Pull out
              return

            penny_label_index = len(self.interviewInfo2)
            layer.label().setLabelField(QgsLabel.Text, penny_label_index)
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

            ## Reset the rubberbands and then clear out the income type related objects
            for capPolyRub in self.capturedPolygonsRub:
              capPolyRub.reset()
            self.capturedPolygons = []
            self.capturedPolygonsPennies = []
            self.capturedPolygonsRub = []

            #Reset penny count
            self.pennies_left = 100

            #Decides whether to clear state and go to the 
            #next step or continue in the inner loop
            if self.currentStep == self.comm_fish_str:
                if len(self.res_groups) > 0:
                    self.startNextResGroup()
                    return
                self.commFishIncome = None
                #Remove all fishery attribs leave rest
                self.remove_attribs(self.fishery_attribs)
                self.nextStep(drawGui)
                
            elif self.currentStep == self.comm_sport_fish_str:
                if len(self.res_groups) > 0:
                    self.startNextResGroup()
                    return
                self.sportFishIncome = None
                #Remove all fishery attribs, leave rest
                self.remove_attribs(self.fishery_attribs)
                self.nextStep(drawGui)
                
            elif self.currentStep == self.priv_fish_str:
                if len(self.res_groups) > 0:
                    self.startNextResGroup()
                    return
                self.privateFishIncome = None
                #Remove all fishery attribs, leave rest
                self.remove_attribs(self.fishery_attribs)
                self.nextStep(drawGui)            
                
            elif self.currentStep == self.eco_str:            
                if len(self.activities) > 0:
                    self.eco_wnd.startNextActivity()
                    return
                self.ecotourismIncome = None    
                #Remove all ecotourism attribs
                self.remove_attribs(self.ecotourism_attribs)
                self.nextStep(drawGui)
                
            elif self.currentStep == self.consci_str:
                #Remove all consci attribs, leave rest
                if len(self.foci) > 0:
                    self.consci_wnd.startNextFocus()
                    return
                self.consScienceIncome = None    
                #Remove all ecotourism attribs
                self.remove_attribs(self.consci_attribs)
                self.nextStep(drawGui)                
                        
  def retranslate(self):
      self.first_name_str = QA.translate("InterviewStartGui", "firstname", "Interviewee first name attribute", QA.UnicodeUTF8)
      self.last_name_str = QA.translate("InterviewStartGui", "lastname", "Interviewee last name attribute", QA.UnicodeUTF8)      
      
      self.start_comm_fish_str = QA.translate("Interview", 'Starting commercial fishery interview', "", QA.UnicodeUTF8)      
      self.comm_fish_str = QA.translate("Interview", 'Commercial Fishery', "", QA.UnicodeUTF8)
      self.start_comm_sport_fish_str = QA.translate("Interview", 'Starting commercial sport fishery interview', "", QA.UnicodeUTF8)
      self.comm_sport_fish_str = QA.translate("Interview", 'Sport Fishery', "", QA.UnicodeUTF8)
      self.start_priv_fish_str = QA.translate("Interview", 'Starting private sport fishery interview', "", QA.UnicodeUTF8)          
      self.priv_fish_str = QA.translate("Interview", 'Private Fishery', "", QA.UnicodeUTF8)
      self.start_eco_str = QA.translate("Interview", "Starting ecotourism interview", "", QA.UnicodeUTF8)
      self.eco_str = QA.translate("Interview", 'Ecotourism', "", QA.UnicodeUTF8)
      self.start_consci_str = QA.translate("Interview", "Starting conservation/scientist interview", "", QA.UnicodeUTF8)
      self.consci_str = QA.translate("Interview", 'Conservationist Scientist', "", QA.UnicodeUTF8)
      self.start_other_str = QA.translate("Interview", "Starting other interview", "", QA.UnicodeUTF8)
      self.other_str = QA.translate("Interview", "Other", "", QA.UnicodeUTF8)
      self.income_str = QA.translate("Interview", "Income", "", QA.UnicodeUTF8)
      self.success_str = QA.translate("Interview", "Success", "", QA.UnicodeUTF8)
      self.int_comp_str = QA.translate("Interview", "Interview Completed", "", QA.UnicodeUTF8)
      self.int_finished_str = QA.translate("Interview", "Interview Finished", "", QA.UnicodeUTF8)
      self.no_info_str = QA.translate("Interview", "No info, returning to previous choices", "", QA.UnicodeUTF8)
      self.save_text_str = QA.translate("Interview", "Save Text as", "", QA.UnicodeUTF8)
      self.overwrite_support_str = QA.translate("Interview","Overwriting existing text file is not supported: ", None, QA.UnicodeUTF8)
      self.other_info_save_str = QA.translate("Other Income Saved","Other income info successfully saved to: ", None, QA.UnicodeUTF8)
      self.save_shape_str = QA.translate("Interview","Save Shapes as", None, QA.UnicodeUTF8)
      self.writing_text_str = QA.translate("Interview","Writing text file", None, QA.UnicodeUTF8)
      self.writing_shape_str = QA.translate("Interview","Writing shapefile", None, QA.UnicodeUTF8)
      self.no_shapes_str = QA.translate("Interview","No shapes drawn", None, QA.UnicodeUTF8)
      self.wrote_shape_str = QA.translate("Interview","Wrote shapefile", None, QA.UnicodeUTF8)
      self.save_error_str = QA.translate("Interview","Error reading file, did it save correctly?  If not, do you have write permission in the save directory you chose?", None, QA.UnicodeUTF8)
      self.cancel_str = QA.translate("Interview","Canceling interview", None, QA.UnicodeUTF8)
      self.leaving_step_str = QA.translate("Interview","Leaving this step", None, QA.UnicodeUTF8)
      
      self.f_user_group_income_str = QA.translate("Interview","ug_inc", "Percent income value", QA.UnicodeUTF8)
      self.f_pennies_str = QA.translate("Interview","pennies", "fishing ground penny value attribute", QA.UnicodeUTF8)
      
      self.f_user_group_str = QA.translate("Interview", "ug", "User group for current shape", QA.UnicodeUTF8)
