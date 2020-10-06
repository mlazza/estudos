"""
METODISTA
Ciência de Dados e Big Data
Disciplina: Algoritmos
Acadêmico: Marlon Augusto Lazzarotti
2 fase

Atividade Avaliativa (aula 1)
Crie um arquivo e escreva os códigos abaixo, em seguida salve o arquivo e poste na tarefa. 
"""

# a) Faça um Programa que leia dois números quaisquer, e escreva o maior deles.  

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

if a > b:
	print('O numero {} é maior do que {}'.format(a, b))
elif a < b:
	print('O numero {} é menor do que {}'.format(a, b))
else:
	print('Os numeros digitados são iguais')




# b) Faça um Programa que leia um número inteiro. Informar se o número é “PAR” ou “ÍMPAR”. 

x = int(input('Digite um numero:'))

if x % 2 == 0:
	print('O numero digitado é par')
else:
	print('O numero digitado é impar')