def maior_primo(num):

	i = 1
	quant_divisores = 0
	max = 0
	aux = 1

	while (num > 1):

		dois = num % 2
		tres = num % 3
		cinco = num % 5

		if(dois != 0 and tres != 0 and cinco != 0):
			return num
		num -= 1

	return max

digito = int(input("Digite um número maior ou igual a 2: "))

if(digito < 2):
	digito = int(input("Digite um número maior ou igual a 2: "))

print(maior_primo(digito))