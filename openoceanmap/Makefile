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


all: resources_rc.py mainwindow_ui.py interviewstart_ui.py \
     nextpolygon_ui.py pythoninterp_ui.py


clean:
	rm -f mainwindow_ui.py resources_rc.py interviewstart_ui.py
	rm -f *.pyc


mainwindow_ui.py: mainwindow.ui
	pyuic4 -o mainwindow_ui.py mainwindow.ui

interviewstart_ui.py: interviewstart.ui
	pyuic4 -o interviewstart_ui.py interviewstart.ui

nextpolygon_ui.py: nextpolygon.ui
	pyuic4 -o nextpolygon_ui.py nextpolygon.ui

pythoninterp_ui.py: pythoninterp.ui
	pyuic4 -o pythoninterp_ui.py pythoninterp.ui

resources_rc.py: resources.qrc
	pyrcc4 -o resources_rc.py resources.qrc

