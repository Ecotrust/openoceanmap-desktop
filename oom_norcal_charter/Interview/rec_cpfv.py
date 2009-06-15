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
        self.cpfv_target_tuna.setText('0')
        self.cpfv_target_salmon.setText('0')
        self.cpfv_target_halibut.setText('0')
        self.cpfv_target_groundfish.setText('0')
        self.cpfv_target_dcrab.setText('0')

    def on_pbnFinished_released(self):
        
        # do our error checking before adding fields to the data store
        cpfv_fisheries = []
        if self.cpfv_target_tuna.text() != '0':
            cpfv_fisheries.append(('Tuna',self.cpfv_target_tuna.text()))
        if self.cpfv_target_salmon.text() != '0':
            cpfv_fisheries.append(('Salmon',self.cpfv_target_salmon.text()))
        if self.cpfv_target_halibut.text() != '0':
            cpfv_fisheries.append(('Halibut',self.cpfv_target_halibut.text()))
        if self.cpfv_target_groundfish.text() != '0':
            cpfv_fisheries.append(('Groundfish',self.cpfv_target_groundfish.text()))
        if self.cpfv_target_dcrab.text() != '0':
            cpfv_fisheries.append(('Dungeness Crab',self.cpfv_target_dcrab.text())) 
            
        total_values = 0
        for (fishery,value) in cpfv_fisheries:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your fishery percentages is not a number")
                return 
            total_values = total_values + int(value)
                
        if total_values == 0:
            QMessageBox.warning(self, "Input Error", "At least one fishery must exceed 0% of annual trips")
            return 
                
        # error checks complete, go ahead and add fields to data store
        self.parent.fisheries = cpfv_fisheries
        
        interviewInfo2 = self.parent.interviewInfo2
        interviewInfo2.append(["user_group", "charter"])

        interviewInfo2.append(["cp_num_own", self.cpfv_num_own_line.text()])
        interviewInfo2.append(["cp_yr_own", self.cpfv_yr_own_line.text()])
        #interviewInfo2.append(["annl_rev",self.cpfv_revenue_line.text()])
        interviewInfo2.append(["oper_cost",self.cpfv_operating_cost_line.text()])
        interviewInfo2.append(["labor_cost",self.cpfv_labor_cost_line.text()])
        interviewInfo2.append(["fuel_cost",self.cpfv_fuel_cost_line.text()])
        
        interviewInfo2.append(["pcnt_inc", self.cpfv_percent_income_line.text()])
        interviewInfo2.append(["cp_type", self.cpfv_type_combo.currentText()])
        interviewInfo2.append(["v_doc_num", self.cpfv_lic_line.text()])
        interviewInfo2.append(["v_fed_num", self.cpfv_fed_doc_line.text()])
        interviewInfo2.append(["v_name",self.cpfv_name_line.text()])
        interviewInfo2.append(["v_length",self.cpfv_len_line.text()])
        interviewInfo2.append(["homeport",self.cpfv_home_port_line.text()])
        interviewInfo2.append(["cp_num_op", self.cpfv_num_op_line.text()])
        interviewInfo2.append(["cp_yr_op", self.cpfv_yr_op_line.text()])
        interviewInfo2.append(["days_fish",self.cpfv_num_days_line.text()])
        interviewInfo2.append(["num_pass",self.cpfv_num_pass_line.text()])
        interviewInfo2.append(["num_out_st",self.cpfv_num_out_state_line.text()])
        interviewInfo2.append(["num_crew",self.cpfv_num_crew_line.text()])
         
        interviewInfo2.append(["pcnt_dcrab",self.cpfv_target_dcrab.text()])
        interviewInfo2.append(["tlen_dcrab",self.cpfv_tlen_combo_dcrab.currentText()])
        interviewInfo2.append(["acst_dcrab",self.cpfv_angler_cost_dcrab.text()])
   
        interviewInfo2.append(["pcnt_grndf",self.cpfv_target_groundfish.text()])
        interviewInfo2.append(["tlen_grndf",self.cpfv_tlen_combo_groundfish.currentText()])
        interviewInfo2.append(["acst_grndf",self.cpfv_angler_cost_groundfish.text()])
    
        interviewInfo2.append(["pcnt_halib",self.cpfv_target_halibut.text()])
        interviewInfo2.append(["tlen_halib",self.cpfv_tlen_combo_halibut.currentText()])
        interviewInfo2.append(["acst_halib",self.cpfv_angler_cost_halibut.text()])
              
        interviewInfo2.append(["pcnt_salmn",self.cpfv_target_salmon.text()])
        interviewInfo2.append(["tlen_salmn",self.cpfv_tlen_combo_salmon.currentText()])
        interviewInfo2.append(["acst_salmn",self.cpfv_angler_cost_salmon.text()])
             
        interviewInfo2.append(["pcnt_tuna",self.cpfv_target_tuna.text()])
        interviewInfo2.append(["tlen_tuna",self.cpfv_tlen_combo_tuna.currentText()])
        interviewInfo2.append(["acst_tuna",self.cpfv_angler_cost_tuna.text()])

        #total = sum([int(b) for (a,b) in cpfv_fisheries])
        #print "Total: "+str(total)

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
