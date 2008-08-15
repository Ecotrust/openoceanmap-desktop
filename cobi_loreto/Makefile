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


all:
	cd Main; $(MAKE)
	cd Tools; $(MAKE)
	cd Util; $(MAKE)
	cd Interview; $(MAKE)

translate:
	qmake -project -o oom.pro
	pylupdate4 -verbose oom.pro
	# missing generating translating sources for .py files
	# this will patch then manually fix paths and insert:
	pylupdate4 -verbose  Main/*.py Interview/*.py Util/*.py Tools/*.py -ts i18n/es_MX.ts

clean:
	rm -f *.pyc
	rm -f *~
	cd Main; $(MAKE) clean
	cd Tools; $(MAKE) clean
	cd Util; $(MAKE) clean
	cd Interview; $(MAKE) clean