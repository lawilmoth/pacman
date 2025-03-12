import pygame
from consumable import Consumable
class Map:
    """A tool for building maps"""
    GAP = 10
    def __init__(self):
        self.pellets = [
            [0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
                        ]
    def load_map(self, game):
        for i, row in enumerate(self.pellets):
            for j, item in enumerate(row):
                print(f"({i}, {j}): {item}")
                cons = Consumable(game, i, j, 5, (255, 255, 255))
                game.consumables.add(cons)

