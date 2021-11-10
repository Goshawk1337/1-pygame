import pygame
from pygame.constants import K_LEFT, K_RIGHT

vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = vec(0,0)
        self.accel = vec(0,0)
        self.vel = vec(0,0)
        self.onGround = False
##        self.image = pygame.image.load("assets/char/player/player_idle.png")
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,255,0))
        self.rect = self.surf.get_rect()
    def move(self):
        self.accel = vec(0,0.5)
        key_event = pygame.key.get_pressed()
        if key_event[K_LEFT]:
            self.accel.x = -ACC
        if key_event[K_RIGHT]:
            self.accel.x = ACC
        self.accel.x += self.vel.x * FRIC
        self.vel += self.accel
        self.pos += self.vel + 0,5 * self.accel

