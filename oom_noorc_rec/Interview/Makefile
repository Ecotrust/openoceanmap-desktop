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


all: interviewstart_ui.py nextpolygon_ui.py selectfishery_ui.py rec_all_ui.py nextclippedpolygon_ui.py

clean:
	rm -f *_ui.py
	rm -f *.pyc
	rm -f *~

interviewstart_ui.py: interviewstart.ui
	pyuic4 -o interviewstart_ui.py interviewstart.ui

nextpolygon_ui.py: nextpolygon.ui
	pyuic4 -o nextpolygon_ui.py nextpolygon.ui

selectfishery_ui.py: selectfishery.ui
	pyuic4 -o selectfishery_ui.py selectfishery.ui

rec_all_ui.py: rec_all.ui
	pyuic4 -o rec_all_ui.py rec_all.ui
    
nextclippedpolygon_ui.py: nextclippedpolygon.ui
	pyuic4 -o nextclippedpolygon_ui.py nextclippedpolygon.ui
