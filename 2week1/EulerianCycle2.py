def parsePath(edge):
    """
    Takes path in the following format:
    0 -> 1
    1 -> 3
    creates and returns an adjacency list.
    """


    pathList = [int(node) for node in edge.split(' -> ')[1].split(',')]

    return pathList

def EulerianCycle(edges):
    """
    Given an Eulerian graph where a cycle exists, returns an Eulerian Cycle in 1->2->3 format. Graph should be a node-list in form of a dict.
    """
    path = []
    #start_position = getStartPosition()
    number_of_edges = 0
    for key in edges:
        number_of_edges += len(edges[key])

    def walk(start_position, edges):
        """
        
        Recursively walks path until no more edges are left, and returns first node in cycle with remaining edges
        
        """
        
        current_position = start_position
        #walk a cycle
        if edges[current_position]:
            current_position = edges[current_position].pop(0)
            #print("Walking to ", current_position)
            #print("The edges are now: ", edges)
            path.append(current_position)
            #print("The path is now: ", path)
            walk(current_position, edges)
        #Return node with unvisited edges

    
    def getStartPosition():
        """
        Finds a starting node with outgoing edges
        """
        for edge in edges:
            if (edges[edge] and edge in path) or path == []:
                print("Starting at:", edge)
                return edge
    def tryAnotherStart(edge):
        """
        Permutes cylce to first node with remaining unvisited edges
        """
        nonlocal path
        edge_index = path.index(edge)

        path = path[edge_index:] + path[1:edge_index+1]
        return path[edge_index]

    new_start_position = getStartPosition()
    i = 0
    path.append(new_start_position)
    while any([v != [] for v in edges.values()]):
        i+= 1
        print("ITERATION: ",i)

        walk(new_start_position, edges)
        next = getStartPosition()
        if next == None:
            break
        new_start_position = tryAnotherStart(next)

        
        
    


    return path
"""
Test Code:
graph = {0: [3,1], 1: [2], 2:[0, 2, 2], 3:[0]}
EulerianCycle(graph)
p
graph = {0: [1], 
        1: [2,3], 
        2:[0], 
        3: [4], 
        4: [1]}
EulerianCycle(graph)
"""



import sys
def main():
    with open(sys.argv[1]) as graphFile:
        file = graphFile.readlines()
        graph = {}
        for line in file:
            graph[int(line.split(" ")[0])] = parsePath(line)

    path = EulerianCycle(graph)


    path = [str(node) for node in path]
    print("The path is this long: ", len(path))
    path = "->".join(path)
    print("Eulerian Path: ", path)
    
    with open('output.txt', "w") as file:
        file.write(path)

if __name__ == "__main__":
    main()