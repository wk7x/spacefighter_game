import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision_detector(self, other_circle):
        pos_1 = self.position
        pos_2 = other_circle.position
        distance = pos_1.distance_to(pos_2)
        return distance <= self.radius + other_circle.radius