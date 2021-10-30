import profileProb



import sys

with open(sys.argv[1]) as file: 
#######Format input

	text = file.readline().rstrip('\n')
	
	k = int(file.readline().rstrip('\n'))

	matrix = []
	lines = [col.strip('\n').split(" ") for col in file.readlines()]
	for line in lines:
		matrix += line
	
	matrix = [float(i) for i in matrix]

profile = profileProb.profileMaker(matrix, k)
mpk = profileProb.findMostProbableKmer(text, k, profile)
print("+++++++++++++++++++++++++\n")
print("Optimal k-mer:")
print(mpk)
print()
print("+++++++++++++++++++++++++")