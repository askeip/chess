import chessboard as c
import pieces as p
import show as s
import sys

def make_move(chessboard, x, y, new_x, new_y, color):
    if chessboard.chessboard[x][y]:
        if chessboard.chessboard[x][y].color == color:
            result = chessboard.try_move(x, y, new_x, new_y)
            if result == None:
                s.show_note("CHECK!")
                return 0
            if result == c.Move_type.Impossible:
                s.show_note("Impossible move")
                return 0
            elif result == c.Move_type.Castling_short:
                chessboard.chessboard[x + 1][y] = chessboard.chessboard[new_x + 1][y]
                chessboard.chessboard[new_x + 1][y] = None
            elif result == c.Move_type.Castling_long:
                chessboard.chessboard[x - 1][y] = chessboard.chessboard[new_x - 2][y]
                chessboard.chessboard[new_x - 2][y] = None
            elif result == c.Move_type.En_passant:
                chessboard.chessboard[new_x][y] = None
            if isinstance(chessboard.chessboard[x][y], p.Pawn) and (new_y == 0 or new_y == 7):
                pieces = [p.Queen(color), p.Rook(color), p.Bishop(color), p.Knight(color)]
                note = "Choose piece:from {}".format(pieces)
                #s.show_note(note)
                while True:
                    s.show_note(note)
                    choice = input(sys.argv)
                    try:
                        chessboard.chessboard[new_x][new_y] = pieces[int(choice[0])]
                        chessboard.chessboard[x][y] = None
                        break
                    except:
                        note = "Incorrect choice,try again"
                        continue
            else:
                if isinstance(chessboard.chessboard[x][y], p.Pawn) or isinstance(chessboard.chessboard[x][y], p.King) \
                        or isinstance(chessboard.chessboard[x][y], p.Rook):
                    chessboard.chessboard[x][y].moved = 1
                chessboard.chessboard[new_x][new_y] = chessboard.chessboard[x][y]
                chessboard.chessboard[x][y] = None
            return 1
        else:
            s.show_note("NOT YOUR TURN!")
        return 0
    else:
        s.show_note("ITS NOT CHESSMAN")
    return 0