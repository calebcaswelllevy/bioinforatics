


def profiler(kmers):
    """

	Computes profile matrix from alignment of motifs (list of strings). Returns profile as as a list of dicts.

    """
    #Initialize count profile with pseudocounts as list of dicts for each locus
    profile = [ {"A" : 1, "C" : 1, "G" :1, "T" : 1} for _ in kmers[0]]

    #iterate through matrix and count chars for each index
    for string in kmers:


        for index, char in enumerate(string):


            profile[index][char] += 1

    # make counts into frequencies:
    for index, dict in enumerate(profile):
        total = sum(dict.values())
        profile[index] = {k : v / total for k, v in dict.items()}
    
    return profile


