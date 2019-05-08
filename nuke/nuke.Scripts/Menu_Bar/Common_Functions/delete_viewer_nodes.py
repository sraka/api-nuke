import nuke

def delete_viewer_nodes():
    ''' delete all vierwer nodes in the flow'''
    [nuke.delete(node) for node in nuke.allNodes() if node.Class() == 'Viewer']
    