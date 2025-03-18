from pygame.sprite import Sprite
import pygame
from spritesheet import SpriteSheet

class PM_Sprite(Sprite):
    current_frame = 0
    FRAME_RATE = 1
    SPEED = 24
    SIZE = 15

    """A class that makes pacman ghosts"""
    def __init__(self, game, x:int , y:int):
        
        super().__init__()
        self.sprite_sheet = SpriteSheet("images\pacman.png")
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.x = x
        self.y = y

        self.game = game

    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.current_frame += 1
        if self.current_frame % self.FRAME_RATE == 0:
            self.current_sprite = (self.current_sprite + 1)%len(self.sprites)
            self.image = self.sprites[self.current_sprite]
        
        self.image = self.sprites[self.current_sprite]

        self.rect.topleft = (self.x, self.y)

