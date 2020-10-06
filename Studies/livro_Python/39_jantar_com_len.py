#3.9 Pegando o programa do jantar e usando len() para exibir uma mensagem do
#numero de pessoas que voce esta convidando para o jantar

convidados = ['Machado de Assis', 'Rochelle Kazapi', 'Michael Jackson']

print("Convite de janta para " + convidados[0])
print("Convite de janta para " + convidados[1])
print("Convite de janta para " + convidados[2])

print("\nNumero de convidados: " + str(len(convidados)) + "\n")

conv_desmarc = convidados.pop()
print(conv_desmarc + " não poderá participar mais.")

convidados.append('Dona Florinda')

print("Convite de janta para " + convidados[0])
print("Convite de janta para " + convidados[1])
print("Convite de janta para " + convidados[2])

print("\nNumero de convidados: " + str(len(convidados)) + "\n")

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

print("\nNumero de convidados: " + str(len(convidados)) + "\n")

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

print("\nNumero de convidados: " + str(len(convidados)) + "\n")

del convidados[1]
del convidados[0]

print(convidados)

print("\nNumero de convidados: " + str(len(convidados)) + "\n")