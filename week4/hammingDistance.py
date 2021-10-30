def hammingDistance(p, q):
    """
    Returns hamming distance between strings p and q
    """
    d = 0
    n = len(p)
    for i in range(n):
    	if p[i] != q[i]:
	    	d = d + 1
    return d