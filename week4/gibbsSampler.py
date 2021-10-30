from RandomizedMotifSearch import randomKmers
import profiler
import random
import calculateMotifProbabilities
import entropy
import score

def gibbsSampler(dna, k, t, n):
    """
    Implements gibbs sampling algorithm to search for motifs in a dna matrix.  Takes matrix dna as list of strings, 
    motif length k, size of alignment t, and number of iterations n. 
    Returns best motifs found
    """
    #randomly select kmers from each string
    newMotifs = randomKmers(dna, k)
    bestMotifs = newMotifs[:]
 

    for i in range(n):
        index = random.randint(0,t-1)

        #creates profile of new matrix with deleted row ()
        """
        print("+++++++++++++++++++++++++++++")
        print("Debugging to see if matrix is being subsetted correctly")
        print("full kmer matrix:  ", newMotifs)
        print("Deleting this row: ", newMotifs[index])
        print("Should be this:    ", newMotifs[0:index] + newMotifs[index+1:])
        print("Current best:      ", bestMotifs,)

        print()
        print("best entropy:    ", entropy.entropy(bestMotifs))
        print("current entropy: ", entropy.entropy(newMotifs))
        print("")
        """
        profile = profiler.profiler(newMotifs[0:index] + newMotifs[index+1:])

        #calculate profile probability of each locus
        probabilities = calculateMotifProbabilities.calculateMotifProbabilities(dna[index], profile, k)

        newKmerIndex = random.choices([i for i in range(len(probabilities))], weights= probabilities, k = 1)
        newKmerIndex = newKmerIndex[0]
        newKmer = dna[index][newKmerIndex : newKmerIndex + k]
        newMotifs[index] = newKmer
        if score.score(newMotifs) < score.score(bestMotifs):
            bestMotifs = newMotifs[:]
            
    
    return bestMotifs

"""
dna = [
    "GGGGGAAAGGGGGGGAGGGGGGG",
    "CCCCCACACCCCCCCCCCCCCCC",
    "TTTTTAAATTTTTTTTTTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be mixed: ", gibbsSampler(dna, 3, 5, 100))
"""