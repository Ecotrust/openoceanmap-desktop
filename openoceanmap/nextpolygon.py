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
from polygontool import *
# UI specific includes
from nextpolygon_ui import Ui_NextPolygon
# General system includes
import sys

class NextPolygonGui(QDialog, Ui_NextPolygon):
    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.parent = parent

    def on_pbnMoreShapes_released(self):
        self.parent.capturedPolygonsPennies.append(self.line_1.text())
        self.close()
        mc = self.parent.canvas      
        self.p = polygonTool(mc)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnFinished_released(self):
        self.parent.capturedPolygonsPennies.append(self.line_1.text())
        self.close()
        self.parent.interviewEnd()

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags)
        wnd.show()



