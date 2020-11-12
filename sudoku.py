import pygame
import sys
from settings import Settings

class Sudoku:
    """Overall class to manage the game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Sudoku")

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            pass

if __name__ == '__main__':
    s = Sudoku()
    s.run_game()