import pygame

from pacman import Pacman
from map import Map
from ghosts import Ghost
from settings import Settings
class Game:
    def  __init__(self):
        self.settings = Settings()
        pygame.init()
        self.clock = pygame.time.Clock()
        self.WIDTH = self.settings.screen_width
        self.HEIGHT = self.settings.screen_height
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pacman")
        self.running = True
        self.pacman = Pacman(self)
        self.consumables = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.ghosts.add(Ghost(self, self.settings.ghost_spawns["pinky"][0],self.settings.ghost_spawns["pinky"][1], "pinky"))
        self.ghosts.add(Ghost(self, self.settings.pacman_spawn[0],self.settings.pacman_spawn[1], "pinky"))
        self.map = Map()
        self.map.load_map(self)

    def run(self):
        while self.running:
            self._check_events()

            collisions = pygame.sprite.spritecollide(self.pacman, self.consumables, True)
            self.pacman.update_image()

            self.pacman.move()
            self.pacman.update()

            for ghost in self.ghosts.sprites():
                ghost.update()
                #ghost.move()



            self._update_screen()

    def _check_events(self):
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


    def _update_screen(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.map.bg_image, (0, 0))

        for cons in self.consumables.sprites():
            cons.draw()
        for wall in self.walls.sprites():
            wall.draw()

        for ghost in self.ghosts.sprites():
            ghost.blit(self)

        for check in self.pacman.moves_rects.values():
            pygame.draw.rect(self.window, (255, 0, 0), check)
        for ghost in self.ghosts.sprites():
            for check in ghost.moves_rects.values():
                pygame.draw.rect(self.window, (255, 0, 0), check)
        self.pacman.blit(self)

        pygame.display.update()

        self.clock.tick(15)

##################-----Main Code------#######################
game = Game()
game.run()