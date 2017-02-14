def imprime_matriz(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])

	for i in range(linhas):
		for j in range(colunas):
			#if(j > 0 and j % (colunas - 1) == 0):
			if(j == colunas -1):
				print("%d" %matriz[i][j], end = "")
			else:
				print("%d" %matriz[i][j], end = " ")
		if(i < linhas -1):
			print()
	print()

	'''for x in minha_matriz:
		cont = 0
		for y in x:
			if (cont > 0):
				print(" ", end = "")
			print (y, end = "")
			cont += 1
			
		print()'''

#minha_matriz = [[1], [2], [3]]
#imprime_matriz(minha_matriz)