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

from drawshapes import DrawShapesGui

# UI specific includes
from selectecotourism_ui import Ui_SelectEcotourism
from drawshapes_ui import Ui_DrawShapes

from Util.common_functions import *

# General system includes
import sys

class SelectEcotourismGui(QDialog, Ui_SelectEcotourism):
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent

    def on_pbnStartShapes_released(self):
        #Get fishery value
        cur_fishery = self.fishery_comboBox.currentText()
        if not cur_fishery:
            QMessageBox.warning(self, "Fishery Error", "Please select a fishery")
            return 
        else:
            self.parent.currentFishery = cur_fishery
            
        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnFisheryFinished_released(self):
        self.parent.pennies_left = 100; 
        self.close()
        capture_string = QString("Finished with fishery interview...")
        self.parent.parent.statusbar.showMessage(capture_string)
        
        # add some features
        for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
            
        self.parent.currentFishery = None

        if self.parent.currentEcotourism:
            from ecotourism import EcotourismGui
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
            wnd = EcotourismWindowGui(self.parent,flags)
            wnd.show()    
        
        # need a bunch of logic here...




        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def on_pbnTypeFinished_released(self):
        self.parent.pennies_left = 100;
        self.close()
        capture_string = QString("Finished with gear types...")
        self.parent.parent.statusbar.showMessage(capture_string)

        from ecotourism import EcotourismGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = EcotourismGui(self.parent,flags)
        wnd.show()

        # add some features
        for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawShapesGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()
