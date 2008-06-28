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
from pythoninterp_ui import Ui_PythonWin
# General system includes
import sys
from code import *



class PythonInterpGui(QDialog, Ui_PythonWin):
  def __init__(self, parent, fl):
    QDialog.__init__(self, parent, fl)
    self.setupUi(self)
    self.parent = parent
    #self.console_1 = QTextBrowser(self)
    self.console_1 = EPythonShell(self,self.line_1,parent.__dict__)
    self.console_1.setGeometry(QRect(10,10,571,401))
    self.console_1.setObjectName("console_1")
    self.line_1.setFocus(Qt.OtherFocusReason)  
  def on_pbnFinished_released(self):
    self.close()
    #self.x=1


# Class for capturing stdout
class CaptureClass(object):
  def __init__(self, canvas):
    self.canvas = canvas
  def write(self, capture_string):
    #self.canvas.parentWin.outputWin.append(QString("Made it here"))
    self.canvas.parentWin.outputWin.append(QString(capture_string))

class FileCacher:
    "Cache the stdout text so we can analyze it before returning it"
    def __init__(self): self.reset()
    def reset(self): self.out = []
    def write(self,line): self.out.append(line)
    def flush(self):
        #output = '\n'.join(self.out)
        output = ''.join(self.out)
        self.reset()
        return output.strip()

class Shell(InteractiveConsole):
    "Wrapper around Python that can filter input/output to the shell"
    def __init__(self,locals,canvas):
      self.canvas = canvas
      self.stdout = sys.stdout
      self.stderr = sys.stderr
      self.cache = FileCacher()
      # Output info for user about console
      capture_string = QString("---- OpenOceanMap Python Console ----")
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString(sys.version)
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString("--------")
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString("self == mainWindow self.canvas == mapCanvas " +
                               "self.layers == layerSet")
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString("Example use for QString vars: " +
                               "str(self.canvas.extent().stringRep())")
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString("Example use for list of QString vars: " +
                               "map(str,self.interviewInfo)")
      self.canvas.parentWin.outputWin.append(capture_string)
      capture_string = QString("--------")
      self.canvas.parentWin.outputWin.append(capture_string)
      InteractiveConsole.__init__(self,locals)
      return

    def get_output(self):
        sys.stdout = self.cache
        sys.stderr = self.cache
    def return_output(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def push(self,line):
        self.get_output()
        # you can filter input here by doing something like
        # line = filter(line)
        InteractiveConsole.push(self,line)
        self.return_output()
        output = self.cache.flush()
        # you can filter the output here by doing something like
        # output = filter(output)
        self.canvas.parentWin.outputWin.append(QString(output))
        #print output # or do something else with it
        return 

#class PythonInterp(QLineEdit):
#    def __init__(self, parent):
#        QTextEdit.__init__(self, parent)
#
#        def keyPressEvent(self,e):
#            if e.key() == Qt.Key_Return:
#                print "Got a return key"
#            else:
#                print "Got a gen key"
#                


class EPythonShell(QTextBrowser):
  class Output:
    def __init__( self, writefunc ):
      self.writefunc = writefunc
    def write( self, line ):
      if line != "\n":
        map( self.writefunc, line.split("\n") )
    
  def __init__( self, parent, cmdline, localdict={} ):
    QTextBrowser.__init__( self, parent )
    QObject.connect( cmdline, SIGNAL( "returnPressed()" ),
                     self.slotReturnPressed )
    self.setFont( QFont( "Fixed", 12 ) )
    
    self.console = InteractiveConsole( localdict )
    self.cmdline = cmdline
    
    sys.ps1 = ">>> "
    sys.ps2 = "... "
    
    capture_string = QString("---- OpenOceanMap Python Console ----")
    self.append( capture_string )
    self.append( "Python %s on %s\n" % ( sys.version, sys.platform) )
    #capture_string = QString(sys.version)
    #self.append( capture_string )
    capture_string = QString("--------")
    self.append( capture_string )
    capture_string = QString("Namespace is for QMainWindow ")
    self.append( capture_string )
    capture_string = QString("Example use for QString vars: " +
                             "str(canvas.extent().stringRep())")
    self.append( capture_string )
    capture_string = QString("Example use for list of QString vars: " +
                             "map(str,interviewInfo)")
    self.append( capture_string )
    capture_string = QString("--------")
    self.append( capture_string )

    self.more, self.prompt = 0, sys.ps1
    self.output = EPythonShell.Output( self.writeResult )
    self.stdout = sys.stdout
    self.stderr = sys.stderr
    
  def writeResult( self, result ):
    if result == "":
      return
    #print >> self.stdout, "appending '%s'" % result
    self.append( result )
  
  def handleInput( self, line ):
    self.append( sys.ps1 + line )
    sys.stdout, sys.stderr = self.output, self.output
    self.more = self.console.push( line )
    sys.stdout, sys.stderr = self.stdout, self.stderr
    
  def slotReturnPressed( self ):
    line = str(self.cmdline.text())
    self.cmdline.clear()
    self.handleInput( line )
    #if self.more:
    #  self.prompt = sys.ps2
    #else:
    #  self.prompt = sys.ps1
    #self.append( self.prompt )
    self.append( QString("--------") )
