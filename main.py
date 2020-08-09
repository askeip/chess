import sys
import pieces as p
import chessboard as c
import choices as ch
import move as m
import show as s


def main():
    move = (p.Color.White, p.Color.Black)
    turn = 0
    color = ch.choose_color()
    enemy = ch.choose_enemy(color)
    width = 8
    height = 8
    chessboard = c.Chessboard(width,height)
    while True:
        hits, king_pos = chessboard.fill_hits(move[turn % 2])
        s.drawBoard(width,height,chessboard)
        if not hits[king_pos[0]][king_pos[1]]:
            stalemate = chessboard.stalemate(move[turn % 2])
            if stalemate:
                s.show_note("STALEMATE")
                break
        else:
            game_over = chessboard.checkmate(king_pos, hits)
            if game_over:
                s.show_note("GAME OVER")
                break
            else:
                s.show_note("CHECK!")
        if enemy is not None and color != move[turn % 2]:
            turn += enemy.move(chessboard)
        else:
            x, y, = s.interruption()
            new_x, new_y = s.interruption()
            turn += m.make_move(chessboard, x, y, new_x, new_y, move[turn % 2])


if __name__ == '__main__':
    main()
