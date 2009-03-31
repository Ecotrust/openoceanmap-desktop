#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
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
from Tools.polygontool import *
# UI specific includes
from ecotourism_ui import Ui_Ecotourism
from drawecotourism import DrawEcotourismGui
from Util.common_functions import *
# General system includes
import sys

class EcotourismGui(QDialog, Ui_Ecotourism):
    def __init__(self, parent, flags, prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI
        
        self.retranslate()

    def on_pbnSelectActivity_released(self):          
        err_code = self.fetchAttribs()
        if err_code <= 0:
            return
                    
        err_code = self.fetchActivities()
        #self.parent.shapeType = activity_type                   
        #self.parent.add_attrib(self.f_act_type_str, activity_type)         

        if err_code >= 0:
            self.startNextActivity()
            #self.close()            
            #self.parent.nextStep()
         
#        self.close()
#        from selectecotourism import SelectEcotourismGui
#        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
#        wnd = SelectEcotourismGui(self.parent,flags)
#        wnd.show()

    '''
    Pulls the next activity and 
    '''
    def startNextActivity(self):        
        if len(self.activities) > 0:
            (activity,value) = self.activities.pop()
            self.parent.shapeType = activity            

            self.hide()        
            mc = self.parent.canvas      
            self.p = PolygonTool(mc,self.parent)
            QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
            self.saveTool = mc.mapTool()
            self.parent.parent.interviewSaveTool = None
            mc.setMapTool(self.p)          

    def nextPolygon(self):        
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawEcotourismGui(self.parent,flags,self.parent.pennies_left, self.parent.shapeType, self)
        wnd.show()

    def on_pbnExitEcoStep_released(self):
        self.close()
        self.parent.ecotourismIncome = None
        self.parent.nextStep(self, self.cancel_ecotourism_str)

    '''
    Fetch general ecotourism information from dialog
    '''
    def fetchAttribs(self):
        self.parent.add_attrib(self.f_v_len_str, self.vessel_length_line.text())
        self.parent.add_attrib(self.f_v_motor_str, self.vessel_motor_line.text())
        self.parent.add_attrib(self.f_v_cap_str, self.haul_capacity_line.text())
        self.parent.add_attrib(self.f_v_homep_str, self.home_port_line.text())
        self.parent.add_attrib(self.f_trabajos_str, self.workers_line.text())    
        if not self.comboEmpType.currentText():
            QMessageBox.warning(self, self.emp_error_str, self.choose_activity_str)
            return -1
        else:
            self.parent.add_attrib(self.f_emp_type_str, self.comboEmpType.currentText())
        return 1

    '''
    Fetch activities and % interest from dialog and verify they
    add up to 100%.  These will be looped through
    '''
    def fetchActivities(self):        
        self.activities = []
        if self.activity_diving.text() != '0':
            self.activities.append(('Diving',self.activity_diving.text()))
        if self.activity_snorkeling.text() != '0':
            self.activities.append(('Snorkeling',self.activity_snorkeling.text()))
        if self.activity_kayaking.text() != '0':
            self.activities.append(('Kayaking',self.activity_kayaking.text()))
        if self.activity_watching.text() != '0':
            self.activities.append(('Marine Fauna Watching',self.activity_watching.text()))                                    

        if self.activity_other_1_name.text() != '':            
            group_tuple = (str(self.activity_other_1_name.text()), self.activity_other_1_interest.text())
            self.activities.append(group_tuple)
        if self.activity_other_2_name.text() != '':            
            group_tuple = (str(self.activity_other_2_name.text()), self.activity_other_2_interest.text())
            self.activities.append(group_tuple)                                             

        for (group, value) in self.activities:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your activity percentages is not a number")
                return -1 
        
        total = sum([int(b) for (a,b) in self.activities])
        if total != 100:
            QMessageBox.warning(self, "Percent Error", "Your percentages must add up to 100, currently: "+str(total))
            return -1        
        return 1

    def retranslate(self):       
        self.f_emp_type_str = QA.translate("EcotourismGui", "emp_type", "Employee type DB field name", QA.UnicodeUTF8)
        self.f_v_len_str = QA.translate("EcotourismGui", "v_len", "Vessel length DB field name", QA.UnicodeUTF8)
        self.f_v_motor_str = QA.translate("EcotourismGui", "v_motor", "Vessel motor (horsepower) DB field name", QA.UnicodeUTF8)
        self.f_v_cap_str = QA.translate("EcotourismGui", "v_cap", "Vessel capacity (kilograms) DB field name", QA.UnicodeUTF8)
        self.f_v_homep_str = QA.translate("EcotourismGui", "v_homep", "Vessel homeport DB field name", QA.UnicodeUTF8)
        self.f_trabajos_str = QA.translate("EcotourismGui", "workers", "Number that work for company DB field name", QA.UnicodeUTF8)
        self.emp_error_str = QA.translate("EcotourismGui", "Employee Error", "Error given when user fails to enter an employee type", QA.UnicodeUTF8)
        self.choose_activity_str = QA.translate("EcotourismGui", "Please Choose an Ecotourism Activity", "Error given when user fails to enter an employee type", QA.UnicodeUTF8)
        self.cancel_ecotourism_str = QA.translate("EcotourismGui", "Canceling ecotourism interview", "", QA.UnicodeUTF8)

        self.f_act_type_str = QA.translate("EcotourismGui", "act_type", "Type of ecotourism activity", QA.UnicodeUTF8)
        self.tourism_error_str = QA.translate("SelectEcotourismGui", "Ecotourism Error", "Error when user didn't select an ecotourism type ", QA.UnicodeUTF8)        
        self.other_error_str = QA.translate("EcotourismGui", "Ecotourism Error", "Error message given when user doesn't enter an other activity type", QA.UnicodeUTF8)
        self.no_other_error_str = QA.translate("EcotourismGui", "You selected 'Other' activity, you must enter the name of that activity", "Top title of error window when you dont enter a name for the other activity", QA.UnicodeUTF8)        
        self.select_tourism_str = QA.translate("EcotourismGui", "Please select an ecotourism type", "", QA.UnicodeUTF8)
        self.finish_tourism_str = QA.translate("EcotourismGui", "Finished with ecotourism interview", "", QA.UnicodeUTF8)