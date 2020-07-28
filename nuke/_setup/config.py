'''
This file contains all the paths that are req in the pipeline.
'''
print "Load Config from = " , __file__
import os
import sys

# ::_______ PIPELINE PATH ________
SELF_PATH = os.getenv('SELF_PATH')
CORE_LIBRARY = os.getenv('CORE_LIBRARY')
NUKE_PATH = os.getenv('NUKE_PATH')

# All nuke api folder's variables
NUKE_API_FONTS = os.path.join(SELF_PATH, 'nuke.Fonts').replace(os.sep, "/")
NUKE_API_GIZMOS = os.path.join(SELF_PATH, 'nuke.Gizmos').replace(os.sep, "/")
NUKE_API_ICONS = os.path.join(SELF_PATH, 'nuke.Icons').replace(os.sep, "/")
NUKE_API_PRESETS = os.path.join(SELF_PATH, 'nuke.Presets').replace(os.sep, "/")
NUKE_API_SCRIPTS = os.path.join(SELF_PATH, 'nuke.Scripts').replace(os.sep, "/")
NUKE_API_TEMPLATES = os.path.join(SELF_PATH, 'nuke.Templates').replace(os.sep, "/")
NUKE_API_TOOLSETS = os.path.join(SELF_PATH, 'nuke.Toolsets').replace(os.sep, "/")
NUKE_API_USERPRESETS = os.path.join(SELF_PATH, 'nuke.UserPresets').replace(os.sep, "/")
NUKE_API_WORKSPACE = os.path.join(SELF_PATH, 'nuke.Workspace').replace(os.sep, "/")

