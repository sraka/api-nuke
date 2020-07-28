"""
Module Doc:
"""
__ver__ = 1.0
__author__ = 'sraka'

import os
import sys
import nuke
import nukescripts

# Import Custom written nuke modules from _setup folder
import config as init
import menu_functions as menu_functions
from callbacks import Callbacks

reload(menu_functions)

def load_custom_menus():
    """
    To Create a Menu in nuke
    """

    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='acg_tools',
                                       menu_name='|ACG Tools|'
                                       )
    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='UIs',
                                       menu_name='|UIs|'
                                       )


def load_nukelib_modules():
    """
    loads all the req nukelib modules in nuke at launch
    to easily access the module functions in nuke script editor.
    :return:
    """

    print "---AA---"
    import dcc.nuke.nukeClasses as nukeClasses;
    reload(nukeClasses)
    nukenode = nukeClasses.NukeNode()
    nukescene = nukeClasses.NukeSession()
    nukevray = nukeClasses.NukeVray()

    import dcc.nuke.nukeGui as nukeGui;
    reload(nukeGui)


def main():
    nuke.addOnScriptLoad(menu_functions.kill_viewers)  # Delete viewer nodes while opening any script/nukefile

    # Create MENU_BAR items - All paths of the menu scripts dir get appended by when calling the function
    load_custom_menus()
    custom_formats_load()
    custom_shortcuts_load()
    custom_knob_defaults_load()

    load_menu_EditMenu()
    load_menu_viewer()

    # TODO
    # load_custom_workspaces()
    # load_custom_icons()
    if os.getenv("CORE_LIBRARY"):
        load_nukelib_modules()
    # load_callbacks()


#################################################################################################################################

def custom_formats_load():
    nuke.addFormat("720 540 0 0 720 540 1.0 NTSC_square")
    nuke.addFormat("960 540 0 0 960 540 1.0 540p")
    nuke.addFormat("1280 720 0 0 1280 720 1.0 720p")
    nuke.addFormat("1920 1080 0 0 1920 1080 1.0 1080p")

    nuke.addFormat("1920 1440 0 0 1920 1440 1.0 1920_4x3")
    nuke.addFormat("960 720 0 0 960 720 1.0 1920_4x3_half")
    nuke.addFormat("3840 2160 0 0 3840 2160 1.0 HD_double")
    nuke.addFormat("4096 4096 0 0 4096 4096 1.0 4k_square")
    nuke.addFormat("2048 1108 0 0 2048 1108 1.0 2k_185_crop")
    nuke.addFormat("2048 1157 0 0 2048 1157 1.0 2k_3perf_crop")
    nuke.addFormat("2048 872 0 0 2048 872 1.0 2k_235_crop")


def custom_shortcuts_load():
    nuke.menu('Nuke').addCommand('File/Clear', "nuke.scriptClear()", 'ctrl+Alt+c')


def custom_knob_defaults_load():
    """
    Add default knob values for various nodes present in nuke, for faster workflow.
    When you create the below nodes in nuke, the knob mentioned will have the mentioned value selected by default
    :return:
    """
    #                       FILE NAME
    nuke.knobDefault("Roto.output", "rgba")
    nuke.knobDefault('Bezier.linear', 'true')
    nuke.knobDefault("RotoPaint.output", "all")

    nuke.knobDefault('Blur.label', '[value size]')

    nuke.knobDefault("Grade.channels", "rgba")
    nuke.knobDefault('Grade.black_clamp', 'false')  # this turns off black clamp on Grade nodes

    #                       FILE NAME
    nuke.knobDefault("Shuffle.label", "[value in]")
    nuke.knobDefault("ShuffleCopy.label", "[value in]- [value out]")

    #                       FILE NAME
    nuke.knobDefault("PostageStamp.hide_input", '1')
    nuke.knobDefault('Switch.label', '[value which]')

    #                       FILE NAME
    nuke.knobDefault("Exposure.mode", 'Stops')
    nuke.knobDefault('Dissolve.label', '[value which]')
    nuke.knobDefault('Tracker.label', '[value transform] / ref:[value reference_frame]')
    nuke.knobDefault('Colorspace.label', '[value colorspace_in] >> [value colorspace_out]')

    # nuke.knobDefault('nuke.ViewerProcess','rec709')
    # nuke.knobDefault('root.ViewerProcess','rec709')

    # -------------------------------
    #			WRITE_NODE

    nuke.knobDefault("Write.channels", "rgba")
    nuke.knobDefault("Write.file_type", "jpg")
    nuke.knobDefault("Write._jpeg_quality", "1")
    nuke.knobDefault("Write._jpeg_sub_sampling", "1")
    # nuke.knobDefault('Write.beforeRender' , 'readList.updatereadList()')

    # -------------------------------
    #			3D DEFAULTS

    # toolbar.addCommand("3D/Camera", "nuke.createNode('Camera2');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")                #modify camera to have Add Constrain Tab
    # toolbar.addCommand("3D/Axis", "nuke.createNode('Axis2');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")                    #modify camera to have Add Constrain Tab
    # toolbar.addCommand("3D/Geometry/Card", "nuke.createNode('Card2');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")           #modify Card to have Add Constrain Tab
    # toolbar.addCommand("3D/Geometry/Cube", "nuke.createNode('Cube');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")            #modify Cube to have Add Constrain Tab
    # toolbar.addCommand("3D/Geometry/Cylinder", "nuke.createNode('Cylinder');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")    #modify Cylinder to have Add Constrain Tab
    # toolbar.addCommand("3D/Lights/Light", "nuke.createNode('Light2');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")           #modify Light to have Add Constrain Tab
    # toolbar.addCommand("3D/Lights/Direct", "nuke.createNode('DirectLight');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")     #modify DirectLight to have Add Constrain Tab
    # toolbar.addCommand("3D/Lights/Spotlight", "nuke.createNode('Spotlight');addconstraintab.constrain();nuke.selectedNode().knob('display').setFlag(0)")    #modify Spotlight to have Add Constrain Tab


#################################################################################################################################

def load_callbacks():
    """
    This function is to load nuke callback functions as required
    :return:
    """
    cb = Callbacks()
    # OnUserCreate
    nuke.addOnUserCreate(cb.function)
    nuke.removeOnUserCreate(cb.function)

    # onCreate
    nuke.addOnCreate(cb.function)
    nuke.removeOnCreate(cb.function)

    # onScriptLoad
    nuke.addOnScriptLoad(cb.function)
    nuke.removeOnScriptLoad(cb.function)

    # onScriptSave
    nuke.addOnScriptSave(cb.function)
    nuke.removeOnScriptSave(cb.function)

    # onScriptClose
    nuke.addOnScriptClose(cb.function)
    nuke.removeOnScriptClose(cb.function)

    # onDestroy
    nuke.addOnDestroy(cb.function)
    nuke.removeOnDestroy(cb.function)

    # knobChanged
    nuke.addKnobChanged(cb.function)
    nuke.removeKnobChanged(cb.function)

    # updateUI
    nuke.addUpdateUI(cb.function)
    nuke.removeUpdateUI(cb.function)

    # autolabel
    nuke.addAutolabel(cb.function)
    nuke.removeAutolabel(cb.function)

    # beforeRender
    nuke.addBeforeRender(cb.function)
    nuke.removeBeforeRender(cb.function)

    # afterRender
    nuke.addAfterRender(cb.function)
    nuke.removeAfterRender(cb.function)

    # beforeFrameRender
    nuke.addBeforeFrameRender(cb.function)
    nuke.removeBeforeFrameRender(cb.function)

    # afterFrameRender
    nuke.addAfterFrameRender(cb.function)
    nuke.removeAfterFrameRender(cb.function)

    # afterBackgroundRender
    nuke.addAfterBackgroundRender(cb.function)
    nuke.removeAfterBackgroundRender(cb.function)

    # afterBackgroundFrameRender
    nuke.addBackgroundFrameRender(cb.function)
    nuke.removeAfterBackgroundFrameRender(cb.function)

    # filenameFilter
    nuke.addFilenameFilter(cb.function)
    nuke.removeFilenameFilter(cb.function)

    # validateFilename
    nuke.addValidateFilename(cb.function)
    nuke.removeValidateFilename(cb.function)

    # autoSaveFilter
    nuke.addAutoSaveFilter(cb.function)
    nuke.removeAutoSaveFilter(cb.function)

    # autoSaveRestoreFilter
    nuke.addAutoSaveRestoreFilter(cb.function)
    nuke.removeAutoSaveRestoreFilter(cb.function)


#################################################################################################################################


"""
> Menu Bar
> Viewer
"""


# ________________________________________________________________________________________________________________________________
#			MENU BAR
# ________________________________________________________________________________________________________________________________

# nMenuItem = nuke.menu('Nuke')

# menu_name_01 = 'Custom Menu'
# nMenuItem.addCommand( '%s/CreateCC'% (menu_name_01), "nuke.createNode('ColorCorrect')", icon='ohu_icon.png' )
# nMenuItem.findItem( '%s' % (menu_name_01) ).addSeparator()

# menu_name_02 = 'Utilities'
# nMenuItem.addCommand( '%s/CreateCC'% (menu_name_02), "nuke.createNode('ColorCorrect')", icon='ohu_icon.png' )
# nMenuItem.findItem( '%s' % (menu_name_02) ).addSeparator()


# menu_name_03 = 'Tools'
# nMenuItem.addCommand( '%s/CreateCC'% (menu_name_03), "nuke.createNode('ColorCorrect')", icon='ohu_icon.png' )
# nMenuItem.findItem( '%s' % (menu_name_03) ).addSeparator()

def load_menu_EditMenu():
    menubar = nuke.menu("Nuke")
    m = menubar.addMenu("Edit")
    m.addCommand('Reload All Custom MenuBars', 'make_menubar_menu()')


# ________________________________________________________________________________________________________________________________
#			VIEWER
# ________________________________________________________________________________________________________________________________

# nViewer = nuke.menu( 'Viewer' )
# nViewer.addMenu( 'MyStuff',"nuke.createNode('NoOp')", icon='logo08.png' )
def load_menu_viewer():
    nuke.menu('Viewer').addCommand('MyStuff/aaaaa', "nuke.createNode('Blur')")
    nuke.menu('Viewer').addCommand('Reset Viewing channel', "menu_functions.set_Viewer_Channels()", "`")


# ________________________________________________________________________________________________________________________________
#			MENU BAR              
# ________________________________________________________________________________________________________________________________


# ________________________________________________________________________________________________________________________________
#			MENU BAR              
# ________________________________________________________________________________________________________________________________


# ________________________________________________________________________________________________________________________________
#			MENU BAR              
# ________________________________________________________________________________________________________________________________


# ________________________________________________________________________________________________________________________________
#			MENU BAR              
# ________________________________________________________________________________________________________________________________


if __name__ == '__main__':
    main()
