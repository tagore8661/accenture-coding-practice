#Write a program to find GCD of two numbers.
def gcd(a, b):

	if (a == 0):
		return b
	if (b == 0):
		return a

	if (a == b):
		return a

	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)

a = 98
b = 56
if(gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
	print('not found')