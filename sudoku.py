import pygame
import sys
from pygame.locals import *
from time import time
from settings import Settings
from board import Board

class Sudoku:
    """Overall class to manage the game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.window = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Sudoku")

        self.board = Board(self.settings)
        self.key = None
        self.start = time()
        self.tries = 0

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            self.check_events()

            play_time = round(time() - self.start)
            self.settings.redraw_window(self.window, self.board, play_time, self.tries)
            pygame.display.update()

    def check_events(self):
        """Check events for the game"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    self.key = 1
                if event.key == K_2:
                    self.key = 2
                if event.key == K_3:
                    self.key = 3
                if event.key == K_4:
                    self.key = 4
                if event.key == K_5:
                    self.key = 5
                if event.key == K_6:
                    self.key = 6
                if event.key == K_7:
                    self.key = 7
                if event.key == K_8:
                    self.key = 8
                if event.key == K_9:
                    self.key = 9
                if event.key == K_DELETE:
                    self.board.clear()
                    self.key = None
                if event.key == K_RETURN:
                    i, j = self.board.selected
                    if self.board.cubes[i][j].temp != 0:
                        if not self.board.place_num(self.board.cubes[i][j].temp):
                            self.tries += 1
                        self.key = None

                        if self.board.is_completed():
                            pass
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = self.board.click(pos)
                if clicked:
                    self.board.select(clicked[0], clicked[1])
                    self.key = None

        if self.board.selected and self.key != None:
            self.board.sketch(self.key)

if __name__ == '__main__':
    s = Sudoku()
    s.run_game()