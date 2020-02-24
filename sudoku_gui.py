"""
The sudoku GUI class

"""
from tkinter import *
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from solver import sudoku_board

MARGIN = 20  # margin of the board
SIDE = 50  # each cell side length
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # The width and height of the board

class sudoku_gui(Frame):
    """
    Object Oriented Class Sudoku GUI
    main functions:
    /clear to original
    /solve the puzzle
    /mouse click + key board press

    """
    def __init__(self, parent, game):
        self.game = game
        self.board = game.board
        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = -1, -1
        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, heigh=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        solve_button = Button(self, text="Solve Sudoku", command=self.__solve_answers)
        solve_button.pack(fill=BOTH, side=BOTTOM)

        check_answer = Button(self, text="Check Answer", command=self.__check_answers)
        check_answer.pack(fill=BOTH, side=BOTTOM)

        new_game = Button(self, text="New Game", command=self.__new_game())
        new_game.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        for i in range(10):
            color = "black" if i % 3 == 0 else "lightgray"
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __solve_answers(self):
        self.__clear_answers()
        self.game.solve_sudoku()
        self.__draw_puzzle()

    def __clear_answers(self):
        self.game.reset()
        # self.canvas.delete("victory")
        self.__draw_puzzle()

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.board[i][j]
                if answer != 0:
                    row = MARGIN + j * SIDE + SIDE / 2
                    col = MARGIN + i * SIDE + SIDE / 2
                    self.canvas.create_text(
                        row, col, text=answer, tags="numbers", fill="pink"
                    )

    def __check_answers(self):
        window = Tk()
        window.title("Results")
        if self.game.find_empty() == [-1, -1] and self.game.valid():
            lbl = Label(window, text="Congrats! You solved the sudoku! :)))")
            lbl.grid(column=30, row=0)
            window.geometry('400x80')
            window.mainloop()
        else:
            lbl = Label(window, text="Wrong Solution! Keep trying! :')")
            lbl.grid(column=30, row=0)
            window.geometry('400x80')
            window.mainloop()

    def __cell_clicked(self, event):
        x, y = event.x, event.y

        if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            self.canvas.focus_set()
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
            if row == self.row and col == self.col:
                # The current box is selected
                self.row, self.col = -1, -1
            elif self.game.start_board[row][col] == 0:
                self.row, self.col = row, col
        # delete previous click
        self.canvas.delete("cursor")

        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="purple1", tags="cursor"
            )

    def __key_pressed(self, event):
        key = event.char
        if self.row >= 0 and self.col >= 0 and key in "123456789":
            self.game.board[self.row][self.col] = int(key)
            self.__draw_puzzle()

    def __new_game(self):
        # Initiates a new sudoku game
        self.game = sudoku_board()
        self.__draw_puzzle()
