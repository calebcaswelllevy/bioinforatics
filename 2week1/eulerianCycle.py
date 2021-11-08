

def parsePath(edge):
    """
    Takes path in the following format:
    0 -> 1
    1 -> 3
    creates and returns an adjacency list.
    """


    pathList = [int(node) for node in edge.split(' -> ')[1].split(',')]

    return pathList


def eulerianPath(graph):
    """
    
    """
    # Global Variables:
    n = len(graph) #no. vertices
    m = len([item for sublist in graph for item in sublist])#no. edges


    inEdges = [0 for i in range(n)]
    outEdges = [0 for i in range(n)]
    path = []


    def findEulerianPath():
        countInOutDegrees()
        if not graphHasEulerianPath():
            
            return None
        dfs(findStartNode())

        #return only if we traversed all the edges (i.e. might be disconnected graph):
        if len(path) == m + 1: 
            
            return path   
        return path
        
    
    def countInOutDegrees():
        for node, edges in enumerate(graph):
            for edge in edges:

                outEdges[node] += 1
                inEdges[edge] += 1


    def graphHasEulerianPath():
        start_nodes, end_nodes = 0, 0

        for i in range(n):
            if outEdges[i] - inEdges[i] > 1 or inEdges[i] - outEdges[i] > 1:
                return False
            elif outEdges[i] - inEdges[i] == 1:
                start_nodes += 1
            elif inEdges[i] - outEdges[i] == 1:
                end_nodes += 1
            return (end_nodes == 0 and start_nodes == 0) or (end_nodes == 1 and start_nodes == 1)

    def dfs(node):
        """
        Does a recursive depth first search of graph to find (backwards) path
        """
        while outEdges[node] != 0:
            outEdges[node] -= 1
            next_edge = graph[node][outEdges[node]]#not totally sure what the pseudocode is doing here
            dfs(next_edge)
        path.append(node)


    def findStartNode():
        """
        Method to find a good starting node in graph. returns node index
        """
        for i in range(n):
            if outEdges[i]:
                return i
 

    path = findEulerianPath()[::-1]      
    print("The number of edges: ", m)
    print("The length of path: ", len(path))
    return path

import sys
def main():
    with open(sys.argv[1]) as graphFile:
        file = graphFile.readlines()
        nodes = [int(line.split(" ")[0]) for line in file]
        print("nodes are : ", nodes)
        graph = []
        [graph.append([]) for item in range(max(nodes)+1)]

        print("The graph should have 11 blanks: ", graph)

        for line in file:

            graph[int(int(line.split(" ")[0]))] = parsePath(line)

            




    path = eulerianPath(graph)


    path = [str(node) for node in path]
    path = "->".join(path)
    print("Eulerian Path: ", path)
    with open('output.txt', "w") as file:
        file.write(path)

if __name__ == "__main__":
    main()