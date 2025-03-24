from pm_sprites import PM_Sprite
import pygame
import random
from settings import Settings
settings = Settings()
#Tile priority is up left down right

class Ghost(PM_Sprite):
    SPRITE_SHEET_FRAMES = 8
    scatter_time = 7
    frightened_count = 0
    FRIGHTENED_TO_BLINK_TIME = 3
    FRIGHTENED_TIME = 5
    GHOST_HOUSE_COORDS = (settings.TILE_SIZE*13 + settings.INITIAL_X_GAP, settings.TILE_SIZE*11 + settings.INITIAL_Y_GAP)
    
    def __init__(self, game, x, y, name="pinky"):
        super().__init__(game, x, y, name)
        self.settings = game.settings
        self.current_direction = "up"
        self.speed = (0, 0)
        self.target = (0, 0)
        self.mode = "scatter"
        self.frightened_sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0] + 8 *self.sprite_sheet.SS_GAP, 
            self.sprite_sheet.SS_REFERENCE[1] + 4 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            2)
        for i in range(2):
            self.frightened_sprites.extend(self.frightened_sprites)


        self.blink_sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0] +10 *self.sprite_sheet.SS_GAP, 
            self.sprite_sheet.SS_REFERENCE[1] + 4 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            2)
        for i in range(2):
            self.blink_sprites.extend(self.frightened_sprites)

        self.dead_sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0] +8 *self.sprite_sheet.SS_GAP, 
            self.sprite_sheet.SS_REFERENCE[1] + 5 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            4)
        
        self.dead_sprites.extend(self.dead_sprites)



    def set_frightened(self):
        if self.mode != "frightened":
            self.change_directions()
        self.mode = "frightened"
        Ghost.frightened_count = 0

        self.sprites = self.frightened_sprites


    def change_directions(self):
        if self.current_direction == "up":
            if self.can_move("down"):
                self.current_direction = "down"
            elif self.can_move("left"):
                self.current_direction = "left"
            elif self.can_move("right"):
                self.current_direction = "right"
        elif self.current_direction == "down":
            if self.can_move("up"):
                self.current_direction = "up"
            elif self.can_move("left"):
                self.current_direction = "left"
            elif self.can_move("right"):
                self.current_direction = "right"
        elif self.current_direction == "left":
            if self.can_move("right"):
                self.current_direction = "right"
            elif self.can_move("up"):
                self.current_direction = "up"
            elif self.can_move("down"):
                self.current_direction = "down"

                
        elif self.current_direction == "right":
            if self.can_move("left"):
                self.current_direction = "left"
            elif self.can_move("up"):
                self.current_direction = "up"
            elif self.can_move("down"):
                self.current_direction = "down"
            

    def update_target(self):

        if self.game.frame_count == self.scatter_time*self.settings.FPS and self.mode == "scatter":
            self.mode = "chase"
            self.change_directions()

        if self.mode == "frightened":
            if Ghost.frightened_count > self.FRIGHTENED_TIME*self.settings.FPS:
                Ghost.frightened_count = 0
            if Ghost.frightened_count >= self.FRIGHTENED_TIME*self.settings.FPS:
                self.mode = "chase"
                self.change_directions()
                self.sprites = self.sprites_default
                
            elif Ghost.frightened_count >= self.FRIGHTENED_TO_BLINK_TIME*self.settings.FPS:
                self.sprites = self.blink_sprites
                
        if self.mode == "eaten":
            self.sprites = self.dead_sprites 
            self.target = self.GHOST_HOUSE_COORDS


        


    def move(self):
        self.update_target()
        # if canmove dir, check distance to target
        move_choices = {"up": True,
                        "down":True,
                        "left": True,
                        "right": True
                        }
        if self.current_direction == "up":
            move_choices["down"] = False
        elif self.current_direction == "down":
            move_choices["up"] = False
        elif self.current_direction == "left":
            move_choices["right"] = False
        elif self.current_direction == "right":
            move_choices["left"] = False
        
        for key in move_choices.keys():
            if not self.can_move(key):
                move_choices[key] = False
        
        self.current_direction = None

        if self.mode != "frightened":
            closest_distance = 1000000
        if self.mode == "frightened":
            closest_distance = -1

        
        for key, value in move_choices.items():
            if value:
                rect = self.moves_rects[key]
                distance = ((rect.centerx - self.target[0])**2 + (rect.centery - self.target[1])**2)**0.5
                if self.mode != "frightened":
                    if distance < closest_distance:
                        closest_distance = distance
                        self.current_direction = key
                elif self.mode == "frightened":
                    if distance > closest_distance:
                        closest_distance = distance
                        self.current_direction = key

        


        self.set_move(self.current_direction)
        if self.mode == "frightened":
            self.x += self.speed[0]//2
            self.y += self.speed[1]//2
        else:
            self.x += self.speed[0]
            self.y += self.speed[1]
        self.current_frame += 1
        self.current_frame %= self.SPRITE_SHEET_FRAMES
        self.image = self.sprites[self.current_frame]
        

        self.check_teleport()



class Pinky(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "pinky")

        self.sprites_default = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 5 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.sprites = self.sprites_default
        self.image = self.sprites[self.current_frame]

    def check_target(self):
        if self.mode == "scatter":
            self.target = (0,0)
        elif self.mode == "chase":
            self.target = (self.game.pacman.x, self.game.pacman.y)

        

class Inky(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "inky")
        
        self.sprites_default = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 6 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.sprites = self.sprites_default
        self.image = self.sprites[self.current_frame]

    def check_target(self):
        if self.mode == "scatter":
            self.target= (self.game.WIDTH, self.game.HEIGHT)
        elif self.mode == "chase":
            self.target = (self.game.pacman.x, self.game.pacman.y)
        
class Blinky(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "blinky")
        
        self.sprites_default = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 4 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.sprites = self.sprites_default
        self.image = self.sprites[self.current_frame]

    def check_target(self):
        if self.mode == "scatter":
            self.target= (self.game.WIDTH, 0)
        elif self.mode == "chase":
            self.target = (self.game.pacman.x, self.game.pacman.y)


class Clyde(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "clyde")
        
        self.sprites_default = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 7 *self.sprite_sheet.SS_GAP, 
            self.SPRITE_SIZE, 
            self.SPRITE_SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.sprites = self.sprites_default
        self.image = self.sprites[self.current_frame]

    def check_target(self):
        if self.mode == "scatter":
            self.target= (0, self.game.HEIGHT)
        elif self.mode == "chase":
            self.target = (self.game.pacman.x, self.game.pacman.y)