import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Snake Game')
window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
fps = 10  # Frame per second

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Starting position of the snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food position
food_pos = [300, 200]
food_spawn = True

# Direction control for the snake
direction = 'RIGHT'
change_to = direction

def change_direction(new_dir):
    global direction
    if new_dir == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if new_dir == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if new_dir == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if new_dir == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

def update_snake():
    global snake_pos, snake_body, food_pos, food_spawn
    # Moving the snake position
    if direction == 'RIGHT':
        snake_pos[0] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0]//10)) * 10,
                    random.randrange(1, (window_size[1]//10)) * 10]
        food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0]-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_size[1]-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()


def game_over():
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    change_direction(change_to)
    update_snake()

    # Rysowanie wszystkich elementów na ekranie
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Odświeżanie ekranu gry
    pygame.display.update()
    # Klatki na sekundę / częstotliwość odświeżania
    clock.tick(fps)
