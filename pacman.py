import time
import pygame


from pm_sprites import PM_Sprite
class Pacman(PM_Sprite):
    def __init__(self, game):
        self.settings = game.settings
        self.ss_pacman_x = 458

        self.starting_y = 300
        super().__init__(game, self.settings.pacman_spawn_x, self.settings.pacman_spawn_x, "pacman")
        self.speed = (0, 0) 
        self.game = game
        self.direction = "stop"

        #Found the frame with the circle
        self.circle_frame = self.sprite_sheet.get_image(
            self.sprite_sheet.SS_REFERENCE[0] + 2 * self.sprite_sheet.SS_GAP, 
            self.sprite_sheet.SS_REFERENCE[1], 
            self.SIZE, self.SIZE
            )
        self.rect = self.circle_frame.get_rect()
        self.stop_sprites = [self.circle_frame]



        #Found 2 frames moving right 
        self.sprites_right = self.sprite_sheet.get_images(self.ss_pacman_x, 0, self.SIZE,  self.SIZE, 2) #Changed to only be 2 frames because one is the circle
        #added the circle
        self.sprites_right.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_left = self.sprite_sheet.get_images(self.ss_pacman_x, self.sprite_sheet.SS_GAP, self.SIZE,  self.SIZE, 2)
        #added the circle
        self.sprites_left.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_up = self.sprite_sheet.get_images(self.ss_pacman_x, 2*self.sprite_sheet.SS_GAP, self.SIZE,  self.SIZE, 2)
        #added the circle
        self.sprites_up.append(self.circle_frame)
        #Found 2 frames moving right 
        self.sprites_down = self.sprite_sheet.get_images(self.ss_pacman_x, 3*self.sprite_sheet.SS_GAP, self.SIZE,  self.SIZE, 2)
        #added the circle
        self.sprites_down.append(self.circle_frame)


        self.sprites = self.stop_sprites
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        




    def move(self):
        if self.can_move(self.direction):
            self.x += self.speed[0]
            self.y += self.speed[1]
        else:
            self.set_move("stop")

            
                

        if self.x < 0 - 2*self.SIZE:
            self.x = self.game.WIDTH + self.SIZE
        elif self.x > self.game.WIDTH + self.SIZE:
            self.x = - self.SIZE



    def prepare_turn(self, direction):
        if self.direction == "right" or self.direction == "left":
            if direction == "up" or direction == "down":
                self.set_move(direction)

        