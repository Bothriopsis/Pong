import pygame

class Bar:
    def __init__(self, x, y, color):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.x = x
        self.y = y
        self.width = SCREEN_WIDTH/100
        self.height = SCREEN_HEIGHT/5
        self.color = color
        self.dy = 20
    
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.y -= self.dy
        if keys[down]:
            self.y += self.dy
    
    def collision(self, other):
        if self.rect.colliderect(other.rect):
            if abs(self.rect.top - other.rect.bottom) <= abs(other.dy) or abs(self.rect.bottom - other.rect.top) <= abs(other.dy):
                other.dy = -other.dy
            if abs(self.rect.left - other.rect.right) <= abs(other.dx) or abs(self.rect.right - other.rect.left) <= abs(other.dx):
                other.dx = -other.dx * 1.2