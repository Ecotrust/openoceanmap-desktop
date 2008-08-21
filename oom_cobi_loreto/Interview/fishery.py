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
from fishery_ui import Ui_Fishery

from Util.common_functions import *

# General system includes
import sys

class FisheryGui(QDialog, Ui_Fishery):
    def __init__(self, parent, flags, fishery_sector,prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI
        self.currentStep = fishery_sector
        self.fishery_sector_label.setText(unicode(self.currentStep))
        self.retranslate()
 
    def append_data(self):
        self.parent.add_attrib(self.f_v_len_str, self.vessel_length_line.text())
        self.parent.add_attrib(self.f_v_motor_str, self.vessel_motor_line.text())
        self.parent.add_attrib(self.f_haul_cap_str, self.haul_capacity_line.text())
        self.parent.add_attrib(self.f_v_homep_str, self.home_port_line.text())
        self.parent.add_attrib(self.f_landp_1_str, self.landing_port_line.text())
        self.parent.add_attrib(self.f_landp_2_str, self.landing_port_line_2.text())
        self.parent.add_attrib(self.f_landp_3_str, self.landing_port_line_3.text())
        self.parent.add_attrib(self.f_landp_4_str, self.landing_port_line_4.text())        

    def on_pbnSelectGear_released(self):        
        if self.currentStep == self.comm_fish_str:
            if not self.parent.commFishStarted:
                self.append_data()
                self.parent.commFishStarted = True
        elif self.currentStep == self.comm_sport_fish_str :
            if not self.parent.commFishStarted:
                self.append_data()
                self.parent.sportFishStarted = True
        elif self.currentStep == self.priv_fish_str:
            if not self.parent.commFishStarted:
                self.append_data()
                self.parent.privateFishStarted = True

        self.close()
        from selectgear import SelectGearGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = SelectGearGui(self.parent,flags, self.currentStep, self.prevGUI)
        wnd.show()

    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetInterview()

    #Not used
    def on_pbnBack_clicked(self):
        self.close()
        self.parent.parent.statusbar.showMessage(self.back_to_interview_str)

        from interviewstart import InterviewStartGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        try:
            self.prevGUI.show()
        except:
            wnd = InterviewStartGui(self.parent,flags)
            wnd.show()
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def retranslate(self):
        self.comm_fish_str = QA.translate("FisheryGui", 'Commercial Fishery', "", QA.UnicodeUTF8)
        self.comm_sport_fish_str = QA.translate("FisheryGui", 'Sport Fishery', "", QA.UnicodeUTF8)
        self.priv_fish_str = QA.translate("FisheryGui", 'Private Fishery', "", QA.UnicodeUTF8)
        self.back_to_interview_str = QA.translate("FisheryGui", "Going back to first interview step...", "landing port 4", QA.UnicodeUTF8)

        self.f_v_len_str = QA.translate("FisheryGui", 'v_len', "vessel length attribute", QA.UnicodeUTF8)
        self.f_v_motor_str = QA.translate("FisheryGui", 'v_motor', "vessel motor horsepower attribute", QA.UnicodeUTF8)
        self.f_haul_cap_str = QA.translate("FisheryGui", 'haul_cap', "vessel haul capacity in kilograms attribute", QA.UnicodeUTF8)
        self.f_v_homep_str = QA.translate("FisheryGui", 'v_homep', "vessel homeport attribute", QA.UnicodeUTF8)
        self.f_landp_1_str = QA.translate("FisheryGui", 'landp_1', "landing port 1 attribute", QA.UnicodeUTF8)
        self.f_landp_2_str = QA.translate("FisheryGui", 'landp_2', "landing port 2 attribute", QA.UnicodeUTF8)
        self.f_landp_3_str = QA.translate("FisheryGui", 'landp_3', "landing port 3 attribute", QA.UnicodeUTF8)
        self.f_landp_4_str = QA.translate("FisheryGui", 'landp_4', "landing port 4 attribute", QA.UnicodeUTF8)
