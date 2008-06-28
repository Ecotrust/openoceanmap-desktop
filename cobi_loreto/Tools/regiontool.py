#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
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
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *

# Region tool class - Used to capture rectangular region from user
class RegionTool(QgsMapTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self,canvas)
        self.dragging=False
        self.selectRect = QRect()
        self.rubberBand = 0
        self.canvas=canvas
        self.ll = None
        self.ur = None
        self.o = QObject()
        self.cursor = QCursor(QPixmap(["16 16 3 1",
                                       "# c None","a c #000000",". c #ffffff",
                                       ".###############",
                                       "...#############",
                                       ".aa..###########",
                                       "#.aaa..a.a.a.a.#",
                                       "#.aaaaa..#####a#",
                                       "#a.aaaaaa..###.#",
                                       "#..aaaaaa...##a#",
                                       "#a.aaaaa.#####.#",
                                       "#.#.aaaaa.####a#",
                                       "#a#.aa.aaa.###.#",
                                       "#.##..#..aa.##a#",
                                       "#a##.####.aa.#.#",
                                       "#.########.aa.a#",
                                       "#a#########.aa..",
                                       "#.a.a.a.a.a..a.#",
                                       "#############.##"]))
        
    def canvasPressEvent(self,event):
        self.selectRect.setRect(event.pos().x(),event.pos().y(),0,0)
        capture_string = QString("Starting Rectangle")
        #self.canvas.parentWin.outputWin.append(capture_string)

    def canvasMoveEvent(self,event):
        if not event.buttons() == Qt.LeftButton:
            return
        if not self.dragging:
            self.dragging=True
            self.rubberBand = QRubberBand(QRubberBand.Rectangle,self.canvas)
        self.selectRect.setBottomRight(event.pos())
        self.rubberBand.setGeometry(self.selectRect.normalized())
        self.rubberBand.show()

    def canvasReleaseEvent(self,e):
        if not self.dragging:
            return
        self.rubberBand.hide()
        self.selectRect.setRight(e.pos().x())
        self.selectRect.setBottom(e.pos().y())
        transform = self.canvas.getCoordinateTransform()
        ll = transform.toMapCoordinates(self.selectRect.left(),
                                        self.selectRect.bottom())
        ur = transform.toMapCoordinates(self.selectRect.right(),
                                        self.selectRect.top())
        self.bb = QgsRect(
            QgsPoint(ll.x(),ll.y()),
            QgsPoint(ur.x(),ur.y())
            )
        self.o.emit(SIGNAL("finished()"))
        capture_string = QString("Starting Rectangle")
        
    def activate(self):
        #print "Start Rectangle Tool"
        capture_string = QString("Starting Rectangle")
        self.canvas.setCursor(self.cursor)
        capture_string = QString("Draw rectangle on canvas " +
                                 "to capture coordinates...")
        #self.canvas.parentWin.outputWin.append(capture_string)

    def deactivate(self):
        capture_string = QString("End Rectangle Tool")
        #self.canvas.parentWin.outputWin.append(capture_string)


    def isZoomTool(self):
        return False


