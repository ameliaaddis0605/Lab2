"""
Match Coin Game 
Amelia Addis
This program is an interactive coin toss game.
09-29-2026
"""

import random 

class Coin:
    def __init__(self):
        self.__sideup = "Heads"
        
    def toss(self):
        number = random.randint(0,1)
        
        
        if number == 0:
           self.__sideup ="Heads"

        else:
            self.__sideup = "Tails" 
            
    def get_sideup(self):
        return self.__sideup 