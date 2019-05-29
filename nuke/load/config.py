'''
This file contains all the paths that are req in the pipeline.
'''
print "Load Config from = " , __file__
import os
import sys

# ::_______ PIPELINE PATH ________
CORE_LIBRARY = os.getenv('CORE_LIBRARY')
SELF_PATH = os.getenv('SELF_PATH')
# ::_______ NUKE PATH ________
NUKE_PATH = os.getenv('NUKE_PATH')

# All nuke api folder's variables
NUKE_API_FONTS = os.path.join(SELF_PATH,'nuke.Fonts').replace('\\','/')
NUKE_API_GIZMOS = os.path.join(SELF_PATH,'nuke.Gizmos').replace('\\','/')
NUKE_API_ICONS = os.path.join(SELF_PATH,'nuke.Icons').replace('\\','/')
NUKE_API_PREFERENCES = os.path.join(SELF_PATH,'nuke.Preferences').replace('\\','/')
NUKE_API_PRESETS = os.path.join(SELF_PATH,'nuke.Presets').replace('\\','/')
NUKE_API_SCRIPTS = os.path.join(SELF_PATH,'nuke.Scripts').replace('\\','/')
NUKE_API_TEMPLATES = os.path.join(SELF_PATH,'nuke.Templates').replace('\\','/')
NUKE_API_TOOLSETS = os.path.join(SELF_PATH,'nuke.Toolsets').replace('\\','/')
NUKE_API_USERPRESETS = os.path.join(SELF_PATH,'nuke.UserPresets').replace('\\','/')
NUKE_API_WORKSPACE = os.path.join(SELF_PATH,'nuke.Workspace').replace('\\','/')

