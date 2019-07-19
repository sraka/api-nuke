import nuke

def set_label_value(class_name,value):
    if not nuke.allNodes(str(class_name)):
        # nuke.message('No {} nodes present in the flow'.format(class_name))
        print "No Shuffle/ShuffleCopy Nodes Present in the flow"
    else:
        for s_node in nuke.allNodes(str(class_name)):
            if not s_node['label'].getValue():
                s_node['label'].setValue(str(value))

def set_shuffle_label():
    set_label_value('Shuffle','[value in]')
    set_label_value('ShuffleCopy','[value in]- [value out]')

