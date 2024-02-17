import tkinter as tk
from tkinter import messagebox

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[i] for i in win) == 3:
            return "X"
        if sum(zState[i] for i in win) == 3:
            return "O"
    return None

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1
        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, i, j):
        if self.turn == 1:
            if self.xState[i * 3 + j] == 0 and self.zState[i * 3 + j] == 0:
                self.xState[i * 3 + j] = 1
                self.buttons[i][j].config(text="X")
                self.turn = 0
        else:
            if self.xState[i * 3 + j] == 0 and self.zState[i * 3 + j] == 0:
                self.zState[i * 3 + j] = 1
                self.buttons[i][j].config(text="O")
                self.turn = 1

        winner = checkWin(self.xState, self.zState)
        if winner:
            messagebox.showinfo("Winner", f"{winner} wins!")
            self.root.quit()
        elif sum(self.xState) + sum(self.zState) == 9:
            messagebox.showinfo("Draw", "It's a draw!")
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()