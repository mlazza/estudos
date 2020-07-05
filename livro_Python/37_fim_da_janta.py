#3.7 Lista de convidados alterada - menos convites

convidados = ['Machado de Assis', 'Rochelle Kazapi', 'Michael Jackson']

print("Convite de janta para " + convidados[0])
print("Convite de janta para " + convidados[1])
print("Convite de janta para " + convidados[2])

conv_desmarc = convidados.pop()
print(conv_desmarc + " não poderá participar mais.")

convidados.append('Dona Florinda')

print("Convite de janta para " + convidados[0])
print("Convite de janta para " + convidados[1])
print("Convite de janta para " + convidados[2])

print("Encontramos mais lugares, mais convidados virão!")

convidados.insert(0, 'Donald Trump')
convidados.insert(2, 'Regina Casé')
convidados.append('Tony Stark')

print("Convite de janta para " + convidados[0])
print("Convite de janta para " + convidados[1])
print("Convite de janta para " + convidados[2])
print("Convite de janta para " + convidados[3])
print("Convite de janta para " + convidados[4])
print("Convite de janta para " + convidados[5])

print("Infelizmente apenas duas ficarão, desculpe galerinha!")

removido = convidados.pop()
print("Desculpe, " + removido + ", mas tem gente mais importante que você na lista.")
removido = convidados.pop()
print("Desculpe, " + removido + ", mas tem gente mais importante que você na lista.")
removido = convidados.pop(0)
print("Desculpe, " + removido + ", mas tem gente mais importante que você na lista.")
removido = convidados.pop(1)
print("Desculpe, " + removido + ", mas tem gente mais importante que você na lista.")

print("\n" + convidados[0] + " e " + convidados[1] + ", vocês continuma na janta, ok?!")

del convidados[1]
del convidados[0]

print(convidados)