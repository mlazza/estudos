#3.6 Lista de convidados alterada - mais convites

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

