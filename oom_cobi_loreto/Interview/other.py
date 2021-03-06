#---------------------------------------------------------------------
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
from other_ui import Ui_Other

from Util.common_functions import *

# General system includes
import sys

class OtherGui(QDialog, Ui_Other):
    def __init__(self, parent, flags, textType, previousGui):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.textType = textType
        self.previousGui = previousGui
        self.retranslate()

    def on_pbnFinished_released(self):
        interviewInfo2 = self.parent.interviewInfo2
        self.parent.capturedText = self.other_line.text()
        self.parent.capturedTextType = self.textType
        self.parent.otherIncome = None
        self.parent.saveText(self)
        self.parent.nextStep(self, self.finish_str)
        
    def on_pbnCancel_clicked(self):
        self.close()
        self.parent.otherIncome = None
        self.parent.nextStep(self, self.cancel_str)

    def retranslate(self):
        self.finish_str = QA.translate("OtherGui", "Finishing Other income interview", "Status message for finishing 'other' portion of interview", QA.UnicodeUTF8)
        self.cancel_str = QA.translate("OtherGui", "Canceling other interview", "Status message shown when user cancels out of the 'other' portion of the interview", QA.UnicodeUTF8)
