import time
import pygame
from spritesheet import SpriteSheet
from map import Map
class Pacman(pygame.sprite.Sprite):
    FRAME_RATE = 1
    PACMAN_SIZE = 15
    PACMAN_SPEED = Map.GAP//4
    
    def __init__(self, game):
        super().__init__()
        sprite_sheet = SpriteSheet("images\pacman.png")
        self.x = 300
        self.y = 300
        self.speed = (0, 0)
        
        self.game = game
        self.direction = "stop"

        #Found the frame with the circle
        self.circle_frame = sprite_sheet.get_image(457 + self.PACMAN_SIZE*2 , 0, self.PACMAN_SIZE, self.PACMAN_SIZE)
        self.rect = self.circle_frame.get_rect()
        self.stop_sprites = [self.circle_frame]
        #Found 2 frames moving right 
        self.sprites_right = sprite_sheet.get_images(457, 0, self.PACMAN_SIZE,  self.PACMAN_SIZE, 2) #Changed to only be 2 frames because one is the circle
        #added the circle
        self.sprites_right.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_left = sprite_sheet.get_images(457, self.PACMAN_SIZE, self.PACMAN_SIZE,  self.PACMAN_SIZE, 2)
        #added the circle
        self.sprites_left.append(self.circle_frame)

        self.sprites = self.stop_sprites
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.count = 0
        self.update()

    def set_move(self, dir):
        if dir == "right":
            self.direction = "right"
            self.speed = (self.PACMAN_SPEED,0)
            self.sprites = self.sprites_right
        elif dir == "left":
            self.direction = "left"
            self.speed = (-self.PACMAN_SPEED,0)
            self.sprites = self.sprites_left
        elif dir == "up":
            self.direction = "up"
            self.speed = (0, -self.PACMAN_SPEED)
        elif dir == "down":
            self.direction = "down"
            self.speed = (0, self.PACMAN_SPEED)
        elif dir == "stop":
            self.direction = "stop"
            self.speed = (0, 0)
            self.sprites = self.stop_sprites

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        wall_collisions = pygame.sprite.spritecollide(self, self.game.walls, False)
        if wall_collisions:
            time.sleep(0.1)
            print(self.speed, self.x, self.y)
            self.x = self.x - 2*self.speed[0]
            self.y = self.y - 2*self.speed[1]
            self.update()
            self.set_move("stop")
                

        if self.x < 0 - 2*self.PACMAN_SIZE:
            self.x = self.game.WIDTH + self.PACMAN_SIZE
        elif self.x > self.game.WIDTH + self.PACMAN_SIZE:
            self.x = - self.PACMAN_SIZE

    def update(self):
        self.count += 1
        if self.count % self.FRAME_RATE == 0:
            self.current_sprite = (self.current_sprite + 1)%len(self.sprites)
            self.image = self.sprites[self.current_sprite]
        
        self.image = self.sprites[self.current_sprite]

        self.rect.topleft = (self.x, self.y)


    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
        