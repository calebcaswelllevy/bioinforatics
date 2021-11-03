def composition(s, k):
    """
    Generates the kmer composition of a string
    """
    comp = []
    for i in range(len(s)-k+1):
        kmer = s[i:i+k]
        comp.append(kmer)
    return comp
