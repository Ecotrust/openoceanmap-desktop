--------------------------------------------------------------------

OpenOceanMap - An Open Source GIS tool for performing interviews
to obtain socio-economic data using spatial information.

Copyright (C) 2008  Ecotrust
Copyright (C) 2008  Aaron Racicot
Copyright (C) 2008  Tim Welch
Copyright (C) 2008  Dane Springmeyer

--------------------------------------------------------------------

licensed under the terms of GNU GPL 2

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

--------------------------------------------------------------------

Based on QGIS tutorials (ALL GPL LISCENSED) provided by:
- http://wiki.qgis.org/qgiswiki/PythonBindings
- Tim Sutton - Original sources - Copyright (c) 2006
  svn co https://svn.qgis.org/repos/qgis/trunk/code_examples/
- Martin Dobias - Tim's tutorials ported to Python - Copyright (c) 2006-2007
  http://mapserver.sk/~wonder/qgis/tutorials.tar.gz
- Barry Rowlingson - Original region tool - Copyright (c) 2007
  http://www.maths.lancs.ac.uk/~rowlings/Software/regionTool/
- Matthew T. Perry - QGIS GeoCoding plugin - Copyright (c) 2007
  svn checkout http://perrygeo.googlecode.com/svn/trunk/qgis/geocode

--------------------------------------------------------------------

This software has been developed to provide a framework for application
development using the QGIS core and gui libraries and sits on top of
the QT gui development libraries.  

This software is written in Python and utilizes the python bindings
to QGIS and QT.  In order to develope with this software you must
first install the PyQT development framework and the >= 0.9 version
of QGIS with Python support.

--------------------------------------------------------------------

INSTALL

To install this software you can just unzip it into a directory
and set the Python path variables to locate the QGIS libraries 
(if the global install was not set on QGIS install).  The
openoceanmap.py contains the #!/usr/bin/env python statement that might
need to be modified to fit your system.  Then from the command line run:

./openoceanmap.py

--------------------------------------------------------------------

PACKAGE

To package openoceanmap on multiple platforms you can follow these
instructions:

MAC: py2app

WIN: py2exe

LINUX: ???

