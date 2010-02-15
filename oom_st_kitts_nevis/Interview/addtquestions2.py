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
from addtquestions2_ui import Ui_AdditionalQuestions2
from Util.common_functions import *
# General system includes
import sys, copy

class AddtQuestions2Gui(QDialog, Ui_AdditionalQuestions2):
    def __init__(self, parent):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent   
        self.catch_personal.setText('0')
        self.catch_customers.setText('0')
        self.catch_hotel.setText('0')
        self.catch_agency.setText('0')
        self.catch_other.setText('0')

    def on_pbnFinished_released(self):
        
        # do our error checking before adding fields to the data store
            
        catch_alloc = []
        if self.catch_personal.text() != '0':
            catch_alloc.append(('Crew',self.catch_personal.text()))
        if self.catch_customers.text() != '0':
            catch_alloc.append(('Boat',self.catch_customers.text()))
        if self.catch_hotel.text() != '0':
            catch_alloc.append(('Captain',self.catch_hotel.text()))
        if self.catch_agency.text() != '0':
            catch_alloc.append(('Owner',self.catch_agency.text()))
        if self.catch_other.text() != '0':
            catch_alloc.append(('Owner',self.catch_other.text()))
            
        total_values = 0
        for (catch_type,value) in catch_alloc:
            if not strIsInt(value):
                QMessageBox.warning(self, "Input Error", "One of your catch percentages is not a number")
                return 
            total_values = total_values + int(value)
                
        if total_values != 100:
            QMessageBox.warning(self, "Input Error", "Catch percentages must add up to 100 (current sum: "+str(total_values)+")")
            return 
                
        # error checks complete, go ahead and add fields to data store

        
        interviewInfo2 = self.parent.interviewInfo2
         
        interviewInfo2.append(["c_persnl",self.catch_personal.text()])
        interviewInfo2.append(["c_custmr",self.catch_customers.text()])
        interviewInfo2.append(["c_hotel",self.catch_hotel.text()])
        interviewInfo2.append(["c_agency",self.catch_agency.text()])
        interviewInfo2.append(["c_other",self.catch_other.text()])
        interviewInfo2.append(["c_oth_tp",self.catch_other_type.text()])
        
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
