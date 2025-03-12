import pygame
from pacman import Pacman

class Game:
    def  __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Pacman")
        self.running = True
        self.pacman = Pacman(self)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pacman.set_move("left")
                    if event.key == pygame.K_RIGHT:
                        self.pacman.set_move("right")
                    elif event.key == pygame.K_UP:
                        self.pacman.set_move("up")
            self.pacman.move()
            
            self._update_screen()

    def _update_screen(self):
        self.window.fill((0, 0, 0))
        self.pacman.draw(self)
        pygame.display.update()
        self.clock.tick(60)

##################-----Main Code------#######################
game = Game()
game.run()