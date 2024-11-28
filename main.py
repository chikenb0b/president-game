# dependencies
import random
import pygame
import os

# Game varibles
extreme_score = 0

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

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(144)

pygame.quit()