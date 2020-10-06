#4.11 Minhas pizzas, suas pizzas. Comece com o prog 4.1 p. 97
# faça uma copia da lista de pizzas e chame-a de friend_pizzas
# adicione uma nova pizza a lista original
# adicione uma nova pizza a lista dos amigos
# prove que vc tem duas listas diferentes
# exiba no laco for as duas listas

my_pizzas = ['Frango', 'Coração', 'Marguerita']
friend_pizzas = my_pizzas[:]

friend_pizzas.append('Califórnia')
my_pizzas.append('Chocolate com sorvete')

print("Meus sabores prediletos: ")
for pizza in my_pizzas:
	print("\t" + pizza)

print("Os sabores prediletos do meu amigo: ")
for pizza in friend_pizzas:
	print("\t" + pizza)

