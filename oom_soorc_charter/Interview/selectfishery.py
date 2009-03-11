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
#from nextpolygon import *
# UI specific includes
from selectfishery_ui import Ui_SelectFishery
from nextpolygon_ui import Ui_NextPolygon

from Util.common_functions import *

# General system includes
import sys

class SelectFisheryGui(QDialog, Ui_SelectFishery):
    def __init__(self, parent, fishery, trip_value):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent
        self.fishery = fishery
        self.trip_value = trip_value

        self.fishery_line.setText(self.fishery)
        self.perc_trip_fish_line.setText(self.trip_value)
        self.parent.currentFishery = self.fishery

    def on_pbnStartShapes_released(self):        
        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)

    def nextPolygon(self):        
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()


class NextPolygonGui(QDialog, Ui_NextPolygon):
    def __init__(self, parent, fl, pennies_left):
        QDialog.__init__(self, parent.mainwindow, fl)
        self.setupUi(self)
        self.parent = parent
        self.discardLast = False
        self.pennies_left = pennies_left
        self.pl_label.setText("  "+str(self.pennies_left)+" left")
        if pennies_left == 0:
            self.pbnMoreShapes.setDisabled(True)

    #Called when "More Shapes this fishery" button pressed        
    def on_pbnMoreShapes_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies or num_pennies == '0' or not strIsInt(num_pennies):
                QMessageBox.warning(self, "Pennies Error", "Missing or invalid penny value")
                return
            elif int(num_pennies) > self.pennies_left:
                QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
                return            
            else:
                self.parent.pennies_left = self.pennies_left - int(num_pennies)
                self.parent.capturedPolygonsPennies.append(num_pennies)
                        
            self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
            self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
            
        self.close()

        #Check if this fishery should be done (no pennies left)
        if self.parent.pennies_left == 0:
            QMessageBox.warning(self, "Pennies Error", "You are out of pennies.  This fishery is now done.")
            self.parent.end_fishery()
        else:
            mc = self.parent.canvas      
            self.p = PolygonTool(mc,self.parent)
            QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
            self.saveTool = mc.mapTool()
            mc.setMapTool(self.p)
            
    def on_pbnShapeDiscard_released(self):
        # Dump the last shape...
        self.parent.capturedPolygons.pop()
        rub = self.parent.capturedPolygonsRub.pop()
        rub.reset()
        # Grey out the button...
        self.pbnShapeDiscard.setEnabled(False)
        self.pbnShapeFinished.setEnabled(False)
        self.discardLast = True
            
    #"Finished with Fishery" button clicked
    def on_pbnShapeFinished_released(self):
        num_pennies = self.line_1.text()

        if not num_pennies or num_pennies == '0' or not strIsInt(num_pennies):
            QMessageBox.warning(self, "Pennies Error", "Missing or invalid penny value")
            return
        elif int(num_pennies) > self.parent.pennies_left:
            QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
            return
        elif int(num_pennies) < self.parent.pennies_left:
            QMessageBox.warning(self, "Pennies Error", "You would still have pennies left.  Please enter a larger penny value or draw additional shapes")
            return
        else:
            self.parent.capturedPolygonsPennies.append(num_pennies)
                    
        self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
        self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
        
        self.close()
        self.parent.end_fishery()
       
        # turn off the draw tool
        self.parent.canvas.setMapTool(self.parent.parent.toolPan)
        

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()
