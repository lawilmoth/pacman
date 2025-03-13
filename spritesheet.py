import pygame

class SpriteSheet():
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * 3, height * 3))
        return image
    
    def get_images(self, xi, yi, width, height, number_of_frames):
        return [self.get_image(xi + i * width, yi, width, height) for i in range(number_of_frames)]
    
