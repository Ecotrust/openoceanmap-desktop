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
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent.mainwindow, fl)
        self.setupUi(self)
        self.parent = parent
        self.permits = []

    def on_pbnStartShapes_released(self):
        #Get fishery value
        cur_fishery = self.fishery_comboBox.currentText()
        if not cur_fishery:
            QMessageBox.warning(self, "Fishery Error", "Please select a fishery")
            return 
        else:
            self.parent.currentFishery = cur_fishery
        

        #Build permit id string
        permits = []
        
        if self.p1.isChecked():
            permits.append('01')
        if self.p2.isChecked():
            permits.append('02')
        if self.p3.isChecked():
            permits.append('03')
        if self.p4.isChecked():
            permits.append('04')
        if self.p5.isChecked():
            permits.append('05')
        if self.p6.isChecked():
            permits.append('06')
        if self.p7.isChecked():
            permits.append('07')
        if self.p8.isChecked():
            permits.append('08')
        if self.p9.isChecked():
            permits.append('09')
        if self.p10.isChecked():
            permits.append('10')
        if self.p11.isChecked():
            permits.append('11')
        if self.p12.isChecked():
            permits.append('12')
        if self.p13.isChecked():
            permits.append('13')
        if self.p14.isChecked():
            permits.append('14')
        if self.p15.isChecked():
            permits.append('15')
        if self.p16.isChecked():
            permits.append('16')
        if self.p17.isChecked():
            permits.append('17')
        if self.p18.isChecked():
            permits.append('18')
        if self.p19.isChecked():
            permits.append('19')
        if self.p20.isChecked():
            permits.append('20')
        if self.p21.isChecked():
            permits.append('21')
        if self.p22.isChecked():
            permits.append('22')
        if self.p23.isChecked():
            permits.append('23')
        if self.p24.isChecked():
            permits.append('24')
        if self.p25.isChecked():
            permits.append('25')
        if self.p26.isChecked():
            permits.append('26')
        if self.p27.isChecked():
            permits.append('27')
        if self.p28.isChecked():
            permits.append('28')
        if self.p29.isChecked():
            permits.append('29')
                        
        permit_str = ','.join(permits)
        self.parent.currentPermits = permit_str 
        
        self.close()
        
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnFisheryFinished_released(self):
        self.parent.pennies_left = 100;            
        self.close()        
        
        # add some features
        for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
        self.parent.parent.interviewInProgress = False
        self.parent.parent.interviewSaveTool = None
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def nextPolygon(self):        
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()

class NextPolygonGui(QDialog, Ui_NextPolygon):
    def __init__(self, parent, fl, num_pennies):
        QDialog.__init__(self, parent.mainwindow, fl)
        self.setupUi(self)
        self.parent = parent
        self.discardLast = False
        self.pl_label.setText("  "+str(num_pennies)+" left")
        if num_pennies == 0:
            self.pbnMoreShapes.setDisabled(True)

    #Called when "More Shapes this fishery" button pressed        
    def on_pbnMoreShapes_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies or num_pennies == '0' or not strIsInt(num_pennies):
                QMessageBox.warning(self, "Pennies Error", "Missing or invalid penny value")
                return
            elif int(num_pennies) > self.parent.pennies_left:
                QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
                return            
            else:
                self.parent.pennies_left = self.parent.pennies_left - int(num_pennies)
                self.parent.capturedPolygonsPennies.append(num_pennies)
                        
            self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
            self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
            self.parent.capturedPolygonsPermits.append(self.parent.currentPermits)
            
        self.close()

        #Check if this fishery should be done (no pennies left)
        if self.parent.pennies_left == 0:
            QMessageBox.warning(self, "Pennies Error", "You are out of pennies.  This fishery is now done.")
            self.parent.interviewEnd()
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
        self.discardLast = True
            
    #"Finished with Fishery" button clicked
    def on_pbnShapeFinished_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            print "got here"
            print num_pennies
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
                        
            self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
            self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
            self.parent.capturedPolygonsPermits.append(self.parent.currentPermits)
        self.close()
        self.parent.interviewEnd()

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()
