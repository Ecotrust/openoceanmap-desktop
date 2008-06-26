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

        if self.comm_fish_line:
            if not strIsInt(self.comm_fish_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.comm_fish_line.text() == '0':
                    self.parent.currentFisheryIncome = 1
                    #self.parent.currentFisheryIncome = int(self.comm_fish_line.text())

        if self.comm_sport_line:
            if not strIsInt(self.comm_sport_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.comm_sport_line.text() == '0':
                    self.parent.currentFisheryIncome = 1
                    #self.parent.currentFisheryIncome = int(self.parent.currentFisheryIncome) + int(self.comm_sport_line.text())

        if self.private_fish_line:
            if not strIsInt(self.private_fish_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.private_fish_line.text() == '0':
                    self.parent.currentFisheryIncome = 1
                    #self.parent.currentFisheryIncome = int(self.parent.currentFisheryIncome) + int(self.private_fish_line.text())

        if self.ecotourism_line:
            if not strIsInt(self.ecotourism_line.text()):
                QMessageBox.warning(self, "Income Error", "Incomevalue must be a number (no decimals)")
                return
            else:
                if not self.ecotourism_line.text() == '0':
                    self.parent.currentEcotourismIncome = 1
                    #self.parent.currentEcotourismIncome = int(self.ecotourism_line.text())

        if self.cons_science_line:
            if not strIsInt(self.cons_science_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.cons_science_line.text() == '0':
                    self.parent.currentConsScienceIncome = 1
                    #self.parent.currentConsScienceIncome = int(self.cons_science_line.text())

        if self.other_line:
            if not strIsInt(self.other_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.other_line.text() == '0':
                    self.parent.currentOtherIncome = 1
                    #self.parent.currentOtherIncome = int(self.other_line.text())
                    
                    if not len(self.define_other_line.text()):
                        QMessageBox.warning(self, "Income Error", "Please Define the Other Income")
                        return


        total = int(self.comm_fish_line.text()) + int(self.comm_sport_line.text()) + int(self.private_fish_line.text()) + int(self.ecotourism_line.text()) + int(self.cons_science_line.text()) + int(self.other_line.text())
        if not int(total) == int(100):
            QMessageBox.warning(self, "Income Error", "All Values currently total %s: Please confirm they add up to 100." % total)
            return

        # setup for next gui depending on what incomes were specified
        self.hide()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint         
        if self.parent.currentFisheryIncome:
            capture_string = QString("Fishery Income exists, starting that interview...")
            self.parent.parent.statusbar.showMessage(capture_string)
            from fishery import FisheryGui
            wnd = FisheryGui(self.parent,flags,self)
            wnd.show()
            
        elif self.parent.currentEcotourismIncome:
            capture_string = QString("Ecotourism Income exists, starting that interview...")
            self.parent.parent.statusbar.showMessage(capture_string)
            from ecotourism import EcotourismGui
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
            wnd = EcotourismGui(self.parent,flags)
            wnd.show()
            
        elif self.parent.currentConsScienceIncome:
            capture_string = QString("Ecotourism Income exists, starting that interview...")
            self.parent.parent.statusbar.showMessage(capture_string)
            from consscience import ConsScienceGui
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
            wnd = ConsScienceGui(self.parent,flags)
            wnd.show()
            
        elif self.parent.currentOtherIncome:
            capture_string = QString("Ecotourism Income exists, starting that interview...")
            self.parent.parent.statusbar.showMessage(capture_string)
            from other import OtherGui
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
            wnd = OtherGui(self.parent,flags)
            wnd.show()
        
            
    def on_pbnCancel_clicked(self):
        self.close()
        capture_string = QString("Cancelled out of fishery interview...")
        print capture_string
        self.parent.parent.statusbar.showMessage(capture_string)
        
        # stop interview process
        self.parent.parent.interviewInProgress = False
        self.parent.parent.interviewSaveTool = None
        self.parent.currentFishery = None
        self.parent.currentEcotourism = None
        self.parent.currentConsScience = None
        self.parent.currentOther = None
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)