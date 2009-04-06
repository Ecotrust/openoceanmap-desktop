#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
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
from consscience_ui import Ui_ConsScience
from drawconsscience import DrawConsScienceGui

from Util.common_functions import *
# General system includes
import sys

class ConsScienceGui(QDialog, Ui_ConsScience):
    def __init__(self, parent, flags, prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI        
        self.foci_mapping = {
            'cst_reef':'Coastal reef ecosystem - fish and invertebrates',
            'dp_reef':'Deep sea reef ecosystem - fish and invertebrates',
            'soft':'Soft bottom - sand, mud, etc',
            'sm_plgc':'Small pelagics - sardines, anchovy, etc',
            'migr_fish':'Migratory fish - tuna, swordfish, sailfish',
            'sea_trtl':'Sea turtles'        
        }
        
        self.retranslate()

    def on_pbnSelectConsScience_released(self):
        err_code = self.saveAttribs()
        if err_code <= 0:
            return                    
        err_code = self.fetchFoci()        
        if err_code >= 0:
            self.startNextFocus()        

    '''
    Skip the conservation/scientist survey step
    '''
    def on_pbnExitEcoStep_released(self):
        self.close()
        self.parent.ecotourismIncome = None
        self.parent.nextStep(self, self.cancel_ecotourism_str)

    '''
    Pulls the next focus and allows the user to draw shapes for it 
    '''
    def startNextFocus(self):        
        if len(self.parent.foci) > 0:
            (focus,value) = self.parent.foci.pop()
            self.parent.add_attrib(self.f_focus_str, focus)
            self.parent.add_attrib(self.f_focus_inc_str, value)
            
            info_str = ''
            if self.foci_mapping.has_key(focus):
                self.parent.shapeType = self.foci_mapping.get(focus)
                info_str = self.draw_next_focus_str + self.foci_mapping.get(focus)
            else:
                self.parent.shapeType = focus
                info_str = self.draw_next_focus_str + focus

            self.hide()        
            QMessageBox.information(self, self.next_focus_str, info_str)            
            
            mc = self.parent.canvas      
            self.p = PolygonTool(mc,self.parent)
            QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
            self.saveTool = mc.mapTool()
            self.parent.parent.interviewSaveTool = None
            mc.setMapTool(self.p)  

    '''
    Loads the dialog for assigning a penny value
    '''
    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawConsScienceGui(self.parent,flags,self.parent.pennies_left, self.parent.shapeType, self)
        wnd.show()
            
    '''
    Save general ecotourism attributes
    '''
    def saveAttribs(self):
        self.parent.add_attrib(self.f_add_info_str, self.add_info_line.text())
        if not self.comboSpecialist.currentText():
            QMessageBox.warning(self, self.consci_error_str, self.spc_error_str)
            return -1
        else:
            self.parent.add_attrib(self.f_spc_type_str, self.comboSpecialist.currentText())
        return 1

    '''
    Fetch foci and % interest from dialog and verify they
    add up to 100%.  These will be looped through
    '''
    def fetchFoci(self):
        foci = []
        if self.focus_coast_reef.text() != '0':
            foci.append(('cst_reef',self.focus_coast_reef.text()))
        if self.focus_deep_reef.text() != '0':
            foci.append(('dp_reef',self.focus_deep_reef.text())) 
        if self.focus_soft.text() != '0':
            foci.append(('soft',self.focus_soft.text())) 
        if self.focus_pelagic.text() != '0':
            foci.append(('sm_plgc',self.focus_pelagic.text())) 
        if self.focus_migratory.text() != '0':
            foci.append(('migr_fsh',self.focus_migratory.text())) 
        if self.focus_turtles.text() != '0':
            foci.append(('sea_trtl',self.focus_turtles.text()))             

        if self.focus_other_1_name.text() != '':         
            foci_tuple = (str(self.focus_other_1_name.text()), self.focus_other_1_interest.text())
            foci.append(foci_tuple)                                            
        if self.focus_other_2_name.text() != '':            
            foci_tuple = (str(self.focus_other_2_name.text()), self.focus_other_2_interest.text())
            foci.append(foci_tuple) 
            
        for (focus, interest) in foci:
            if not strIsInt(interest):
                QMessageBox.warning(self, "Input Error", "One of your focus percentages is not a number")
                return -1 
        
        total = sum([int(b) for (a,b) in foci])
        if total != 100:
            QMessageBox.warning(self, "Percent Error", "Your percentages must add up to 100, currently: "+str(total))
            return -1
        
        #Maintain the foci at the Interview level since DrawConsScience needs
        #to keep track of the number left too
        self.parent.foci = foci
        return 1
        
    def retranslate(self):
        self.spec_error_str = QA.translate("ConsScienceGui", 'Specialist Error', "Error message when specialist type not selected", QA.UnicodeUTF8)
        self.choose_specialist_str = QA.translate("ConsScienceGui", "Please choose a specialist position", "Error message when specialist type not selected", QA.UnicodeUTF8)
        self.f_spc_type_str = QA.translate("ConsScienceGui", "spc_type", "conservationist/scientist area of specialization", QA.UnicodeUTF8)
        self.f_add_info_str = QA.translate("ConsScienceGui", "add_info", "additional info about con/science focus (kelp, mangrove, etc)", QA.UnicodeUTF8)
        self.cancel_conscience_str = QA.translate("ConsScienceGui", "Canceled conservationist/scientist interview", "", QA.UnicodeUTF8)
        self.next_focus_str = QA.translate("EcotourismGui", "Next Focus", "", QA.UnicodeUTF8)
        self.draw_next_focus_str = QA.translate("EcotourismGui", "Please begin drawing shapes for the following focus area: ", "", QA.UnicodeUTF8)
        
        self.f_focus_str = QA.translate("SelectConsScienceGui", "focus", "Area of Focus for conservation/scientist", QA.UnicodeUTF8)
        self.f_focus_inc_str = QA.translate("EcotourismGui", "focus_v", "Type of ecotourism activity", QA.UnicodeUTF8)
        self.consci_error_str = QA.translate("SelectConsScienceGui", "Cons/Science Error", "Error when user fails to select type of conservationist/scientist", QA.UnicodeUTF8)        
        self.spc_error_str = QA.translate("SelectConsScienceGui", "Please select a specialist area", "", QA.UnicodeUTF8)
        self.finish_cons_str = QA.translate("SelectConsScienceGui", "Finishing Cons/Sci interview", "", QA.UnicodeUTF8)        