import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 224), self.position, self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt

class MegaBlast(Shot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = MEGA_BLAST_RADIUS
        self.velocity = MEGA_BLAST_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, (57, 255, 20), self.position, self.radius, 1)
