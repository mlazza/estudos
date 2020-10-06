#3.8 Cinco lugares do mundo que você gostaria de visitar
#armazene em uma lista, sem ordem alfabética
#Exiba a lista
#Utilize sorted() para exibir em ordem alfabética, sem modifica-la
#Mostre a lista original
#Utilize sorted() para exibir sua lista em ord. alf. inversa sem altera-la
#Mostre a lista original
#Utilize reverse() para mudar a ordem da lista. Exiba-a
#Utilize reverse() para mudar a ordem novamente. Exiba-a e veja que voltou ao original
#Utilize sort() para mudar a lista de modo que ela seja armazenada em ord. alf.
#Utilize sort() para mudar a lista para que seja armazenada em ord. alf. inversa

lugares = ['Buenos Aires', 'Bologna', 'Roma', 'Boston', 'Calgary']
print(lugares)

print(sorted(lugares))
print(lugares)

print(sorted(lugares, reverse=True))
print(lugares)

lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)

lugares.sort()
print(lugares)

lugares.sort(reverse=True)
print(lugares)
