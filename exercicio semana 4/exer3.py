num = int(input("Digite um número inteiro: "))

soma = 0 
new_valor = num 

while (new_valor > 0): 
	digito = new_valor%10 
	soma += digito
	new_valor = int(new_valor/10) 

print (soma)