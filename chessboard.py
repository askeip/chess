import pieces as p
import randoms as r
from enum import Enum

class Move_type(Enum):
    Impossible = 0
    Classic = 1
    Castling_long = 2
    Castling_short = 3
    En_passant = 4


class Chessboard:
    def __init__(self,width,height):
        self.chessboard = [[] for i in range(width)]
        for i in range(width):
            for j in range(height):
                self.chessboard[i].append(None)
        self._create_new_chessboard(0, 1, p.Color.Black)
        self._create_new_chessboard(height - 1, height - 2, p.Color.White)

    def _create_new_chessboard(self,first_row, second_row, color):
        for (i, piece) in enumerate((p.Rook, p.Knight,p.Bishop,p.Queen,p.King,p.Bishop,p.Knight,p.Rook)):
            self.chessboard[i][first_row] = piece(color)
            self.chessboard[i][second_row] = p.Pawn(color)

    def fill_hits(self, color, flag=False):
        king_pos = (0, 0)
        width = len(self.chessboard)
        height = len(self.chessboard[width - 1])
        hits = [[[] for i in range(width)] for j in range(height)]
        for i in range(width):
            for j in range(height):
                if self.chessboard[i][j]:
                    if flag and self.chessboard[i][j].color == color:
                        continue
                    if isinstance(self.chessboard[i][j], p.King):
                        if self.chessboard[i][j].color == color:
                            king_pos = (i, j)
                    self.chessboard[i][j].check(i, j, self)
                    for hit in self.chessboard[i][j].moves:
                        hits[hit[0]][hit[1]].append((i, j, self.chessboard[i][j].Worth, self.chessboard[i][j].color))
        return hits, king_pos

    def update_enpassant(self,color):
        width = len(self.chessboard)
        height = len(self.chessboard[width - 1])
        for i in range(width):
            for j in range(height):
                if self.chessboard[i][j] and self.chessboard[i][j].color == color:
                    if isinstance(self.chessboard[i][j], p.Pawn):
                        self.chessboard[i][j].long_move = False

    def try_move(self,x, y, new_x, new_y):
        result = self.chessboard[x][y].move(x, y, new_x, new_y, self)
        if not result:
            return Move_type.Impossible
        move_type = Move_type.Classic
        if isinstance(result, p.King) and abs(x - new_x) == 2 and y == new_y:
            if x > new_x:
                self.chessboard[x - 1][y] = self.chessboard[new_x - 2][y]
                self.chessboard[new_x - 2][y] = None
                move_type = Move_type.Castling_long
            elif x < new_x:
                self.chessboard[x + 1][y] = self.chessboard[new_x + 1][y]
                self.chessboard[new_x + 1][y] = None
                move_type = Move_type.Castling_short
        elif isinstance(result, p.Pawn) and abs(x - new_x) == 1 and not self.chessboard[new_x][new_y]:
            pawn_reserve = self.chessboard[new_x][y]
            self.chessboard[new_x][y] = None
            move_type = Move_type.En_passant
        reserve = self.chessboard[new_x][new_y]
        self.chessboard[x][y] = None
        self.chessboard[new_x][new_y] = result
        hits, king_pos = self.fill_hits(result.color)
        if move_type == Move_type.Castling_long:
            self.chessboard[new_x - 2][y] = self.chessboard[x - 1][y]
            self.chessboard[x - 1][y] = None
        elif move_type == Move_type.Castling_short:
            self.chessboard[new_x + 1][y] = self.chessboard[x + 1][y]
            self.chessboard[x + 1][y] = None
        elif move_type == Move_type.En_passant:
            self.chessboard[new_x][y] = pawn_reserve
        if len(hits[king_pos[0]][king_pos[1]]) > 0:
            move_type = None
        self.chessboard[x][y] = result
        self.chessboard[new_x][new_y] = reserve
        self.fill_hits(result.color)
        return move_type

    def checkmate(self,king_pos, hits):
        num = 0
        sign = [1, 1]
        interval = list(range(8))
        clr = self.chessboard[king_pos[0]][king_pos[1]].color
        possible_move = None
        #print(hits[king_pos[0]][king_pos[1]])
        for hit in hits[king_pos[0]][king_pos[1]]:
            if not isinstance(self.chessboard[hit[0]][hit[1]], p.Knight):
                for i in range(2):
                    if king_pos[i] - hit[i] < 0:
                        sign[i] = -1
                    elif hit[i] == king_pos[i]:
                        num = (i + 1) % 2
                        sign[i] = 0
                    else:
                        sign[i] = 1
                for i in range(abs(king_pos[num] - hit[num]) + 1):
                    if i * sign[0] + hit[0] in (interval) and i * sign[1] + hit[1] in (interval):
                        for trying in hits[i * sign[0] + hit[0]][i * sign[1] + hit[1]]:
                            if clr in trying:
                                possible_move = self.try_move(trying[0], trying[1], i*sign[0] + hit[0], i*sign[1] + hit[1])
                                if possible_move and possible_move != Move_type.Impossible:
                                    return False
            else:
                for trying in hits[hit[0]][hit[1]]:
                    if clr in trying:
                        possible_move = self.try_move(trying[0], trying[1], hit[0], hit[1])
                        if possible_move and possible_move != Move_type.Impossible:
                            return False
            if possible_move and possible_move != Move_type.Impossible:
                return False
        if not possible_move or possible_move == Move_type.Impossible:
            #print(king_pos)
            #print(self.chessboard[king_pos[0]][king_pos[1]].moves)
            for king_move in self.chessboard[king_pos[0]][king_pos[1]].moves:
                result = self.chessboard[king_pos[0]][king_pos[1]].move(king_pos[0], king_pos[1], king_move[0],
                                                                        king_move[1],self)
                if not result:
                    continue
                reserve = self.chessboard[king_move[0]][king_move[1]]
                self.chessboard[king_pos[0]][king_pos[1]] = None
                self.chessboard[king_move[0]][king_move[1]] = result
                hits, king_p = self.fill_hits(result.color)
                self.chessboard[king_pos[0]][king_pos[1]] = result
                self.chessboard[king_move[0]][king_move[1]] = reserve
                if not hits[king_p[0]][king_p[1]]:
                    self.chessboard[king_pos[0]][king_pos[1]].check(king_pos[0],king_pos[1],self)
                    return False
        else:
            return False
        return True

    def stalemate(self, color):
        width = len(self.chessboard)
        height = len(self.chessboard[width - 1])
        for x in range(width):
            for y in range(height):
                if self.chessboard[x][y] and self.chessboard[x][y].color == color:
                    move, move_try = r.random_move((x, y), self)
                    if move is not Move_type.Impossible:
                        return False
        return True