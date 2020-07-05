#4.13 Buffet - Cinco tipos basicos de comida, pense em 5 pratos e armazene numa tupla
# Use laco for para exibir os pratos
# Tente modificar um dos itens para q o python rejeite
# restaurante muda o cardapio, substituindo dois pratos
# use laco for para ver a alteracao

cardapio = ('Camarão à grega', 'Filet ao molho mignon', 'Lasanha di Bernardi',
            'Risoto Funghi', 'Pizza de Milho')

print("Cardápio: ")
for prato in cardapio:
	print("\t" + prato)

#cardapio[4] = 'Pizza de Calabresa'

cardapio = ('Camarão à grega', 'Filé ao cavalo', 'Lasanha di Bernardi',      
            'Risoto Funghi', 'Pizza de Bacon')

print("\nNovo cardápio: ")
for prato in cardapio:
	print("\t" + prato)