import math
# ponto A
x1 = int(input("Ponto Ax: "))
y1 = int(input("Ponto Ay: "))
# ponto B
x2 = int(input("Ponto Bx: "))
y2 = int(input("Ponto By: "))

d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

if d >= 10:
	print("longe")
else:
	print("perto")
