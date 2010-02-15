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
        self.fish_pct_1.setText('0')
        self.fish_pct_2.setText('0')
        self.fish_pct_3.setText('0')
        self.fish_pct_4.setText('0')
        self.fish_pct_5.setText('0')
        self.fish_pct_6.setText('0')
        self.fish_pct_7.setText('0')
        self.fish_pct_8.setText('0')
        self.fish_pct_9.setText('0')
        self.fish_pct_10.setText('0')
        self.fish_pct_11.setText('0')
        self.fish_pct_12.setText('0')
        self.fish_pct_13.setText('0')
        self.fish_pct_14.setText('0')
        self.fish_pct_15.setText('0')
        self.fish_pct_16.setText('0')
        self.fish_pct_17.setText('0')
        self.fish_pct_18.setText('0')        

    def on_pbnFinished_released(self):
        
        # do our error checking before adding fields to the data store
        cpfv_fisheries = []
        if self.fish_pct_1.text() != '0':
            cpfv_fisheries.append(('cpel_sein',self.fish_pct_1.text()))
        if self.fish_pct_2.text() != '0':
            cpfv_fisheries.append(('cpel_trol',self.fish_pct_2.text()))
        if self.fish_pct_3.text() != '0':
            cpfv_fisheries.append(('opel_trol',self.fish_pct_3.text()))
        if self.fish_pct_4.text() != '0':
            cpfv_fisheries.append(('cdem_trap',self.fish_pct_4.text()))
        if self.fish_pct_5.text() != '0':
            cpfv_fisheries.append(('cdem_pole',self.fish_pct_5.text()))
        if self.fish_pct_6.text() != '0':
            cpfv_fisheries.append(('cdem_spr',self.fish_pct_6.text()))
        if self.fish_pct_7.text() != '0':
            cpfv_fisheries.append(('cdem_gil',self.fish_pct_7.text()))
        if self.fish_pct_8.text() != '0':
            cpfv_fisheries.append(('ddem_trap',self.fish_pct_8.text()))
        if self.fish_pct_9.text() != '0':
            cpfv_fisheries.append(('ddem_pole',self.fish_pct_9.text()))
        if self.fish_pct_10.text() != '0':
            cpfv_fisheries.append(('lob_trap',self.fish_pct_10.text()))
        if self.fish_pct_11.text() != '0':
            cpfv_fisheries.append(('lob_scuba',self.fish_pct_11.text()))
        if self.fish_pct_12.text() != '0':
            cpfv_fisheries.append(('lob_free',self.fish_pct_12.text()))
        if self.fish_pct_13.text() != '0':
            cpfv_fisheries.append(('con_scuba',self.fish_pct_13.text()))
        if self.fish_pct_14.text() != '0':
            cpfv_fisheries.append(('con_free',self.fish_pct_14.text()))
        if self.fish_pct_15.text() != '0':
            cpfv_fisheries.append(('shk_hook',self.fish_pct_15.text()))
        if self.fish_pct_16.text() != '0':
            cpfv_fisheries.append(('shk_gil',self.fish_pct_16.text()))
        if self.fish_pct_17.text() != '0':
            cpfv_fisheries.append(('dsqd_hook',self.fish_pct_17.text()))
        if self.fish_pct_18.text() != '0':
            cpfv_fisheries.append(('trtl_net',self.fish_pct_18.text()))
            
        total_values = 0
        for (fishery,value) in cpfv_fisheries:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your fishery percentages is not a number")
                return 
            total_values = total_values + int(value)
                
        if total_values != 100:
            QMessageBox.warning(self, "Input Error", "Fishery percentages must add up to 100 (current sum: "+str(total_values)+")")
            return 
                
        # error checks complete, go ahead and add fields to data store
        #self.parent.fisheries = cpfv_fisheries
        #self.parent.clipped_fisheries = copy.copy(cpfv_fisheries)
        
        interviewInfo2 = self.parent.interviewInfo2
         
        interviewInfo2.append(["cpel_sein",self.fish_pct_1.text()])
        interviewInfo2.append(["cpel_trol",self.fish_pct_2.text()])
        interviewInfo2.append(["opel_trol",self.fish_pct_3.text()])
        interviewInfo2.append(["cdem_trap",self.fish_pct_4.text()])
        interviewInfo2.append(["cdem_pole",self.fish_pct_5.text()])
        interviewInfo2.append(["cdem_spr",self.fish_pct_6.text()])
        interviewInfo2.append(["cdem_gil",self.fish_pct_7.text()])
        interviewInfo2.append(["ddem_trap",self.fish_pct_8.text()])
        interviewInfo2.append(["ddem_pole",self.fish_pct_9.text()])
        interviewInfo2.append(["lob_trap",self.fish_pct_10.text()])
        interviewInfo2.append(["lob_scuba",self.fish_pct_11.text()])
        interviewInfo2.append(["lob_free",self.fish_pct_12.text()])
        interviewInfo2.append(["con_scuba",self.fish_pct_13.text()])
        interviewInfo2.append(["con_free",self.fish_pct_14.text()])
        interviewInfo2.append(["shk_hook",self.fish_pct_15.text()])
        interviewInfo2.append(["shk_gil",self.fish_pct_16.text()])
        interviewInfo2.append(["dsqd_hook",self.fish_pct_17.text()])
        interviewInfo2.append(["trtl_net",self.fish_pct_18.text()])
        
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
