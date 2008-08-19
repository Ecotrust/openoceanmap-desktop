#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
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
from drawgear_ui import Ui_DrawGear
from Util.common_functions import *
# General system includes
import sys

class DrawGearGui(QDialog, Ui_DrawGear):
    def __init__(self, parent, flags, pennies_left, previousGui):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.retranslate()
        
        self.discardLast = False
        self.pennies_left = pennies_left
        self.previousGui = previousGui
        self.type_label.setText("  "+unicode(self.parent.shapeType)+": ")
        self.pl_label_4.setText(u"  "+unicode(self.pennies_left)+self.left_str)
        if pennies_left == 0:
            self.pbnMoreShapes.setDisabled(True)
        self.species = []    
 
    def fetch_species(self):
            species = []
            if self.s1.isChecked():
                species.append(unicode(self.sharks_and_skates_str))
            if self.s2.isChecked():
                species.append(unicode(self.coastal_reef_fish_str))
            if self.s3.isChecked():
                species.append(unicode(self.deep_reef_fish_str))
            if self.s4.isChecked():
                species.append(unicode(self.migratory_fish_str))
            if self.s5.isChecked():
                species.append(unicode(self.benthic_fish_str))
            if self.s6.isChecked():
                species.append(unicode(self.shrimp_str))
            if self.s7.isChecked():
                species.append(unicode(self.other_str))
            species_list_text = u','.join(species)
            return species_list_text
            
    #Called when "More Shapes" button pressed        
    def on_pbnMoreShapes_released(self):
        if not self.discardLast:
            num_pennies = self.line_3.text()
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
            
            self.parent.capturedPolygonsSpecies.append(self.fetch_species())
            self.parent.capturedPolygonsType.append(self.parent.shapeType)
            self.parent.save_gear_inc()
            
        self.close()

        #Check if this shape type should be done (no pennies left)
        if self.parent.pennies_left == 0:
            QMessageBox.warning(self, self.pennies_error_str, self.out_penny_str)
            self.parent.saveShapes(self) # sends itself as the 'drawGui'
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
        try:
            current_pennies = int(self.line_3.text())
        except:
           current_pennies = 0
        if not current_pennies == self.parent.pennies_left:
            # then we assume they placed pennies but then decides to descard shape
            self.line_3.setText(unicode(current_pennies-current_pennies))
        # Grey out the button...
        self.pbnShapeDiscard.setEnabled(False)
        self.discardLast = True
            
    #"Finished with Type" button clicked
    def on_pbnShapeFinished_released(self):
        if not self.discardLast:
            num_pennies = self.line_3.text()
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
                
            self.parent.capturedPolygonsSpecies.append(self.fetch_species())            
            self.parent.capturedPolygonsType.append(self.parent.shapeType)
            self.parent.save_gear_inc()
        
        self.parent.saveShapes(self) # sends itself as the 'drawGui'

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawGearGui(self.parent,flags,self.parent.pennies_left, self.previousGui)
        wnd.show()

    def retranslate(self):
        self.pennies_error_str = QA.translate("DrawGearGui", "Pennies Error", "", QA.UnicodeUTF8)
        self.missing_penny_str = QA.translate("DrawGearGui", "Missing penny value", "", QA.UnicodeUTF8)
        self.penny_number_str = QA.translate("DrawGearGui", "Penny value must be a number (no decimals)", "", QA.UnicodeUTF8)
        self.add_penny_str = QA.translate("DrawGearGui", "Please add a penny value", "", QA.UnicodeUTF8)
        self.no_penny_str = QA.translate("DrawGearGui", "You don't have that many pennies left", "", QA.UnicodeUTF8)
        self.more_penny_str = QA.translate("DrawGearGui", "You would still have pennies left.  Please enter a larger penny value or draw additional shapes", "", QA.UnicodeUTF8)
        self.out_penny_str = QA.translate("DrawGearGui", "You are out of pennies.  This shape drawing session is now done.", "", QA.UnicodeUTF8)
        self.sharks_and_skates_str = QA.translate("DrawGearGui", 'Sharks and Skates', "", QA.UnicodeUTF8)
        self.coastal_reef_fish_str = QA.translate("DrawGearGui", 'Coastal reef fish', "", QA.UnicodeUTF8)
        self.deep_reef_fish_str = QA.translate("DrawGearGui", 'Deep reef fish', "", QA.UnicodeUTF8)
        self.migratory_fish_str = QA.translate("DrawGearGui", 'Migratory fish', "", QA.UnicodeUTF8)
        self.benthic_fish_str = QA.translate("DrawGearGui", 'Benthic fish', "", QA.UnicodeUTF8)
        self.shrimp_str = QA.translate("DrawGearGui", 'Shrimp', "", QA.UnicodeUTF8)
        self.other_str = QA.translate("DrawGearGui", 'Other', "", QA.UnicodeUTF8)
        self.left_str = QA.translate("DrawGearGui", " left", "Partial string used to tell you how many pennies you have remaining, for example '20 left'", QA.UnicodeUTF8)
