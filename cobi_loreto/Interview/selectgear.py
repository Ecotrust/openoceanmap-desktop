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
# Custom Functions
from Util.common_functions import *
# UI specific includes
from selectgear_ui import Ui_SelectGear

# General system includes
import sys

class SelectGearGui(QDialog, Ui_SelectGear):
    def __init__(self, parent, flags, fishery_sector):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.fishery_sector = fishery_sector
        self.fishery_sector_label.setText(str(self.fishery_sector))
        
        self.pbnStepFinished.setText('Exit ' + str(self.fishery_sector) + ' Step')
    
    def on_pbnStartShapes_released(self):
        shape_type = self.gear_comboBox.currentText()
        if not shape_type:
            QMessageBox.warning(self, "Fishery Error", "Please select a fishery")
            return 
        else:
            self.parent.shapeType = shape_type

        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            

    def on_pbnStepFinished_released(self): 
        self.close()
        fishery_msg = 'Finished with %s interview step' % self.fishery_sector
        print self.fishery_sector
        if self.fishery_sector == 'Commercial Fishery':
            self.parent.commFishIncome = None
            self.parent.nextStep(self, fishery_msg)
        elif self.fishery_sector == 'Sport Fishery':
            self.parent.sportFishIncome = None
            self.parent.nextStep(self, fishery_msg)
        elif self.fishery_sector == 'Private Fishery':
            self.parent.privateFishIncome = None
            self.parent.nextStep(self, fishery_msg)
        

    def nextPolygon(self):
        from drawgear import DrawGearGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawGearGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()
