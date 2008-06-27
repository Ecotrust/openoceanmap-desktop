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
                    self.parent.commFishIncome = int(self.comm_fish_line.text())

        if self.comm_sport_line:
            if not strIsInt(self.comm_sport_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.comm_sport_line.text() == '0':
                    self.parent.sportFishIncome = int(self.comm_sport_line.text())

        if self.private_fish_line:
            if not strIsInt(self.private_fish_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.private_fish_line.text() == '0':
                    self.parent.privateFishIncome =  int(self.private_fish_line.text())

        if self.ecotourism_line:
            if not strIsInt(self.ecotourism_line.text()):
                QMessageBox.warning(self, "Income Error", "Incomevalue must be a number (no decimals)")
                return
            else:
                if not self.ecotourism_line.text() == '0':
                    self.parent.ecotourismIncome = int(self.ecotourism_line.text())

        if self.cons_science_line:
            if not strIsInt(self.cons_science_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.cons_science_line.text() == '0':
                    self.parent.consScienceIncome = int(self.cons_science_line.text())

        if self.other_line:
            if not strIsInt(self.other_line.text()):
                QMessageBox.warning(self, "Income Error", "Income value must be a number (no decimals)")
                return
            else:
                if not self.other_line.text() == '0':
                    self.parent.otherIncome = int(self.other_line.text())
                    
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

        self.parent.nextStep(self)
        
            
    def on_pbnCancel_clicked(self):
        self.close()
        self.parent.resetInterview()