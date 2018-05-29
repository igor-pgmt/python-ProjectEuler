from helpers import getPrimeNumbers, CheckTime
import math

# This is the fastest function
def EvDiv1(k):
	N = 1
	check = True
	limit = math.sqrt(k)
	p = getPrimeNumbers(k+3)
	i = 1
	while p[i] <= k:
		a=1
		if check:
			if p[i] <= limit:
				c = math.log(k) / math.log(p[i])
				a = math.floor(c)
			else:
				check=False
		N = N*(p[i]**a)
		i+=1
	return N

def EvDiv2(k):
	i=k
	while True :
		z=0
		for j in range(2, k+1):
			z+=i%j
		if z == 0:
			return i
		i+=k
	return k

print(EvDiv1(20))
