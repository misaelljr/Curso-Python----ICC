def soma_matrizes(m1, m2):
	matriz_soma = []

	if(verifica_dimensoes(m1, m2)):

		quant_linhas = len(m1)
		quant_colunas = len(m1[0])

		for i in range(quant_linhas):
			matriz_soma.append([])
			for j in range(quant_colunas):
				soma = m1[i][j] + m2[i][j]
				matriz_soma[i].append(soma)

		return matriz_soma
	else:
		return False

def verifica_dimensoes(m1, m2):
	quant_linhas_m1 = len(m1)
	quant_colunas_m1 = len(m1[0])

	quant_linhas_m2 = len(m2)
	quant_colunas_m2 = len(m2[0])

	if(quant_linhas_m1 == quant_linhas_m2 and quant_colunas_m1 == quant_colunas_m2):
		return True
	else:
		return False

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))