import time
import pygame


from pm_sprites import PM_Sprite
class Pacman(PM_Sprite):
    def __init__(self, game):
        self.settings = game.settings
        self.ss_pacman_x = self.settings.PACMAN_SPRITESHEET_REFERENCE[0]
        self.ss_pacman_y = self.settings.PACMAN_SPRITESHEET_REFERENCE[1]

        
        super().__init__(game, self.settings.PACMAN_SPAWN_X, self.settings.PACMAN_SPAWN_Y, "pacman")
        self.speed = (0, 0) 
        self.game = game
        self.direction = "stop"
        self.prepared_turn = None

        #Found the frame with the circle
        self.circle_frame = self.sprite_sheet.get_image(
            self.sprite_sheet.SS_REFERENCE[0] + 2 * self.sprite_sheet.SS_GAP, 
            self.sprite_sheet.SS_REFERENCE[1], 
            self.SPRITE_SIZE, self.SPRITE_SIZE
            )
        #self.rect = self.circle_frame.get_rect()
        self.stop_sprites = [self.circle_frame]



        #Found 2 frames moving right 
        self.sprites_right = self.sprite_sheet.get_images(self.ss_pacman_x, 0, self.SPRITE_SIZE,  self.SPRITE_SIZE, 2) #Changed to only be 2 frames because one is the circle
        #added the circle
        self.sprites_right.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_left = self.sprite_sheet.get_images(self.ss_pacman_x, self.sprite_sheet.SS_GAP, self.SPRITE_SIZE,  self.SPRITE_SIZE, 2)
        #added the circle
        self.sprites_left.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_up = self.sprite_sheet.get_images(self.ss_pacman_x, 2*self.sprite_sheet.SS_GAP, self.SPRITE_SIZE,  self.SPRITE_SIZE, 2)
        #added the circle
        self.sprites_up.append(self.circle_frame)
        #Found 2 frames moving right 
        self.sprites_down = self.sprite_sheet.get_images(self.ss_pacman_x, 3*self.sprite_sheet.SS_GAP, self.SPRITE_SIZE,  self.SPRITE_SIZE, 2)
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

            
                
        self.check_teleport()
    



    def prepare_turn(self, direction):
        if self.direction == "right" or self.direction == "left":
            if direction == "up" or direction == "down":
                self.prepared_turn = direction
                return direction

            elif direction == "right" or direction == "left":
                self.prepared_turn = direction
                return direction
        
        elif self.direction == "up" or self.direction == "down":
            if direction == "right" or direction == "left":
                self.prepared_turn = direction
                return direction
            elif direction == "up" or direction == "down":
                self.prepared_turn = direction
                return direction


        