import math

a = int(input("Digite o valor da constante a: "))
b = int(input("Digite o valor da constante b: "))
c = int(input("Digite o valor da constante c: "))

delta = b**2 - 4*a*c

if delta < 0:
	print("esta equação não possui raízes reais")

if (delta == 0):
	x1 = (-b + math.sqrt(delta)) / (2*a)
	print("a raiz desta equação é ", x1)

if delta > 0:
	x1 = (-b + math.sqrt(delta)) / (2*a)
	x2 = (-b - math.sqrt(delta)) / (2*a)

	if x1 > x2:
		x = x2
		y = x1
	print("as raízes da equação são", x ,"e", y)
	