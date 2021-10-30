

def consensus(text):
    """
    Finds consensus string from dna alignment. alignment is list of strings. returns string.
    """
    #list of dicts for each locus:
    countDict = [{"A": 0, "G": 0, "C":0, "T": 0} for i in range(len(text[0]))]
    
    #tally up each string:
    for line in text:
        for i, char in enumerate(line):
            countDict[i][char] += 1


    consensusString = [max(dict, key = dict.get) for dict in countDict]
    return "".join(consensusString)


