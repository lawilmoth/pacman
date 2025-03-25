import pygame

class SoundMixer:
    def __init__(self):
        self.volume = .3
        pygame.mixer.init()
        
        self.beginning_sound = pygame.mixer.Sound("sounds/pacman_beginning.wav")
        self.beginning_sound.set_volume(self.volume)
        self.chomp_sound = pygame.mixer.Sound("sounds/pacman_chomp.wav")
        self.chomp_sound.set_volume(self.volume)
        self.dead_sound = pygame.mixer.Sound("sounds/pacman_death.wav")
        self.dead_sound.set_volume(self.volume)
        self.eat_ghost = pygame.mixer.Sound("sounds/pacman_eatghost.wav")
        self.eat_ghost.set_volume(self.volume)


