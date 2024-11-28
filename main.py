# dependencies
import random
import pygame
import os

# Game varibles
extreme_score = 0
card_number = random.randint(1, 95) # must be a number from 1-95 in the current state
list_of_Card_names = f"card_{card_number}.png"
# Pygame vars
flags = pygame.RESIZABLE | pygame.SCALED


# pygame setup
running = True

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((960, 540), flags, vsync=1)
pygame.display.set_caption("President game (prototype version)")
icon = pygame.image.load("assets/Flag_of_the_United_States.png")
pygame.display.set_icon(icon)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game logic

    # rendering stuff
    screen.fill("purple")
    screen.blit(pygame.image.load(f"assets/cards/{list_of_Card_names}").convert_alpha(), (0,0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(144)

pygame.quit()