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


all: interviewstart_ui.py resgroup_ui.py fishery_ui.py selectecotourism_ui.py ecotourism_ui.py selectconsscience_ui.py consscience_ui.py  drawgear_ui.py drawecotourism_ui.py drawconsscience_ui.py other_ui.py

clean:
	rm -f interviewstart_ui.py nextpolygon_ui.py resgroup_ui.py fishery_ui.py ecotourism_ui.py consscience_ui.py drawgear_ui.py drawecotourism_ui.py drawconsscience_ui.py interview.pyc other_ui.py
	rm -f *.pyc
	rm -f *~

interviewstart_ui.py: interviewstart.ui
	pyuic4 -o interviewstart_ui.py interviewstart.ui

drawgear_ui.py: drawgear.ui
	pyuic4 -o drawgear_ui.py drawgear.ui

drawecotourism_ui.py: drawecotourism.ui
	pyuic4 -o drawecotourism_ui.py drawecotourism.ui
	
drawconsscience_ui.py: drawconsscience.ui
	pyuic4 -o drawconsscience_ui.py drawconsscience.ui
	
resgroup_ui.py: resgroup.ui
	pyuic4 -o resgroup_ui.py resgroup.ui

fishery_ui.py: fishery.ui
	pyuic4 -o fishery_ui.py fishery.ui

ecotourism_ui.py: ecotourism.ui
	pyuic4 -o ecotourism_ui.py ecotourism.ui

selectecotourism_ui.py: selectecotourism.ui
	pyuic4 -o selectecotourism_ui.py selectecotourism.ui
	
consscience_ui.py: consscience.ui
	pyuic4 -o consscience_ui.py consscience.ui

selectconsscience_ui.py: selectconsscience.ui
	pyuic4 -o selectconsscience_ui.py selectconsscience.ui

other_ui.py: other.ui
	pyuic4 -o other_ui.py other.ui	