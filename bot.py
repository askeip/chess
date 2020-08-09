import move as m
import randoms as r
import pieces as p
from abc import ABCMeta, abstractmethod, abstractproperty
from enum import Enum


class Bot_lvl(Enum):
    Stupid = 0
    Medium = 0
    Hard = 0


class Bot():
    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self,chessboard):
        """move piece"""

    @abstractproperty
    def color(self):
        """color"""

class EzBot(Bot):
    def __init__(self,color):
        self.color = color

    def color(self):
        return self.color

    def move(self,chessboard):
        self.pieces = []
        for x in range(len(chessboard.chessboard)):
            for y in range(len(chessboard.chessboard)):
                if chessboard.chessboard[x][y] and chessboard.chessboard[x][y].color == self.color:
                    self.pieces.append((x, y))
        self.make_move(chessboard)
        return self.turn

    def make_move(self,chessboard):
        piece, move, try_move = r.random_piece_move(self.pieces, chessboard)
        self.turn = m.make_move(chessboard, piece[0], piece[1], move[0], move[1], self.color)


class MedBot(Bot):
    def __init__(self,color):
        self.color = color

    def color(self):
        return self.color

    def move(self,chessboard):
        self.pieces = []
        for x in range(len(chessboard.chessboard)):
            for y in range(len(chessboard.chessboard)):
                if chessboard.chessboard[x][y] and chessboard.chessboard[x][y].color == self.color:
                    self.pieces.append((x, y))
        self.make_move(chessboard)
        return self.turn
    pass

    #def make_move(self):



'''
Это еще не работает
class Bot2():
    def __init__(self, mode, color):
        self.mode = mode
        self.color = color

    def move(self, chessboard):
        self.pieces = []
        for x in range(len(chessboard.chessboard)):
            for y in range(len(chessboard.chessboard)):
                if chessboard.chessboard[x][y] and chessboard.chessboard[x][y].color == self.color:#not isinstance(chessboard[x][y], str) and chessboard[x][y].color == self.color:
                    self.pieces.append((x, y))
        if self.mode == Bot_lvl.Stupid:
            self.stupid_bot(chessboard)
        return self.turn


    def check_cost(color, hits, position):
        white_moves = []
        black_moves = []
        worth = 0
        for hit in hits[position[0]][position[1]]:
            if hit[3] == Color.White:
                white_moves.append(hit)
            elif hit[3] == Color.Black:
                black_moves.append(hit)
            else:
                raise Exception("SMTHNG WRONG")
        if white_moves and color == Color.White:
            return -100, None
        elif black_moves and color == Color.Black:
            return -100, None
        white_moves.sort(key=lambda x: x[3])
        black_moves.sort(key=lambda x: x[3])
        count = min(len(black_moves), len(white_moves))
        checking_check = 0
        for check in range(count):
            if color == Color.White:
                while True:
                    hit = (black_moves[check], white_moves[check])
                    check_x = black_moves[check + checking_check][0]
                    check_y = black_moves[check + checking_check][1]
                    result = try_move(check_x, check_y, position[0], position[1])
                    if result == None:
                        checking_check += 1
                    else:
                        break
            else:
                while True:
                    hit = (white_moves[check + checking_check], black_moves[check])
                    check_x = white_moves[check + checking_check][0]
                    check_y = white_moves[check + checking_check][1]
                    result = try_move(check_x, check_y, position[0], position[1])
                    if result == None:
                        checking_check += 1
                    else:
                        break
            worth -= hit[check][0]
            if check < count:
                worth += hit[check][1]
        if color == Color.White:
            if count < len(white_moves) and count != 0:
                worth += black_moves[len(black_moves) - 1]
            return worth, white_moves[0]
        elif color == Color.Black:
            if count < len(black_moves) and count != 0:
                worth += white_moves[len(white_moves) - 1]
            return worth, black_moves[0]
        else:
            raise Exception("WHAT THE HELL IS THIS COLOR?", color)
            return worth, None


if __name__ == '__main__':
    pass'''