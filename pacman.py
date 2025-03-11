import pygame

class Pacman:
    def __init__(self, game):
        self.x = 0
        self.y = 300
        self.speed = 5
        self.rect = pygame.draw.circle(game.window, (255, 255, 0), (self.x, self.y), 10)

    def move(self, dir):
        self.x += self.speed

    def draw(self, game):
        self.rect = pygame.draw.circle(game.window, (255, 255, 0), (self.x, self.y), 10)