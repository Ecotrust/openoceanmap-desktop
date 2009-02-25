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
        interviewInfo2.append(["age", self.age_line.text()])
        interviewInfo2.append(["gender", self.gender_comboBox.currentText()])
        interviewInfo2.append(["city", self.city_line.text()])

        interviewInfo2.append(["date", self.date_line.text()])        
        interviewInfo2.append(["int1_fname", self.interviewer1_first_name_line.text()])
        interviewInfo2.append(["int1_lname", self.interviewer1_last_name_line.text()])
        interviewInfo2.append(["mood", self.mood_line.text()])

        self.close()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 

        self.parent.nextStep(self)
        
        #mc = self.parent.canvas      
        #self.p = PolygonTool(mc,self.parent)
        #QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        #self.saveTool = mc.mapTool()
        #mc.setMapTool(self.p)
            
    def on_pbnCancel_clicked(self):
        self.close()

    #def nextPolygon(self):
    #    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    #    wnd = NextPolygonGui(self.parent,flags)
    #    wnd.show()



