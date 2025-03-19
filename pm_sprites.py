from pygame.sprite import Sprite
import pygame
from spritesheet import SpriteSheet

class PM_Sprite(Sprite):
    current_frame = 0
    FRAME_RATE = 1
    SPEED = 24
    SIZE = 14
    MOVE_DECTECTOR_SIZE = 8



    """A class that makes pacman ghosts"""
    def __init__(self, game, x:int , y:int):
        
        super().__init__()
        self.sprite_sheet = SpriteSheet("images\pacman.png")
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.x = x
        self.y = y

        self.game = game

        self.moves_rects = {
            "right": pygame.Rect(0, 0, self.MOVE_DECTECTOR_SIZE, self.MOVE_DECTECTOR_SIZE),
            "left": pygame.Rect(0, 0, self.MOVE_DECTECTOR_SIZE, self.MOVE_DECTECTOR_SIZE),
            "up": pygame.Rect(0, 0, self.MOVE_DECTECTOR_SIZE, self.MOVE_DECTECTOR_SIZE),
            "down": pygame.Rect(0, 0, self.MOVE_DECTECTOR_SIZE, self.MOVE_DECTECTOR_SIZE),    
        }


    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
    
    def update_image(self):
        self.current_frame += 1
        if self.current_frame % self.FRAME_RATE == 0:
            self.current_sprite = (self.current_sprite + 1)%len(self.sprites)
            self.image = self.sprites[self.current_sprite]
        
        self.image = self.sprites[self.current_sprite]

        
    def update(self):
        self.rect.topleft = (self.x, self.y)
        
        for key, rect in self.moves_rects.items():
            if key == "up":
                rect.center = (self.rect.centerx , self.rect.centery - 1.5*self.SPEED)
            elif key == "down":
                rect.center = (self.rect.centerx , self.rect.centery + 1.5*self.SPEED)
            elif key == "right":
                rect.center = (self.rect.centerx + 1.5*self.SPEED, self.rect.centery)
            elif key == "left":
                rect.center = (self.rect.centerx - 1.5*self.SPEED, self.rect.centery)

    def can_move(self, direction):
        if direction != "stop":
            for wall in self.game.walls.sprites():
                if wall.rect.colliderect(self.moves_rects[direction]):
                    return False
        return True
    
    def set_move(self, dir):
        if dir == "right":
            self.direction = "right"
            self.speed = (self.SPEED,0)
            
            #self.sprites = self.sprites_right
        elif dir == "left":
            self.direction = "left"
            self.speed = (-self.SPEED,0)
            #self.sprites = self.sprites_left
        elif dir == "up":
            self.direction = "up"
            self.speed = (0, -self.SPEED)
            #self.sprites = self.sprites_up
        elif dir == "down":
            self.direction = "down"
            self.speed = (0, self.SPEED)
            #self.sprites = self.sprites_down
        elif dir == "stop":
            self.direction = "stop"
            self.speed = (0, 0)
            #self.sprites = self.stop_sprites