import os
import nuke

# TODO: if multiple read nodes  are selected , then browse for all of them
# TODO: incorporate support for all other type of nodes as well
def browse_file():
    """

    :return:
    """
    selNode = nuke.selectedNode()
    if selNode:
        if 'file' in selNode.knobs().keys():
            filepath = selNode.knob("file").getValue()
            dir = os.path.dirname(filepath)
            os.startfile(dir)
        else:
            nuke.message("No File Knob exits on the '{}' node".format(selNode.name()))
    else:
        nuke.message('No Nodes Selected')
    
browse_file()