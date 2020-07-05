#4.5 Somando um milhão - crie lista de numeros de 1 a 1 milhao
# em seguida use min() e max() e sum()

lista = []

for num in range(1, 1000001):
	lista.append(num)

print(min(lista))
print(max(lista))
print(sum(lista))

