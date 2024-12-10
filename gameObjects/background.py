import pygame

class Background:
    def __init__(self):
        self.color = "#F1828D"
    
    def draw(self, screen):
        screen.fill(self.color)

    def right_won(self, screen, other_1, other_2):
        self.color = "black"
        self.font = pygame.font.Font("resources/Tiny5-Regular.ttf", 300)
        self.text = self.font.render("LEFT WON", True, "white")
        self.text_rect = self.text.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2))
        screen.blit(self.text, self.text_rect)
        other_1.color = "beige"
        other_2.color = "beige"
    
    def left_won(self, screen, other_1, other_2):
        self.color = "white"
        self.font = pygame.font.Font("resources/Tiny5-Regular.ttf", 300)
        self.text = self.font.render("RIGHT WON", True, "black")
        self.text_rect = self.text.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2))
        screen.blit(self.text, self.text_rect)
        other_1.color = "dark gray"
        other_2.color = "dark gray"

