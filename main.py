import pygame
import time
from pacman import Pacman
from map import Map 
class Game:
    def  __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.WIDTH = 670
        self.HEIGHT = 800
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pacman")
        self.running = True
        self.pacman = Pacman(self)
        self.consumables = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.map = Map()
        self.map.load_map(self)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pacman.set_move("left")
                        print("left")

                    elif event.key == pygame.K_RIGHT:
                        self.pacman.set_move("right")
                    elif event.key == pygame.K_UP:
                        self.pacman.set_move("up")
                    elif event.key == pygame.K_DOWN:
                        self.pacman.set_move("down")
            collisions = pygame.sprite.spritecollide(self.pacman, self.consumables, True)
            if collisions:
                print(len(self.consumables))

            

            



            self.pacman.move()

            self.pacman.update()

            self._update_screen()


    def _update_screen(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.map.bg_image, (0, 0))

        for cons in self.consumables.sprites():
            cons.draw()
        for wall in self.walls.sprites():
            wall.draw()
        self.pacman.blit(self)

        pygame.display.update()
        self.clock.tick(60)

##################-----Main Code------#######################
game = Game()
game.run()