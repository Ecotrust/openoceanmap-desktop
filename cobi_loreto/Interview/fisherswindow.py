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
#from interviewstart_ui import Ui_InterviewStart
from selectfishery import *
# UI specific includes
#from selectfishery_ui import Ui_SelectFishery
#from nextpolygon_ui import Ui_NextPolygon
from fisherswindow_ui import Ui_FishersWindow

from Util.common_functions import *

# General system includes
import sys

class FishersWindowGui(QDialog, Ui_FishersWindow):
    def __init__(self, parent, flags, prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI

    def on_pbnSelectFishery_released(self):
        interviewInfo2 = self.parent.interviewInfo2
        interviewInfo2.append(["artespesca", self.gear_comboBox.currentText()])
        interviewInfo2.append(["v_len", self.vessel_length_line.text()])
        interviewInfo2.append(["v_motor", self.vessel_motor_line.text()])
        interviewInfo2.append(["haul_cap", self.haul_capacity_line.text()])
        interviewInfo2.append(["v_homep", self.home_port_line.text()])
        interviewInfo2.append(["landp_1", self.landing_port_line.text()])
        interviewInfo2.append(["landp_2", self.landing_port_line_2.text()])
        interviewInfo2.append(["landp_3", self.landing_port_line_3.text()])
        interviewInfo2.append(["landp_4", self.landing_port_line_4.text()])

        if not self.gear_comboBox.currentText():
            QMessageBox.warning(self, "Gear Error", "Please Choose a Fishing Gear Type")
            return

        self.close()
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = SelectFisheryGui(self.parent,flags)
        wnd.show()
        #mc = self.parent.canvas      
        #self.p = PolygonTool(mc,self.parent)
        #QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        #self.saveTool = mc.mapTool()
        #mc.setMapTool(self.p)
            
    def on_pbnCancel_clicked(self):
        self.close()
        capture_string = QString("Cancelled out of fishery interview...")
        print capture_string
        self.parent.parent.statusbar.showMessage(capture_string)
        
        # stop interview process
        self.parent.parent.interviewInProgress = False
        self.parent.parent.interviewSaveTool = None
        self.parent.currentCommFish = False
        self.parent.currentCommSport = False
        self.parent.currentPrivateFish = False
        self.parent.currentEcotourism = False
        self.parent.currentConsScience = False
        self.parent.currentOther = False
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def on_pbnBack_clicked(self):
        self.close()
        capture_string = QString("Going back to first interview step...")
        self.parent.parent.statusbar.showMessage(capture_string)

        from interviewstart import InterviewStartGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        try:
            self.prevGUI.show()
        except:
            wnd = InterviewStartGui(self.parent,flags)
            wnd.show()
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)