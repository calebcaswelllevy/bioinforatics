import greedyMotifSearch as gms
import sys

with open(sys.argv[1]) as file:
	params = file.readline().rstrip('\n').split(" ")
	print(params)
	k, t = params
	k, t = int(k), int(t)
	dna = file.readline().rstrip('\n').split(" ")

bestMotifs = gms.greedyMotifSearch(dna, k, t)

print("the best motifs are:")
[print(motif) for motif in bestMotifs]




