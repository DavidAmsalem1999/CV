from basics import (
    Move
)
from typing import(
    Optional,
    Union
)

class Res():
    move:Move
    win:bool
    def __init__(self, _win:Optional[bool]=None, _move:Optional[Move]=None):
        self.move = _move
        self.win = _win

class Player():
    
    name:str
    last_move:Res
    moves:list[Res]
    score:int

    def __init__(self, name:Optional[str]=None):
        self.score = 0
        if not name ==None:
            print("Hey, what is your name?")
            self.name = input().capitalize()
        else:
            self.name = "Bot"

    def win(self):
        self.score +=1