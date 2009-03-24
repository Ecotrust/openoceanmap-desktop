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
from selectecotourism_ui import Ui_SelectEcotourism

from Util.common_functions import *

# General system includes
import sys

class SelectEcotourismGui(QDialog, Ui_SelectEcotourism):
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.retranslate()

    #Controls whether other field activity lineEdit is enabled
    def on_comboActivity_activated(self):
        import pdb
        pdb.set_trace()
        activity_type = self.comboActivity.currentText()
        if activity_type == 'Other':
            self.other_line.setEnabled(True)
        else:
            self.other_line.setEnabled(False)

    def on_pbnStartShapes_released(self):       
        shape_type = self.comboActivity.currentText()
        if not shape_type:
            QMessageBox.warning(self, self.tourism_error_str, self.select_tourism_str)
            return 

        if shape_type == 'Other':
            shape_type = self.other_line.text()
            if not shape_type:
                QMessageBox.warning(self, self.other_error_str, self.no_other_error_str)
                return

        self.parent.add_attrib(self.f_emp_type_str, activity_type)
        self.parent.shapeType = shape_type            
        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnFinished_released(self): 
        self.close()
        self.parent.ecotourismIncome = None
        self.parent.nextStep(self, self.finish_tourism_str)


    def nextPolygon(self):
        from drawecotourism import DrawEcotourismGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawEcotourismGui(self.parent,flags,self.parent.pennies_left, self.parent.shapeType, self)
        wnd.show()
        
    def retranslate(self):
        self.tourism_error_str = QA.translate("SelectEcotourismGui", "Ecotourism Error", "Error when user didn't select an ecotourism type ", QA.UnicodeUTF8)        
        self.other_error_str = QA.translate("EcotourismGui", "Ecotourism Error", "Error message given when user doesn't enter an other activity type", QA.UnicodeUTF8)
        self.no_other_error_str = QA.translate("EcotourismGui", "You selected 'Other' activity, you must enter the name of that activity", "Top title of error window when you dont enter a name for the other activity", QA.UnicodeUTF8)        
        self.select_tourism_str = QA.translate("SelectEcotourismGui", "Please select an ecotourism type", "", QA.UnicodeUTF8)
        self.finish_tourism_str = QA.translate("SelectEcotourismGui", "Finished with ecotourism interview", "", QA.UnicodeUTF8)        