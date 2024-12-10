import pygame

class Background:
    def __init__(self):
        self.color = "#2A2A2A"
    
    def draw(self, screen):
        screen.fill(self.color)

    def right_won(self, screen, other_1, other_2):
        self.color = "#2C876C"
        self.font = pygame.font.Font("resources/Tiny5-Regular.ttf", 300)
        self.text = self.font.render("LEFT WON", True, "#3B1E51")
        self.text_rect = self.text.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2))
        self.font2 = pygame.font.Font("resources/Tiny5-Regular.ttf", 100)
        self.text2 = self.font2.render("PRESS SPACE FOR MAIN SCREEN", True, "#3B1E51")
        self.text2_rect = self.text2.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/3*2))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text2_rect)

        other_1.color = "#3AFF00"
        other_2.color = "#3AFF00"
    
    def left_won(self, screen, other_1, other_2):
        self.color = "#164E68"
        self.font = pygame.font.Font("resources/Tiny5-Regular.ttf", 300)
        self.text = self.font.render("RIGHT WON", True, "#8EF8FF")
        self.text_rect = self.text.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2))
        self.font2 = pygame.font.Font("resources/Tiny5-Regular.ttf", 100)
        self.text2 = self.font2.render("PRESS SPACE FOR MAIN SCREEN", True, "#8EF8FF")
        self.text2_rect = self.text2.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/3*2))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text2_rect)
        other_1.color = "#4AC8ED"
        other_2.color = "#4AC8ED"

    def starting_screeen(self, screen):
        self.color = "#4AC8ED"
        self.font1 = pygame.font.Font("resources/Tiny5-Regular.ttf", 300)
        self.text = self.font1.render("PONG", True, "#DAA520")
        self.text_rect = self.text.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/2))
        self.font2 = pygame.font.Font("resources/Tiny5-Regular.ttf", 100)
        self.text2 = self.font2.render("PRESS SPACE TO START", True, "#B4FFFF")
        self.text2_rect = self.text2.get_rect(center=(pygame.display.Info().current_w/2, pygame.display.Info().current_h/3*2))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text2_rect)
