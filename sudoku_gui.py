"""
The sudoku GUI class

Author: Robert Zhang
02/23/2020
"""
from tkinter import *
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from solver import sudoku_board
from time import sleep

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
        """
        Constructor class of sudoku GUI

        :param parent: The super class, Tkinter frame
        :param game: the game class with the sudoku board
        """
        self.game = game
        self.board = game.board
        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = -1, -1
        self.__initUI()

    def __initUI(self):
        """
        Initialize the GUI helper function

        :return:
        """
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

        new_game = Button(self, text="New Game", command=self.__new_game)
        new_game.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws the grid of the GUI

        :return:
        """
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
        """
        Solve the answer calls the board GUI to solve and print out the solution

        :return:
        """
        self.__clear_answers()
        self.solve_helper()
        # self.game.solve_sudoku()
        # self.__draw_puzzle()

    def solve_helper(self):
        [row, col] = self.game.find_empty()
        if row == -1 and col == -1:
            # Sudoku is solved
            return True

        for i in range(1, 10):
            # sleep(0.5)
            self.game.board[row][col] = i
            self.__draw_puzzle()
            self.canvas.update()
            if not self.game.valid():
                self.game.board[row][col] = 0
                self.__draw_puzzle()
                self.canvas.update()
                continue
            if self.solve_helper():
                return True
            else:
                self.game.board[row][col] = 0
                self.__draw_puzzle()
                self.canvas.update()
        return False



    def __clear_answers(self):
        """
        Clear the answer function

        :return:
        """
        self.game.reset()
        # self.canvas.delete("victory")
        self.__draw_puzzle()

    def __draw_puzzle(self):
        """
        Draw puzzle method draws a new puzzle

        :return:
        """
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
        """
        Check the answers

        :return:
        """
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
        """
        The cell clicked finds the index of the row, col of where it's clicked

        :param event: the event clicker location
        :return:
        """
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
        """
        The key pressed function registers the value of the key

        :param event: the event of key pressed event
        :return:
        """
        key = event.char
        if self.row >= 0 and self.col >= 0 and key in "123456789":
            self.game.board[self.row][self.col] = int(key)
            self.__draw_puzzle()

    def __new_game(self):
        """
        Generates a random new game for the GUI
        :return:
        """
        # Initiates a new sudoku game
        self.game = sudoku_board()
        # self.__initUI()
        self.__draw_puzzle()
