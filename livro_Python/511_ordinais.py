#5.11 Numeros Ordinais. Indicam sua posicao numa lista:
#Armazene os numeros de 1 a 9 numa lista
#Percorra a lista com laco
#Use if-elif-else no laco para exibir a terminacao apropriada p os ordinais, tipo 1st, 2nd, etc
#e cada resultado deve estar numa lista separada

numeros = list(range(1,10))
print(type(numeros))

for n in numeros:
	print(n)

ordinais = []

for n in numeros:
	if n == 1:
		ord1 = str(n) + "st"
		ordinais.append(ord1)

	elif n == 2:
		ord2 = str(n) + "nd"
		ordinais.append(ord2)

	elif n == 3:
		ord3 = str(n) + "rd"
		ordinais.append(ord3)

	else:
		ordinais.append(str(n) + "th")

for n in ordinais:
	print(n)


