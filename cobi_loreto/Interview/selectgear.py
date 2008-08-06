#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer
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
from selectgear_ui import Ui_SelectGear

# General system includes
import sys

class SelectGearGui(QDialog, Ui_SelectGear):
    def __init__(self, parent, flags, fishery_sector, previousGui):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.fishery_sector = fishery_sector
        self.retranslate()
        
        self.fishery_sector_label.setText(str(self.fishery_sector))        
        self.pbnStepFinished.setText(self.exit_part_str + str(self.fishery_sector) + self.step_str)
    
    def on_pbnStartShapes_released(self):
        shape_type = self.gear_comboBox.currentText()
        if not shape_type:
            QMessageBox.warning(self, self.gear_error_str, self.select_gear_str)
            return 
        else:
            self.parent.shapeType = shape_type

        gear_perc_inc = self.gear_perc_income.text()
        if not gear_perc_inc or gear_perc_inc == '0':
            QMessageBox.warning(self, self.percent_error_str, self.missing_gear_str)
            return
        else:
            self.parent.interviewInfo2.append([self.f_gear_inc_str,gear_perc_inc])


        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnStepFinished_released(self): 
        self.close()
        fishery_msg = self.finish_str + self.fishery_sector + self.interview_step_str
        print self.fishery_sector
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
        from drawgear import DrawGearGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawGearGui(self.parent,flags,self.parent.pennies_left, self)
        wnd.show()

    def retranslate(self):
        self.gear_error_str = QA.translate("SelectGearGui", "Gear Type Error", "Displayed when user forgot to select a gear type", QA.UnicodeUTF8)
        self.select_gear_str = QA.translate("SelectGearGui", "Please select a gear type", "Displayed when user forgot to select a gear type", QA.UnicodeUTF8)
        self.exit_part_str = QA.translate("SelectGearGui", 'Exit ', "Partial text used to build a larger message, for example 'Exit Sport Fishery Step'", QA.UnicodeUTF8)
        self.step_str = QA.translate("SelectGearGui", ' Step', "Partial text used to build a larger message, for example 'Exit Sport Fishery Step'", QA.UnicodeUTF8)
        self.percent_error_str = QA.translate("SelectGearGui", "Percent Error", "Displayed when there is an error with the percentage given for gear type", QA.UnicodeUTF8)
        self.missing_gear_str = QA.translate("SelectGearGui", "Missing percentage for gear type", "", QA.UnicodeUTF8)
        self.finish_str = QA.translate("SelectGearGui", 'Finished with', "Partial text used to build a larger message, for example 'finished with sport fishery interview step'", QA.UnicodeUTF8)
        self.interview_step_str = QA.translate("SelectGearGui", ' interview step', "Partial text used to build a larger message, for example 'finished with sport fishery interview step'", QA.UnicodeUTF8)
        self.comm_fish_str = QA.translate("SelectGearGui", 'Commercial Fishery', "", QA.UnicodeUTF8)
        self.sport_fish_str = QA.translate("SelectGearGui", 'Sport Fishery', "", QA.UnicodeUTF8)
        self.priv_fish_str = QA.translate("SelectGearGui", 'Private Fishery', "", QA.UnicodeUTF8)
        self.f_gear_inc_str = QA.translate("SelectGearGui", "gear_inc", "Attribute for income from gear type", QA.UnicodeUTF8)        