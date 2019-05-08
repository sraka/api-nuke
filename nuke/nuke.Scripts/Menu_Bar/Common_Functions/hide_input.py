import sys
import nuke
import nukescripts

def hide_input():
    selnodes = nuke.selectedNodes()
    selsize = len(selnodes)
    print selsize
    if selsize == 0:
        print "b"
        nuke.message("No Nodes Selected..")
    else:
        for nodes in selnodes:
            print nodes.name()
            curstatus = int(nodes.knob("hide_input").getValue())
            print curstatus
            if curstatus == 0:
                nodes.knob("hide_input").setValue("1")
            if curstatus == 1:
                nodes.knob("hide_input").setValue(0)
            print "DONE"
    nukescripts.clear_selection_recursive()
