num = int(input("Digite um número natural: "))

if num >= 0:
	fat = 1

for i in range(1, num+1):
	fat *=i

print(fat)
