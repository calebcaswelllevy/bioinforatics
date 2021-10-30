import sys
from neighbors import *
import numpy as np
import itertools

def AllStrings(k):
	"""
	For an int k, returns a list all possible kmers.
	"""
	
	bases = ["A", "C", "G", "T"]
	seq = "".join(list(itertools.repeat("A", k)))
	allKmers = neighbors(seq, len(seq))
	return allKmers


def distanceBetweenPatternAndStrings(pattern, DNA):
	
	"""
	takes string pattern and list of strings DNA, returns sum of hamming distance between template string and all strings in DNA.
	"""
	distance = 0
	for seq in DNA:
		minimumDistance = np.inf
		for i in range(len(seq) - len(pattern) + 1):

			currentDistance = hammingDistance(pattern, seq[i:i+len(pattern)])
			
			if minimumDistance > currentDistance:
				minimumDistance = currentDistance
		distance += minimumDistance
	return distance

def medianString(DNA, k):
	distance = np.inf
	patterns = AllStrings(k)
	for pattern in patterns:
		currentDistance = distanceBetweenPatternAndStrings(pattern, DNA)
		if distance > currentDistance:
			distance = currentDistance
			median = pattern
	return median