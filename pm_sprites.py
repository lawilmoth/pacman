from pygame.sprite import Sprite
import pygame
from spritesheet import SpriteSheet
from settings import Settings
settings = Settings()
class PM_Sprite(Sprite):
    current_frame = 0
    FRAME_RATE = 1
    SPEED = settings.TILE_SIZE
    SPRITE_SIZE = 14
    SIZE = SPRITE_SIZE*settings.SCALE_FACTOR
    
    OFFSET = - settings.SCALE_FACTOR*2



    """A class that makes pacman ghosts"""
    def __init__(self, game, x:int , y:int, name:str):
        
        super().__init__()
        self.sprite_sheet = SpriteSheet("images\pacman.png")

        self.rect = pygame.Rect(0, 0, self.SIZE , self.SIZE) 
        self.x:int = x
        self.y:int = y
        self.name = name
        

        self.game = game

        self.moves_rects = {
            "right": pygame.Rect(0, 0, self.SIZE//2, self.SIZE),
            "left": pygame.Rect(0, 0, self.SIZE//2, self.SIZE),
            "up": pygame.Rect(0, 0, self.SIZE, self.SIZE//2),
            "down": pygame.Rect(0, 0, self.SIZE, self.SIZE//2),    
        }
        
        

    def blit(self, game):
        game.window.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(game.window, (255, 0, 255), self.rect)
        pass
    
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
                rect.bottomleft = (self.rect.x, self.rect.top)
            elif key == "down":
                rect.topleft = (self.rect.x, self.rect.bottom)
            elif key == "right":
                rect.topleft = (self.rect.right, self.y )
            elif key == "left":
                rect.topright = (self.rect.x, self.rect.y)
        
    def can_move(self, direction):
        if direction and direction != "stop":
            for wall in self.game.walls.sprites():
                if wall.rect.colliderect(self.moves_rects[direction]):

                    if wall.name == "gate" and self.name != "pacman":
                        if self.mode == "eaten":
                            
                            return True
                    return False
        return True
    
    def set_move(self, dir):
        self.prepared_turn = None
        if dir == "right":
            self.direction = "right"
            self.speed = (self.SPEED,0)
            if self.name == "pacman":
                self.sprites = self.sprites_right

        elif dir == "left":
            self.direction = "left"
            self.speed = (-self.SPEED,0)
            if self.name == "pacman":
                self.sprites = self.sprites_left

        elif dir == "up":
            self.direction = "up"
            self.speed = (0, -self.SPEED)
            if self.name == "pacman":
                self.sprites = self.sprites_up

        elif dir == "down":
            self.direction = "down"
            self.speed = (0, self.SPEED)
            if self.name == "pacman":
                self.sprites = self.sprites_down
        elif dir == "stop":
            self.direction = "stop"
            self.speed = (0, 0)
            if self.name == "pacman":
                self.sprites = self.stop_sprites
    
    def check_teleport(self):
        if self.x < 0 - self.SIZE:
            if self.direction == "left":
                self.x = self.settings.INITIAL_X_GAP + self.game.settings.TILE_SIZE * (self.game.settings.NUMBER_OF_TILES_X + 1)

        elif self.x > self.game.WIDTH :
            if self.direction == "right":
                self.x = self.settings.INITIAL_X_GAP - self.game.settings.TILE_SIZE

    def __str__(self):
        return f"{self.name} at {self.x}, {self.y}"