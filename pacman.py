import pygame

class Pacman:
    def __init__(self, game):
        self.x = 0
        self.y = 300
        self.speed = (0, 0)
        self.draw(game)

    def set_move(self, dir):
        if dir == "right":
            self.speed = (5,0)
        if dir == "left":
            self.speed = (-5,0)
        if dir == "up":
            self.speed = (0, -5)
        if dir == "down":
            self.speed = (0, 5)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def draw(self, game):
        self.rect = pygame.draw.circle(game.window, (255, 255, 0), (self.x, self.y), 20)