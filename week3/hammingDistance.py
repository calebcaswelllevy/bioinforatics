data = open("dataset_9_3.txt")
p = data.readline().rstrip("\n")
q = data.readline().rstrip("\n")

def hammingDistance(p, q):
	d = 0
	n = len(p)
	for i in range(n):
		if p[i] != q[i]:
			d = d + 1
	return d

print(hammingDistance(p, q)) 
