import sys

#Read in data from first argument file:
data = open(str(sys.argv[1]))
text = data.readline().rstrip('\n')
params = data.readline().rstrip('\n')

k, d = params.split(" ")
k, d = int(k), int(d)



# Define accessory functions:

def hammingDistance(p, q):
        d = 0
        n = len(p)
        for i in range(n):
                if p[i] != q[i]:
                        d = d + 1
        return d

def neighbors(pattern, d):
        pattern = pattern.strip(" ")
        if d == 0:
                return {pattern} #only neighbor with 0 distance is self
        if len(pattern) == 1:
                return {"A", "C", "G", "T"} #Base Case

        neighborhood = set() #Empty set of neighbors
        suffixNeighbors = neighbors(pattern[1:], d)

        for substring in suffixNeighbors:
                if hammingDistance(pattern[1:], substring) < d:
                        for base in ["A", "C", "G", "T"]:
                                neighborhood.add(base + substring)
                else:
                        neighborhood.add(pattern[0] + substring)

        return neighborhood

def maxMap(map):
	max = 0
	for key in map:
		if map[key] > max:
			max = map[key]
	return max

def reverseComplement(string):
	code = {"A":"T", "T":"A", "G":"C", "C":"G"}
	reverseComp = ""
	i = 1
	while i <= len(string):
		reverseComp += code[string[-i]]
		i += 1
	return reverseComp
	
#define main function:

def frequentWordsWithMismatches(text, k, d):
	patterns = []
	freqMap = {}
	n = len(text)

	for i in range(n-k+1):
		pattern = text[i:i+k]
		neighborhood = neighbors(pattern, d)
		for neighbor in neighborhood:
			if not freqMap.get(neighbor):
				freqMap[neighbor] = 1
			else:
				freqMap[neighbor] += 1
	#Find and add reverse complements:
	rcTotals = {}
	for seq in freqMap:
		rc = reverseComplement(seq)
		if freqMap.get(rc):
			rcTotals[seq]= freqMap[seq] + freqMap[rc] 
	m = maxMap(rcTotals)
	for pattern in rcTotals:
		if rcTotals[pattern] == m:
			patterns.append(pattern)
	return patterns

# Print answer to console:
commonWords = frequentWordsWithMismatches(text, k, d)

print(" ".join(commonWords))



