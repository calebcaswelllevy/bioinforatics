import sys

def parse(file, delim=" ", removeNewline=True):
    """
    parses dna seq files with the formats common in the bioinformatics course. file is the string pathway to the input
    delim is the char that separates sequences in the alignment. It assumes the first line has parameters to be passed
    on to other functions.
    """
    with open(file) as f:
        #Store params as list
        params = []
        [params.append(int(i)) for i in f.readline().rstrip('\n').split(" ")]
        
        dna = []
        
        #read in the data, separated by the delim char:
        for line in f.readlines():
            dna += line.split(delim)

        #remove newlines at end of seq if needed:
        if removeNewline:
            for index, seq in enumerate(dna):
                dna[index] = seq.strip('\n')
    return [params, dna]