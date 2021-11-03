def string(path):
    """
    takes a list of kmers in genome path order, and returns string
    """
    seq = ""
    for s in path:
        seq += s[0]
    seq += path[len(path)-1][1:]
    return seq

