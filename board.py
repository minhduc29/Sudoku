import pygame
from puzzles import choose_board, is_valid_sudoku
from cube import Cube
from solver import is_valid, solve

class Board:
    """Class to manage the main board of the game"""
    def __init__(self, settings):
        """Initialize sudoku board"""
        self.rows = settings.rows
        self.cols = settings.cols
        self.width = settings.window_width
        self.height = settings.window_width
        self.board = choose_board()
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]
        self.model = None
        self.selected = None

    def update_model(self):
        """Update model"""
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def draw_grid(self, window, settings):
        """Draw grid lines"""
        size = self.width / self.rows

        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(window, settings.black, (0, i * size), (self.width, i * size), thick)
            pygame.draw.line(window, settings.black, (i * size, 0), (i * size, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw_cube(window)

    def place_num(self, value):
        """Check validation of a number to place in the board"""
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_value(value)
            self.update_model()

            if is_valid(self.model, value, (row, col)) and solve(self.model):
                return True
            elif is_valid_sudoku(self.model):
                return True
            else:
                self.cubes[row][col].set_value(0)
                self.cubes[row][col].set_temporary(0)
                self.update_model()
                return False

    def sketch(self, value):
        """Sketch the temporary value for the board"""
        row, col = self.selected
        self.cubes[row][col].set_temporary(value)

    def select(self, row, col):
        """Select the cube to place the number"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        """Clear the cube"""
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temporary(0)
        else:
            self.cubes[row][col].set_value(0)

    def click(self, pos):
        """Record click event of the player"""
        if pos[0] < self.width and pos[1] < self.height:
            size = self.width / self.rows
            x = pos[1] // size
            y = pos[0] // size
            return (int(x), int(y))
        else:
            return None

    def is_completed(self):
        """Check if the board is completed"""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False

        return True