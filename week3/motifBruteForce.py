import sys
from neighbors import *

with open(sys.argv[1]) as file:
	params = file.readline().rstrip('\n')
	dna = file.readline().rstrip('\n')

k, d = params.split(' ')
k, d = int(k), int(d)
dna = dna.split(' ')


def motifEnum(dna, k, d):
	kmer_list = [set() for _ in dna]                  
	for pos, pattern in enumerate(dna):                  
		for k_pos in range(len(pattern) - k + 1):    
			#generate neighbors for kmers in all strings
			kmer = pattern[k_pos:k_pos+k]        
			neighbor_list = neighbors(kmer, d).   

			#add them to set in kmer_list
			kmer_list[pos].update(neighbor_list)


	patterns = set.intersection(*kmer_list)
	return patterns

p = motifEnum(dna, k, d)

print(*p)
