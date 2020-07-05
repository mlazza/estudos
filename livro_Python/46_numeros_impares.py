#4.6 Números ímpares - use o terceiro argumento da função range() para
# criar uma lista de numeros impares de 1 a 20. Utilize laco for para exibir

impares = []

for impar in range(1,20,2):
	impares.append(impar)

for impar in impares:
	print(impar)