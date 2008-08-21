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

from consscience_ui import Ui_ConsScience

from Util.common_functions import *

# General system includes
import sys

class ConsScienceGui(QDialog, Ui_ConsScience):
    def __init__(self, parent, flags, prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI
        self.retranslate()

    def on_pbnSelectConsScience_released(self):

        self.parent.add_attrib(self.f_focus_str, self.comboBox.currentText())
        self.parent.add_attrib(self.f_add_info_str, self.add_info_line.text())

        if not self.comboBox.currentText():
            QMessageBox.warning(self, self.spec_error_str, self.choose_specialist_str)
            return

        self.close()
        from selectconsscience import SelectConsScienceGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = SelectConsScienceGui(self.parent,flags)
        wnd.show()

    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetInterview(self.cancel_conscience_str)

    def retranslate(self):
        self.spec_error_str = QA.translate("ConsScienceGui", 'Specialist Error', "Error message when specialist type not selected", QA.UnicodeUTF8)
        self.choose_specialist_str = QA.translate("ConsScienceGui", "Please choose a specialist position", "Error message when specialist type not selected", QA.UnicodeUTF8)
        self.f_focus_str = QA.translate("ConsScienceGui", "focus", "conservationist/scientist area of focus", QA.UnicodeUTF8)
        self.f_add_info_str = QA.translate("ConsScienceGui", "add_info", "additional info about con/science focus (kelp, mangrove, etc)", QA.UnicodeUTF8)
        self.cancel_conscience_str = QA.translate("ConsScienceGui", "Canceled conservationist/scientist interview", "", QA.UnicodeUTF8)        