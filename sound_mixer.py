import pygame

class SoundMixer:
    def __init__(self):
        self.volume = 1
        pygame.mixer.init()
        
        self.beginning_sound = pygame.mixer.Sound("sounds/pacman_beginning.wav")
        self.beginning_sound.set_volume(self.volume)
        self.chomp_sound = pygame.mixer.Sound("sounds/pacman_chomp.wav")
        self.chomp_sound.set_volume(self.volume)
    


