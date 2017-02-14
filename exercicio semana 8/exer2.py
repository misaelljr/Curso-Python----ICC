def cria_matriz(num_linha, num_coluna):
	
	matriz = []

	for i in range(num_linha):
		linha = []
		for j in range(num_coluna):
			valor = int(input("Digite o elemento ["+ str(i) + "]["+ str(j) + "]: "))
			linha.append(valor)

		matriz.append(linha)

	return matriz

def dimensoes(matriz):

	print(str(len(matriz))+"X"+str(len(matriz[0])))
	
def lermatriz():
	lin = int(input("Digite o número de linhas da matriz: "))
	col = int(input("Digite o número de colunas da matriz: "))
	
	dimensoes(cria_matriz(lin, col))

lermatriz()