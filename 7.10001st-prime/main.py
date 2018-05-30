# https: // projecteuler.net/problem = 7
# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

def getPrimeNumber(num):
	primeNumbers = [2, 3, 5, 7]
	endings = [1, 3, 7, 9]
	currentNum = 0
	i = 1
	while len(primeNumbers) <= num:
		def checkPrime():
			for ending in endings:
				currentNum = ConcatINT(i, ending)
				if shortCheckPrimeNumbers(currentNum, primeNumbers):
					primeNumbers.append(currentNum)
					if len(primeNumbers) == num:
						return True
		if checkPrime():
			break
		i += 1
	return primeNumbers[num-1]

def shortCheckPrimeNumbers(num, primes):
	sqrt = math.sqrt(num)
	i = 0
	while primes[i] <= sqrt:
		if num % primes[i] == 0:
			return False
		i += 1
	return True

def ConcatINT(a, b):
	lenB = len(str(b))
	exp = 10**lenB
	return exp*a + b

print(getPrimeNumber(10001))
