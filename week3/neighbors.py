

def hammingDistance(p, q):
	"""
	Takes two strings p and q. Returns hamming distance between the strings
	"""
	d = 0
	n = len(p)

	for i in range(n):
		if p[i] != q[i]:
			d = d + 1
	return d

def neighbors(pattern, d):
	"""
	Takes a string pattern and int distance d. returns set of sequences that are d or less away iinpn Hamming space.
	"""
	
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


