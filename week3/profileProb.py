

import math as m


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




def profileProb(kmer, profile):
	
	"""

	Takes in a profile matrix in form of list of dicts and kmer sequence. iterates through and finds prob of each locus given profile, and returns p(kmer | profile)

	"""

	print("kmer'= ", kmer)
	p = 1
	for index, char in enumerate(kmer):
		p *= profile[index][char]

	return p

def profileMaker(profile, k): #profile is a 1d list

	"""
	takes 1D list profile matrix and int k. 
	Returns profile formatted as list of dicts to pass to profileProb.
	"""
	bases = ["A","C","G","T"]
	profile2 = [{} for _ in range(k)]

	for i in range(len(profile)):
		if m.floor((i)/k) == 0:
			# A row of i % kth col
			profile2[i%k]["A"] = profile[i]

		elif m.floor((i)/k) == 1:
			# G row of i % kth col
			profile2[i%k]["C"] = profile[i]

		elif m.floor((i)/k) == 2:
			# C row of i % kth col
			profile2[i%k]["G"] = profile[i]

		else:	
			# T row of i % kth col		
			profile2[i%k]["T"] = profile[i]
	
		
	#deal with problem from sparse matrix 0 probabilities:
	
	return profile2

def findMostProbableKmer(text, k, profile):

	"""
	
	Takes string text (dna seq), int k (length of kmer), and a list of dicts profile (profile matrix). returns most probably kmer. 
	"""
	#initialize to first kmer in case all kmers have 0 prob. This is an issue with small alignments because some bases will not show up at all.
	kmer = text[0:k]
	
	p = 0
	for i in range(len(text) - k + 1):
		slice = text[i:i+k]
		print("i = :", i)
		q = profileProb(slice, profile)
		print("kmer = ", kmer)
		print("p(kmer | profile) = ", p)
		print("p(kmer'| profile) = ", q)
		print("----------------------------")
		
		
		if q > p:
			print("Better kmer found! Updating p")
			p = q
			kmer = slice
	
	return kmer


def findMostProbableKmer2(text, k, motifs):

	"""
	
	Takes string text (dna seq), int k (length of kmer), and a list of strings(motifs). returns most probable kmer. 

	Same as original function, but makes profile with both original and candidate kmer as a way to deal with 0 probability problem
	"""
	#initialize to first kmer in case all kmers have 0 prob. This is an issue with small alignments because some bases will not show up at all.
	kmer = text[0:k]
	
	p = 0
	for i in range(len(text) - k + 1):
		slice = text[i:i+k]
		print("i = :", i)
		tempMotifs = motifs + [slice]
		profile = profiler(tempMotifs)
		q = profileProb(slice, profile)
		print("kmer = ", kmer)
		print("p(kmer | profile) = ", p)
		print("p(kmer'| profile) = ", q)
		print("----------------------------")
		
		
		if q > p:
			print("Better kmer found! Updating p")
			p = q
			kmer = slice
	
	return kmer
