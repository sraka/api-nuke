'''
This file gets loaded while launching nuke.
The contents of this file is loaded at application startup
'''
__version__ = "1.1"


print "Load init from = " , __file__

import os
import sys
import PySide
import platform
from PySide import QtCore

import config as init;reload(init)

print "Load init from = " , __file__

#================================================================================================================================
#                       INFO
#================================================================================================================================
print "Nuke : {nuke} / Python : {python} / PySide : {pyside} / QtCore : {qtcore}".format(
   nuke=nuke.NUKE_VERSION_STRING,
   python=platform.python_version(),
   pyside=PySide.__version__,
   qtcore=QtCore.qVersion())
   
#================================================================================================================================
#                       ADD_PLUGIN_PATH'S
#================================================================================================================================

# ::_______ PIPELINE PATH ________

nuke.pluginAddPath(init.CORE_LIBRARY)

# ::_______Append Path - "pipeline/CoreLibrary" Paths at Launch (All Core-Lib's)
        '''Example     :   nuke.pluginAddPath('./../CoreLibrary/moduleNuke')'''
for each in os.listdir(init.CORE_LIBRARY):
    folder_path = os.path.join(init.CORE_LIBRARY,each)
    if os.path.isdir(folder_path):
        nuke.pluginAddPath(folder_path)

# ::_______Append Path - nuke. folder paths (nuketools.Scripts)
        '''Example     :   nuke.pluginAddPath('./../nuke.Gizmos')'''
for each in os.listdir(os.path.join(init.NUKE_API , init.NUKE_API_01)):
    if each.startswith('nuke.'):
        nuke.pluginAddPath('./../{}'.format(each))

#================================================================================================================================
#                       LOAD_MODULES
#================================================================================================================================

# def init_load_modules():
#         import nukeClasses as nukeClasses;reload(nukeClasses)
#         nukenode = nukeClasses.NukeNode()
#         nukescene = nukeClasses.NukeSession()
#         nukevray = nukeClasses.NukeVray()

#         import nukeGui as nukeGui;reload(nukeGui)

# init_load_modules()





