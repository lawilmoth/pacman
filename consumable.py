import pygame
from pygame.sprite import Sprite

class Consumable(Sprite):
    """A class that makes pacman consumables"""
    def __init__(self, game, x:int , y:int , radius:int , color:tuple):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.game = game
        self.color = color
        self.draw()


    def draw(self):
        """Draws the consumable on the window"""
        self.rect = pygame.draw.circle(self.game.window, self.color, (self.x, self.y), self.radius)


class PowerPellet(Consumable):
    def __init__(self, game, x, y, radius, color):
        super().__init__(game, x, y, radius, color)

    def trigger_ghost_frightened(self):
        for ghost in self.game.ghosts.sprites():
            ghost.set_frightened()
            ghost.frightened_timer = 0