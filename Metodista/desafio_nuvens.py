# -*- coding: utf-8 -*-
"""
Disciplina de Algoritmos

Aluno: Marlon Lazzarotti
"""

def pular_nuvens(nuvens):
    saltos = 0
    indice = 0
    while indice < (len(nuvens) - 2):
        if nuvens[indice + 2] != 1:
            saltos += 1 #realiza um salto
            indice += 2 #o salto é realizado para dois indices a frente, pois não é nuvem escura
        else:
            saltos += 1 #realiza o salto
            indice += 1 #o salto é realizado um indice a frente apenas, pois a proxima nuvem seria escura
    return saltos


#caso de teste 1
nuvens = [0,0,1,0,0,1,0]
print(pular_nuvens(nuvens))

#caso de teste 2
nuvens = [0,0,0,0,1,0]
print(pular_nuvens(nuvens))
