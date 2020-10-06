#3.5 Lista de convidados alterada

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
