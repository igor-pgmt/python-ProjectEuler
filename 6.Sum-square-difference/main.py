# https: // projecteuler.net/problem = 6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(k):
    result = 0
    for i in range(1, k+1):
        result+=i**2
    return result

def squareOfSum(k):
    result = 0
    for i in range(1, k+1):
        result += i
    return result**2

def diff1(k):
    return squareOfSum(k) - sumOfSquares(k)

# One-liner:
def diff2(k):
	return sum(range(1, k+1)) ** 2 - sum([i ** 2 for i in range(1, k+1)])

print(diff1(10), diff1(100))
print(diff2(10), diff2(100))
