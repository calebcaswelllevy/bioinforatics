import sys, time

def parsePath(edge):
    """
    Takes path in the following format:
    0 -> 1
    1 -> 3
    creates and returns an adjacency list.
    """


    pathList = [int(node) for node in edge.split(' -> ')[1].split(',')]

    return pathList

def findStart(graph):
        """
        Because of the problem specifications, this function assumes the graph is eulerian, returns either first node or node with outDegree greater than in degree. Logic to check for
        non-eulerian would simply involve counting number of nodes with inNodes-Outnodes == 1, Outnodes-inNodes == 1, and throwing
        an error if either count was more than 1, or if any of the differences were greater than 1.
        """

        inDegrees = {node : 0 for node in graph}
        outDegrees = {node : 0 for node in graph}

        for node in graph:
            print(node)
            for edge in graph[node]:
                if not edge in inDegrees.keys():
                    inDegrees[edge] = 0
                    graph[edge] = []
                outDegrees[node] += 1
                inDegrees[edge] += 1
        #Return node with more out than in, if exists
        for node in inDegrees:
            
            if outDegrees[node] - inDegrees[node] == 1:
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
    
def main():    
    time1 = time.perf_counter()
    run()
    time2 = time.perf_counter()
    print("Elapsed time: ", time2-time1)
if __name__ == "__main__":
    main()