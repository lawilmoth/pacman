class Settings:
    def __init__(self):
        self.screen_width = 670
        self.screen_height = 800
        self.tile_size = 24
        self.tile_gap = 2
        self.initial_x_gap = 11
        self.initial_y_gap = 11
        self.pacman_spawn_x = self.initial_x_gap + self.tile_size*12 
        self.pacman_spawn_y = self.initial_x_gap + self.tile_size*12


        self.ghost_spawns = {
            "blinky": (self.initial_x_gap + self.tile_size*12, self.initial_x_gap + self.tile_size*11),
            "pinky": (self.initial_x_gap + self.tile_size*11, self.initial_x_gap + self.tile_size*11),
            "inky": (self.initial_x_gap + self.tile_size*13, self.initial_x_gap + self.tile_size*11),
            "clyde": (self.initial_x_gap + self.tile_size*14, self.initial_x_gap + self.tile_size*11),
        }