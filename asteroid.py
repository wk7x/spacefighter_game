import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (173, 216, 230), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        randnum = random.uniform(20,50)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        vector1= self.velocity.rotate(randnum)
        vector2= self.velocity.rotate(-randnum)
        asteroid1 = Asteroid(self.position.x, self.position.y, newradius)
        asteroid1.velocity = vector1*1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, newradius)
        asteroid2.velocity = vector2*1.2

        return [asteroid1, asteroid2]