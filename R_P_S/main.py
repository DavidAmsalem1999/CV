from data import *
from basics import (
    Turn,
    Winner,
)
from entities import(
    Player,
)
class Play():
    _user:Player
    _bot:Player
    def __init__(self):
        self._bot = Player()
        self._user = Player("user")
        print(f"Hey {self._user.name} let's play Rock Paper Scissors\nAre you READY? Y/n")
        self.delay()

    def get(self):
        return self._user,self._bot

    def delay(self):
        if not input().upper() == "Y":
            print("Press Y when you ready.")
            self.delay()
        else:
            return
    

if __name__ == "__main__":
    user,bot = Play().get()
    run = True
    while run:
        bot_turn, user_turn = Turn().get()
        winner = Winner(bot_turn,user_turn)
        if winner.res == "bot":
            bot.win()
            print(f"{user.name} lost")
        elif winner.res == user:
            user.win()
            print(f"{user.name} WON")
        else:
            print("Draw")
        print("Should We Play Again? Y/n")
        if not input().upper() == "Y":
            run = False
            print("Come again sometime :) ")