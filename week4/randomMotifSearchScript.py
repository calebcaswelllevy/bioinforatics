import RandomizedMotifSearch as rms
import sys

with open(sys.argv[1]) as file:
    k , t = file.readline().rstrip('\n').split(' ')
    dna = file.readline().rstrip('\n').split(' ')

k = int(k)

results = rms.MCMotifSearch(dna, k, iterations=1000, method="entropy")
motif = results[0]
score = results[1]

motif = " ".join(motif)
print(motif)
print("Score: ", score)
with open('mcMotifSearch.txt', 'w') as file:
    strings  = " ".join(motif)
    file.write(strings + "\n")
    file.close()