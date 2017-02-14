def is_primo(x):
    
    dois = x % 2
    tres = x % 3
    cinco = x % 5
        
    if(dois != 0 and tres != 0 and cinco != 0):
        return True
    if(x == 2 or x == 3 or x == 5):
        return True
    return False

def n_primos(numero):
    cont = 2
    n_primo = 0
    while cont <= numero:
        if(is_primo(cont)):
            n_primo = n_primo + 1

        cont = cont + 1

    return n_primo 
    
numero = 0
while True:
    numero = int(input("Digite um numero: "))
    if(numero >= 2):
        break
        
print(n_primos(numero))