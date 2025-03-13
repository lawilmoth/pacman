import pygame
from consumable import Consumable
class Map:
    """A tool for building maps"""
    GAP = 50
    def __init__(self):
        self.pellets = [
            [0, 1, 1, 1, 0,0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1,0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0,0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1,0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0,0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1,0, 1, 1, 1, 0],
                        ]
    def load_map(self, game):
        for i, row in enumerate(self.pellets):
            for j, item in enumerate(row):
                print(f"({i}, {j}): {item}")
                if item == 1:
                    cons = Consumable(game, i*self.GAP, j*self.GAP, 5, (255, 255, 255))
                    game.consumables.add(cons)


class Wall:
    def __init__(self, game, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.game = game
        self.draw()

    def draw(self):
        pygame.draw.rect(self.game.window, self.color, (self.x, self.y, self.width, self.height))