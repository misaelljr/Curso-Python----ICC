def sao_multiplicaveis(m1, m2):
	
	quant_linhas = len(m2)
	quant_colunas = len(m1[0])

	if(quant_colunas == quant_linhas):
		return True
	else:
		return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(sao_multiplicaveis(m1,m2))
