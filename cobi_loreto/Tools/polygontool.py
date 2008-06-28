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


# Polygon tool class - Used to capture polygon region from user
class PolygonTool(QgsMapTool):
    def __init__(self, canvas, parent):
        QgsMapTool.__init__(self,canvas)
        self.parent = parent
        self.canvas=canvas

        self.dragging=False
        self.rubberBand = 0
        self.polygonList = []
        self.lastPoint = None
        self.down=False
        self.started=False
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
        self.down=True
        capture_string = QString("Starting Polygon - Down event")

    def canvasMoveEvent(self,event):
        if self.started==True:
            capture_string = QString("Move event")
            transform = self.canvas.getCoordinateTransform()
            pt = transform.toMapCoordinates(event.pos().x(),
                                            event.pos().y())
            self.rubberBand.movePoint(QgsPoint(pt.x(),pt.y()))

    def canvasReleaseEvent(self,event):
        if self.down==True:
            if (self.started==False) and (event.button() == Qt.RightButton):
                # We have a right button but have not started a poly... just return
                return
            if self.started==False:
                self.rubberBand = QgsRubberBand(self.canvas,True)
                self.parent.capturedPolygonsRub.append(self.rubberBand)
                self.rubberBand.show()
                self.currentPolygon = 'POLYGON(('
                self.numberOfPoints = 0
            self.started=True
            capture_string = QString("Polygon point added")
            
            transform = self.canvas.getCoordinateTransform()
            pt = transform.toMapCoordinates(event.pos().x(),
                                            event.pos().y())
            self.rubberBand.addPoint(QgsPoint(pt.x(),pt.y()))
            self.numberOfPoints = self.numberOfPoints + 1
            if self.currentPolygon == 'POLYGON((':
                self.originalPoint = '%f %f' % (pt.x(), pt.y())
            self.currentPolygon = self.currentPolygon + '%f %f' % (pt.x(), pt.y()) + ',' 
            if (event.button() == Qt.RightButton) and (self.numberOfPoints > 2):
                self.down=False
                self.started=False
                self.currentPolygon = self.currentPolygon + self.originalPoint
                self.currentPolygon = self.currentPolygon + '))'
                self.parent.capturedPolygons.append(self.currentPolygon)
                self.o.emit(SIGNAL("finished()"))
            
    def activate(self):
        #print "Start Polygon Tool"
        capture_string = QString("Starting Polygon Tool")
        self.canvas.setCursor(self.cursor)
        capture_string = QString("Draw polygon on canvas " +
                                 "by digitizing points...")

    def deactivate(self):
        #print "End Polygon Tool Selection"
        capture_string = QString("End Polygon Tool Selection")

    def isZoomTool(self):
        return False


