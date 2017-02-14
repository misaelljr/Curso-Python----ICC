import re

def le_assinatura():

	print("Bem-vindo ao detector automático de COH-PIAH.")

	wal = float(input("Entre o tamanho medio de palavra:"))
	ttr = float(input("Entre a relação Type-Token:"))
	hlr = float(input("Entre a Razão Hapax Legomana:"))
	sal = float(input("Entre o tamanho médio de sentença:"))
	sac = float(input("Entre a complexidade média da sentença:"))
	pal = float(input("Entre o tamanho medio de frase:"))

	return [wal, ttr, hlr, sal, sac, pal]

'''Funções auxiliares'''

def le_textos():
	i = 1
	textos = []
	texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
	while texto:
		textos.append(texto)
		i += 1
		texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

	return textos

def separa_sentencas(texto):

	sentencas = re.split(r'[.!?]+', texto)

	if sentencas[-1] == '':
		del sentencas[-1]

	return sentencas

def separa_frases(sentenca):

	return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):

	return frase.split()

def n_palavras_unicas(lista_palavras):

	freq = dict()
	unicas = 0

	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			if freq[p] == 1:
				unicas -= 1
			freq[p] += 1
		else:
			freq[p] = 1
			unicas += 1

	return unicas

def n_palavras_diferentes(lista_palavras):
	freq = dict()

	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			freq[p] += 1
		else:
			freq[p] = 1

	return len(freq)

def soma_quant_caract(lista_palavras):
	quant_caract = 0

	for x in lista_palavras:
		#p = x.lower()
		quant_caract += len(x)

	return quant_caract

def extrair_palavras(textos):
	lista_sentencas = []
	lista_frases = []
	lista_palavras = []

	lista_sentencas = separa_sentencas(textos) 

	for x in lista_sentencas:
		lista_frases += separa_frases(x)

	for x in lista_frases:
		lista_palavras += separa_palavras(x)

	return lista_palavras

def extrair_frases(texto):    
	sentencas = separa_sentencas(texto)  
	frases = []    
	for sentenca in sentencas:        
		frases += separa_frases(sentenca)      
	return frases 
	
''' Funções estatísticas '''

def tam_med_palavra (textos):

	'''lista_sentencas = []
	lista_frases = []
	lista_palavras = []

	for x in textos:
		lista_sentencas += separa_sentencas(x)

	print(lista_sentencas) 

	for x in lista_sentencas:
		lista_frases += separa_frases(x)

	for x in lista_frases:
		lista_palavras += separa_palavras(x)


	quant_palavra = len(lista_palavras)
	quant_caracteres = soma_quant_caract(lista_palavras)

	tam_medio = quant_caracteres/quant_palavra'''

	lista_palavras = extrair_palavras(textos)

	quant_palavra = len(lista_palavras)
	quant_caracteres = soma_quant_caract(lista_palavras)

	tam_medio = quant_caracteres/quant_palavra

	return tam_medio

def type_token(texto):

	lista_palavras = extrair_palavras(texto)
	quant_palavra_dif = n_palavras_diferentes(lista_palavras)
	total_palavras = len(lista_palavras)

	return quant_palavra_dif/total_palavras

def hapax_legomana(texto):

	lista_palavras = extrair_palavras(texto)
	quant_palavras_unicas = n_palavras_unicas(lista_palavras)
	total_palavras = len(lista_palavras)

	return quant_palavras_unicas/total_palavras

def tam_med_sentenca(texto): 

	sentencas = separa_sentencas(texto) 
	lista_palavras = extrair_palavras(texto)  
	count = 0
	for palavra in lista_palavras:        
		count += len(palavra)      
		tms = count/len(sentencas)

	return tms

def cpx_sentenca(texto):

	quant_frases = len(extrair_frases(texto))
	sentencas = separa_sentencas(texto)

	return quant_frases / len(sentencas)

def tam_med_frases(texto):
	
	frases = extrair_frases(texto)
	soma_carac = 0

	for x in frases:
		p = x.lower()
		soma_carac += len(p)

	return soma_carac / len(frases)


''' Funções comparativas '''


def compara_assinatura(as_a, as_b):
	cal_ass = 0

	for x,y in zip(as_a,as_b):
		cal_ass += abs((x - y))
	
	return cal_ass/6


def calcula_assinatura(texto):

	wal = tam_med_palavra(texto)
	ttr = type_token(texto)
	hlr = hapax_legomana(texto)
	sal = tam_med_sentenca(texto)
	sac = cpx_sentenca(texto)
	pal = tam_med_frases(texto)

	return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):

	ass_texto = 0  
	cont = 0
	menor = 10000000000

	for x in textos:
		ass_texto = calcula_assinatura(x)
		ass_result = compara_assinatura(ass_texto,ass_cp)
		if(ass_result < menor):
			menor = ass_result
			cont = textos.index(x)

	return cont


''' Execução '''

ass_cp = le_assinatura()
#ass_cp = [4.79,0.72,0.56,80.5,2.5,31.6]
#ass = [4.35,0.58,0.35,69.75,2.0,42.56]

textos = le_textos()

result_ass = avalia_textos(textos, ass_cp)

print("O autor do texto", result_ass+1, "está infectado com COH-PIAH")

'''textos = ["Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."]

#textos = le_textos()

lista_sentencas = []
lista_frases = []
lista_palavras = []

for x in textos:
	lista_sentencas += separa_sentencas(x) 

for x in lista_sentencas:
	lista_frases += separa_frases(x)

for x in lista_frases:
	lista_palavras += separa_palavras(x)

for x in textos:
 	print(tam_med_palavra(x))'''
 




