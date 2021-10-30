
from neighbors import *
from medianString import *
import sys 

with open(sys.argv[1]) as data:

	k = int(data.readline().rstrip('\n'))
	dna = data.readline().rstrip('\n')
	dna = dna.split(" ")
	dna = [pattern.strip(" ") for pattern in dna]

median = medianString(dna, k)
print(median)
