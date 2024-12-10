import pygame

class Background:
    def __init__(self, width, height):
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.color = "beige"
    
    def draw(self, screen):
        screen.fill(pygame.Color(self.color))