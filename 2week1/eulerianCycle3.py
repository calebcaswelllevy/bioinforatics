import sys
import time

def isPermutationOfCycle(cycle1, cycle2):
    """
    Tests if cycle one is same as cycle two
    """
    cycle21 = "->".join(cycle2.split("->")[1:])

    
    print(cycle1)
    print(cycle2)
    cycle2X = cycle2 + "->" + cycle21
    cycle1, cycle2X = cycle1.strip(" "), cycle2X.strip(" ")
    if cycle1 in cycle2X:
        print("YES")
    else:
        print("NO")
    print(cycle2X.find(cycle1))

def parsePath(edge):
    """
    Takes path in the following format:
    0 -> 1
    1 -> 3
    creates and returns an adjacency list.
    """


    pathList = [int(node) for node in edge.split(' -> ')[1].split(',')]

    return pathList



"""algorithm for directed graphs:
Start with an empty stack and an empty circuit (eulerian path).
    - If all vertices have same out-degrees as in-degrees - choose any of them.
    - If all but 2 vertices have same out-degree as in-degree, and one of those 2 vertices has out-degree with one greater than its in-degree, and the other has in-degree with one greater than its out-degree - then choose the vertex that has its out-degree with one greater than its in-degree.
    - Otherwise no euler circuit or path exists.

If current vertex has no out-going edges (i.e. neighbors) - add it to circuit, remove the last vertex from the stack and set it as the current one. Otherwise (in case it has out-going edges, i.e. neighbors) - add the vertex to the stack, take any of its neighbors, remove the edge between that vertex and selected neighbor, and set that neighbor as the current vertex.

Repeat step 2 until the current vertex has no more out-going edges (neighbors) and the stack is empty."""

def main():
    
    def findStart(graph):
        """
        This assumes graph is eulerian, returns either first node or node with outDegree greater than in degree
        """
        inDegrees = {node : 0 for node in graph}
        outDegrees = {node : 0 for node in graph}

        for node in graph:
            for edge in graph[node]:
                outDegrees[node] += 1
                inDegrees[edge] += 1
        #Return node with more out than in, if exists
        for node in inDegrees:
            if outDegrees[node] > inDegrees[node]:
                return node
        #Else return first node:       
        for node in graph.keys():
            return node

    def euler(graph):
        stack = []
        circuit = []
        current = findStart(graph)
       # print(len(stack))
        #print(graph[current] != [] and len(stack) > 0)
        i = 0
        while graph[current] != [] or (len(stack) > 0 or i == 0):
           # print(f"(++++++ITERATION {i}++++++)")
            
           # print("Stack: ", stack)
            #print("Circuit: ", circuit)
            #print("current: ", current)
            #print("Current neighbors: ", graph[current])
            if graph[current] == []:
                #print(f"Appening {current} to circuit")
                circuit.append(current)
                current = stack.pop()
                #print(f"backtracking to {current}")
            else: 
                #print(f"Adding {current} to stack")
                
                stack.append(current)
                current = graph[current].pop()
                #print(f"Moving to {current}")
            i += 1
        circuit = [circuit[-1]] + circuit
        return "->".join([str(n) for n in circuit[::-1]])



    def test():
    
        with open(sys.argv[1]) as graphFile:
            file = graphFile.readlines()
            graph = {}
            for line in file:
                graph[int(line.split(" ")[0])] = parsePath(line)
        with open(sys.argv[2]) as path:
            cycle2 = path.readline()     
        cycle = euler(graph)   
        isPermutationOfCycle(cycle, cycle2)

        




    def run():
        with open(sys.argv[1]) as graphFile:
            file = graphFile.readlines()
            graph = {}
            for line in file:
                graph[int(line.split(" ")[0])] = parsePath(line)

        cycle = euler(graph)
        print(cycle)
        with open('output.txt', 'w') as file:
            file.write(cycle)
    
    time1 = time.perf_counter()
    run()
    time2 = time.perf_counter()
    print("Elapsed time: ", time2-time1)
if __name__ == "__main__":
    main()