import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)

from the_game_ui import Ui_TicTacToe

class Window(QMainWindow, Ui_TicTacToe):

    def _getTurnSign(self):
        signs = 'OX'
        return signs[self.currentTurn]
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.currentTurn = 0
        self.moveCount = 0
        self.setupUi(self)
        self.pushButton11.clicked.connect(self.on_11_clicked)
        self.pushButton12.clicked.connect(self.on_12_clicked)
        self.pushButton13.clicked.connect(self.on_13_clicked)
        self.pushButton21.clicked.connect(self.on_21_clicked)
        self.pushButton22.clicked.connect(self.on_22_clicked)
        self.pushButton23.clicked.connect(self.on_23_clicked)
        self.pushButton31.clicked.connect(self.on_31_clicked)
        self.pushButton32.clicked.connect(self.on_32_clicked)
        self.pushButton33.clicked.connect(self.on_33_clicked)
    
    def check_status(self):
        board=[
            [
                self.pushButton11.text(),
                self.pushButton12.text(),
                self.pushButton13.text()
            ],
            [
                self.pushButton21.text(),
                self.pushButton22.text(),
                self.pushButton23.text()
            ],
            [
                self.pushButton31.text(),
                self.pushButton32.text(),
                self.pushButton33.text()
            ],
        ]
        for i in range(3):
            if board[i][0] != '' and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                Window.show_messagebox('Finish', f'{board[i][0]} won the game.', QMessageBox.Information)
                exit()
        for i in range(3):
            if board[0][i] != '' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                Window.show_messagebox('Finish', f'{board[0][i]} won the game.', QMessageBox.Information)
                exit()
        if board[0][0] != '' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            Window.show_messagebox('Finish', f'{board[0][0]} won the game.', QMessageBox.Information)
            exit()
        if board[0][2] != '' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            Window.show_messagebox('Finish', f'{board[0][2]} won the game.', QMessageBox.Information)
            exit()
        if self.moveCount == 9:
            Window.show_messagebox('Finish', 'Draw', QMessageBox.Information)
            exit()
    
    def change_board(self, cell):
        cell.setText(self._getTurnSign())
        self.currentTurn = 1 - self.currentTurn
        cell.setEnabled(False)
        self.moveCount += 1
        self.check_status()

    def on_11_clicked(self):
        self.change_board(self.pushButton11)

    def on_12_clicked(self):
        self.change_board(self.pushButton12)

    def on_13_clicked(self):
        self.change_board(self.pushButton13)

    def on_21_clicked(self):
        self.change_board(self.pushButton21)

    def on_22_clicked(self):
        self.change_board(self.pushButton22)

    def on_23_clicked(self):
        self.change_board(self.pushButton23)

    def on_31_clicked(self):
        self.change_board(self.pushButton31)

    def on_32_clicked(self):
        self.change_board(self.pushButton32)

    def on_33_clicked(self):
        self.change_board(self.pushButton33)

    @staticmethod
    def show_messagebox(title, text, icon, buttons = QMessageBox.Ok): 
        msg = QMessageBox() 
        msg.setIcon(icon) 
        msg.setText(text) 
        msg.setWindowTitle(title) 
        msg.setStandardButtons(buttons) 
        return msg.exec_() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())