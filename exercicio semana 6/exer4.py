largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
rect = ''
i = 1
j = 1

while i <= altura:
    while j <= largura:
        if(j == 1 or i == 1 or j == largura or i == altura):
            rect += '#'
        else:
            rect += ' '
        j += 1
    if(i != altura and j != largura):
        rect += '\n'
    j = 1
    i += 1
print(rect)
