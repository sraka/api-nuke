"""
Module Doc:
Load all the necessary menu items in nuke at launch.
"""
__ver__ = 1.0
__author__ = 'sraka'

import os
import sys
import json
import nuke
import nukescripts

# TODO : convert all the print statements into logger.debug statments
# Import Custom written nuke modules from _setup folder
import config as init
import menu_functions as menu_functions
from callbacks import Callbacks

reload(menu_functions)

cece_menu='|ACG Tools|'
acg_menu='|ACG Tools|'
uis_menu='|UIs|'
nukepedia_menu='|Nukepedia|'
utilities_menu='|Utilities|'
menubar = nuke.menu("Nuke")             # All the menu's in Nuke

ccMonoIcon = "ccMono_500x500.png"
ccDualIcon = "ccDual_500x500.png"


def load_custom_menus_recursively():
    """
    To Create a Menu in nuke
    """

    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='CeCe',
                                       menu_name=cece_menu
                                       )
    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='acg_tools',
                                       menu_name=acg_menu
                                       )
    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='UIs',
                                       menu_name=uis_menu
                                       )
    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='Nukepedia',
                                       menu_name=nukepedia_menu
                                       )
    menu_functions.make_menu_recursive(src_path=''.join([init.NUKE_API_SCRIPTS, '/ui_exe/Menu_Bars']),
                                       folder_name='Utilities',
                                       menu_name=utilities_menu
                                       )

def load_custom_gizmo_menu():
    """

    :return:
    """
    menu_functions.make_gizmo_menu_recurcively(src_path=init.NUKE_API_GIZMOS,
                                               folder_name='CeCe',
                                               menu_name='CeCe',
                                               icon=ccDualIcon
                                               )
    menu_functions.make_gizmo_menu_recurcively(src_path=init.NUKE_API_GIZMOS,
                                               folder_name='ACG',
                                               menu_name='ACG_Gizmos',
                                               icon='Python.png'
                                               )
    menu_functions.make_gizmo_menu_recurcively(src_path=init.NUKE_API_GIZMOS,
                                               folder_name='OpenSource',
                                               menu_name='OpenSource',
                                               icon = 'Folder BlackRed.png'
                                               )
    menu_functions.make_gizmo_menu_recurcively(src_path=init.NUKE_API_GIZMOS,
                                               folder_name='Nukepedia',
                                               menu_name='Nukepedia',
                                               icon = 'nukepedia_gizmos.png'
                                               )

def load_nukelib_modules():
    """
    loads all the req nukelib modules in nuke at launch
    to easily access the module functions in nuke script editor.
    :return:
    """

    print "---AA---"
    import dcc.nuke.nukeClasses as nukeClasses
    reload(nukeClasses)
    nukenode = nukeClasses.NukeNode()
    nukescene = nukeClasses.NukeSession()
    nukevray = nukeClasses.NukeVray()

    import dcc.nuke.nukeGui as nukeGui
    reload(nukeGui)



########################################################################################################################
#=======================================================================================================================
#=======================================================================================================================
# CUSTOM MENU's - add manual menu item's


def add_tools_manually_to_cece_menu():
    """
    Function to manually add tools to acg custom menu in Nuke.
    :return:
    """
    acg = menubar.addMenu(cece_menu)
    acg.addSeparator()
    acg.addCommand('Vece', "nuke.createNode('Blur')")

def add_tools_manually_to_acg_menu():
    """
    Function to manually add tools to acg custom menu in Nuke.
    :return:
    """
    acg = menubar.addMenu(acg_menu)
    acg.addSeparator()
    acg.addCommand('aaaaa', "nuke.createNode('Blur')")

def add_tools_manually_to_utilities_menu():
    """
    Function to manually add tools to utilities custom menu in Nuke.
    :return:
    """
    acg = menubar.addMenu(utilities_menu)
    acg.addSeparator()
    acg.addCommand('aaaaaUtil', "nuke.createNode('Blur')", icon=ccDualIcon)
    acg.addCommand('aaaaaUtsil', "nuke.createNode('Blur')", icon=ccMonoIcon)


########################################################################################################################
#=======================================================================================================================
#=======================================================================================================================
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

########################################################################################################################
#=======================================================================================================================
#=======================================================================================================================
# DEFAULT MENU's - add custom menu item's
"""
[each.name() for each in nuke.menu('Nuke').items()]
['File', 'Edit', 'Workspace', 'Viewer', 'Render', 'Cache', 'Help',]
"""

# File Menu
def load_menu_file():
    f = menubar.findItem("File")

# Edit Menu
def load_menu_edit():
    m = menubar.findItem("Edit")
    m.addCommand('Reload All Custom MenuBars', 'make_menubar_menu()')

# Workspace Menu
def load_menu_workspace():
    f = menubar.findItem("Workspace")

# Viewer Menu
def load_menu_viewer():
    """
    # nViewer = nuke.menu( 'Viewer' )
# nViewer.addMenu( 'MyStuff',"nuke.createNode('NoOp')", icon='logo08.png' )
    :return:
    """
    v = menubar.findItem("Viewer")
    v.addCommand('MyStuff/aaaaa', "nuke.createNode('Blur')")
    v.addCommand('MyStuffdddd', "nuke.createNode('NoOp')", icon='logo08.png')
    v.addCommand('Reset Viewing channel', "menu_functions.set_Viewer_Channels()", "`")

# Render Menu
def load_menu_render():
    r = menubar.findItem("Render")

# Cache Menu
def load_menu_cache():
    c = menubar.findItem("Cache")

# Help Menu
def load_menu_help():
    h = menubar.findItem("Help")
    h.addSeparator()
    h.addCommand("CeCe Menu's", "nuke.createNode('Blur')", icon=ccDualIcon)
    h.addCommand("CeCe Gizmos & Plugins", "nuke.createNode('Blur')", icon=ccDualIcon)
    h.addCommand("CeCe Tools", "nuke.createNode('Blur')", icon=ccDualIcon)
    h.addCommand("CeCe Nuke Tools Workflow", "nuke.createNode('Blur')", icon=ccDualIcon)
    h.addCommand("CeCe Nuke Wiki", "nuke.createNode('Blur')", icon=ccDualIcon)

#=======================================================================================================================
#=======================================================================================================================

def load_custom_menus_icons_shortcuts():
    """
    To load shortcuts and icons for menu's that are recursively created by the load_custom_menus() function.
    Define the name of the menu in the dict ,
        menu_name : [<icon_name>, <shortcut>]

    if defined in dict - it will load that
    else - icon with same name in nuke.Icons dir will be loaded, if this file is not found then no icon is loaded
            default - only png file formats are loaded
    :return:
    """
    menu_ico_config_file = os.path.join(os.path.dirname(__file__), "config/menu_ico.json")
    with open(menu_ico_config_file, 'r') as f:
        custom_icons_dict = json.load(f)

    def addIcon(custom_menu_obj, obj):
        """
        Set Icon and Shortcut,
        if icon is NOT defined in dict , then load the icon with same name from nuke.Icons dir ,
        if that is also not present then no icon for menuItem

        DICT Conditions:
            if "None" in icon - then the default icon (icon file with same name in nuke.Icons dir)
            if "None" in shortcut - then add no shortcut


        :param custom_menu_obj: custom_menu_obj.name() = |ACG Tools|
        :param obj: obj.name() = External
        :return:
        """
        print("---------------",  custom_menu_obj.name()), "---------------", obj.name()

        # Apply the icon and shortcut as per the json data
        # Check if the main custom UI is present in json data

        def set_default_icon(obj):
            """
            Set Default Icon = The Icon file with same name as the menuItem
            :param obj:
            :return:
            """
            icon_file_path = os.path.join(init.NUKE_API_ICONS, (obj.name()+'.png'))
            print("set Icon - Default {}".format(icon_file_path))
            if os.path.exists(icon_file_path):
                obj.setIcon(icon_file_path)

        if obj.name() in custom_icons_dict[custom_menu_obj.name()]:
            obj_icon, obj_shortcut = custom_icons_dict[custom_menu_obj.name()][obj.name()]
            print("Values Defined in Dict : >> ", obj_icon, obj_shortcut)
            icon_file_path = os.path.join(init.NUKE_API_ICONS, obj_icon)

            if obj_icon == "default":
                set_default_icon(obj)
            elif os.path.exists(icon_file_path):
                print("set Icon - Custom from DICT. {}".format(icon_file_path))
                obj.setIcon(icon_file_path)
            else:
                print("Icon file does not exists. {}".format(icon_file_path))

            if obj_shortcut != "None":
                print("set ShortCut - Custom from DICT. {}".format(obj_shortcut))
                obj.setShortcut(obj_shortcut)
        else:
            set_default_icon(obj)

    def list_menus(custom_menu_obj, men_obj):
        """
        This is to recursively list and add icon to all the menus and menuItems.
        :param custom_menu_obj:
        :param men_obj:
        :return:
        """
        # print("setting Icon for MENUs", men_obj.name())
        addIcon(custom_menu_obj, men_obj)

        for each in men_obj.items():
            if each.__doc__ == "Menu":
                # Recursively check for all menus
                list_menus(custom_menu_obj, each)
            elif each.__doc__ == "MenuItem":
                # add icons for menuItems
                # print("setting Icon for MENU-Items", each.name())
                addIcon(custom_menu_obj, each)

    nuke_menu_obj = nuke.menu('Nuke')
    nuke_node_menus_obj = nuke.menu('Nodes')
    nuke_menu_list = [e.name() for e in nuke_menu_obj.items()]      # all menus under Nuke
    nuke_nodes_menu_list = [e.name() for e in nuke_node_menus_obj.items()]      # all menus under Nuke
    all_menus = nuke_menu_list + nuke_nodes_menu_list
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(all_menus)

    # for each menu on all the custom menus defined in the dict json
    for each_custom_menu in custom_icons_dict.keys():   # "|ACG Tools|" , "|UIs|", "|Nukepedia|"
        if each_custom_menu in nuke_menu_list:
            each_custom_menu_obj = nuke_menu_obj.findItem(str(each_custom_menu))
            # print(each_custom_menu , each_custom_menu_obj.name())
            # set icon for every menu item in a custom menu, eg, for menus in |ACG Tools|
            for each in nuke_menu_obj.findItem(each_custom_menu_obj.name()).items():
                list_menus(each_custom_menu_obj, each)
                
def load_custom_formats():
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

def load_custom_shortcuts():
    nuke.menu('Nuke').addCommand('File/Clear', "nuke.scriptClear()", 'ctrl+Alt+c')

def load_custom_knob_defaults():
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

########################################################################################################################
#=======================================================================================================================
#=======================================================================================================================
# CALLBACKS

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


"""
[each.name() for each in nuke.menu('Nodes').items()]
['Image', 'Draw', 'Time', 'Channel', 'Color', 'Filter', 'Keyer', 'Merge', 'Transform', '3D', 'Particles', 'Deep', 
'Views', 'MetaData', 'ToolSets', 'Other', 'FurnaceCore', 'CaraVR']
"""

def load_menu_nodes():
    n = menubar.findItem("Nodes")

"""
"""






def load_menu_layout():
    l = menubar.findItem("Layout")

def load_menu_view():
    v = menubar.findItem("View")
#################################################################################################################################


def main():
    nuke.addOnScriptLoad(menu_functions.kill_viewers)  # Delete viewer nodes while opening any script/nukefile

    # Create MENU_BAR items - All paths of the menu scripts dir get appended by when calling the function
    load_custom_menus_recursively()
    load_custom_gizmo_menu()
    load_custom_menus_icons_shortcuts()

    # always execute this after load_custom_menus_icons_shortcuts()
    # as it is failing when trying to add the icon for a separator -> TODO
    add_tools_manually_to_acg_menu()
    add_tools_manually_to_utilities_menu()

    load_custom_shortcuts()
    load_custom_formats()
    load_custom_knob_defaults()

    load_menu_edit()
    load_menu_viewer()

    menu_functions.make_custom_toolset_window()
    # TODO
    # load_custom_workspaces()
    # load_callbacks()

    if os.getenv("CORE_LIBRARY"):
        load_nukelib_modules()



if __name__ == '__main__':
    main()


"""
Setting Icons Manually in nuke

# -- for gizmo menus 
acg = nuke.menu('Nodes').findItem('ACG_Gizmos')
cs_gizmo = acg.findItem('ContactShadow')
cs_gizmo.setIcon(os.path.join(init.NUKE_API_ICONS,'NukeApp.ico'))

# -- for nuke menus
ui = nuke.menu('Nuke').findItem('|UIs|')
#ui.setIcon(os.path.join(init.NUKE_API_ICONS,'Folder Docs.png'))
UI = ui.findItem('PySide')
UI.setIcon(os.path.join(init.NUKE_API_ICONS,'Folder Docs.png'))

"""