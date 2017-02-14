numero = 1
list = []

while (numero != 0):
	numero = int(input("Digite um número: "))
	if numero != 0:
		list.append(numero)

cont = len(list) - 1

while (cont >= 0):
	print(list[cont])
	cont -= 1

