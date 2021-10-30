def search(seq, index = 0):
    """
    Searches for start and stop codons starting at index. returns string slice representing coding region assuming no introns
    """
    start = "ATG"
    stop = ["TAG", "TGA", "TAA"]
    
    seq = seq[index:]
    startCodon = seq.find(start)
    stopCodon = len(seq)
    for i in range(len(seq[startCodon:]), step=3):
        if seq[startCodon + i: startCodon + i+3] in stop:
            stopCodon = i
            break

    #Slice out the coding sequence:
    gene = seq[startCodon : startCodon + stopCodon + 3]
    
    return gene
