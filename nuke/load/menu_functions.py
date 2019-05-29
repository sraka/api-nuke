import os
import nuke
import nukescripts

print "Importing Menu Functions = " , __file__


def set_Viewer_Channels():
    '''
    Description     :   reset the viewer channel to 'rgba'
    '''
    vNode = nuke.activeViewer().node()
    vNode.knob('channels').setValue('rgba')

def kill_viewers():
    '''
    Description     :   kill all the viewers present in the flow
    '''
    for v in nuke.allNodes("Viewer"):
        nuke.delete(v)

def make_menu(path,menu_name):
    '''
    Description     :   Make's the menu with the specified menu name and add all the python files as menuitems and load them (to execute)
                        - This will only load the files present in the given directory
                        
    Note            :   - *Call the function that needs to be executed inside the .py file only.
                        - Only .py files will be loaded as menu items     
    
    Args            :   path (string)  = folder path 
                        menu_name (string)  = name of the menu

    Example         :   menu_functions.make_menu('.../Menu_Bar/Common_Functions'),'|Common_Functions|')
    '''
    MenuItem = nuke.menu('Nuke')
    nuke.pluginAddPath(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            file = file.split('.')[0]
            MenuItem.addCommand( '%s/%s'% (menu_name,file), "import {0} as {0};reload({0})".format(file), icon='ohu_icon.png' )

def make_menu_from_dir(src_path , folder_name , menu_name):
    '''
    Description     :   make's the menu with the specified menu name and add all the python files as menuitems and load them (to execute)
    
    Note            :   - file name = def name
                        - Only .py files will be loaded as menu items    
    
    Args            :   src_path (string) = Path where the folder is present
                        folder_name (string)  = name of the folder in which the scripts are present
                        menu_name (string)  = name of the menu

    Example         :   make_menu_from_dir('../nuketool.Scripts/Menu_Bar' , 'Common_Functions' , '|Common_Functions|')
    '''
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


                    