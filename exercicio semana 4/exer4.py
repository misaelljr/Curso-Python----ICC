num = int(input("Digite um número inteiro: "))

aux = num // 10

digitoAnterior = aux % 10
digitoAtual = num % 10

temAdjacentes = False

while aux > 0 and not temAdjacentes:
	if (digitoAtual == digitoAnterior):
		temAdjacentes = True
	print(digitoAnterior)
	print(digitoAtual)
	aux = aux // 10
	digitoAtual = aux % 10

if (temAdjacentes):
	print("sim");
else:
	print("não");
