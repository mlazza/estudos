# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:42:05 2020

@author: lazza
"""

# 15 itens para ir para a mochila
# cada item tem um peso e um valor associado
# o peso total preccisa ser <= limite definido
# o valor precisa ser o maior possivel


import random

limite = 30


def Gerador_valores():
    
    lista = []
    for i in range(1, 15):
        lista.append(random.randint(1,5))
    return lista

def Gerador_pesos():
    lista = []
    for i in range(1,15):
        lista.append(random.randint(1, 20))
    return lista

valores = Gerador_valores()
pesos = Gerador_pesos()
final_list = []


for i in range(0, 14):
    final_list.append(valores[i] * pesos[i])
    
print(final_list)
    
