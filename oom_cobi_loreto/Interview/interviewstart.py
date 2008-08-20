#---------------------------------------------------------------------
# -*- coding: latin-1 -*-
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Dane Springmeyer
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
from PyQt4.QtGui import QApplication as QA
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
        self.retranslate()

    def on_pbnNextWindow_released(self):
        interviewInfo2 = self.parent.interviewInfo2        
        # interviewee group
        interviewInfo2.append([self.f_first_name_str, self.interviewee_first_name_line.text()])
        self.parent.first_name = self.interviewee_first_name_line.text().toLower()
        interviewInfo2.append([self.f_last_name_str, self.interviewee_last_name_line.text()])
        self.parent.last_name = self.interviewee_last_name_line.text().toLower()
        interviewInfo2.append([self.f_age_str, self.age_line.text()])
        interviewInfo2.append([self.f_gender_str, self.gender_comboBox.currentText()])
        interviewInfo2.append([self.f_city_str, self.city_line.text()])
        # interviewer group
        interviewInfo2.append([self.f_date_str, self.date_line.text()])        
        interviewInfo2.append([self.f_int_first_name_str, self.interviewer_first_name_line.text()])
        interviewInfo2.append([self.f_int_last_name_str, self.interviewer_last_name_line.text()])
        interviewInfo2.append([self.f_years_str, self.years_spinBox.text()])

        if self.comm_fish_line:
            if not strIsInt(self.comm_fish_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_str)
                return
            else:
                if not self.comm_fish_line.text() == '0':
                    self.parent.commFishIncome = int(self.comm_fish_line.text())

        if self.comm_sport_line:
            if not strIsInt(self.comm_sport_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_st)
                return
            else:
                if not self.comm_sport_line.text() == '0':
                    self.parent.sportFishIncome = int(self.comm_sport_line.text())

        if self.private_fish_line:
            if not strIsInt(self.private_fish_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_st)
                return
            else:
                if not self.private_fish_line.text() == '0':
                    self.parent.privateFishIncome =  int(self.private_fish_line.text())

        if self.ecotourism_line:
            if not strIsInt(self.ecotourism_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_st)
                return
            else:
                if not self.ecotourism_line.text() == '0':
                    self.parent.ecotourismIncome = int(self.ecotourism_line.text())

        if self.cons_science_line:
            if not strIsInt(self.cons_science_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_st)
                return
            else:
                if not self.cons_science_line.text() == '0':
                    self.parent.consScienceIncome = int(self.cons_science_line.text())

        if self.other_line:
            if not strIsInt(self.other_line.text()):
                QMessageBox.warning(self, self.income_error_str, self.income_value_st)
                return
            else:
                if not self.other_line.text() == '0':
                    self.parent.otherIncome = int(self.other_line.text())

        total = int(self.comm_fish_line.text()) + int(self.comm_sport_line.text()) + int(self.private_fish_line.text()) + int(self.ecotourism_line.text()) + int(self.cons_science_line.text()) + int(self.other_line.text())
        if int(total) != int(100):
            QMessageBox.warning(self, self.income_error_str, self.values_total_str + unicode(total) + self.change_str)
            return

        # setup for next gui depending on what incomes were specified
        self.hide()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint         

        self.parent.nextStep(self)        
            
    def on_pbnCancel_clicked(self):
        self.close()
        self.parent.resetInterview()

    def retranslate(self):
        self.f_first_name_str = QA.translate("InterviewStartGui", "f_name", "Interviewee first name attribute", QA.UnicodeUTF8)
        self.f_last_name_str = QA.translate("InterviewStartGui", "l_name", "Interviewee last name attribute", QA.UnicodeUTF8)       
        self.f_age_str = QA.translate("InterviewStartGui", "age", "Age attribute", QA.UnicodeUTF8)
        self.f_gender_str = QA.translate("InterviewStartGui", "gender", "Gender attribute", QA.UnicodeUTF8)
        self.f_city_str = QA.translate("InterviewStartGui", "city", "City attribute", QA.UnicodeUTF8)
        self.f_date_str = QA.translate("InterviewStartGui", "date", "Date of interview attribute", QA.UnicodeUTF8)
        self.f_int_first_name_str = QA.translate("InterviewStartGui", "i_f_name", "Interviewer first name attribute", QA.UnicodeUTF8)
        self.f_int_last_name_str = QA.translate("InterviewStartGui", "i_l_name", "Interview last name attribute", QA.UnicodeUTF8)
        self.f_years_str = QA.translate("InterviewStartGui", "years", "Number of years fishing attribute", QA.UnicodeUTF8)
        self.income_error_str = QA.translate("InterviewStartGui", "Income Error", "", QA.UnicodeUTF8)
        self.income_value_str = QA.translate("InterviewStartGui", "Income value must be a number (no decimals)", "", QA.UnicodeUTF8)
        self.values_total_str = QA.translate("InterviewStartGui", "All Values currently total ", "First part of text that tells the user the total for all income percentages they entered", QA.UnicodeUTF8)        
        self.change_str = QA.translate("InterviewStartGui", ". Please change them.", "Second part of text telling the user their incomes don't add up to 100 so they need to change the values such that they do add up to 100", QA.UnicodeUTF8)