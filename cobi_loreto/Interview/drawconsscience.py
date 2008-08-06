#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Dane Springmeyer
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
from drawconsscience_ui import Ui_DrawConsScience
from Util.common_functions import *
# General system includes
import sys

class DrawConsScienceGui(QDialog, Ui_DrawConsScience):
    def __init__(self, parent, flags, pennies_left, shapeType, previousGui):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.discardLast = False
        self.pennies_left = pennies_left
        self.pl_label.setText("  "+str(self.pennies_left)+self.pennies_left_str)
        self.shapeType = shapeType
        self.previousGui = previousGui
        self.type_label.setText(self.shapeType)
        if pennies_left == 0:
            self.pbnMoreShapes.setDisabled(True)
        
        self.retranslate()

    #Called when "More Shapes" button pressed        
    def on_pbnMoreShapes_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies:
                QMessageBox.warning(self, self.pennies_error_str, self.missing_penny_str)
                return
            elif not strIsInt(num_pennies):
                QMessageBox.warning(self, self.pennies_error_str, self.penny_number_str)
                return
            elif num_pennies == '0':
                QMessageBox.warning(self, self.pennies_error_str, self.add_penny_str)
                return
            elif int(num_pennies) > self.pennies_left:
                QMessageBox.warning(self, self.pennies_error_str, self.no_penny_str)
                return
            else:
                self.parent.pennies_left = self.pennies_left - int(num_pennies)
                self.parent.capturedPolygonsPennies.append(num_pennies)

            self.parent.capturedPolygonsType.append(self.parent.shapeType)

        self.close()

        #Check if this shape type should be done (no pennies left)
        if self.parent.pennies_left == 0:
            QMessageBox.warning(self, self.pennies_error_str, self.out_penny_str)
            self.parent.saveShapes(self)
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
            
    #"Finished with Type" button clicked
    def on_pbnShapeFinished_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies:
                QMessageBox.warning(self, self.pennies_error_str, self.missing_penny_str)
                return
            elif not strIsInt(num_pennies):
                QMessageBox.warning(self, self.pennies_error_str, self.penny_number_str)
                return
            elif num_pennies == '0':
                QMessageBox.warning(self, self.pennies_error_str, self.add_penny_str)
                return
            elif int(num_pennies) > self.parent.pennies_left:
                QMessageBox.warning(self, self.pennies_error_str, self.no_penny_str)
                return
            elif int(num_pennies) < self.parent.pennies_left:
                QMessageBox.warning(self, self.pennies_error_str, self.more_penny_str)
                return
            else:
                self.parent.capturedPolygonsPennies.append(num_pennies)
                        
            self.parent.capturedPolygonsType.append(self.parent.shapeType)
        
        self.parent.saveShapes(self)


    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawConsScienceGui(self.parent,flags,self.parent.pennies_left,self.parent.shapeType, self.previousGui)
        wnd.show()

    def retranslate(self):
        self.pennies_error_str = QA.translate("DrawConsScienceGui", "Pennies Error", "", QA.UnicodeUTF8)
        self.missing_penny_str = QA.translate("DrawConsScienceGui", "Missing penny value", "", QA.UnicodeUTF8)
        self.penny_number_str = QA.translate("DrawConsScienceGui", "Penny value must be a number (no decimals)", "", QA.UnicodeUTF8)
        self.add_penny_str = QA.translate("DrawConsScienceGui", "Please add a penny value", "", QA.UnicodeUTF8)
        self.no_penny_str = QA.translate("DrawConsScienceGui", "You don't have that many pennies left", "", QA.UnicodeUTF8)
        self.more_penny_str = QA.translate("DrawConsScienceGui", "You would still have pennies left.  Please enter a larger penny value or draw additional shapes", "", QA.UnicodeUTF8)
        self.out_penny_str = QA.translate("DrawConsScienceGui", "You are out of pennies.  This shape drawing session is now done.", "", QA.UnicodeUTF8)
        self.pennies_left_str = QA.translate("DrawConsScienceGui", " left", "Partial text used as part of a larger message about number of pennies left, for example '20 left'", QA.UnicodeUTF8)        