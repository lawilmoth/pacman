import pygame
from consumable import Consumable, PowerPellet
from spritesheet import SpriteSheet
from settings import Settings
settings = Settings()
class Map:
    """A tool for building maps"""
    TILE_SIZE = settings.TILE_SIZE
    INITIAL_X_GAP = settings.INITIAL_X_GAP
    INITIAL_Y_GAP = settings.INITIAL_Y_GAP
    def __init__(self):
        self.bg_image = SpriteSheet("images\pacman.png").get_image(228, 0, 228, 250)
        # 0 = empty space
        # 1 = pellet
        # 2 = big pellet
        # 3 = wall
        # 4 = pacman
        # 5 = ghost house
        # Map is 28x32
        self.map_grid = [
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 2, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 2, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 3, 3, 3, 3, 3, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3],
                [3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3],
                [3, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3],
                [3, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3],
                [3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3],
                [3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3],
                [3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3],
                [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],


            ]



    def load_map(self, game):
        
        for i, row in enumerate(self.map_grid):
            for j, item in enumerate(row):
                
                if item == 1:
                    cons = Consumable(
                        game, 
                        j*self.TILE_SIZE + self.INITIAL_X_GAP, 
                        i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                        settings.CONSUMABLE_SIZE, 
                        settings.CONSUMABLE_COLOR
                        )
                    game.consumables.add(cons)
                if item == 2:
                    cons = PowerPellet(
                        game, 
                        j*self.TILE_SIZE + self.INITIAL_X_GAP, 
                        i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                        settings.CONSUMABLE_SIZE*5, 
                        settings.CONSUMABLE_COLOR
                        )
                    game.power_pellets.add(cons)
                if item == 3:
                    if  i < len(self.map_grid) - 1 and j < len(self.map_grid[0]) - 1 :
                        if self.map_grid[i+1][j] == 3 and self.map_grid[i][j+1] == 3 and self.map_grid[i+1][j+1] == 3 :
                            wall = Wall(
                                game, 
                                j*self.TILE_SIZE + self.INITIAL_X_GAP, 
                                i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                                self.TILE_SIZE,
                                self.TILE_SIZE, 
                                (255, 0, 255)
                                )
                            game.walls.add(wall)
                    #Top wall
                    if i == 0 :
                        wall = Wall(
                            game, 
                            j*self.TILE_SIZE, 
                            i*self.TILE_SIZE , 
                            self.TILE_SIZE * 2,
                            self.INITIAL_Y_GAP, 
                            (0, 0, 255)
                            )
                        game.walls.add(wall)
                    #Left wall
                    elif j == 0 and (i+1 < len(self.map_grid) and self.map_grid[i+1][j] == 3):
                        wall = Wall(
                            game, 
                            j*self.TILE_SIZE - 2*self.INITIAL_X_GAP, 
                            i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                            self.INITIAL_X_GAP *3,
                            self.TILE_SIZE, 
                            (255, 0, 0)
                            )
                        game.walls.add(wall)
                    #bottom wall
                    elif i == len(self.map_grid) - 1:
                        wall = Wall(
                            game, 
                            j*self.TILE_SIZE, 
                            i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                            self.TILE_SIZE*2,
                            self.TILE_SIZE, 
                            (0, 0, 255)
                            
                        )
                        game.walls.add(wall)
                    #right wall
                    elif j == len(self.map_grid[0]) - 1 and i+1 < len(self.map_grid) and self.map_grid[i+1][j] == 3:
                        wall = Wall(
                            game, 
                            j*self.TILE_SIZE + self.INITIAL_X_GAP, 
                            i*self.TILE_SIZE + self.INITIAL_Y_GAP, 
                            self.TILE_SIZE * 3,
                            self.TILE_SIZE, 
                            (0, 0, 255)
                            )
                        game.walls.add(wall)


                        

                    
                if item == 4:
                    game.pacman.x = j*self.TILE_SIZE + self.INITIAL_X_GAP//2 - game.pacman.SPRITE_SIZE 
                    game.pacman.y = i*self.TILE_SIZE + self.INITIAL_Y_GAP//2 - game.pacman.SPRITE_SIZE



class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        


    def draw(self):
        pygame.draw.rect(self.game.window, self.color, self.rect)

