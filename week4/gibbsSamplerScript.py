from os import environb
from entropy import entropy
import gibbsSampler as gs
import sys
import re
import score


"""
#############################################################################
#                   DEBUGING CODE:
#
#TESTING MCMotifSearch:
#Motifs are AAA
k = 1000

dna = [
    "AAAA",
    "AAAA",
    "AAAA",
    "AAAA",
    "AAAA"
]
print("The motifs should be AAA: ", gs.gibbsSampler(dna, 3, 5, 100))

#Motifs are AAA in larger alignment
dna = [
    "GGGGGAAAGGGGGGG",
    "CCCCCAAACCCCCCC",
    "TTTTTAAATTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be AAA: ", gs.gibbsSampler(dna, 3, 5, 100))

#Motifs are mixed
dna = [
    "GGGGGAAAGGGGGGGAGGGGGGG",
    "CCCCCACACCCCCCCCCCCCCCC",
    "TTTTTAAATTTTTTTTTTTTTTT",
    "AAAAAAAAAAAAAAA",
    "GCTAGCTGCTAGCTGCTAGCTAAAGCTAGCT"
]
print("The motifs should be mixed: ", gs.gibbsSampler(dna, 3, 5, 100))
"""
"""
##############################################

"""

"""
with open(sys.argv[1]) as f:
    k, t = [int(i) for i in f.readline().rstrip('\n').split(" ")]
    
    dna = []
    
    for line in f.readlines():
        dna += line.split(' ')

    for index, seq in enumerate(dna):
        dna[index] = seq.strip('\n')
        """

def runGibbsSampler(dna:list, k:int, t:int, reps:int=20, searchLength:int=2000) -> list:
    bestAnswer = gs.gibbsSampler(dna, k, t, 1000)
    for i in range(reps):
        answer = gs.gibbsSampler(dna, k, t, searchLength)
        if score.score(answer) < score.score(bestAnswer):
            bestAnswer = answer[:]
    [print(line, end= " ") for line in bestAnswer]
    print(score.score(bestAnswer))
    return [score.score(bestAnswer), bestAnswer]

