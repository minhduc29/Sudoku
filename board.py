from cube import Cube

class Board:
    """Class to manage the main board of the game"""
    def __init__(self, settings):
        """Initialize sudoku board"""
        self.rows = settings.rows
        self.cols = settings.cols
        self.width = settings.window_width
        self.height = settings.window_height
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]
        self.model = None
        self.selected = None

    def update_model(self):
        """Update model"""
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]