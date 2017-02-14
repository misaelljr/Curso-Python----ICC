
numero = int(input("Digite uma sequência de numeros:"))
fat = 1

while (numero >= 0): 
	fat = 1
	while numero > 1:
		fat *= (numero)
		numero -= 1
	print(fat)
	numero = int(input("Digite uma sequência de numeros:"))
	