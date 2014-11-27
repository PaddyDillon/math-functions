def GCD(n1,n2):
	if n1==0: return n2
	return GCD(n2%n1,n1)

print (GCD(15,-77))