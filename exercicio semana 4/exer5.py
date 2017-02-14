num = int(input("Digite um número: "))

i = 1
quant_divisores = 0

while(i<=num):
	if(num % i == 0):
		quant_divisores += 1
	i += 1

if(quant_divisores == 2):
	print("primo")
else:
	print("nao primo")