def cria_matriz(num_linha, num_coluna):
	
	matriz = []

	for i in range(num_linha):
		linha = []
		for j in range(num_coluna):
			valor = int(input("Digite o elemento ["+ str(i) + "]["+ str(j) + "]: "))
			linha.append(valor)

		matriz.append(linha)

	return matriz

def print_matriz(matriz):

	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			print (matriz[i][j])

def lermatriz():
	lin = int(input("Digite o número de linhas da matriz: "))
	col = int(input("Digite o número de colunas da matriz: "))
	
	return print_matriz(cria_matriz(lin, col))

print(lermatriz())