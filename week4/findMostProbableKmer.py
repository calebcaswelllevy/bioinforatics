import profileProb

def findMostProbableKmer(text, profile, k):
    """
    Takes string text (dna seq), int k (length of kmer), and a list of dicts profile (profile matrix). r
	Returns most probably kmer. 
    TESTED: returns most probable kmer in test sets. returns first of tied kmers. returns kmer at 0 or at n-k
    """
    #initialize to first kmer in text:
    kmer = text[0:k]
    #initialize p:
    p=0

    for i in range( len(text) - k + 1 ):
        #look at each kmer in text:
        slice = text[i : i + k]
        #find p(kmer | profile):
        q = profileProb.profileProb(slice, profile)

        #compare this slice to best kmer, and update best kmer if needed
        if q > p:
            p = q
            kmer = slice

    return kmer

