import pygame
from spritesheet import SpriteSheet
from map import Map
class Pacman(pygame.sprite.Sprite):
    FRAME_RATE = 4
    PACMAN_SIZE = 15
    PACMAN_SPEED = Map.GAP//4
    
    def __init__(self, game):
        super().__init__()
        sprite_sheet = SpriteSheet("images\pacman.png")
        self.x = 300
        self.y = 300
        self.speed = (0, 0)
        self.frame_count = 3

        #Found the frame with the circle
        self.circle_frame = sprite_sheet.get_image(457 + self.PACMAN_SIZE*2 , 0, self.PACMAN_SIZE, self.PACMAN_SIZE)
        self.rect = self.circle_frame.get_rect()

        #Found 2 frames moving right 
        self.sprites_right = sprite_sheet.get_images(457, 0, self.PACMAN_SIZE,  self.PACMAN_SIZE, 2) #Changed to only be 2 frames because one is the circle
        #added the circle
        self.sprites_right.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_left = sprite_sheet.get_images(457, self.PACMAN_SIZE, self.PACMAN_SIZE,  self.PACMAN_SIZE, 2)
        #added the circle
        self.sprites_left.append(self.circle_frame)

        self.sprites = self.sprites_right
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.blit(game)
        self.count = 0
        self.update()

    def set_move(self, dir):
        if dir == "right":
            self.speed = (self.PACMAN_SPEED,0)
            self.sprites = self.sprites_right
        if dir == "left":
            self.speed = (-self.PACMAN_SPEED,0)
            self.sprites = self.sprites_left
        if dir == "up":
            self.speed = (0, -self.PACMAN_SPEED)
        if dir == "down":
            self.speed = (0, self.PACMAN_SPEED)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def update(self):
        self.count += 1
        if self.count % self.FRAME_RATE == 0:
            self.current_sprite = (self.current_sprite + 1)%self.frame_count
            self.image = self.sprites[self.current_sprite]
        
        self.image = self.sprites[self.current_sprite]

        self.rect.topleft = (self.x, self.y)


    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
        