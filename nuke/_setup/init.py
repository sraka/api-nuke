"""
Module Doc:
This file gets loaded while launching nuke.
The contents of this file is loaded at application startup
"""
__version__ = "1.1"

import os
import platform

import config as init; reload(init)
print "Load init from = ", __file__

#=======================================================================================================================
#                       SET_VARIABLES
#=======================================================================================================================

NUKE_API_PATH= os.path.normpath(os.getcwd() + os.sep + os.pardir)       #../nuke
NUKE_API_INIT_PATH = os.path.dirname(__file__)                          #../nuke/_setup

#=======================================================================================================================
#                       INFO
#=======================================================================================================================
print "Nuke : {nuke} / Python : {python} ".format(
   nuke=nuke.NUKE_VERSION_STRING,
   python=platform.python_version())

   
#=======================================================================================================================
#                       ADD_PLUGIN_PATH'S
#=======================================================================================================================

# ::_______Append Path  "../CoreLibrary"
# nuke.pluginAddPath(init.CORE_LIBRARY)

# ::_______Append Path  "pipeline/CoreLibrary" Folders (All Core-Lib's)
# '''Example     :   nuke.pluginAddPath('./../CoreLibrary/dcc')'''
# for each in os.listdir(init.CORE_LIBRARY):
#     folder_path = os.path.join(init.CORE_LIBRARY,each)
#     if os.path.isdir(folder_path):
#         nuke.pluginAddPath(folder_path)

# ::_______Append Path  -  nuke.*  - all folder paths (nuke.Scripts)
#  '''Example     :   nuke.pluginAddPath('./../nuke.Gizmos')'''
for each in os.listdir(os.getcwd()):
    if each.startswith('nuke.'):
        each_path = os.path.join(NUKE_API_PATH, 'nuke', each)
        nuke.pluginAddPath(each_path)

# ::_______Append Path  -  nuke.Scripts = for nuke scripts
nuke.pluginAddPath(os.path.join(init.NUKE_API_SCRIPTS, "ui_src"))


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





