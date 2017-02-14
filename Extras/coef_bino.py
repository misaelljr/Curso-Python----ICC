def fatorial (n):
	fat = 1

	while (n >= 1):
		fat *= n
		n -= 1

	return fat

def coef_bino(n, k):

	return fatorial(n) / (fatorial(k)*fatorial(n-k))

print(coef_bino(5, 3))