import math
import time

def getPrimeNumbers(num):
	primeNumbers = [1, 2, 3, 5, 7]
	endings = [1, 3, 7, 9]
	currentNum = 0
	i = 1
	while len(primeNumbers) < num:
		for ending in endings:
			currentNum = ConcatINT(i, ending)
			if shortCheckPrimeNumbers(currentNum, primeNumbers):
				primeNumbers.append(currentNum)
				if len(primeNumbers) >= num:
					break
		i+=1
	return primeNumbers


def shortCheckPrimeNumbers(num, primes):
	sqrt = math.sqrt(num)
	i = 2
	while primes[i] <= sqrt:
		if num%primes[i]==0:
			return False
		i += 1
	return True

def ConcatINT(a,b):
	lenB = len(str(b))
	exp = 10**lenB
	return exp*a + b

def CheckTime(f, num):
	start = time.time()
	f(num)
	return time.time()-start
