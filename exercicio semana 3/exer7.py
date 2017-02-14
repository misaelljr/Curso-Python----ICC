import math

nx1 = int(input("Ponto x no plano 1: "))
ny1 = int(input("Ponto y no plano 1: "))
nx2 = int(input("Ponto x no plano 2: "))
ny2 = int(input("Ponto y no plano 2: "))

distancia = math.sqrt((nx1 - nx2)**2 + (ny1 - ny2)**2)

if distancia > 10:
	print("longe")
else:
	print("perto")