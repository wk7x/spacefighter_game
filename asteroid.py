import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (173, 216, 230), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
