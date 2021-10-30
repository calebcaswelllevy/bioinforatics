import sys


data = open(str(sys.argv[1]))
pattern = data.readline().rstrip("\n")
text = data.readline().rstrip("\n")
d = int(data.readline().rstrip("\n"))

"""

pattern = 'AAAAA'
text = 'AACAAGCTGATAAACATTTAAAGAG'
d = 2
"""


def hammingDistance(p, q):
        d = 0
        n = len(p)
        for i in range(n):
                if p[i] != q[i]:
                        d = d + 1
        return d


def ApproxPatMat(pattern, text, d):
	n = len(pattern)
	l = len(text)
	loc = []

	for i in range(l-n + 1):
		substring = text[i : i+n]
		h = hammingDistance(pattern, substring)
		if h <= d:
			loc.append(i)
	return loc

loc = ApproxPatMat(pattern, text, d)

if sys.argv[2] == "count":
	print("count = ", len(loc))

print("The locations are: ")
print(*loc, sep=" ")
