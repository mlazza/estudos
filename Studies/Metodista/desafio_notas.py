# -*- coding: utf-8 -*-
"""
Disciplina de Algoritmos

@aluno: Marlon Lazzarotti
"""

def calcula_menor(notas):
    return min(notas)

def calcula_maior(notas):
    return max(notas)    

notas = []
condicao = True

while condicao:
    x = (int(input('Digite a nota [-1 para encerrar]: ')))
    
    if x == -1:
        condicao = False
    else:
        notas.append(x)

print('A menor nota foi: {}'.format(calcula_menor(notas)))

print('\n')

print('A maior nota foi: {}'.format(calcula_maior(notas)))