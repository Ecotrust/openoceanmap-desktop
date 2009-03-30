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
from selectconsscience_ui import Ui_SelectConsScience

from Util.common_functions import *

# General system includes
import sys

class SelectConsScienceGui(QDialog, Ui_SelectConsScience):
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.retranslate()

    #Controls whether other field activity lineEdit is enabled
    def on_comboFocus_activated(self):
        focus = self.comboFocus.currentText()
        if focus == 'Other':
            self.other_line.setEnabled(True)
        else:
            self.other_line.setEnabled(False)        
        
    def on_pbnStartShapes_released(self):
        focus = self.comboFocus.currentText()
        if not focus:
            QMessageBox.warning(self, self.consci_error_str, self.focus_str)
            return 
        else:
            self.parent.shapeType = focus
            self.parent.add_attrib(self.f_focus_str, focus)
            
        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        self.parent.parent.interviewSaveTool = None
        mc.setMapTool(self.p)
            
    def on_pbnFinished_released(self):
        self.close()
        self.parent.consScienceIncome = None
        self.parent.nextStep(self, self.finish_cons_str)

    def nextPolygon(self):
        from drawconsscience import DrawConsScienceGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawConsScienceGui(self.parent,flags,self.parent.pennies_left, self.parent.shapeType, self)
        wnd.show()
        
    def retranslate(self):
        self.f_focus_str = QA.translate("SelectConsScienceGui", "focus", "Area of Focus for conservation/scientist", QA.UnicodeUTF8)
        self.consci_error_str = QA.translate("SelectConsScienceGui", "Cons/Science Error", "Error when user fails to select type of conservationist/scientist", QA.UnicodeUTF8)        
        self.focus_str = QA.translate("SelectConsScienceGui", "Please select a focus area", "", QA.UnicodeUTF8)
        self.finish_cons_str = QA.translate("SelectConsScienceGui", "Finishing Cons/Sci interview", "", QA.UnicodeUTF8)