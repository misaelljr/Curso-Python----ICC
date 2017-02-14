import math
 
def is_Hipotenusa(k):
    cat_1 = 1
    cat_2 = 1
    isHipotenusa = False
    while cat_1 <= k:
        while cat_2 <= k:
            s = cat_1 ** 2 + cat_2 ** 2
            hip = math.sqrt(s)
            cat_2 = cat_2 + 1
            
            if hip == k:
                isHipotenusa = True
        cat_2 = 1
        cat_1 = cat_1 + 1
 
    return isHipotenusa
 
def soma_hipotenusas(n):
    i = 1
    soma = 0
    while i <= n:
        if is_Hipotenusa(i) == True:
            print(i)
            soma = soma + i
        i = i + 1
    return soma
 
numero = int(input("Digite um numero: "))
 
print(soma_hipotenusas(numero))