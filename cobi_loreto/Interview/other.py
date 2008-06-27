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

    def on_pbnFinished_released(self):

        interviewInfo2 = self.parent.interviewInfo2
        print interviewInfo2
        #info = ', '.join(interviewInfo2[0])
        self.parent.capturedText = self.other_line.text()
        self.parent.capturedTextType = self.textType
        self.parent.otherIncome = None
        self.parent.saveText(self)
#        self.parent.nextStep(self, "Finishing Other income interview")
        
    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetInterview("Cancelled out of Other Income interview...")
