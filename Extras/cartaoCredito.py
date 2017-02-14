meuCartão = int(input("Digite o numero do seu cartão de crédito: "))

encontreiMeuCartão = False
prox_cartão = 1

while prox_cartão != 0 and not encontreiMeuCartão:
	prox_cartão = int(input("Digite o numero do próximo cartão de crédito: "))

	if prox_cartão == meuCartão:
		encontreiMeuCartão = True

if encontreiMeuCartão:
	print("Eba!! Encontrei o meu cartão :-) ")
else:
	print("Xii!! Não encontrei o meu cartão :-( ")