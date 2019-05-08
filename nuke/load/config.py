
'''
This file contains all the paths that are req in the pipeline.
'''


print "Load Config from = " , __file__



import os
import sys


# ::_______ PIPELINE PATH ________
PIPELINE_PATH = os.getenv('PIPELINE_PATH')
CORE_LIBRARY = os.getenv('CORE_LIBRARY')


# ::_______ NUKE PATH ________
NUKE_PATH = os.getenv('NUKE_PATH')
NUKE_API = os.getenv('NUKE_API')                                                                    # _nuke_API folder
NUKE_API_01 = os.getenv('NUKE_API_01')                                                              # API name
# NUKE_API_01_SCRIPT = os.path.join(NUKE_API,NUKE_API_01,'nuke.Scripts').replace('\\','/')            # API scripts folder

# All nuke api folder's variables
'''
Example     :   NUKE_API_FONTS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Fonts
                NUKE_API_GIZMOS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Gizmos
                NUKE_API_ICONS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Icons
                NUKE_API_PREFERENCES = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Preferences
                NUKE_API_PRESETS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Presets
                NUKE_API_SCRIPTS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Scripts
                NUKE_API_TOOLSETS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Toolsets
                NUKE_API_USERPRESETS = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.UserPresets
                NUKE_API_WORKSPACE = D:/__CS/___HOME_DIR/pipeline/API/_nukeAPI/api_pipe/nuke.Workspace

for each in os.listdir(os.path.join(NUKE_API , NUKE_API_01)):
    if each.startswith('nuke.'):
        path = os.path.join(NUKE_API , NUKE_API_01 , each)
        #os.startfile(path.replace('\\','/'))
        each = each.replace('nuke.','')
        # print 'NUKE_API_{}'.format(each.upper()) , '=' , path
        # 'NUKE_API_{}'.format(each.upper()) = path
'''
NUKE_API_FONTS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Fonts').replace('\\','/')
NUKE_API_GIZMOS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Gizmos').replace('\\','/')
NUKE_API_ICONS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Icons').replace('\\','/')
NUKE_API_PREFERENCES = os.path.join(NUKE_API,NUKE_API_01,'nuke.Preferences').replace('\\','/')
NUKE_API_PRESETS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Presets').replace('\\','/')
NUKE_API_SCRIPTS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Scripts').replace('\\','/')
NUKE_API_TEMPLATES = os.path.join(NUKE_API,NUKE_API_01,'nuke.Templates').replace('\\','/')
NUKE_API_TOOLSETS = os.path.join(NUKE_API,NUKE_API_01,'nuke.Toolsets').replace('\\','/')
NUKE_API_USERPRESETS = os.path.join(NUKE_API,NUKE_API_01,'nuke.UserPresets').replace('\\','/')
NUKE_API_WORKSPACE = os.path.join(NUKE_API,NUKE_API_01,'nuke.Workspace').replace('\\','/')

