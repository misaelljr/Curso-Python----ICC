def remove_repetidos(lista):
	c = []

	for elemento in lista:
		if(elemento not in c):
			c.append(elemento)
	c.sort()

	return c

numero = 1
lista = []
while (numero != 0):
	numero = int(input("Digite os números para a lista: "))
	if numero != 0:
		lista.append(numero)

print("Lista: ", lista)

print("Lista sem elementos repetidos: ", remove_repetidos(lista))