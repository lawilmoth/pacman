import pygame
from spritesheet import SpriteSheet

class Pacman:
    FRAME_RATE =5
    
    def __init__(self, game):
        sprite_sheet = SpriteSheet("images\pacman.png")
        self.x = 0
        self.y = 300
        self.speed = (0, 0)
        self.frame_count = 3
        self.sprites_right = sprite_sheet.get_images(457, 0, 15,  15, self.frame_count)
        self.sprites_left = sprite_sheet.get_images(457, 15, 15,  15, self.frame_count)

        self.sprites = self.sprites_right
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.blit(game)
        self.count = 0

    def set_move(self, dir):
        if dir == "right":
            self.speed = (5,0)
            self.sprites = self.sprites_right
        if dir == "left":
            self.speed = (-5,0)
            self.sprites = self.sprites_left
        if dir == "up":
            self.speed = (0, -5)
        if dir == "down":
            self.speed = (0, 5)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def update(self):
        self.count += 1
        if self.count % self.FRAME_RATE == 0:
            self.current_sprite = (self.current_sprite + 1)%self.frame_count
            self.image = self.sprites[self.current_sprite]
        
        self.image = self.sprites[self.current_sprite]
        
        print(self.current_sprite)

    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
        