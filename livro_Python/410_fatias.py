#4.10 Fatias - Usando um programa q ja escreveu acrescente varias linhas no final que facam:
# exibir os 3 primeiros itens da lista / 3 do meio / e os 3 finais
# use uma fatia para exibi-los

pizzas = ['Frango', 'Coração', 'Marguerita', 'Baiana', 'Calabresa', 'Alho e Óleo', 'Champignon', 'Muzzarela']

#print(pizzas[:3])

print("As três primeiras pizzas:")
for pizza in pizzas[:3]:
	print("\t" + pizza)

print("\nTrês pizzas do meio:")
for pizza in pizzas[2:5]:
	print("\t" + pizza)

print("\nAs três últimas pizzas:")
for pizza in pizzas[-3:]:
	print("\t" + pizza)