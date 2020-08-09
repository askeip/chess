import sys

def interruption():
    move = input(sys.argv)
    x = int(move[0])
    y = int(move[1])
    return x, y

def drawBoard(width,height,chessboard):
    x_line = "  0  1  2  3  4  5  6  7"
    for column in range(width):
        print(column, end=' ')
        for raw in range(height):
            if not chessboard.chessboard[raw][column]:
                print("__", end=' ')
            else:
                print(chessboard.chessboard[raw][column], end=' ')
        print()
    print(x_line)

def show_note(note):
    print(note)