import pygame
from consumable import Consumable
from spritesheet import SpriteSheet

class Map:
    """A tool for building maps"""
    GAP = 24
    INTIIAL_X_GAP = 11
    INTIIAL_Y_GAP = 11
    def __init__(self):
        self.bg_image = SpriteSheet("images\pacman.png").get_image(0, 0, 228, 250)
        # 0 = empty space
        # 1 = pellet
        # 2 = big pellet
        # 3 = wall
        self.map_grid = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 2, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 2, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [0, 0, 0, 0, 0, 3, 1, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 1, 3, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0],
            ]
        for row in self.map_grid:
            print(row)


    def load_map(self, game):
        for i, row in enumerate(self.map_grid):
            for j, item in enumerate(row):
                
                if item == 1:
                    cons = Consumable(
                        game, 
                        j*self.GAP + self.INTIIAL_X_GAP, 
                        i*self.GAP + self.INTIIAL_Y_GAP, 
                        4, 
                        (255, 255, 255)
                        )
                    game.consumables.add(cons)
                if item == 2:
                    cons = Consumable(
                        game, 
                        j*self.GAP + self.INTIIAL_X_GAP, 
                        i*self.GAP + self.INTIIAL_Y_GAP, 
                        15, 
                        (255, 255, 255)
                        )
                    game.consumables.add(cons)
                if item == 3:
                    wall = Wall(
                        game, 
                        j*self.GAP + self.INTIIAL_X_GAP, 
                        i*self.GAP + self.INTIIAL_Y_GAP, 
                        1,
                        1, 
                        (0, 0, 255)
                        )
                    game.walls.add(wall)

        print(len(game.consumables.sprites()))
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()


    def draw(self):
        pygame.draw.rect(self.game.window, self.color, self.rect)

