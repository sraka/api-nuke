import nuke

def delete_floating_nodes():
    ''' delete all floating nodes present in the flow except ['Viewer','BackdropNode'] '''
    skipNodeTypes = ['Viewer','BackdropNode']
    [nuke.delete(node) for node in nuke.allNodes() if not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]

delete_floating_nodes()
