import findMostProbableKmer
import profiler

def motifs(dna, profile, k):
    """
    Takes dna matrix as list of strings, int k length of motifs, and probability profile as list of dicts. Iterates through each sequence in alignment
    and finds profile most probable kmer from each seq. returns this as list of strings
    """
    motifs = []
    for seq in dna:
        kmer = findMostProbableKmer.findMostProbableKmer(seq, profile, k)
        motifs.append(kmer)

    return motifs
