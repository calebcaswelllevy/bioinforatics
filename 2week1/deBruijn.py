def StringToDeBruijn(string, k):
    
    """
    Creates the deBruijn graph of a string. That is a graph that treats kmers as edges
    and overlaps as nodes.
    """

    #this is the function we used in an earlier lesson that breaks a string into its 
    #kmer composition:
    import stringComposition

    #get set of k-1mers in string:
    kmers = list(set(stringComposition.composition(string, k-1)))
    kmers.sort()

    #initialize graph as dictionary of lists
    graph = {kmer : [] for kmer in kmers}

    #find adjacencies for each k-1mer and add to graph dict:
    for kmer in graph:
        for i in range(len(string)-k+1):
            if kmer == string[i:i+k-1]:
                graph[kmer].append(string[i+1:i+k])
        graph[kmer].sort()

    #Filter out kmers with no adjacency:
    graph2 = {kmer : graph[kmer] for kmer in graph if graph[kmer]}
    return graph2

def KmersToDeBruijn(kmers):
    """
    Creates the deBruijn graph of a set of kmers. That is a graph that treats kmers as edges
    and overlaps as nodes.
    """

    #initialize graph as dictionary of lists
    kmers.sort()
    graph = {kmer[:-1] : [] for kmer in kmers}

    #find adjacencies for each k-1mer and add to graph dict:
    for kmer in kmers:
        graph[kmer[:-1]].append(kmer[1:])
        graph[kmer[:-1]].sort()

    #Filter out kmers with no adjacency:

    return graph

import sys
import parseFile

kmers = parseFile.parse(sys.argv[1], delim=" \n", param=False)[0]

kmers = list(filter(lambda x: x != "", kmers))
graph = KmersToDeBruijn(kmers)

#write graph to output file
with open('output.txt', 'w') as f:
    [f.write(key+' -> ' + ",".join(graph[key]) + '\n') for key in graph]
