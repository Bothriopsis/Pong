import pygame

class Bar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "white"
        self.dy = 10
    
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.x += self.dy
        if keys[pygame.K_DOWN]:
            self.x -= self.dy