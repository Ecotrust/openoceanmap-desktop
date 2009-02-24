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
import sys

class RecCpfvGui(QDialog, Ui_RecCpfv):
    def __init__(self, parent):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent

    def on_pbnFinished_released(self):
        interviewInfo2 = self.parent.interviewInfo2
        interviewInfo2.append(["user_group", "cpfv"])
        
        interviewInfo2.append(["cp_num_op", self.cpfv_num_op_line.text()])
        interviewInfo2.append(["cp_yr_op", self.cpfv_yr_op_line.text()])

        interviewInfo2.append(["cp_num_own", self.cpfv_num_own_line.text()])
        interviewInfo2.append(["cp_yr_own", self.cpfv_yr_own_line.text()])
        interviewInfo2.append(["oper_cost",self.cpfv_operating_cost_line.text()])
        interviewInfo2.append(["labor_cost",self.cpfv_labor_cost_line.text()])
        interviewInfo2.append(["fuel_cost",self.cpfv_fuel_cost_line.text()])
        
        interviewInfo2.append(["cp_type", self.cpfv_type_combo.currentText()])
        interviewInfo2.append(["v_doc_num", self.cpfv_lic_line.text()])
        interviewInfo2.append(["v_name",self.cpfv_name_line.text()])
        interviewInfo2.append(["v_length",self.cpfv_len_line.text()])
        interviewInfo2.append(["trip_len",self.cpfv_trip_length_combo.currentText()])
        interviewInfo2.append(["homeport",self.cpfv_home_port_line.text()])
        interviewInfo2.append(["yrs_fishin",self.cpfv_yr_exp_line.text()])
        interviewInfo2.append(["days_fish",self.cpfv_num_days_line.text()])
        interviewInfo2.append(["num_pass",self.cpfv_num_pass_line.text()])
        interviewInfo2.append(["num_out_st",self.cpfv_num_out_state_line.text()])
        interviewInfo2.append(["num_crew",self.cpfv_num_crew_line.text()])
        
        interviewInfo2.append(["str_tuna",self.cpfv_strat_tuna.text()])
        interviewInfo2.append(["str_coast",self.cpfv_strat_coast.text()])
        interviewInfo2.append(["str_island",self.cpfv_strat_island.text()])
        interviewInfo2.append(["str_rock",self.cpfv_strat_rock.text()])
        interviewInfo2.append(["str_misc",self.cpfv_strat_misc.text()])
        
        cpfv_fisheries = []
        if self.cpfv_target_barracuda.text() != '0':
            cpfv_fisheries.append(('Barracuda',self.cpfv_target_barracuda.text()))
        if self.cpfv_target_bonito.text() != '0':
            cpfv_fisheries.append(('Bonito',self.cpfv_target_bonito.text()))
        if self.cpfv_target_calico.text() != '0':
            cpfv_fisheries.append(('Calico Bass',self.cpfv_target_calico.text()))
        if self.cpfv_target_humboldt.text() != '0':
            cpfv_fisheries.append(('Humboldt Squid',self.cpfv_target_humboldt.text()))
        if self.cpfv_target_halibut.text() != '0':
            cpfv_fisheries.append(('Halibut',self.cpfv_target_halibut.text()))
        if self.cpfv_target_lingcod.text() != '0':
            cpfv_fisheries.append(('Lingcod',self.cpfv_target_lingcod.text()))
        if self.cpfv_target_rockfish.text() != '0':
            cpfv_fisheries.append(('Rockfish',self.cpfv_target_rockfish.text()))
        if self.cpfv_target_sand.text() != '0':
            cpfv_fisheries.append(('Sand Bass',self.cpfv_target_sand.text()))
        if self.cpfv_target_sculpin.text() != '0':
            cpfv_fisheries.append(('Sculpin (Cal. Scorpion Fish)',self.cpfv_target_sculpin.text()))
        if self.cpfv_target_white.text() != '0':
            cpfv_fisheries.append(('White Seabass',self.cpfv_target_white.text()))
        if self.cpfv_target_yellowtail.text() != '0':
            cpfv_fisheries.append(('Yellowtail',self.cpfv_target_yellowtail.text()))
        if self.cpfv_target_sheephead.text() != '0':
            cpfv_fisheries.append(('Sheephead',self.cpfv_target_sheephead.text()))
        if self.cpfv_target_shark.text() != '0':
            cpfv_fisheries.append(('Thresher/Mako/Blue Shark',self.cpfv_target_shark.text()))
        if self.cpfv_target_salmon.text() != '0':
            cpfv_fisheries.append(('Salmon',self.cpfv_target_salmon.text()))
        if self.cpfv_target_tuna.text() != '0':
            cpfv_fisheries.append(('Tuna & Dorado',self.cpfv_target_tuna.text()))
        if self.cpfv_target_whitefish.text() != '0':
            cpfv_fisheries.append(('Whitefish',self.cpfv_target_whitefish.text()))

        self.parent.fisheries = cpfv_fisheries

        for (fishery,value) in cpfv_fisheries:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your fishery percentages is not a number")
                return 

            print str(fishery)+" : "+str(value)
        
        total = sum([int(b) for (a,b) in cpfv_fisheries])
        print "Total: "+str(total)

        self.hide()
        self.parent.next_fishery();

    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetInterview("Cancelled out of interview")
