from neighbors import *
from medianString import *
import sys

with open(sys.argv[1]) as data:


	pattern = data.readline().rstrip('\n')
	pattern = pattern.strip(" ")
	dna = data.readline().rstrip('\n')
	dna = dna.split(" ")
	dna = [pattern.strip(" ") for pattern in dna]

distance = distanceBetweenPatternAndStrings(pattern, dna)
print(distance)

