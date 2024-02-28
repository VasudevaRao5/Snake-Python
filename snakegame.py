# Snake Game in Python using Pygame

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('GeeksforGeeks Snakes')

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize snake position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Initialize fruit position randomly
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Set initial direction
direction = 'RIGHT'
change_to = direction

# Set snake speed
snake_speed = 15

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update snake direction based on user input
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            change_to = 'LEFT'
        if keys[pygame.K_RIGHT]:
            change_to = 'RIGHT'
        if keys[pygame.K_UP]:
            change_to = 'UP'
        if keys[pygame.K_DOWN]:
            change_to = 'DOWN'

    # Update snake position
    if change_to == 'LEFT':
        snake_position[0] -= 10
    if change_to == 'RIGHT':
        snake_position[0] += 10
    if change_to == 'UP':
        snake_position[1] -= 10
    if change_to == 'DOWN':
        snake_position[1] += 10

    # Update snake body
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        fruit_spawn = False
    else:
        snake_body.pop()

    # Spawn new fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

    # Update game window
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)
