# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:41:10 2020

A simple dice simulator 

Um simulador simples de dado (portuguese)

@author: Marlon Lazzarotti
"""

import random
import PySimpleGUI as sg


class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.msg = 'Do you like to play the dice?'
        #layout
        self.layout = [
            [sg.Text('Play the Dice?')],
            [sg.Button('yes'), sg.Button('no')]
                
        ]
        

        
    def Start(self):
        #create a window
        self.screen = sg.Window('Dice Simulator',self.layout)
        #read the values on the screen
        self.events, self.values = self.screen.Read()
        #do something with the values
        while True:
            try:               
                if self.events == 'yes' or self.events == 's':
                    self.PlayDice()
                elif self.events == 'no' or self.events == 'n':
                    print('Thank you and good bye!')
                else:
                    print('Please, answer with "yes" or "no".')
            except:
                print('There is a error with your input.')
            
    def PlayDice(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()
simulator.Start()
