from pm_sprites import PM_Sprite
import pygame
import random

class Ghost(PM_Sprite):
    SPRITE_SHEET_FRAMES = 8
    def __init__(self, game, x, y, name="pinky"):
        super().__init__(game, x, y)
        self.current_direction = "up"
        self.speed = (0, 0)
        self.name = name

        self.sprites = self.sprite_sheet.get_images(
            self.sprite_sheet.SS_REFERENCE[0], 
            self.sprite_sheet.SS_REFERENCE[1] + 5 *self.sprite_sheet.SS_GAP, 
            self.SIZE, 
            self.SIZE, 
            self.SPRITE_SHEET_FRAMES)
        self.image = self.sprites[self.current_frame]
        self.target = (0, 0)

    def move(self):
        if self.can_move(self.current_direction):
        
            self.x += self.speed[0]
            self.y += self.speed[1]
        else:
            while not self.can_move(self.current_direction):
                self.current_direction = random.choice(["up", "down", "left", "right"])
        self.set_move(self.current_direction)
        print(self.current_direction)
        self.current_frame += 1
        self.current_frame %= self.SPRITE_SHEET_FRAMES
        self.image = self.sprites[self.current_frame]
        
