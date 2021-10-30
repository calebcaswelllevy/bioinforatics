def profileProb(kmer, profile):
    """	
    Takes in a profile matrix in form of list of dicts and kmer sequence. iterates through and finds prob of each locus given profile, and returns p(kmer | profile)
    TESTED: returns product of probs for string
    """

    #initialize probability to 1
    p = 1

    #Iterate through kmer, and multiply p by p of that nucleotide at that locus
    for index, char in enumerate(kmer):
        p *= profile[index][char]

    return p