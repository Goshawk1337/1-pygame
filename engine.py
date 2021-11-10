# a platformer
import pygame
import tkinter
from sys import exit
import os
import tilehandler

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

while True:
    #draw'nupdate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('black')
    pygame.display.update()
    clock.tick(30)

#coords of 0-255 x 0-255, variable whitin limits
#tilesize in pixels of 64