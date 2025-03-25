class Settings:
    def __init__(self):
        self.SCALE_FACTOR = 3
        self.SCREEN_WIDTH = 222 * self.SCALE_FACTOR
        self.SCREEN_HEIGHT = 266 * self.SCALE_FACTOR
        self.TILE_SIZE = 8 * self.SCALE_FACTOR
        self.SPRITE_SIZE = 14
        self.INITIAL_X_GAP = 4*self.SCALE_FACTOR
        self.INITIAL_Y_GAP = 4*self.SCALE_FACTOR
        self.NUMBER_OF_TILES_X = 28
        self.NUMBER_OF_TILES_Y = 30
        self.PACMAN_SPAWN_X = self.INITIAL_X_GAP//2 + self.TILE_SIZE*12 + self.SPRITE_SIZE//2
        self.PACMAN_SPAWN_Y = self.INITIAL_Y_GAP//2 + self.TILE_SIZE*17 - self.SPRITE_SIZE

        self.PACMAN_SPRITESHEET_REFERENCE = (457, 1)
        self.FPS = 15

        self.CONSUMABLE_SIZE = 1 * self.SCALE_FACTOR
        self.CONSUMABLE_COLOR = (255, 255, 0)

        self.GHOST_SPAWNS = {
            "blinky": (self.INITIAL_X_GAP + self.TILE_SIZE*12, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "pinky": (self.INITIAL_X_GAP + self.TILE_SIZE*11, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "inky": (self.INITIAL_X_GAP + self.TILE_SIZE*13, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "clyde": (self.INITIAL_X_GAP + self.TILE_SIZE*14, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
        }
