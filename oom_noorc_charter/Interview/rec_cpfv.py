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
from rec_cpfv_ui import Ui_RecCpfv
from Util.common_functions import *
# General system includes
import sys, copy

class RecCpfvGui(QDialog, Ui_RecCpfv):
    def __init__(self, parent):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent

    def on_pbnFinished_released(self):
        
        
        interviewInfo2 = self.parent.interviewInfo2
        interviewInfo2.append(["user_group", "charter"])

        interviewInfo2.append(["cp_num_own", self.cpfv_num_own_line.text()])
        interviewInfo2.append(["cp_yr_own", self.cpfv_yr_own_line.text()])
        interviewInfo2.append(["annl_rev",self.cpfv_revenue_line.text()])
        interviewInfo2.append(["oper_cost",self.cpfv_operating_cost_line.text()])
        interviewInfo2.append(["labor_cost",self.cpfv_labor_cost_line.text()])
        interviewInfo2.append(["fuel_cost",self.cpfv_fuel_cost_line.text()])
        
        interviewInfo2.append(["pcnt_inc", self.cpfv_percent_income_line.text()])
        interviewInfo2.append(["cp_type", self.cpfv_type_combo.currentText()])
        interviewInfo2.append(["v_doc_num", self.cpfv_lic_line.text()])
        #interviewInfo2.append(["v_fed_num", self.cpfv_fed_doc_line.text()])
        interviewInfo2.append(["v_name",self.cpfv_name_line.text()])
        interviewInfo2.append(["v_length",self.cpfv_len_line.text()])
        interviewInfo2.append(["homeport",self.cpfv_home_port_line.text()])
        interviewInfo2.append(["cp_num_op", self.cpfv_num_op_line.text()])
        interviewInfo2.append(["cp_yr_op", self.cpfv_yr_op_line.text()])
        interviewInfo2.append(["days_fish",self.cpfv_num_days_line.text()])
        interviewInfo2.append(["num_pass",self.cpfv_num_pass_line.text()])
        interviewInfo2.append(["pct_out_st",self.cpfv_num_out_state_line.text()])
        interviewInfo2.append(["num_crew",self.cpfv_num_crew_line.text()])

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
