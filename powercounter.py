import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot

class PowerUpCounter:
    def __init__(self, initial_count=3):
        self.count = initial_count
        self.font = pygame.font.Font(None, 36)
        self.color = (0, 255, 0)
        self.last_recharge_time = pygame.time.get_ticks()
    
    def use_powerup(self):
        self.count -= 1
        if self.count == 2:
            self.last_recharge_time = pygame.time.get_ticks()

    def recharge(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_recharge_time >= 15000):
            if self.count < 3:
                self.count += 1
                self.last_recharge_time = current_time

    def render(self, screen):
        text = self.font.render(f"Mega-Blasts [E]: {self.count}", True, self.color)
        text_rect = text.get_rect(bottomleft=(20, SCREEN_HEIGHT - 60))
        screen.blit(text, text_rect)