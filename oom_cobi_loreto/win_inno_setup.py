#!/usr/bin/python
#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2008  Ecotrust
# Copyright (C) 2008  Aaron Racicot
# Copyright (C) 2008  Tim Welch
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


# A setup script showing how to extend py2exe.
#
# In this case, the py2exe command is subclassed to create an installation
# script for InnoSetup, which can be compiled with the InnoSetup compiler
# to a single file windows installer.
#
# By default, the installer will be created as dist\Output\setup.exe.

#*********************** READ THIS! *******************
# To build OOM you'll want to copy the plugins and resources directory
# from the QGIS install directory and put them in the root directory of OOM
# were openoceanmap.py is located.  Then change the QGIS prefix path to "."
# in openoceanmap.py.  That point QGIS to the right place when it looks for the necessary 
# data provider plugins at runtime.
#
# This build script will also look for and include the resources and plugins
# directory and include them in the install executable.

from distutils.core import setup
#import matplotlib
import py2exe
#import sys
#import glob
import os

#Build tree of files given a dir (for appending to py2exe data_files)
#Taken from http://osdir.com/ml/python.py2exe/2006-02/msg00085.html
def tree(src):
    list = [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]
    new_list = []
    for (root, files) in list:
	#print "%s , %s" % (root,files)
        if len(files) > 0 and root.count('.svn') == 0:
            new_list.append((root, files))
    return new_list 

################################################################

class InnoScript:
    def __init__(self,
                 name,
                 lib_dir,
                 dist_dir,
                 windows_exe_files = [],
                 lib_files = [],
                 version = "0.2"):
        self.lib_dir = lib_dir
        self.dist_dir = dist_dir
        if not self.dist_dir[-1] in "\\/":
            self.dist_dir += "\\"
        self.name = name
        self.version = version
        self.windows_exe_files = [self.chop(p) for p in windows_exe_files]
        self.lib_files = [self.chop(p) for p in lib_files]

    def chop(self, pathname):
        assert pathname.startswith(self.dist_dir)
        return pathname[len(self.dist_dir):]
    
    def create(self, pathname="dist\\OpenOceanMap.iss"):
        self.pathname = pathname
        ofi = self.file = open(pathname, "w")
        print >> ofi, "; WARNING: This script has been created by py2exe. Changes to this script"
        print >> ofi, "; will be overwritten the next time py2exe is run!"
        print >> ofi, r"[Setup]"
        print >> ofi, r"AppName=%s" % self.name
        print >> ofi, r"AppVerName=%s %s" % (self.name, self.version)
        print >> ofi, r"DefaultDirName={pf}\%s" % self.name
        print >> ofi, r"DefaultGroupName=%s" % self.name
        print >> ofi, r"VersionInfoVersion=%s" % self.version
        print >> ofi, r"VersionInfoCompany=Ecotrust"
        print >> ofi, r"VersionInfoDescription=OpenOceanMap Loreto Bay"
        print >> ofi, r"VersionInfoCopyright=Ecotrust"
        print >> ofi, r"AppCopyright=Ecotrust"
        print >> ofi, r"InfoAfterFile=U:\dev\cobi_loreto\README.TXT"
        print >> ofi, r"LicenseFile=U:\dev\cobi_loreto\LICENSE.TXT"
        print >> ofi, r"WizardImageBackColor=clBlack"
        print >> ofi, r"WizardImageFile=U:\dev\cobi_loreto\Images\OCEAN_VERT_INNO.bmp"
        print >> ofi, r"WizardSmallImageFile=U:\dev\cobi_loreto\Images\OCEAN_SMALL_INNO.bmp"
        print >> ofi, r"SetupIconFile=U:\dev\cobi_loreto\Images\OCEAN_SMALL_INNO.ico"
        print >> ofi

        print >> ofi, r"[Files]"
        for path in self.windows_exe_files + self.lib_files:
            print >> ofi, r'Source: "%s"; DestDir: "{app}\%s"; Flags: ignoreversion' % (path, os.path.dirname(path))
        
        #Additional libraries that may not be used but which the pre-build QGIS binary will look for and error if it can't find
        print >> ofi, r'Source: lib\libgdal-1.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\libgrass_dbmibase.6.3.0.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\libgrass_dgl.6.3.0.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\libgrass_rtree.6.3.0.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\QtSvg4.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi, r'Source: lib\libproj.dll; DestDir: {app}\lib; Flags: ignoreversion'

        print >> ofi, r"[Icons]"
        #print >> ofi, r'WorkingDir: {app}'                  
        for path in self.windows_exe_files:
            print >> ofi, r'Name: "{group}\%s"; Filename: "{app}\%s"; WorkingDir: {app}' % \
                  (self.name, path)                  
        print >> ofi, 'Name: "{group}\Uninstall %s"; Filename: "{uninstallexe}"' % self.name
        print >> ofi, r'Name: "{group}\Documentation - English"; Filename: "{app}\Documentation\English_Manual.html"'        

    def compile(self):
        try:
            import ctypes2
        except ImportError:
            try:
                import win32api
            except ImportError:
                import os
                os.startfile(self.pathname)
            else:
                print "Ok, using win32api."
                win32api.ShellExecute(0, "compile",
                                                self.pathname,
                                                None,
                                                None,
                                                0)
        else:
            print "Cool, you have ctypes installed."
            res = ctypes.windll.shell32.ShellExecuteA(0, "compile",
                                                      self.pathname,
                                                      None,
                                                      None,
                                                      0)
            if res < 32:
                raise RuntimeError, "ShellExecute failed, error %d" % res


################################################################

from py2exe.build_exe import py2exe

class build_installer(py2exe):
    # This class first builds the exe file(s), then creates a Windows installer.
    # You need InnoSetup for it.
    def run(self):
        # First, let py2exe do it's work.
        py2exe.run(self)

        lib_dir = self.lib_dir
        dist_dir = self.dist_dir
        
        # create the Installer, using the files py2exe has created.
        script = InnoScript("OpenOceanMap Loreto Bay",
                            lib_dir,
                            dist_dir,
                            self.windows_exe_files,
                            self.lib_files)
        print "*** creating the inno setup script***"
        script.create()
        print "*** compiling the inno setup script***"
        script.compile()
        # Note: By default the final setup.exe will be in an Output subdirectory.

######################## py2exe setup options ########################################

zipfile = r"lib\shardlib"

options = {
    "py2exe": {
        "compressed": 1,
        "optimize": 2,
        "includes": ['sip'],
        "excludes": ['backend_gtkagg', 'backend_wxagg'],
        "dll_excludes": ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll'],
        "packages": ["qgis", "PyQt4"],
        "dist_dir": "dist",
    }
}

matplotlib_data_files = tree('lib\matplotlibdata')
base_files = ("",["LICENSE.txt", "README.txt"])
data_files = tree('Data') + tree('plugins') + tree('Interviews') + tree('resources') + tree('Documentation')

setup(
    options = options,
    # The lib directory contains everything except the executables and the python dll.
    zipfile = zipfile,
    windows=[{"script": "openoceanmap.py", "icon_resources": [(1, "Images\OCEAN_SMALL_INNO.ico")]}],
    # use out build_installer class as extended py2exe build command
    cmdclass = {"py2exe": build_installer},
    data_files = data_files
)
