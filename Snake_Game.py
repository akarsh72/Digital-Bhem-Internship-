                                        ###    Snake Game    ###

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up colors
bg_color = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game fonts
font = pygame.font.Font(None, 36)

# Set up the snake variables
snake_size = 20
snake_speed = 10
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_dx = 0
snake_dy = 0
snake_body = []
snake_length = 1

# Set up the food variables
food_size = 20
food_x = random.randint(0, screen_width - food_size) // 20 * 20
food_y = random.randint(0, screen_height - food_size) // 20 * 20

# Set up the score variable
score = 0

# Function to display the score on the screen
def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Function to display the game over message
def game_over():
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 20))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != snake_size:
                snake_dx = 0
                snake_dy = -snake_size
            elif event.key == pygame.K_DOWN and snake_dy != -snake_size:
                snake_dx = 0
                snake_dy = snake_size
            elif event.key == pygame.K_LEFT and snake_dx != snake_size:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -snake_size:
                snake_dx = snake_size
                snake_dy = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with boundaries
    if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
        running = False

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        snake_length += 1
        food_x = random.randint(0, screen_width - food_size) // 20 * 20
        food_y = random.randint(0, screen_height - food_size) // 20 * 20

    # Check for collision with snake's body
    snake_head = [snake_x, snake_y]
    if snake_head in snake_body[:-1]:
        running = False

    # Update snake's body
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Clear the screen
    screen.fill(bg_color)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))

    # Display the score
    show_score()

    # Update the screen
    pygame.display.flip()

    # Set the game's FPS
    clock.tick(snake_speed)

# Display the game over message
game_over()

# Update the screen
pygame.display.flip()

# Wait for 2 seconds
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()
