import random
import  chessboard as c


def random_piece_move(pieces, chessboard):
    move = None
    try_move = c.Move_type.Impossible
    piece = None
    while len(pieces) != 0:
        rnd_piece = random.randint(0, len(pieces) - 1)
        piece = pieces.pop(rnd_piece)
        move, try_move = random_move(piece, chessboard)
        if try_move != c.Move_type.Impossible and try_move != None:
            break
    return piece, move, try_move


def random_move(piece, chessboard):
    move = None
    trying_move = c.Move_type.Impossible
    piece_moves = chessboard.chessboard[piece[0]][piece[1]].moves
    while (trying_move == c.Move_type.Impossible or trying_move == None) and len(piece_moves) > 0:
        rnd_move = random.randint(0, len(piece_moves) - 1)
        move = piece_moves.pop(rnd_move)
        trying_move = chessboard.try_move(piece[0], piece[1], move[0], move[1])
    if trying_move != c.Move_type.Impossible and trying_move:
        return move, trying_move
    else:
        return c.Move_type.Impossible, trying_move