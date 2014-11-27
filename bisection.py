import math
from fractions import Fraction

def f(x):
	#return -1*(x**2 -2)
	return -math.exp(x)+math.cos(x)+1

def findRoot(alpha, beta, n, error): 
	c=0.5*(beta+alpha)
	temp=f(c)
	print ((Fraction (alpha) ,Fraction (beta), Fraction(c),temp,abs((0.5**n)*(1-0))))
	if abs(((0.5**n)*(1-0)))<error:
		return c
	if temp==0:
		return c 
	elif temp<0:
		return findRoot(alpha,c, n+1, error) 
	elif temp>0:
		return findRoot(c,beta, n+1, error)
	else: 
		return "?"

print (findRoot(0,1,0,0.01))

print (f(0.5))