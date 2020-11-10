# 10.1 Aprendendo Python. Escreva um programa que leia o arquivo e mostre o que você escreveu, três vezes. Exiba o conteudo uma vez lendo o arquivo todo, uma vez percorrendo o
# objeto arquivo com um laço e outra armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with.

with open('texto.txt') as file_object:
    contents = file_object.read()
    print(contents.strip().replace('Python', 'Fortran'))

filename = 'texto.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'Java'))

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C++'))

# 10.2 Aprendendo C: voce pode usar o metodo replace() para substituir qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rapido que mostra
# como substituir a palvra 'dog' por 'cat' em uma frase:
# >>message = "I really like dogs."
# >>message.replace('dog', 'cat')
# 'I really like cats.'
# Leia cada linha do arquivo de texto que voce acabou de criar e substitua a palavra Python pelo nome de outra linguagem. Mostre cada linha modificada na tela.

for line in lines:
    print(line.replace('Python', 'C++'))



