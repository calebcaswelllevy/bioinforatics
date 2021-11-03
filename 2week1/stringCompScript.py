import parseFile
import sys
import stringComposition

k, dna = parseFile.parse(sys.argv[1])
dna = dna[0]
k = int(*k)

comp = stringComposition.composition(dna, k)
with open("output.txt", "w") as f:
    [f.write(f'{line}\n') for line in comp]