# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:45:03 2020

@author: lazza

SUDOKU - CHALLENGE

OBJETIVO: Criar o jogo Sudoku, e criar um solver para ele.

No Sudoku o rearranjo dos números também é o mesmo, só que a regra é que só se 
deve preencher com números de 1 a 9 sem que eles se repitam nem na vertical, 
nem na horizontal e nem nos quadrados de 3x3. 
"""

def Creating_problem(): # creating an example of sudoku game


    problem = [
            [7, 8, 0],
            [6, 0, 0],
            [0, 0, 0],
        ]
    
    return problem


def Visualizing_board_reset():
    
    margin = '|'
    spaces = '  '
    
    #creating a small example with 9 cubes
    cols = 3
    rows = 3
    
    for i in range(1, 15):
        if i % 5 != 0:
            print(margin, spaces, end='')
        else:
            print('\n')
            
def Visualizing_board_numbers(problem):
    
    margin = '|'
    space = ' '
    
    #creating a small example with 9 cubes
    cols = 3
    rows = 3
    
    for i, j in zip(range(0, 8), range(0, 8)):
        if i % 5 != 0:
            print(margin, problem[i][j], end='')
        else:
            print('\n')

first_ex = Creating_problem()
problem
Visualizing_board_numbers(first_ex)





