"""
The sudoku GUI class

"""
# import tkinter
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM


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
        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__initUI()


    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=500, heigh=530)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)
        solve_button = Button(self, text="Solve Sudoku", command = self.__solve_answers)
        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)


    def __draw_grid(self):
        return 1

    def __solve_answers(self):
        return 1

    def __clear_answers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__draw_puzzle()

    def __draw_puzzle(self):
         return 1

    def __cell_clicked(self):
        return 1

    def __key_pressed(self):
        return 1

