def soma_elementos(lista):
	soma = 0
	cont = len(lista) - 1

	while (cont >=0):
		soma = soma + lista[cont]
		cont -= 1

	return soma

numero = 1
lista = []
while (numero != 0):
	numero = int(input("Digite os números para a lista: "))
	if numero != 0:
		lista.append(numero)

print("Lista: ", lista)

print("Soma dos elementos da lista: ", soma_elementos(lista))