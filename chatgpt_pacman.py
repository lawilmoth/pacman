import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
PACMAN_SPEED = 4
GHOST_SPEED = 2
POWERUP_DURATION = 300  # Frames

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Load Pac-Man
pacman = pygame.Rect(WIDTH//2, HEIGHT//2, GRID_SIZE, GRID_SIZE)

# Movement
dx, dy = 0, 0

# Walls
walls = [
    pygame.Rect(100, 100, 400, 20),
    pygame.Rect(100, 200, 20, 300),
    pygame.Rect(480, 200, 20, 300),
    pygame.Rect(100, 500, 400, 20)
]

# Pellets
pellets = [pygame.Rect(x, y, 5, 5) for x in range(50, WIDTH, 50) for y in range(50, HEIGHT, 50)]

# Power-ups
powerups = [pygame.Rect(250, 250, 10, 10), pygame.Rect(350, 350, 10, 10)]

# Ghosts
ghosts = [pygame.Rect(150, 150, GRID_SIZE, GRID_SIZE)]

ghost_frightened = False
powerup_timer = 0

def draw_pacman():
    pygame.draw.circle(screen, YELLOW, (pacman.x + GRID_SIZE // 2, pacman.y + GRID_SIZE // 2), GRID_SIZE // 2)

def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

def draw_pellets():
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, (pellet.x + 2, pellet.y + 2), 3)

def draw_powerups():
    for powerup in powerups:
        pygame.draw.circle(screen, GREEN, (powerup.x + 5, powerup.y + 5), 5)

def draw_ghosts():
    color = LIGHT_BLUE if ghost_frightened else RED
    for ghost in ghosts:
        pygame.draw.rect(screen, color, ghost)

def move_pacman():
    new_pacman = pacman.move(dx, dy)
    if not any(new_pacman.colliderect(wall) for wall in walls):
        pacman.x += dx
        pacman.y += dy

    # Eat pellets
    global pellets
    pellets = [pellet for pellet in pellets if not pacman.colliderect(pellet)]

    # Eat power-ups
    global powerups, ghost_frightened, powerup_timer
    for powerup in powerups[:]:
        if pacman.colliderect(powerup):
            ghost_frightened = True
            powerup_timer = POWERUP_DURATION
            powerups.remove(powerup)

def move_ghosts():
    global ghost_frightened
    for ghost in ghosts:
        if ghost_frightened:
            direction = random.choice([(-GHOST_SPEED, 0), (GHOST_SPEED, 0), (0, -GHOST_SPEED), (0, GHOST_SPEED)])
        else:
            if pacman.x > ghost.x:
                dx = GHOST_SPEED
            elif pacman.x < ghost.x:
                dx = -GHOST_SPEED
            else:
                dx = 0
            if pacman.y > ghost.y:
                dy = GHOST_SPEED
            elif pacman.y < ghost.y:
                dy = -GHOST_SPEED
            else:
                dy = 0
            direction = (dx, dy)
        
        new_ghost = ghost.move(direction[0], direction[1])
        if not any(new_ghost.colliderect(wall) for wall in walls):
            ghost.x += direction[0]
            ghost.y += direction[1]

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -PACMAN_SPEED, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = PACMAN_SPEED, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -PACMAN_SPEED
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, PACMAN_SPEED
    
    move_pacman()
    move_ghosts()
    
    # Handle power-up timer
    if ghost_frightened:
        powerup_timer -= 1
        if powerup_timer <= 0:
            ghost_frightened = False
    
    draw_walls()
    draw_pellets()
    draw_powerups()
    draw_pacman()
    draw_ghosts()
    
    pygame.display.flip()
    pygame.time.delay(30)
    
pygame.quit()
sys.exit()
