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
        interviewInfo2.append(["cpfv_type", self.cpfv_type_combo.currentText()])
        interviewInfo2.append(["license", self.cpfv_lic_line.text()])
        interviewInfo2.append(["yrs_oper", self.cpfv_yr_op_line.text()])   
        interviewInfo2.append(["yrs_own",self.cpfv_yr_own_line.text()])
        interviewInfo2.append(["vessel_len",self.cpfv_len_line.text()])
        interviewInfo2.append(["trip_len",self.cpfv_trip_length_combo.currentText()])
        interviewInfo2.append(["homeport",self.cpfv_home_port_line.text()])
        interviewInfo2.append(["yrs_exp",self.cpfv_yr_exp_line.text()])
        interviewInfo2.append(["days_fish",self.cpfv_num_days_line.text()])
        interviewInfo2.append(["num_clients",self.cpfv_num_clients_line.text()])
        interviewInfo2.append(["num_crew",self.cpfv_num_crew_line.text()])
        interviewInfo2.append(["oper_cost",self.cpfv_operating_cost_line.text()])
        interviewInfo2.append(["labor_cost",self.cpfv_labor_cost_line.text()])
        interviewInfo2.append(["fuel_cost",self.cpfv_fuel_cost_line.text()])
        
        self.hide()
        wnd = SelectFisheryGui(self.parent)
        wnd.show()        
        
    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetIntervizw("Cancelled out of interview")