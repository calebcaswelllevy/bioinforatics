def parsePath(path):
    """
    Takes path in the following format:
    0 -> 1
    1 -> 3
    creates and returns a dictionary.
    """

    path = path.split('\n')
    pathDict = {edge.split(' \n ')[0] : [node for node in edge.split(' \n ')[1].split(',')] for edge in path}

    return pathDict

def randomWalk(node, graph):
    """
    Accessory function that walks a random unvisited path starting at node, and colors visited edges black.
    returns list of node numbers in order visited
    """

def eulerianCycle(graph):
    """
    
    """
    #color each edge white
    #RandomWalk(node, graph): form a cycle by randomly walking, color visited edges black
    #Check for node unvisited edges