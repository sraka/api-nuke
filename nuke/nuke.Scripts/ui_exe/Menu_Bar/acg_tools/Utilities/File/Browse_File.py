import os
import nuke

def GU_browse_file():
    snode = nuke.selectedNode()
    if snode:
        if 'file' in snode.knobs().keys():
            filepath = snode.knob("file").getValue()
            dir = os.path.dirname(filepath)
            os.startfile(dir)
        else:
            nuke.message("No File Knob exits on the '{}' node".format(snode.name()))
    else:
        nuke.message('No Nodes Selected')
    
GU_browse_file()