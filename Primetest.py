from math import sqrt


def test_prime_function(n):
	theBestPossibleNubmer = int(sqrt(n))
	for possibleDivider in xrange(2,theBestPossibleNubmer + 1):
		if n % possibleDivider == 0:
			return False

	return True
primes = set()
for potential_prime in xrange(2,1001):
	if test_prime_function(potential_prime):
		primes.add(potential_prime)
# def is_prime(n):
	# return n in primes
print primes