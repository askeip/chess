from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QColor,QPainter,QBrush, QIcon, QFont, QCursor, QImage
from PyQt5.QtCore import Qt,QRect
import sys
import pieces as p
import chessboard as c
import choices as ch
import move as m
import bot as b
from os.path import *

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.isActive = True
        self.frameWidth = 50
        self.frameHeight = 50
        self.width = 8
        self.height = 8
        self.setGeometry(100,100,self.frameWidth * self.width,self.frameHeight * self.height)
        self.setWindowTitle('Chess')
        self.enemy = None
        self.color = p.Color.White
        self.init_buttons()
        self.qc =   QtChessboard(self.color,self.enemy,self)
        self.show()

    def init_buttons(self):
        standart_button_size = (self.frameWidth * 3,self.frameHeight * 1.2)
        buttons_folder = "images/Buttons/"
        self.continue_button = Button(join(buttons_folder,"continue.png"),self._continue,
                        (self.frameWidth * 2.5, self.frameHeight * 1.5),standart_button_size,self)
        self.play_vs_friend = Button(join(buttons_folder,"play_vs_friend.png"),self._play_vs_friend,
                        (self.frameWidth * 2.5,self.frameHeight * 2.8), standart_button_size, self)
        #self.play_vs_friend_button = Button(buttons_folder + "play_vs_friend.png",self._play_vs_bot,
        #                (self.frameWidth * 2.5,self.frameHeight * 2.8), standart_button_size, self)
        self.new_game_button = Button(join(buttons_folder,"new_game.png"),self._start_game,
                        (self.frameWidth * 2.5,self.frameHeight * 4.1),standart_button_size, self)
        self.exit_button = Button(join(buttons_folder,"exit.png"),self._exit_func,
                        (self.frameWidth * 2.5,self.frameHeight * 5.4),standart_button_size, self)
        self.white_button = Button(join(buttons_folder,"white.png"),self._white,
                        (self.frameWidth * 2.5,self.frameHeight * 2.8),standart_button_size, self)
        self.black_button = Button(join(buttons_folder,"black.png"),self._black,
                        (self.frameWidth * 2.5,self.frameHeight * 4.1),standart_button_size, self)
        self.close_all_buttons()
        #self.show_start_menu()

    def close_all_buttons(self):
        self.continue_button.close()
        self.play_vs_friend.close()
        self.new_game_button.close()
        self.exit_button.close()
        self.white_button.close()
        self.black_button.close()

    def _exit_func(self):
        exit()

    def show_start_menu(self):
        if self.qc:
            self.continue_button.show()
        else:
            self.continue_button.close()
        self.play_vs_friend.show()
        self.new_game_button.show()
        self.white_button.close()
        self.black_button.close()
        self.exit_button.show()

    def _continue(self):
        self.isActive = not self.isActive
        self.qc.isActive = not self.isActive
        self.qc.show()

    def _play_vs_friend(self):
        self.color = p.Color.White
        self.enemy = None
        self._start()

    def _start(self):
        self.qc = QtChessboard(self.color,self.enemy,self)
        self.isActive = not self.isActive
        self.qc.isActive = not self.isActive
        self.qc.show()

    def _start_game(self):
        self.play_vs_friend.close()
        self.new_game_button.close()
        self.white_button.show()
        self.black_button.show()
        self.exit_button.show()

    def _white(self):
        self.color = p.Color.White
        self.enemy = b.EzBot(p.Color.Black)
        self.white_button.close()
        self.black_button.close()
        self._start()

    def _black(self):
        self.white_button.close()
        self.color = p.Color.Black
        self.enemy = b.EzBot(p.Color.White)
        self.black_button.close()
        self._start()

    def mousePressEvent(self, e):
        self.isActive = not self.isActive
        self.qc.isActive = not self.isActive
        if self.qc.isActive:
            self.qc.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape and self.qc != None:
            self.isActive = not self.isActive
            self.qc.isActive = not self.isActive
            if self.isActive:
                self.qc.close()
                self.show_start_menu()
                self.show()
            else:
                self.qc.show()
            self.repaint()

class QtChessboard(QWidget):
    def __init__(self,color,enemy,parent):
        super().__init__()
        self.setParent(parent)
        self.initUI(color,enemy)

    def initUI(self,color,enemy):
        self.isActive = True
        self.move = (p.Color.White, p.Color.Black)
        self.picked_piece = (-1,-1)
        self.turn = 0
        self.menu = False
        self.game_over = False
        self.color = color#ch.choose_color()
        self.enemy = enemy#ch.choose_enemy(self.color)
        self.width = self.parent().width
        self.height = self.parent().height
        self.chessboard = c.Chessboard(self.width,self.height)
        if isinstance(self.enemy, b.Bot) and self.move[self.turn%2] == self.enemy.color:
            self.chessboard.fill_hits(self.move[self.turn%2])
            self.turn += self.enemy.move(self.chessboard)
            self.moveDone()
        self.frameWidth = self.parent().frameWidth
        self.frameHeight = self.parent().frameHeight
        #self.setWindowIcon(QIcon('mda.png'))

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        colors = (QColor(215,190,91),QColor(79,36,2))
        other_colors = (QColor(200,200,200),QColor(25,25,25))
        #(self.getContentsMargins()[2] - self.getContentsMargins()[0]) / self.width
        #(self.getContentsMargins()[1] - self.getContentsMargins()[3]) / self.height
        for column in range(self.width):
            for raw in range(self.height):
                qp.setBrush(colors[(column + raw) % 2])
                qp.drawRect(column * self.frameWidth,raw * self.frameHeight,self.frameWidth,self.frameHeight)
        if self.picked_piece[0] != -1:
            for cell in self.chessboard.chessboard[self.picked_piece[0]][self.picked_piece[1]].moves:
                raw = cell[0] if self.color == p.Color.White else 7 - cell[0]
                column = cell[1] if self.color == p.Color.White else 7 - cell[1]
                qp.setBrush(other_colors[(raw + column) % 2])
                qp.drawRect(raw * self.frameWidth,column * self.frameHeight,self.frameWidth,self.frameHeight)
        for column in range(self.width):
            rl_column = column if self.color == p.Color.White else 7 - column
            for raw in range(self.height):
                rl_raw = raw if self.color == p.Color.White else 7 - raw
                if self.chessboard.chessboard[raw][column]:
                    piece = QImage(join("images/Pieces/",str(self.chessboard.chessboard[raw][column])))\
                        .scaled(self.frameWidth,self.frameHeight)
                    qp.drawImage(rl_raw * self.frameHeight,rl_column * self.frameWidth,piece)
        self.show()

    def mousePressEvent(self, e):
        if not self.isActive:
            return
        if e.buttons() == Qt.LeftButton and not self.isGameOver():
            if self.enemy:
                if self.move[self.turn%2] == self.enemy.color:
                    return
            pos = ((QCursor.pos().x() - self.parent().geometry().x())//self.frameWidth,
                   ((QCursor.pos().y() - self.parent().geometry().y())//self.frameHeight))
            self.move_piece(pos)
            if self.game_over:
                return
            if isinstance(self.enemy, b.Bot) and self.move[self.turn%2] == self.enemy.color:
                self.turn += self.enemy.move(self.chessboard)
                self.moveDone()
                self.isGameOver()

    def move_piece(self,pos):
        rl_x = pos[0] if self.color == p.Color.White else 7 - pos[0]
        rl_y = pos[1] if self.color == p.Color.White else 7 - pos[1]
        pos = (rl_x,rl_y)
        if self.picked_piece[0] == -1:
            if not self.chessboard.chessboard[pos[0]][pos[1]]:
                return
            if self.chessboard.chessboard[pos[0]][pos[1]].color == self.move[self.turn%2]:
                self.picked_piece = (pos[0],pos[1])
            self.repaint()
        else:
            self.turn += m.make_move(self.chessboard, self.picked_piece[0],
                 self.picked_piece[1], pos[0], pos[1], self.move[self.turn % 2])
            self.picked_piece = (-1,-1)
            self.moveDone()

    def moveDone(self):
        #peshka v ferzi checknut
        self.repaint()
        self.chessboard.update_enpassant(self.move[self.turn%2])
        self.isGameOver()

    def isGameOver(self):
        hits, king_pos = self.chessboard.fill_hits(self.move[self.turn % 2])
        if not hits[king_pos[0]][king_pos[1]]:
            stalemate = self.chessboard.stalemate(self.move[self.turn % 2])
            if stalemate:
                self.show_note("STALEMATE")
                self.game_over = True
        else:
            game_over = self.chessboard.checkmate(king_pos, hits)
            if game_over:
                self.show_note("GAME OVER")
                self.game_over = True
            else:
                self.show_note("CHECK!")
        return self.game_over

    def interruption(self):
        move = input(sys.argv)
        x = int(move[0])
        y = int(move[1])
        return x, y

    def show_note(self,note):
        print(note)

class Button(QPushButton):
    def __init__(self, image_path, function, coordinates, size, parent=None):
        super(QPushButton, self).__init__(parent)
        self.function = function
        self.setGeometry(coordinates[0], coordinates[1], size[0], size[1])
        self.setStyleSheet('border-image: url("%s");' % image_path)
        self.clicked.connect(self._on_click)

    def _on_click(self):
        self.function()

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    #qc = QtChessboard()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()