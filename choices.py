import show as s
import pieces as p
import bot as b
from enum import Enum
import sys


def choose_enemy(color):
    while True:
        print('Wanna play vs Player or Bot? Press 0 for Player,1 for Bot')
        choice = input(sys.argv)
        if choice[0] == '0':
            return None
        elif choice[0] == '1':
            if color == p.Color.White:
                return b.EzBot(p.Color.Black)
            else:
                return b.EzBot(p.Color.White)
        else:
            continue


def choose_color():
    while True:
        print("Choose color:0 - White,1 - Black")
        choice = input(sys.argv)
        if choice[0] == '0':
            return p.Color.White
        elif choice[0] == '1':
            return p.Color.Black
        else:
            continue