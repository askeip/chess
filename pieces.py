from enum import Enum
import chessboard as c


class Color(Enum):
    White = 0
    Black = 1


class Bishop:
    Worth = 300

    def __init__(self, color):
        self.color = color
        self.moves = []

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard)
        if (new_x, new_y) in self.moves:
            return self
        return None

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "B"

    def check(self, x, y, chessboard):
        self.moves = []
        for i in range(0, 4):
            changed_x = x
            changed_y = y
            (check_x, check_y) = ((1, 1), (1, -1), (-1, -1), (-1, 1))[i - 1]
            for j in range(0, 8):
                position = (changed_x + check_x, changed_y + check_y)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    break
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                    break
                self.moves.append(position)
                changed_x = position[0]
                changed_y = position[1]


class Rook:
    Worth = 400

    def __init__(self, color):
        self.color = color
        self.moves = []
        self.moved = 0

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard)
        if (new_x, new_y) in self.moves:
            return self
        return None

    def check(self, x, y, chessboard):
        self.moves = []
        for i in range(0, 4):
            changed_x = x
            changed_y = y
            (check_x, check_y) = ((0, 1), (0, -1), (1, 0), (-1, 0))[i - 1]
            for j in range(0, 8):
                position = (changed_x + check_x, changed_y + check_y)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    break
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                    break
                self.moves.append(position)
                changed_x = position[0]
                changed_y = position[1]

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "R"


class Knight:
    Worth = 200

    def __init__(self, color):
        self.color = color
        self.moves = []

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard)
        if (new_x, new_y) in self.moves:
            return self
        return None

    def check(self, x, y, chessboard):
        self.moves = []
        for i in range(0, 4):
            (check_x, check_y) = ((1, 2), (1, -2), (-1, 2), (-1, -2))[i - 1]
            for j in range(0, 2):
                position = (x + check_x, y + check_y)
                if j == 1:
                    position = (x + check_y, y + check_x)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    continue
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                if not chessboard.chessboard[position[0]][position[1]]:
                    self.moves.append(position)

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "N"


class Queen:
    Worth = 500

    def __init__(self, color):
        self.color = color
        self.moves = []

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard)
        if (new_x, new_y) in self.moves:
            return self
        return None

    def check(self, x, y, chessboard):
        self.moves = []
        for i in range(0, 4):
            changed_x = x
            changed_y = y
            (check_x, check_y) = ((1, 1), (1, -1), (-1, -1), (-1, 1))[i - 1]
            for j in range(0, 8):
                position = (changed_x + check_x, changed_y + check_y)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    break
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                    break
                self.moves.append(position)
                changed_x = position[0]
                changed_y = position[1]
        for i in range(0, 4):
            changed_x = x
            changed_y = y
            (check_x, check_y) = ((0, 1), (0, -1), (1, 0), (-1, 0))[i - 1]
            for j in range(0, 8):
                position = (changed_x + check_x, changed_y + check_y)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    break
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                    break
                self.moves.append(position)
                changed_x = position[0]
                changed_y = position[1]

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "Q"


class King:
    Worth = 800

    def __init__(self, color):
        self.color = color
        self.moves = []
        self.moved = 0

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard, True)
        if (new_x, new_y) in self.moves:
            return self
        return None

    def check(self, x, y, chessboard, flag=False):
        self.moves = []
        for i in range(0, 3):
            for j in range(0, 3):
                position = (x + i - 1, y + j - 1)
                if position[0] < 0 or position[1] < 0 or position[0] > 7 or position[1] > 7:
                    continue
                if chessboard.chessboard[position[0]][position[1]]:
                    if chessboard.chessboard[position[0]][position[1]].color != self.color:
                        self.moves.append(position)
                else:
                    self.moves.append(position)
        if flag and self.moved == 0:
            if isinstance(chessboard.chessboard[x + 3][y], Rook) and chessboard.chessboard[x + 3][y].moved == 0:
                hits, k_pos = chessboard.fill_hits(self.color, True)
                if not hits[x][y] and not chessboard.chessboard[x + 1][y] and not hits[x + 1][y]\
                        and not chessboard.chessboard[x + 2][y] and not hits[x + 2][y]:
                    self.moves.append((x + 2, y))
            if isinstance(chessboard.chessboard[x - 4][y], Rook) and chessboard.chessboard[x - 4][y].moved == 0:
                hits, k_pos = chessboard.fill_hits(self.color, True)
                if not hits[x][y] and not chessboard.chessboard[x - 1][y] and not hits[x - 1][y] \
                        and not chessboard.chessboard[x - 2][y] and not hits[x - 2][y]:
                    self.moves.append((x - 2, y))

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "K"


class Pawn:
    Worth = 100

    def __init__(self, color):
        self.color = color
        self.moved = 0
        self.moves = []
        self.long_move = False
        #self.pos_x = -1

    def move(self, x, y, new_x, new_y, chessboard):
        self.check(x, y, chessboard)
        if (new_x, new_y) in self.moves:
            '''if new_x - 1 >= 0 and isinstance(chessboard.chessboard[new_x - 1][new_y], Pawn)\
                    and chessboard.chessboard[new_x - 1][new_y].color != self.color:
                chessboard.chessboard[new_x - 1][new_y].pos_x = new_x
            if new_x + 1 < 8 and isinstance(chessboard.chessboard[new_x + 1][new_y], Pawn)\
                    and chessboard.chessboard[new_x + 1][new_y].color != self.color:
                chessboard.chessboard[new_x + 1][new_y].pos_x = new_x
            self.pos_x = -1'''
            if abs(y - new_y) == 2:
                self.long_move = True
            return self
        return None

    def check(self, x, y, chessboard):
        self.moves = []
        clr = 1
        if self.color == Color.White:
            clr = -1
        for i in range(0, 2):
            j = (-1, 1)[i]
            if x + j >= 0 and x + j < 8 and chessboard.chessboard[x + j][y + clr]\
                    and chessboard.chessboard[x + j][y + clr].color != self.color:
                self.moves.append((x + j, y + clr))
        if not chessboard.chessboard[x][y + clr]:
            self.moves.append((x, y + clr))
            if self.moved == 0 and not chessboard.chessboard[x][y + 2 * clr]:
                self.moves.append((x, y + 2 * clr))
        for i in range(0, 2):
            j = (-1, 1)[i]
            if x + j >= 0 and x + j < 8 and isinstance(chessboard.chessboard[x + j][y], Pawn)\
                    and chessboard.chessboard[x + j][y].color != self.color\
                    and chessboard.chessboard[x + j][y].long_move:
                        self.moves.append((x + j, y + clr))
        #if self.pos_x != -1:
        #    self.moves.append((self.pos_x, y + clr))

    def __str__(self):
        colors = ("W", "B")
        return colors[self.color.value] + "P"


if __name__ == '__main__':
    pass
