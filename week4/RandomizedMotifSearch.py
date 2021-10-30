
import random
import profiler
import motifs
import score
import entropy


def randomKmers(dna, k):
    """
    return t random kmers from dna as list of strings
    TESTED- works
    """
    kmers = []
    for seq in dna:
        n = len(seq)
        i = random.randint(0, n-k)
        kmer = seq[i:i+k]
        kmers.append( kmer)
    return kmers


def randomizedMotifSearch(dna, k, method="score"):
    """
    runs one iteration of randomized motif search
    """
    if method == "score":
        scoreFunc = score.score
    if method == "entropy":
        scoreFunc =  entropy.totalEntropy
    newMotifs = randomKmers(dna, k)
    bestMotifs = newMotifs[:]
    while True:
        profile = profiler.profiler(newMotifs)
        newMotifs = motifs.motifs(dna, profile, k)
        if scoreFunc(newMotifs) < scoreFunc(bestMotifs):
            bestMotifs = newMotifs[:]
        else: 
            return bestMotifs


def MCMotifSearch(dna, k, iterations, method="score"):
    if method == "score":
        scoreFunc = score.score
    if method == "entropy":
        scoreFunc =  entropy.totalEntropy
    #first iteration to find starting motifs and score:
    bestMotifs = randomizedMotifSearch(dna, k)
    bestScore = scoreFunc(bestMotifs)

    #Do {iterations} more searches to find a better estimate:
    for i in range(iterations):
        newMotifs = randomizedMotifSearch(dna, k-1, method)
        newScore = scoreFunc(newMotifs)


        if newScore < bestScore: 
            bestScore = newScore
            bestMotifs = newMotifs[:]
        print(f"The Score for iteration {i} is: {score.score(bestMotifs)}. The Entropy is  {entropy.totalEntropy(bestMotifs)}")
    return [bestMotifs, bestScore]

"""
#############################################################################
#                   DEBUGING CODE:
#
#TESTING MCMotifSearch:
#Motifs are AAA
k = 1000

dna = [
    "AAA",
    "AAA",
    "AAA",
    "AAA",
    "AAA"
]
print("The motifs should be AAA: ", MCMotifSearch(dna, 3, k))

#Motifs are AAA in larger alignment
dna = [
    "GGGGGAAAGGGGGGG",
    "CCCCCAAACCCCCCC",
    "TTTTTAAATTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be AAA: ", MCMotifSearch(dna, 3, k))

#Motifs are mixed
dna = [
    "GGGGGAAAGGGGGGGAGGGGGGG",
    "CCCCCACACCCCCCCCCCCCCCC",
    "TTTTTAAATTTTTTTTTTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be mixed: ", MCMotifSearch(dna, 3, k))
"""
"""
##############################################
#
#TESTING randomized motif search:
#
#Motifs are AAA

dna = [
    "AAA",
    "AAA",
    "AAA",
    "AAA",
    "AAA"
]
print("The motifs should be AAA: ", randomizedMotifSearch(dna, 3))

#Motifs are AAA in larger alignment
dna = [
    "GGGGGAAAGGGGGGG",
    "CCCCCAAACCCCCCC",
    "TTTTTAAATTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be AAA: ", randomizedMotifSearch(dna, 3))

#Motifs are mixed
dna = [
    "GGGGGAAAGGGGGGG",
    "CCCCCACACCCCCCC",
    "TTTTTAAATTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be AAA: ", randomizedMotifSearch(dna, 3))

"""