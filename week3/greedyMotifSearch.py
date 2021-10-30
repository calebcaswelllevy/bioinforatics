
import profileProb as pp
import entropy
import decimal
from collections import Counter

import numpy as np


def profiler(matrix):

	"""

	Computes profile matrix from alignment of motifs (list of strings). Returns profile as as a list of dicts.

	"""

	profile = [ {"A" : 0, "C" : 0, "G" :0, "T" : 0} for _ in matrix[0]]
	
	count = len(matrix) * len(matrix[0]) #assuming all motifs are same length
	for string in matrix:
		for index, char in enumerate(string):
			profile[index][char] += 1

	# Make count dictionaries into frequency dictionaries
	for index, dict in enumerate(profile):
		total = sum(dict.values())
		profile[index] = {k : v / total for k, v in dict.items()}
	"""
	#deal with 0 prob problems from spase matrices:
	for dict in profile:
		for key in ["A", "C", "G", "T"]:
			if dict[key] == 0:
				dict[key] = decimal.Decimal(0.0000000000000000000000000000000000000001)
	"""
	return profile



def profilerPseudoCount(matrix):

	"""
	Same as profiler, but starts count at 1 instead of 0 to deal with sparse alignments
	Computes profile matrix from alignment of motifs (list of strings). Returns profile as as a list of dicts.

	"""

	profile = [ {"A" : 1, "C" : 1, "G" :1, "T" : 1} for _ in matrix[0]]
	for string in matrix:
		for index, char in enumerate(string):
			profile[index][char] += 1

	# Make count dictionaries into frequency dictionaries
	for index, dict in enumerate(profile):
		total = sum(dict.values())
		profile[index] = {k : v / total for k, v in dict.items()}
	
	return profile



def score(motifs):
	motifsArr = np.array([list(seq) for seq in motifs])
	score = 0

	for i in range(motifsArr.shape[1]):
		col_i = motifsArr[:, i]
		count = Counter(col_i)
		maxFreq = count.most_common(1)[0][1]
		score += col_i.shape[0] - maxFreq
	return score



def greedyMotifSearch(dna, k, t):
	
	#initialize with list of first kmers from each sequence:
	bestMotifs = [seq[0:k] for seq in dna]
	
	for i in range(len(dna[0]) - k + 1):
		motifs = [""]
		#slide through each kmer in first strand:
		motifs[0] = dna[0][i:i+k]
		
		
		for i in range(1, t):

			#given first seq, form profile from subsequent motifs
			profile = profilerPseudoCount(motifs)
			#IDEA: Incorporate each new motif into profile to deal with zeros
			#print("profile = ", profile)
			#print("Motifs = ", motifs)

			#find best motif in each string
			bestKmer = pp.findMostProbableKmer(dna[i], k, profile)
			print("DEBUG: bestKmer = ", bestKmer)

			#Add the best motif to the motif list
			motifs.append(bestKmer)
		
		if score(motifs) > score(bestMotifs):
			bestMotifs = motifs

	return bestMotifs





