from pm_sprites import PM_Sprite
import pygame
import random

#Tile priority is up left down right

class Ghost(PM_Sprite):
    SPRITE_SHEET_FRAMES = 8
    def __init__(self, game, x, y, name="pinky"):
        super().__init__(game, x, y, name)
        self.settings = game.settings
        self.current_direction = "up"
        self.speed = (0, 0)
        self.target = (0, 0)

    def move(self):
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
        closest_distance = 1000000
        for key, value in move_choices.items():
            if value:
                rect = self.moves_rects[key]
                distance = ((rect.centerx - self.target[0])**2 + (rect.centery - self.target[1])**2)**0.5
                if distance < closest_distance:
                    closest_distance = distance
                    self.current_direction = key
                

        


        self.set_move(self.current_direction)
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.current_frame += 1
        self.current_frame %= self.SPRITE_SHEET_FRAMES
        self.image = self.sprites[self.current_frame]
        


class Pinky(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "pinky")

        self.sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 5 *self.sprite_sheet.SS_GAP, 
            self.SIZE, 
            self.SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.image = self.sprites[self.current_frame]

        self.target = (0,0)

        

class Inky(Ghost):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, "pinky")
        
        self.sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 6 *self.sprite_sheet.SS_GAP, 
            self.SIZE, 
            self.SIZE, 
            self.SPRITE_SHEET_FRAMES)
        
        self.image = self.sprites[self.current_frame]

        self.target= (game.WIDTH, game.HEIGHT)
