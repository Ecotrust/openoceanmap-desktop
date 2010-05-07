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
from addtquestions_ui import Ui_AdditionalQuestions
from Util.common_functions import *
# General system includes
import sys, copy

class AddtQuestionsGui(QDialog, Ui_AdditionalQuestions):
    def __init__(self, parent):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent   
        self.crew_shares.setText('0')
        self.captain_shares.setText('0')
        
    def on_num_crew_editingFinished(self):
        value = self.num_crew.text()
        if not strIsInt(value):
           QMessageBox.warning(self, "Input Error", "Number of crew must be a number.")
           return 
        int_val = int(value)
        capt_shares = 100 / (int_val + 1)
        crew_shares = 100 - capt_shares
        self.captain_shares.setText(str(capt_shares))
        self.crew_shares.setText(str(crew_shares))

    def on_pbnFinished_released(self):
        
        # do our error checking before adding fields to the data store
        shares = []
        if self.crew_shares.text() != '0':
            shares.append(('Crew',self.crew_shares.text()))
        if self.captain_shares.text() != '0':
            shares.append(('Captain',self.captain_shares.text()))
            
        total_values = 0
        for (share_type,value) in shares:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your share percentages is not a number")
                return 
            total_values = total_values + int(value)
                
        if total_values > 100 or total_values < 0:
            QMessageBox.warning(self, "Input Error", "Share percentages must sum to a value between 0 and 100 (current sum: "+str(total_values)+")")
            return 
            
                
        # error checks complete, go ahead and add fields to data store

        
        interviewInfo2 = self.parent.interviewInfo2
         
        interviewInfo2.append(["yrs_exp", self.yrs_fishing_line.text()]) 
        interviewInfo2.append(["pct_h_inc",self.pct_house_inc.text()])
        interviewInfo2.append(["num_depnd",self.num_dependents.text()])
        interviewInfo2.append(["num_crew",self.num_crew.text()])
        interviewInfo2.append(["crew_shar",self.crew_shares.text()])
        interviewInfo2.append(["crew_paid",self.how_crew_paid.currentText()])
        interviewInfo2.append(["capt_shar",self.captain_shares.text()])

        
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
