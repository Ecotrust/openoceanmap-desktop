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
# Custom Functions
from Util.common_functions import *
# UI specific includes
from resgroup_ui import Ui_ResGroup
from drawresgroup import DrawResGroupGui

# General system includes
import sys

class ResGroupGui(QDialog, Ui_ResGroup):
    def __init__(self, parent, flags, fishery_sector, res_group):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.fishery_sector = fishery_sector
        self.res_group = res_group
        self.retranslate()
        
        self.fishery_sector_label.setText(unicode(self.fishery_sector))
        self.resource_group_label.setText(unicode(self.res_group))
        self.pbnStepFinished.setText(self.exit_part_str + unicode(self.fishery_sector) + self.step_str)
    
    def on_pbnStartShapes_released(self):               
        self.parent.shapeType = self.res_group
        main_species = self.editMainSpecies.document().toPlainText()
        
        #Build permit id string
        gear_types = []        
        if self.gear_hook_line.isChecked():
            gear_types.append('Hook and Line')
        if self.gear_traps.isChecked():
            gear_types.append('Traps')    
        if self.gear_purse_seine.isChecked():
            gear_types.append('Purse Seine')
        if self.gear_gillnet.isChecked():
            gear_types.append('Gillnet')
        if self.gear_trawling.isChecked():
            gear_types.append('Trawling')
        if self.gear_hooka.isChecked():
            gear_types.append('Hooka (compressor)')                                                                       
        if self.gear_other_1.text() != '':
            gear_types.append(str(self.gear_other_1.text()))
        if self.gear_other_2.text() != '':
            gear_types.append(str(self.gear_other_2.text()))
        if self.gear_other_3.text() != '':
            gear_types.append(str(self.gear_other_3.text()))
        if self.gear_other_4.text() != '':
            gear_types.append(str(self.gear_other_4.text()))
                                                            
        gear_type_str = ','.join(gear_types)        
        self.parent.capturedPolygonsGear.append(gear_type_str)

        self.hide()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        self.parent.parent.interviewSaveTool = None
        mc.setMapTool(self.p)
            
    def on_pbnStepFinished_released(self): 
        self.close()
        fishery_msg = self.finish_str + self.fishery_sector + self.interview_step_str
        
        if self.fishery_sector == self.comm_fish_str:
            self.parent.commFishIncome = None
            self.parent.nextStep(self, fishery_msg)
        elif self.fishery_sector == self.sport_fish_str:
            self.parent.sportFishIncome = None
            self.parent.nextStep(self, fishery_msg)
        elif self.fishery_sector == self.priv_fish_str:
            self.parent.privateFishIncome = None
            self.parent.nextStep(self, fishery_msg)

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawResGroupGui(self.parent, self, flags,self.parent.pennies_left, self.fishery_sector, self.res_group)
        wnd.show()

    def retranslate(self):
        self.gear_error_str = QA.translate("ResGroupGui", "Gear Type Error", "Displayed when user forgot to select a gear type", QA.UnicodeUTF8)
        self.select_gear_str = QA.translate("ResGroupGui", "Please select a gear type", "Displayed when user forgot to select a gear type", QA.UnicodeUTF8)
        self.exit_part_str = QA.translate("ResGroupGui", 'Exit ', "Partial text used to build a larger message, for example 'Exit Sport Fishery Step'", QA.UnicodeUTF8)
        self.step_str = QA.translate("ResGroupGui", ' Step', "Partial text used to build a larger message, for example 'Exit Sport Fishery Step'", QA.UnicodeUTF8)
        self.percent_error_str = QA.translate("ResGroupGui", "Percent Error", "Displayed when there is an error with the percentage given for gear type", QA.UnicodeUTF8)
        self.missing_gear_str = QA.translate("ResGroupGui", "Missing percentage for gear type", "", QA.UnicodeUTF8)
        self.finish_str = QA.translate("ResGroupGui", 'Finished with', "Partial text used to build a larger message, for example 'finished with sport fishery interview step'", QA.UnicodeUTF8)
        self.interview_step_str = QA.translate("ResGroupGui", ' interview step', "Partial text used to build a larger message, for example 'finished with sport fishery interview step'", QA.UnicodeUTF8)
        self.comm_fish_str = QA.translate("ResGroupGui", 'Commercial Fishery', "", QA.UnicodeUTF8)
        self.sport_fish_str = QA.translate("ResGroupGui", 'Sport Fishery', "", QA.UnicodeUTF8)
        self.priv_fish_str = QA.translate("ResGroupGui", 'Private Fishery', "", QA.UnicodeUTF8)                