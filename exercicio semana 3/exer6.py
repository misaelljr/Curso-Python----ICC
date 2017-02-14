n1 = int(input ("Digite o numero1: "))
n2 = int(input ("Digite o numero2: "))
n3 = int(input ("Digite o numero3: "))

if (n1 <= n2 and n1 <= n3 and n2 >= n1 and n2 <= n3 and n3 >= n1 and n3 >= n2):
	print("crescente")
else:
	print("não está em ordem crescente")