import hammingDistance
import profiler

def score(kmers):
    """

        Return score of motifs as sum of hamming distances from median string
        TESTED: returns 0 for unanimous strings, finds correct median string, and correct distances

    """
    profile = profiler.profiler(kmers)
    median = ''

    #build consensus string from profile
    for loc in profile:
        consensus = max(loc, key=loc.get)
        median += consensus

    #sum the hamming distances for each motif:
    score = 0
    for seq in kmers:
        distance = hammingDistance.hammingDistance(seq, median)
        score += distance

    return score


