#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
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
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
from Tools.polygontool import *
from selectfishery import *
# UI specific includes
from rec_all_ui import Ui_RecAll
from Util.common_functions import *
# General system includes
import sys, copy

class RecAllGui(QDialog, Ui_RecAll):
    def __init__(self, parent):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent
        

    def on_pbnSelectFishery_released(self):
        
        interviewInfo2 = self.parent.interviewInfo2
        
        interviewInfo2.append(["user_group", "recreational"])

        interviewInfo2.append(["v_type", self.type_boat_line.currentText()])
        interviewInfo2.append(["v_lic", self.boat_license_line.text()])
        interviewInfo2.append(["v_yr_op", self.yrs_operating_line.text()])
        interviewInfo2.append(["v_yr_own", self.yrs_owning_line.text()])
        interviewInfo2.append(["v_len", self.vessel_length_line.text()])
        interviewInfo2.append(["v_str_loc", self.storage_loc_line.text()])
        interviewInfo2.append(["v_homep", self.home_port_line.text()])
        
        interviewInfo2.append(["v_landp_1", self.landing_port_line.text()])                       
        interviewInfo2.append(["v_landp_2", self.landing_port_line_2.text()])
        interviewInfo2.append(["v_landp_3", self.landing_port_line_3.text()])
        interviewInfo2.append(["v_landp_4", self.landing_port_line_4.text()])
        
        interviewInfo2.append(["v_yr_fish", self.years_fishing_line.text()])
        interviewInfo2.append(["v_num_pers", self.avg_people_line.text()])
        interviewInfo2.append(["v_days_fsh", self.avg_days_per_year_line.text()])
        interviewInfo2.append(["d_num_div", self.dive_avg_dives_per_trip.text()])
        interviewInfo2.append(["d_acc_mod", self.dive_access_mode.text()])
        interviewInfo2.append(["d_pct_isl", self.dive_percent_island.text()])
        interviewInfo2.append(["d_pct_shr", self.dive_percent_shore.text()])
        interviewInfo2.append(["d_method", self.dive_primary_method.currentText()])
        
        interviewInfo2.append(["k_port1", self.kyk_launch_port_1.text()])
        interviewInfo2.append(["k_port2", self.kyk_launch_port_2.text()])
        interviewInfo2.append(["k_port3", self.kyk_launch_port_3.text()])
        interviewInfo2.append(["k_port4", self.kyk_launch_port_4.text()])
        interviewInfo2.append(["k_yr_exp", self.kyk_years_experience.text()])
        interviewInfo2.append(["k_days_fsh", self.kyk_avg_days_per_year.text()])

        self.hide()
        self.parent.nextStep();

    def on_pbnCancel_released(self):
        cancel_choice = QMessageBox.question(self, "Really quit this interview?", "Are you sure you want to cancel and lose any entered data for this interview?", QMessageBox.Yes, QMessageBox.No)
        
        if cancel_choice == QMessageBox.Yes:
            # stop interview process
            self.close()
            self.parent.parent.statusbar.showMessage("Cancelled out of interview")
            self.parent.resetInterview()
            self.parent.parent.interviewInProgress = False
