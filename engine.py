import pygame
from sys import exit

from pygame import surface

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2d shooter test')
clock = pygame.time.Clock()

back_surface = pygame.image.load('graphics/background/sky.png')
ground_surface = pygame.image.load('graphics/background/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(back_surface, (0,0))
    screen.blit(ground_surface, (0,400))

    pygame.display.update()
    clock.tick(30)