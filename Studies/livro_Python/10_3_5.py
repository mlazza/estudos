#10.3
'''
filename = 'guest.txt'
name = input('Digite o seu nome:')

with open(filename, 'w') as file_object:
    file_object.write(name)
'''
#10.4
'''
cond = True
filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while cond:
        n = input('Digite o seu nome:')
        print("Olá, ", n)
        file_object.write(n + '\n')
        c = input("Continuar o programa? s-sim / n-não")
        if c == 'n':
            cond = 0
'''
#10.5

cond = True
filename = 'quiz.txt'

with open(filename, 'w') as file_object:
    while cond:
        n = input('Explique o porque que você gosta de programar.')
        file_object.write(n + '\n')
        c = input("Continuar o programa? s-sim / n-não")
        if c == 'n':
            cond = 0
