import sys, parseFile, gibbsSamplerScript, math, medianString

file = sys.argv[1]
data = parseFile.parse(file)
params, dna = data
k, t = params


motifs = {'bestK' : 0, 'bestKScore': math.inf, 'bestMotif' : ''}
for i in range(7, 14):
    answer = gibbsSamplerScript.runGibbsSampler(dna=dna, k=i, t=t, reps=3000, searchLength=2000)
    answerDict = {}
    answerDict["score"] = answer[0]
    answerDict["motifs"] = answer[1]
    answerDict["ratio"] = answerDict["score"]/i
    answerDict["consensus"] = medianString.medianString(answerDict["motifs"], i)
    if answerDict["ratio"] < motifs["bestKScore"]:
        motifs["bestK"] = i
        motifs["bestKScore"] = answerDict["ratio"]
        motifs["bestMotif"] = answerDict["consensus"]
    motifs[i] = answerDict
    ratio=answerDict["ratio"]
    consensus = answerDict["consensus"]
    print(f"Consensus string for k = {i} = {consensus} with score={ratio}")

print("bestK:      ", motifs['bestK'])
print("bestKScore: ", motifs['bestKScore'])
print("Best consensus motif: ", motifs["bestMotif"])
print("Printing answers:")
print(motifs)