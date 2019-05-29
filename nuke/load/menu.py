__ver__=1.0
__author__='sraka'

import os , sys , nuke , nukescripts
import config as init
import menu_functions as menu_functions;reload(menu_functions)

def make_menubar_menu():
    menu_functions.make_menu_from_dir(''.join([init.NUKE_API_SCRIPTS,'/Menu_Bar']), 'Common_Functions' , '|Common_Functions|')
    menu_functions.make_menu_from_dir(''.join([init.NUKE_API_SCRIPTS,'/Menu_Bar']), 'General_Utils' , '|General_Utils|')
    menu_functions.make_menu_from_dir(''.join([init.NUKE_API_SCRIPTS,'/Menu_Bar']), 'third_party' , '|third_party|')


def main_launch_pad():
    nuke.addOnScriptLoad(menu_functions.kill_viewers)       # Delete viewer nodes while opening any script/nukefile
    
    # Create MENU_BAR Menu's - All paths of the dir get appended by when calling the function
    make_menubar_menu()

    load_formats()
    load_shortcuts()
    load_knob_defaults()

    load_menu_EditMenu()
    load_menu_viewer()

    init_load_modules()

def init_load_modules():
    import dcc.nuke.nukeClasses as nukeClasses;reload(nukeClasses)
    nukenode = nukeClasses.NukeNode()
    nukescene = nukeClasses.NukeSession()
    nukevray = nukeClasses.NukeVray()

    import dcc.nuke.nukeGui as nukeGui;reload(nukeGui)


#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
'''
> Custom Formats
> Custom ShortCuts
> Knob Defaults

'''

#================================================================================================================================
#                       > Custom Formats
#================================================================================================================================

def load_formats():
    nuke.addFormat ("720 540 0 0 720 540 1.0 NTSC_square")
    nuke.addFormat ("960 540 0 0 960 540 1.0 540p")
    nuke.addFormat ("1280 720 0 0 1280 720 1.0 720p")
    nuke.addFormat ("1920 1080 0 0 1920 1080 1.0 1080p")

    nuke.addFormat ("1920 1440 0 0 1920 1440 1.0 1920_4x3")     
    nuke.addFormat ("960 720 0 0 960 720 1.0 1920_4x3_half")
    nuke.addFormat ("3840 2160 0 0 3840 2160 1.0 HD_double")
    nuke.addFormat ("4096 4096 0 0 4096 4096 1.0 4k_square")
    nuke.addFormat ("2048 1108 0 0 2048 1108 1.0 2k_185_crop")
    nuke.addFormat ("2048 1157 0 0 2048 1157 1.0 2k_3perf_crop")
    nuke.addFormat ("2048 872 0 0 2048 872 1.0 2k_235_crop")

#================================================================================================================================
#                       > Custom ShortCuts
#================================================================================================================================

def load_shortcuts():
    nuke.menu( 'Nuke' ).addCommand( 'File/Clear',"nuke.scriptClear()", 'ctrl+Alt+c')

#================================================================================================================================
#                       > Knob Defaults
#================================================================================================================================

def load_knob_defaults():
    #                       FILE NAME  
    nuke.knobDefault("Roto.output","rgba")
    nuke.knobDefault('Bezier.linear', 'true' )
    nuke.knobDefault("RotoPaint.output","all")

    nuke.knobDefault('Blur.label', '[value size]')

    nuke.knobDefault("Grade.channels","rgba")
    nuke.knobDefault('Grade.black_clamp','false')# this turns off black clamp on Grade nodes

    #                       FILE NAME  
    nuke.knobDefault("Shuffle.label","[value in]")
    nuke.knobDefault("ShuffleCopy.label","[value in]- [value out]")

    #                       FILE NAME  
    nuke.knobDefault("PostageStamp.hide_input",'1')
    nuke.knobDefault('Switch.label', '[value which]')

    #                       FILE NAME  
    nuke.knobDefault("Exposure.mode",'Stops')
    nuke.knobDefault('Dissolve.label', '[value which]')
    nuke.knobDefault('Tracker.label', '[value transform] / ref:[value reference_frame]')
    nuke.knobDefault('Colorspace.label', '[value colorspace_in] >> [value colorspace_out]')

    #nuke.knobDefault('nuke.ViewerProcess','rec709')
    #nuke.knobDefault('root.ViewerProcess','rec709')

    #-------------------------------
    #			WRITE_NODE                     

    nuke.knobDefault("Write.channels", "rgba")
    nuke.knobDefault("Write.file_type","jpg") 
    nuke.knobDefault("Write._jpeg_quality", "1")
    nuke.knobDefault("Write._jpeg_sub_sampling", "1")
    #nuke.knobDefault('Write.beforeRender' , 'readList.updatereadList()')

    #-------------------------------
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
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

'''
> Menu Bar
> Viewer



'''




# ________________________________________________________________________________________________________________________________
#			MENU BAR              
#________________________________________________________________________________________________________________________________

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
    menubar=nuke.menu("Nuke")
    m=menubar.addMenu("Edit")
    m.addCommand( 'Reload All Custom MenuBars', 'make_menubar_menu()')



# ________________________________________________________________________________________________________________________________
#			VIEWER             
#________________________________________________________________________________________________________________________________

# nViewer = nuke.menu( 'Viewer' )
# nViewer.addMenu( 'MyStuff',"nuke.createNode('NoOp')", icon='logo08.png' )
def load_menu_viewer():
    nuke.menu( 'Viewer' ).addCommand( 'MyStuff/aaaaa',"nuke.createNode('Blur')" )
    nuke.menu( 'Viewer' ).addCommand('Reset Viewing channel',"menu_functions.set_Viewer_Channels()","`")


# ________________________________________________________________________________________________________________________________
#			MENU BAR              
#________________________________________________________________________________________________________________________________







# ________________________________________________________________________________________________________________________________
#			MENU BAR              
#________________________________________________________________________________________________________________________________






# ________________________________________________________________________________________________________________________________
#			MENU BAR              
#________________________________________________________________________________________________________________________________






# ________________________________________________________________________________________________________________________________
#			MENU BAR              
#________________________________________________________________________________________________________________________________









if __name__ == '__main__':
    main_launch_pad()