import sys
import matplotlib.pyplot as plt
from kmerSearch import *

#Process the genome:
genome = ""
with open(sys.argv[1]) as file:
	metadata = file.readline()
	for line in file:
		genome = genome + line.strip('/n')
genome = genome.replace('\n', '')
	
def skew(genome):
	skew = 0
	skewList = []
	for char in genome:
		if char == "C":
			skew -= 1
		if char == "G":
			skew += 1
		skewList.append(skew)

	return skewList

s = skew(genome)

# Take a look at the skew plot for the genome:
plt.plot(s)
plt.ylabel('G - C')
plt.xlabel('Genome Position (mB)')
plt.title('Skew Plot for Salmonella Enterica')
plt.show()

#Skew switches to positive near 3.8mB
minima = [3818426, 3818641, 3819215]

#Search for 9-mers in these three regions:
def makeWindow(genome, locus):
	window = genome[locus-250:locus+250]
	return window
windows = []
for locus in minima:
	windows.append(makeWindow(genome, locus))

#search each window for 9-mers:
words = []
for window in windows:
	words.append(frequentWordsWithMismatches(window, 9, 3))

#take a look:
print(*words)
