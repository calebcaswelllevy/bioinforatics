import math

def entropy(column):
	"""
	Takes a string or list of base pairs representing a locus.
	returns the entropy at that locus.
	"""
	counts = {}
	for char in column:
		if counts.get(char):
			counts[char] += 1
		else:
			counts[char] = 1
	entropy = 0
	for key in counts:
		counts[key] = counts[key]/len(column)
		p = counts[key]
		entropy = entropy - (p*math.log(p, 2))
	return entropy

def totalEntropy(motifs):

	"""
	Takes an alignment matrix as a list of strings. Calculates and returns total
	entropy of the alignment.
	"""


	totEntropy = 0
	for i in range(len(motifs[0])):
		locus = [motifs[j][i] for j in range(len(motifs))]
		totEntropy += entropy(locus)
	return totEntropy

