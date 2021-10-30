import profileProb

def calculateMotifProbabilities(seq, profile, k):
    """
    TO DO: takes sequence, and returns list of probabilities for kmer at each index.
    """
    probabilities = []
    for i in range(len(seq) - k + 1):
        kmer = seq[i : i + k]
        probabilities.append(profileProb.profileProb(kmer, profile))
    return probabilities