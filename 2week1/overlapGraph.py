
def overlapGraph(kmers):
    """
    Given a collection of kmers, returns the overlap graph/adjacency list in dict form
    """

    #initialize adjacency dict of empty lists
    graph = {kmer : [] for kmer in kmers}

    #for each kmer, check if each other kmer is adjacent:
    for index, kmer1 in enumerate(kmers):
        for kmer2 in kmers[0:index] + kmers[index+1:]:
            if kmer1[1:] == kmer2[0:-1]:
                #If its adjacent, add it in there:
                graph[kmer1].append(kmer2)

        graph[kmer1].sort()
        if len(graph[kmer1]) < 1:
            graph.pop(kmer1)
    return graph
"""
import sys
import parseFile as pf
kmers = pf.parse(sys.argv[1], param=False)[0]
graph = overlapGraph(kmers)

with open('output.txt', 'w') as f:
    [f.write(key+' -> ' + " ".join(graph[key]) + '\n') for key in graph]
"""
"""
kmers = ["AAA", "AAT","AAG", "ATA"]
d = overlapGraph(kmers)
print(d)
"""