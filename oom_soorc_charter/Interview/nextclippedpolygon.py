#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
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
from nextclippedpolygon_ui import Ui_NextClippedPolygon

from Util.common_functions import *

# General system includes
import sys

class NextClippedPolygonGui(QDialog, Ui_NextClippedPolygon):
    def __init__(self, parent, fishery, layer):
        QDialog.__init__(self, parent.mainwindow)
        self.setupUi(self)
        self.parent = parent
        self.fishery = fishery
        self.layer = layer
        
        self.fishery_line.setText(self.fishery)
        self.parent.currentFishery = self.fishery
        self.parent.pennies_left = 100;
        
        self.shape_index = 1
        self.num_shapes = layer.featureCount()
        
        #prov = self.layer.getDataProvider()
        #allattr = prov.allAttributesList()
        #prov.select(allattr)
        #feat2 = QgsFeature()
        #print "init next clipped polygon ui"
        #while prov.getNextFeature(feat2):
        #    print str(feat2.featureId())+": "+feat2.attributeMap()[45].toString()
        
        self.next_clipped_polygon()
        

    def on_pbnNextShape_released(self):    
        # save the pennies for current shape
        num_pennies = self.line_1.text()
        if not num_pennies or num_pennies == '0' or not strIsInt(num_pennies):
            QMessageBox.warning(self, "Pennies Error", "Missing or invalid penny value")
            return
        elif int(num_pennies) > self.parent.pennies_left:
            QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
            return       
        elif self.parent.pennies_left - int(num_pennies) < self.num_shapes - self.shape_index:
            QMessageBox.warning(self, "Pennies Error", "You must leave enough pennies to assign at least 1 to each of the remaining shapes")
            return 
        elif self.shape_index == self.num_shapes and self.parent.pennies_left > int(num_pennies):
            QMessageBox.warning(self, "Pennies Error", "This is your last shape -- you must use all your pennies")
            return 
        else:
            self.parent.pennies_left = self.parent.pennies_left - int(num_pennies)
            self.feat.changeAttribute( self.parent.penniesIndex, QVariant( int(num_pennies) ))
            self.provider.changeAttributeValues({ self.feat.featureId(): self.feat.attributeMap() })
            #print str( self.feat.featureId()) + ": " + self.feat.attributeMap()[self.parent.penniesIndex].toString()
    
        # select the next shape
        self.shape_index = self.shape_index + 1
    
        # if no more shapes, close and go to next step
        if self.shape_index > self.num_shapes:
            self.parent.pennies_left = 100;    
            self.close()
            self.layer.setSelectedFeatures([])
            self.parent.next_clipped_fishery()
        else:
            self.next_clipped_polygon()
            
            
    def next_clipped_polygon(self):
        # update the dialog box's labels
        self.pl_label.setText("  "+str(self.parent.pennies_left)+" left")
        self.shapeNum_label.setText("Shape #" + str(self.shape_index) + " of " + str(self.num_shapes))
        if self.shape_index < self.num_shapes:
            self.line_1.setText("")
        else:
            self.line_1.setText(str(self.parent.pennies_left))
        
        # select the next shape (layer's feature iterator gets reset by something -- prob setSelectedFeatures -- so we need to count it up from 0 each time)
        self.feat = QgsFeature()
        self.provider = self.layer.getDataProvider()
        allAttrs = self.provider.allAttributesList()
        self.provider.select(allAttrs)
        
        #print "iterating in next_clipped_polygon"
        for counter in range( self.shape_index ):
            self.provider.getNextFeature(self.feat)
            #print str(self.feat.featureId())+": "+self.feat.attributeMap()[45].toString()
            
        self.layer.setSelectedFeatures([self.feat.featureId()])
