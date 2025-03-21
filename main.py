import pygame

from pacman import Pacman
from map import Map
from ghosts import Ghost, Inky, Pinky
from settings import Settings
from sound_mixer import SoundMixer
class Game:
    frame_count = 0
    def  __init__(self):
        self.settings = Settings()
        pygame.init()
        self.sm = SoundMixer()
        #play beginning sound
        self.sm.beginning_sound.play()
        self.clock = pygame.time.Clock()
        self.WIDTH = self.settings.SCREEN_WIDTH
        self.HEIGHT = self.settings.SCREEN_HEIGHT
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pacman")
        self.running = True
        self.pacman = Pacman(self)
        self.consumables = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()

        self.inky = Inky(self, self.settings.PACMAN_SPAWN_X,self.settings.PACMAN_SPAWN_Y)
        self.pinky = Pinky(self, self.settings.PACMAN_SPAWN_X,self.settings.PACMAN_SPAWN_Y)
        self.ghosts.add(self.inky)
        self.ghosts.add(self.pinky)

        self.map = Map()
        self.map.load_map(self)

    def run(self):
        while self.running:
            self._check_events()

            collisions = pygame.sprite.spritecollide(self.pacman, self.consumables, True)
            if collisions:
                if not pygame.mixer.get_busy():
                    self.sm.chomp_sound.play()
            self.pacman.update_image()

            self.pacman.move()
            self.pacman.update()

            for ghost in self.ghosts.sprites():
                ghost.update()
                ghost.move()



            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.pacman.can_move("left"):
                        if(self.pacman.direction == "right" or self.pacman.direction == "stop"):
                            self.pacman.set_move("left")
                            break
                    self.pacman.prepare_turn("left")


                elif event.key == pygame.K_RIGHT:
                    if self.pacman.can_move("right"):
                        if(self.pacman.direction == "left" or self.pacman.direction == "stop"):
                            self.pacman.set_move("right")
                            break
                    self.pacman.prepare_turn("right")
                elif event.key == pygame.K_UP:
                    if self.pacman.can_move("up"):
                        if(self.pacman.direction == "down" or self.pacman.direction == "stop"):
                            self.pacman.set_move("up")
                            break
                    self.pacman.prepare_turn("up")
                elif event.key == pygame.K_DOWN:
                    if self.pacman.can_move("down"):
                        if(self.pacman.direction == "up" or self.pacman.direction == "stop"):
                            self.pacman.set_move("down")
                            break
                    self.pacman.prepare_turn("down")
        self._execute_turn()

    def _execute_turn(self):
        if self.pacman.direction == "stop":
            self.pacman.set_move(self.pacman.prepared_turn)
        if self.pacman.prepared_turn and self.pacman.can_move(self.pacman.prepared_turn):
            self.pacman.set_move(self.pacman.prepared_turn)
            self.pacman.prepared_turn = None

    def _update_screen(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.map.bg_image, (0, 0))

        for cons in self.consumables.sprites():
            cons.draw()
        for wall in self.walls.sprites():
            #wall.draw()
            pass
        for ghost in self.ghosts.sprites():
            ghost.check_target()
            ghost.update()
            ghost.blit(self)

        for check in self.pacman.moves_rects.values():
            pygame.draw.rect(self.window, (255, 0, 0), check)
        for ghost in self.ghosts.sprites():
            for check in ghost.moves_rects.values():
                pygame.draw.rect(self.window, (255, 0, 0), check)
        self.pacman.blit(self)


        pygame.display.update()

        self.frame_count += 1
        self.clock.tick(15)

##################-----Main Code------#######################
game = Game()
game.run()