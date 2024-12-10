import pygame

class Ball:
    def __init__(self):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.radius = SCREEN_WIDTH/50
        self.color = "white"
        self.dx = 10
        self.dy = -10

    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self, other):
        self.x += self.dx
        self.y += self.dy
        if self.y <= 0 or self.y >= 600:
            self.dy *= -1
        if self.x <= 0 or self.x >= 800:
            self.dx *= -1
        if self.rect.colliderect(other.rect):
            self.dx *= -1
            self.dy *= -1


    