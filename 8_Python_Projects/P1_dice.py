# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:41:10 2020

A simple dice simulator 

Um simulador simples de dado (portuguese)

@author: Marlon Lazzarotti
"""

import random

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.msg = 'Do you like to play the dice?'
        
    def Start(self):
        response = input(self.msg)
        try:
            if response == 'yes' or response == 's':
                self.PlayDice()
            elif response == 'no' or response == 'n':
                print('Thank you and good bye!')
            else:
                print('Please, answer with "yes" or "no".')
        except:
            print('There is a error with your input.')
            
    def PlayDice(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()
simulator.Start()
