class Settings:
    def __init__(self):
        self.SCREEN_WIDTH = 670
        self.SCREEN_HEIGHT = 800
        self.TILE_SIZE = 24
        self.TILE_GAP = 2
        self.INITIAL_X_GAP = 11
        self.INITIAL_Y_GAP = 11
        self.PACMAN_SPAWN_X = self.INITIAL_X_GAP + self.TILE_SIZE*12
        self.PACMAN_SPAWN_Y = self.INITIAL_X_GAP + self.TILE_SIZE*12
        self.PACMAN_SPRITESHEET_REFERENCE = (457, 1)


        self.SETTINGS = {
            "blinky": (self.INITIAL_X_GAP + self.TILE_SIZE*12, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "pinky": (self.INITIAL_X_GAP + self.TILE_SIZE*11, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "inky": (self.INITIAL_X_GAP + self.TILE_SIZE*13, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
            "clyde": (self.INITIAL_X_GAP + self.TILE_SIZE*14, self.INITIAL_Y_GAP + self.TILE_SIZE*11),
        }

settings = Settings()