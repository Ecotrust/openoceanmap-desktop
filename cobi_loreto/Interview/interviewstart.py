#---------------------------------------------------------------------
# -*- coding: latin-1 -*-
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
from fisherswindow import FishersWindowGui
# UI specific includes
from interviewstart_ui import Ui_InterviewStart
# General system includes
import sys

from Util.common_functions import *

class InterviewStartGui(QDialog, Ui_InterviewStart):
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent

    def on_pbnNextWindow_released(self):
        interviewInfo2 = self.parent.interviewInfo2
        
        # interviewee group
        interviewInfo2.append([u"nombre", self.interviewee_first_name_line.text()])
        interviewInfo2.append([u"apellido", self.interviewee_last_name_line.text()])
        interviewInfo2.append([u"edad", self.age_line.text()])
        interviewInfo2.append([u"genero", self.gender_comboBox.currentText()])
        interviewInfo2.append([u"ciudad", self.city_line.text()])

        # interviewer group
        interviewInfo2.append([u"fecha", self.date_line.text()])        
        interviewInfo2.append([u"int_nombre", self.interviewer_first_name_line.text()])
        interviewInfo2.append([u"int_apell", self.interviewer_last_name_line.text()])
        interviewInfo2.append([u"anos", self.years_spinBox.text()])

        # income sources group
        interviewInfo2.append([u"pesca_com", self.comm_fish_line.text()])
        interviewInfo2.append([u"pesca_dep", self.comm_sport_line.text()])
        interviewInfo2.append([u"pesca_pri", self.private_fish_line.text()])
        interviewInfo2.append([u"ecoturismo", self.ecotourism_line.text()])
        interviewInfo2.append([u"ciencia", self.cons_science_line.text()])
        interviewInfo2.append([u"otro", self.other_line.text()])
        interviewInfo2.append([u"otro_desc", self.define_other_line.text()])

        # relaunch interview
        #flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        #wnd = InterviewStartGui(self,flags)
        #wnd.show()


        if self.comm_fish_line:
            if not strIsInt(self.comm_fish_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.comm_fish_line.text() == '0':
                    self.parent.currentCommFish = True

        if self.comm_sport_line:
            if not strIsInt(self.comm_sport_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.comm_sport_line.text() == '0':
                    self.parent.currentCommSport = True

        if self.private_fish_line:
            if not strIsInt(self.private_fish_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.private_fish_line.text() == '0':
                    self.parent.currentPrivateFish = True

        if self.ecotourism_line:
            if not strIsInt(self.ecotourism_line.text()):
                QMessageBox.warning(self, "Income Error", "Incomevalue must be a number (no decimals)")
                return
            else:
                if not self.ecotourism_line.text() == '0':
                    self.parent.currentEcotourism = True

        if self.cons_science_line:
            if not strIsInt(self.cons_science_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.cons_science_line.text() == '0':
                    self.parent.currentConsScience = True

        if self.other_line:
            if not strIsInt(self.other_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.other_line.text() == '0':
                    self.parent.currentOther = True
                    if not len(self.define_other_line.text()):
                        QMessageBox.warning(self, "Income Error", "Please Define the Other Income")
                        return
        total = int(self.comm_fish_line.text()) + int(self.comm_sport_line.text()) + int(self.private_fish_line.text()) + int(self.ecotourism_line.text()) + int(self.cons_science_line.text()) + int(self.other_line.text())
        print total
        if not int(total) == int(100):
            QMessageBox.warning(self, "Income Error", "All Values currently total %s: Please confirm they add up to 100." % total)
            return

        #import pdb
        #pyqtRemoveInputHook()
        #pdb.set_trace()
        # validation example 
        #if not cur_fishery:
         #   QMessageBox.warning(self, "Fishery Error", "Please select a fishery")
           # return 
        #else:
          #  self.parent.currentFishery = cur_fishery

        #interviewInfo2["t_region"] = self.region_comboBox.currentText()
        #interviewInfo2["t_ind_trip"] = self.ind_per_trip_line.text()
        #interviewInfo2["t_day_year"] = self.days_per_year_line.text()
        #interviewInfo2["t_tr_time"] = self.travel_time_line.text()
        #interviewInfo2["t_tr_dist"] = self.travel_distance_line.text()
        #self.parent.interviewInfo.append(self.line_1.text())
        #self.parent.interviewInfo.append(self.line_2.text())
        self.close()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = FishersWindowGui(self.parent,flags)
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
        self.parent.currentCommFish = False
        self.parent.currentCommSport = False
        self.parent.currentPrivateFish = False
        self.parent.currentEcotourism = False
        self.parent.currentConsScience = False
        self.parent.currentOther = False
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    #def nextPolygon(self):
    #    flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
    #    wnd = NextPolygonGui(self.parent,flags)
    #    wnd.show()



