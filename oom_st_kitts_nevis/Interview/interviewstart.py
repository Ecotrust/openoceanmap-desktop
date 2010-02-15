#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
# Copyright (C) 2007  Aaron Racicot
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
# UI specific includes
from interviewstart_ui import Ui_InterviewStart
# General system includes
import sys

class InterviewStartGui(QDialog, Ui_InterviewStart):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent.mainwindow, fl)
        self.setupUi(self)
        self.parent = parent

    def on_pbnSelectFishery_released(self):
        interviewInfo2 = self.parent.interviewInfo2
        
        interviewInfo2.append(["fname", self.interviewee_first_name_line.text()])
        interviewInfo2.append(["lname", self.interviewee_last_name_line.text()])
        interviewInfo2.append(["mailaddr", self.address_line.text()])
        interviewInfo2.append(["phone", self.phone_line.text()])
        interviewInfo2.append(["email", self.email_line.text()])
        interviewInfo2.append(["age", self.age_line.text()])
        interviewInfo2.append(["gender", self.gender_comboBox.currentText()])
        
        interviewInfo2.append(["date", self.date_line.text()])   
        interviewInfo2.append(["location", self.location_line.text()])         
        interviewInfo2.append(["int1_fname", self.interviewer1_first_name_line.text()])
        interviewInfo2.append(["int1_lname", self.interviewer1_last_name_line.text()])
        interviewInfo2.append(["int2_fname", self.interviewer2_first_name_line.text()])
        interviewInfo2.append(["int2_lname", self.interviewer2_last_name_line.text()])
        interviewInfo2.append(["mood", self.mood_line.text()])
        interviewInfo2.append(["data_meth", self.dataMethod_comboBox.currentText()])
        
        interviewInfo2.append(["fish_reg", self.fish_regis_line.text()])
        interviewInfo2.append(["vsl_reg", self.vessel_regis_line.text()])
        interviewInfo2.append(["vsl_name", self.vessel_name_line.text()])
        interviewInfo2.append(["vsl_len", self.vessel_length_line.text()])
        interviewInfo2.append(["vsl_eng", self.vessel_engine_line.text()])
        interviewInfo2.append(["haul_cap", self.haul_capacity_line.text()])
        interviewInfo2.append(["vsl_mpg", self.vessel_mpg_line.text()])
        interviewInfo2.append(["port_reg", self.port_regis_line.text()])
        interviewInfo2.append(["port_op", self.port_op_line.text()])
        interviewInfo2.append(["vsl_relat", self.relation_vessel_line.text()])
        interviewInfo2.append(["yrs_exp", self.yrs_fishing_line.text()])
        interviewInfo2.append(["fish_time", self.fishTime_comboBox.currentText()])

        self.close()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 

        self.parent.nextStep()
        
        #mc = self.parent.canvas      
        #self.p = PolygonTool(mc,self.parent)
        #QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        #self.saveTool = mc.mapTool()
        #mc.setMapTool(self.p)
            
    def on_pbnCancel_released(self):
        cancel_choice = QMessageBox.question(self, "Really quit this interview?", "Are you sure you want to cancel and lose any entered data for this interview?", QMessageBox.Yes, QMessageBox.No)
        
        if cancel_choice == QMessageBox.Yes:
            self.close()
            self.parent.resetInterview()
            self.parent.parent.interviewInProgress = False

    #def nextPolygon(self):
    #    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    #    wnd = NextPolygonGui(self.parent,flags)
    #    wnd.show()



