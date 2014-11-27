def generateIdeal(i,n):
	ideal=[]
	for j in range(n):
		if (i*j)%n not in ideal:
			ideal.append((i*j)%n)
	return ideal 


for i in range(0,12):
	print (generateIdeal(i,12))

