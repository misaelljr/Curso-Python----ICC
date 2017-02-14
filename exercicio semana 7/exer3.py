def maior_elemento(lista):
	maior = lista[len(lista)-1]
	cont = len(lista)-1

	while (cont >=0):
		if(lista[cont] >= maior):
			maior = lista[cont]
		cont -= 1

	return maior

numero = 1
lista = []
while (numero != 0):
	numero = int(input("Digite os números para a lista: "))
	if numero != 0:
		lista.append(numero)

print("Lista: ", lista)

print("Maior elemento da lista: ", maior_elemento(lista))