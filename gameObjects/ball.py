import pygame

class Ball:
    def __init__(self):
        self.__SCREEN_WIDTH = pygame.display.Info().current_w
        self.__SCREEN_HEIGHT = pygame.display.Info().current_h
        self.x = self.__SCREEN_WIDTH/2
        self.y = self.__SCREEN_HEIGHT/2
        self.radius = self.__SCREEN_WIDTH/50
        self.color = "purple"
        self.dx = 5
        self.dy = -5

    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self, other):
        self.x += self.dx
        self.y += self.dy
        if self.y <= 0 or self.y >= self.__SCREEN_HEIGHT - self.radius:
            self.dy = -self.dy
        if self.x <= 0 or self.x >= self.__SCREEN_WIDTH - self.radius:
            self.dx = -self.dx
        if self.rect.colliderect(other.rect):
            if abs(self.rect.top - other.rect.bottom) <= self.dy or abs(self.rect.bottom - other.rect.top) <= self.dy:
                self.dy = -self.dy
            if abs(self.rect.left - other.rect.right) <= self.dx or abs(self.rect.right - other.rect.left) <= self.dx:
                self.dx = -self.dx


    