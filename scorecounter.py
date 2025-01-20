import pygame
from constants import *

class ScoreCounter:
    def __init__(self, initial_count=0):
        self.count = initial_count
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 224)
    
    def addscore(self):
        self.count += 1

    def render(self, screen):
        text = self.font.render(f"Score: {self.count}", True, self.color)
        text_rect = text.get_rect(midtop=(SCREEN_WIDTH / 2, 20))
        screen.blit(text, text_rect)