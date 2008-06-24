#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
# Copyright (C) 2007  Aaron Racicot
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
        
        interviewInfo2.append(["date", self.date_line.text()])
        interviewInfo2.append(["int1_fname", self.interviewer1_first_name_line.text()])
        interviewInfo2.append(["int1_lname", self.interviewer1_last_name_line.text()])
        interviewInfo2.append(["int2_fname", self.interviewer2_first_name_line.text()])
        interviewInfo2.append(["int2_lname", self.interviewer2_last_name_line.text()])
        interviewInfo2.append(["fname", self.interviewee_first_name_line.text()])
        interviewInfo2.append(["lname", self.interviewee_last_name_line.text()])
        interviewInfo2.append(["age", self.age_line.text()])
        interviewInfo2.append(["gender", self.gender_comboBox.currentText()])
        interviewInfo2.append(["years", self.years_line.text()])
        interviewInfo2.append(["license", self.license_line.text()])
        interviewInfo2.append(["city", self.city_line.text()])
        interviewInfo2.append(["user_group", self.user_group_comboBox.currentText()])
        
        interviewInfo2.append(["v_homep", self.home_port_line.text()])
        interviewInfo2.append(["v_license", self.ves_license_line.text()])
        interviewInfo2.append(["v_len", self.vessel_length_line.text()])
        interviewInfo2.append(["years_op", self.years_op_line.text()])
        interviewInfo2.append(["v_yearown", self.years_own_line.text()])
        
        interviewInfo2.append(["t_region", self.region_comboBox.currentText()])
        interviewInfo2.append(["t_ind_trip", self.ind_per_trip_line.text()])
        interviewInfo2.append(["t_day_year", self.days_per_year_line.text()])
        interviewInfo2.append(["t_tr_time", self.travel_time_line.text()])
        interviewInfo2.append(["t_tr_dist", self.travel_distance_line.text()])

        #interviewInfo2 = self.parent.interviewInfo2
        #interviewInfo2["fname"] = self.interviewee_first_name_line.text()
        #interviewInfo2["lname"] = self.interviewee_last_name_line.text()
        #interviewInfo2["age"] = self.age_line.text()
        #interviewInfo2["gender"] = self.gender_comboBox.currentText()
        #interviewInfo2["years"] = self.years_line.text()
        #interviewInfo2["years_op"] = self.years_op_line.text()
        #interviewInfo2["years_own"] = self.years_own_line.text()
        #interviewInfo2["license"] = self.license_line.text()
        #interviewInfo2["city"] = self.city_line.text()
        #interviewInfo2["user_group"] = self.user_group_comboBox.currentText()
        #
        #interviewInfo2["int1_fname"] = self.interviewer1_first_name_line.text()
        #interviewInfo2["int1_lname"] = self.interviewer1_last_name_line.text()
        #interviewInfo2["int2_fname"] = self.interviewer2_first_name_line.text()
        #interviewInfo2["int2_lname"] = self.interviewer2_last_name_line.text()
        #interviewInfo2["date"] = self.date_line.text()
        #
        #interviewInfo2["v_license"] = self.ves_license_line.text()
        #interviewInfo2["v_yearown"] = self.years_own_line.text()
        #interviewInfo2["v_len"] = self.vessel_length_line.text()
        #interviewInfo2["v_homep"] = self.home_port_line.text()
        #
        #interviewInfo2["t_region"] = self.region_comboBox.currentText()
        #interviewInfo2["t_ind_trip"] = self.ind_per_trip_line.text()
        #interviewInfo2["t_day_year"] = self.days_per_year_line.text()
        #interviewInfo2["t_tr_time"] = self.travel_time_line.text()
        #interviewInfo2["t_tr_dist"] = self.travel_distance_line.text()
        #self.parent.interviewInfo.append(self.line_1.text())
        #self.parent.interviewInfo.append(self.line_2.text())
        self.close()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = SelectFisheryGui(self.parent,flags)
        wnd.show()
        #mc = self.parent.canvas      
        #self.p = PolygonTool(mc,self.parent)
        #QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        #self.saveTool = mc.mapTool()
        #mc.setMapTool(self.p)
            
    def on_pbnCancel_clicked(self):
        self.close()
        capture_string = QString("Cancelled out of fishery interview...")
        print capture_string
        self.parent.parent.statusbar.showMessage(capture_string)
        
        # stop interview process
        self.parent.parent.interviewInProgress = False
        self.parent.parent.interviewSaveTool = None
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    #def nextPolygon(self):
    #    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    #    wnd = NextPolygonGui(self.parent,flags)
    #    wnd.show()



