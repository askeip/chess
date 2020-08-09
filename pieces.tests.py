import pieces as p
import chessboard as c
import unittest


def empty_chessboard(width, height):
    chessboard = [[] for i in range(width)]
    for i in range(width):
        for j in range(height):
            chessboard[i].append(None)
    return chessboard


class TestMoves(unittest.TestCase):
    def setUp(self):
        self.chessboard = c.Chessboard(8,8)
        self.chessboard.chessboard = empty_chessboard(8, 8)
        self.chessboard.chessboard[1][4] = p.Pawn(p.Color.White)
        self.chessboard.chessboard[0][4] = p.King(p.Color.White)
        self.chessboard.chessboard[2][5] = p.Pawn(p.Color.Black)
        self.chessboard.chessboard[6][3] = p.Pawn(p.Color.Black)
        self.chessboard.chessboard[4][1] = p.King(p.Color.Black)
        self.chessboard.chessboard[2][1] = p.Pawn(p.Color.Black)
        self.chessboard.chessboard[4][4] = p.Pawn(p.Color.White)
        self.chessboard.chessboard[5][4] = p.Pawn(p.Color.White)
        self.chessboard.chessboard[1][3] = p.Pawn(p.Color.White)
        self.chessboard.chessboard[7][3] = p.Pawn(p.Color.White).pos_x = 6

    def _check_moves(self, piece, x, y, moves_count):
        self.chessboard.chessboard[x][y] = piece
        piece.check(x, y, self.chessboard)
        piece_moves = piece.moves
        self.assertEqual(len(piece_moves), moves_count)

    def testWhiteBishop_CountMoves(self):
        self._check_moves(p.Bishop(p.Color.White), 4, 3, 7)

    def testBlackBishop_CountMoves(self):
        self._check_moves(p.Bishop(p.Color.Black), 4, 3, 6)

    def testWhitePawn_CountMoves(self):
        self._check_moves(p.Pawn(p.Color.White), 4, 3, 1)

    def testBlackPawn_CountMoves(self):
        self._check_moves(p.Pawn(p.Color.Black), 4, 3, 1)

    def testWhiteRook_CountMoves(self):
        self._check_moves(p.Rook(p.Color.White), 3, 3, 11)

    def testBlackRook_CountMoves(self):
        self._check_moves(p.Rook(p.Color.Black), 4, 3, 6)

    def testWhiteKnight_CountMoves(self):
        self._check_moves(p.Knight(p.Color.White), 3, 3, 6)

    def testBlackKnight_CountMoves(self):
        self._check_moves(p.Knight(p.Color.Black), 3, 3, 5)

    def testWhiteQueen(self):
        self._check_moves(p.Queen(p.Color.White), 4, 3, 13)

    def testBlackQueen(self):
        self._check_moves(p.Queen(p.Color.Black), 4, 3, 12)

    def testWhiteKing_CountMoves(self):
        self._check_moves(p.King(p.Color.White), 4, 3, 6)

    def testBlackKing_CountMoves(self):
        self._check_moves(p.King(p.Color.Black), 4, 3, 8)


if __name__ == '__main__':
    unittest.main()