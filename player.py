import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot, MegaBlast

class Player(CircleShape):
    def __init__(self, x, y, power_up_counter):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.power_up_counter = power_up_counter

    # generate triangle coordinates
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, "purple", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vector * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_e]:
            self.mega_blast()
        self.timer -= dt
        

    def shoot(self):
        if self.timer > 0:
            return
        laser = Shot(self.position.x, self.position.y)
        laser.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.timer = PLAYER_SHOT_COOLDOWN

    def mega_blast(self):
        if self.timer > 0:
            return
        if self.power_up_counter.count == 0:
            return
        laser = MegaBlast(self.position.x, self.position.y)
        laser.velocity = pygame.Vector2(0,1).rotate(self.rotation) * MEGA_BLAST_SPEED
        self.timer = MEGA_BLAST_COOLDOWN
        self.power_up_counter.use_powerup()