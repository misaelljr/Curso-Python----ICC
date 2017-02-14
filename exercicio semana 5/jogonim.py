def computador_escolhe_jogada(n,m):
	tirar = m
	
	if(tirar > n):
		tirar -= 1

	while(tirar > 0):
		if((n-tirar) % (m+1) == 0):
			return tirar
		else:
			tirar -= 1

def usuario_escolhe_jogada(n, m):
	tirar = int(input("Quantas peças você vai tirar? "))

	while (tirar > m):
		print("Oops! Jogada inválida! Tente de novo.")
		tirar = int(input("Quantas peças você vai tirar? "))

	return tirar

def partida():

	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	if (n % (m+1) == 0):
		print("Voce começa!")
	else:
		print("Computador começa!")

	while (n > 0):
		if (n % (m+1) == 0):
			num_tirar_user = usuario_escolhe_jogada(n,m)
			print("Voce tirou ", num_tirar_user)
			n = n - num_tirar_user
			if (n <= 0):
				print("Fim do jogo! você ganhou ganhou!")
			else:
				print("Agora restam", n, "peças no tabuleiro.")
				num_tirar_root = computador_escolhe_jogada(n,m)
		else:
			num_tirar_root = computador_escolhe_jogada(n,m)
			print("O computador tirou", num_tirar_root, "peça")
			n = n - num_tirar_root
			if (n <= 0):
				print("Fim do jogo! O computador ganhou!")
			else:
				print("Agora restam", n, "peças no tabuleiro.")

def campeonato():
	cont = 1
	while(cont <= 3):
		print("**** Rodada", cont, "****")
		partida()
		cont += 1
	print("**** Final do campeonato! ****")
	print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")
valor = int(input())

while (valor!=1 and valor!=2):
	print("1 - para jogar uma partida isolada")
	print("2 - para jogar um campeonato 2")
	valor = int(input())

if(valor == 1):
	partida()
if(valor == 2):
	campeonato()

	

	






