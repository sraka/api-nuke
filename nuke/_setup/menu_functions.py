"""

"""
import os
import nuke
import nukescripts

print "Menu Functions Loaded = " , __file__


def set_Viewer_Channels():
    """
    Description     :   reset the viewer channel to 'rgba'
    """
    vNode = nuke.activeViewer().node()
    vNode.knob('channels').setValue('rgba')

def kill_viewers():
    """
    Description     :   kill all the viewers present in the flow
    """
    for v in nuke.allNodes("Viewer"):
        nuke.delete(v)

#################################################################################################################################
#OBSELETE
def make_menu(path,menu_name):
    """
    Description     :   Make's the menu with the specified menu name and add all the python files as menuitems and load them (to execute)
                        - This will only load the files present in the given directory

    Note            :   - *Call the function that needs to be executed inside the .py file only.
                        - Only .py files will be loaded as menu items

    Args            :   path (string)  = folder path
                        menu_name (string)  = name of the menu

    Example         :   menu_functions.make_menu('.../Menu_Bar/Common_Functions'),'|Common_Functions|')
    """
    MenuItem = nuke.menu('Nuke')
    nuke.pluginAddPath(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            file = file.split('.')[0]
            MenuItem.addCommand( '%s/%s'% (menu_name,file), "import {0} as {0};reload({0})".format(file), icon='ohu_icon.png' )

#OBSELETE
def make_menu_from_dir(src_path , folder_name , menu_name):
    """
    Description     :   make's the menu with the specified menu name and add all the python files as menuitems and load them (to execute)
                        file name = function_name
                        This is a Quick Auto Load Function

    Note            :   - file name = def name
                        - Only .py files will be loaded as menu items

    Args            :   src_path (string) = Path where the folder is present
                        folder_name (string)  = name of the folder in which the scripts are present
                        menu_name (string)  = name of the menu

    Example         :   make_menu_from_dir('../nuketool.Scripts/Menu_Bar' , 'Common_Functions' , '|Common_Functions|')
    """
    MenuItem = nuke.menu('Nuke')
    for root, directories, filenames in os.walk(os.path.join(src_path,folder_name).replace('\\','/')):
        nuke.pluginAddPath(root)
        if filenames:
            for each_file in filenames:
                file = os.path.join(root ,each_file).replace('\\','/')
                file = file.replace((src_path + '/' +  folder_name + '/'),'')
                if file.endswith('.py'):
                    file = os.path.splitext(file)[0]
                if each_file.endswith('.py'):
                    each_file = os.path.splitext(each_file)[0]
                    MenuItem.addCommand( '%s/%s'% (menu_name,file), "import {0} as {0};reload({0});{0}.{0}()".format(each_file), icon='ohu_icon.png' )
#################################################################################################################################

def make_menu_recursive(src_path, folder_name, menu_name):
    """
    This is a Quick Auto Load Function for all python files(.py) present in the src_path
    Auto Load LOGO :
    if the .png file of the same name as the python_script is found in nuke.Icons dir ,
    then the logo gets loaded automatically
    This only applies to all menuItems, not for menus themselves, for loading icons on menu's , check menu.py

    """
    MenuItem = nuke.menu('Nuke')
    for root, directories, filenames in os.walk(os.path.join(src_path, folder_name)):
        nuke.pluginAddPath(root)
        if filenames:
            for each_file in filenames:
                if each_file.endswith('.py'):
                    print("\n")
                    each_file_name = os.path.splitext(each_file)[0]
                    each_file_menu_name = os.path.splitext(each_file)[0].replace("_", " ")
                    each_file_path = os.path.join(root, each_file).replace(os.sep, '/')
                    menu_file_path = each_file_path.replace((src_path + '/' + folder_name + '/'), '').split(".")[0].replace("_", " ")
                    MenuItem.removeItem(
                        '{MENU_NAME}/{MENU_FILE_NAME}'.format(MENU_NAME=menu_name, MENU_FILE_NAME=menu_file_path))
                    MenuItem.addCommand(
                        '{MENU_NAME}/{MENU_FILE_NAME}'.format(MENU_NAME=menu_name, MENU_FILE_NAME=menu_file_path),
                        "import {0} as {0};reload({0})".format(each_file_name))

def make_gizmo_menu_recurcively(src_path, folder_name, menu_name, icon):
    node_menu = nuke.menu('Nodes')
    for root, dir, file in os.walk(os.path.join(src_path, folder_name)):
        gizmo_menu = node_menu.addMenu(menu_name, icon=icon)
        if file:
            nuke.pluginAddPath(root)
            for each_file in file:
                if each_file.endswith('.gizmo'):
                    each_file_name = os.path.splitext(each_file)[0]
                    each_file_path = os.path.join(root, each_file).replace(os.sep, '/')
                    menu_file_path = each_file_path.replace((src_path + '/' + folder_name + '/'), '').split(".")[0].replace("_", " ")
                    gizmo_command = "nuke.createNode(\"{}\")".format(each_file_name)
                    gizmo_menu.addCommand('{MENU_FILE_NAME}'.format(MENU_FILE_NAME=menu_file_path), gizmo_command)

def make_custom_toolset_window():
    def load_toolsets():
        print("loading toolsets")


    nuke_tool = nuke.menu('Nodes')
    #nuke_tool.removeItem('API-Toolsets')
    api_toolsets = nuke_tool.addMenu('API-Toolsets', icon='code_paren.png')
    api_toolsets.addCommand('Create', load_toolsets)
    api_toolsets.addCommand('Toolset Browser', load_toolsets)
    # api_toolsets.addSeparator()
    api_toolsets.addMenu('2D')
    api_toolsets.addMenu('3D')
    api_toolsets.addMenu('Particles')
    # api_toolsets.addSeparator()
    api_toolsets.addMenu('S01')
    api_toolsets.addMenu('Char')
#################################################################################################################################


