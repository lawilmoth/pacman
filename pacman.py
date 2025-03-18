import time
import pygame


from pm_sprites import PM_Sprite
class Pacman(PM_Sprite):
    def __init__(self, game):
        
        self.starting_x = 300
        self.starting_y = 300
        super().__init__(self.starting_x, self.starting_y, game)

        self.speed = (0, 0)
        
        self.game = game
        self.direction = "stop"

        #Found the frame with the circle
        self.circle_frame = self.sprite_sheet.get_image(457 + self.SIZE*2 , 0, self.SIZE, self.SIZE)
        self.rect = self.circle_frame.get_rect()
        self.stop_sprites = [self.circle_frame]
        #Found 2 frames moving right 
        self.sprites_right = self.sprite_sheet.get_images(457, 0, self.SIZE,  self.SIZE, 2) #Changed to only be 2 frames because one is the circle
        #added the circle
        self.sprites_right.append(self.circle_frame)

        #Found 2 frames moving right 
        self.sprites_left = self.sprite_sheet.get_images(457, self.SIZE, self.SIZE,  self.SIZE, 2)
        #added the circle
        self.sprites_left.append(self.circle_frame)

        self.sprites = self.stop_sprites
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        


    def set_move(self, dir):
        if dir == "right":
            self.direction = "right"
            self.speed = (self.SPEED,0)
            self.sprites = self.sprites_right
        elif dir == "left":
            self.direction = "left"
            self.speed = (-self.SPEED,0)
            self.sprites = self.sprites_left
        elif dir == "up":
            self.direction = "up"
            self.speed = (0, -self.SPEED)
        elif dir == "down":
            self.direction = "down"
            self.speed = (0, self.SPEED)
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
                

        if self.x < 0 - 2*self.SIZE:
            self.x = self.game.WIDTH + self.SIZE
        elif self.x > self.game.WIDTH + self.SIZE:
            self.x = - self.SIZE



    def prepare_turn(self, direction):
        if self.direction == "right" or self.direction == "left":
            if direction == "up" or direction == "down":
                self.set_move(direction)

        