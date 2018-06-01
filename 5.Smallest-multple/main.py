# https: // projecteuler.net/problem = 5
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from helpers import getPrimeNumbers, CheckTime
import math

# This is the standalone solution; very slow
def EvDiv1(k):
	i = k
	while True:
		z = 0
		for j in range(2, k+1):
			z += i % j
		if z == 0:
			return i
		i += k
	return k

# This is a fast function; it uses Prime Numbers and logarithms
def EvDiv2(k):
	N = 1
	check = True
	limit = math.sqrt(k)
	p = getPrimeNumbers(k)
	i = 0
	while i < len(p):
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

# This is the fastest function
def EvDiv3(k):
	res = 1
	primes = getPrimeNumbers(k)
	for _, val in enumerate(primes):
		mul=0
		mul = val
		while mul <= k:
			mul *= val
		res = res * mul / val
	return int(res)



print(CheckTime(EvDiv1,20))
print(CheckTime(EvDiv2,20))
print(CheckTime(EvDiv3,20))
