# a random function: to generate rock, paper, or scissors. 
# valid function: to check the validity of the move.
# result function: to declare the winner of the round.
# scorekeeper: to keep track of the score

from typing import (
    Union,
    Optional
)
import os
import random

class Move():
    class Rock():
        def __init__(self):
            self._print = None
        
        @property
        def print(self):
            if not self._print:
                return "Rock"
            return
    class Paper():
        def __init__(self):
            self._print = None
        
        @property
        def print(self):
            if not self._print:
                return "Paper"
            return
    class Scissors():
        def __init__(self):
            self._print = None
        
        @property
        def print(self):
            if not self._print:
                return "Scissors"

class Turn():
    def __init__(self):
        self.bot = self.get_guess()
        self.usr = self.user_input()

        print("User choice ",self.usr().print, "\t bot choice ", self.bot().print)
    
    def get(self):
        return self.bot,self.usr

    def get_guess(self):
        obj = Move()
        options = [obj.Paper, obj.Rock, obj.Scissors]
        return random.choices(options, weights=(35.4,29.4,35),k=1)[0]
        # return random.choice(options)
        
    def user_input(self):
        print("R for Rock, P for Paper, S for Scissors")
        user = input().upper()
        return Move.Paper if user == "P" else Move.Rock if user == "R" else Move.Scissors if user == "S" else self.wrong_input()

    def wrong_input(self):
        print("Wrong Input")
        return self.user_input()

class Winner():
    m = Union[Move.Paper,Move.Scissors,Move.Rock]
    
    r = Move.Rock()
    p = Move.Paper()
    s = Move.Scissors()

    res:str
    def __init__(self, user:m, bot:m):
        if user == bot:
            self.draw()
        elif user == self.r and bot == self.s or user == self.p and bot == self.r or user == self.s and bot == self.p:
            self.user_win()
        else:
            self.bot_win()
            
    def user_win(self):
        self.res = "user"
    def bot_win(self):
        self.res = "bot"
    def draw(self):
        self.res = "Draw"





if __name__ == "__main__":
    play = True
    # user  = Player()
    while play:
        Turn()
        print("Again? Y/n")
        if not input().upper() == "Y":
            play = False
            print("Come again sometime :) ")
        
        