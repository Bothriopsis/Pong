from gameObjects.ball import Ball
from gameObjects.bar import Bar
from gameObjects.background import Background

import pygame

class Game:
    pygame.init()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h
    ball = Ball()
    bar = Bar(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 20, 100)
    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.ball = Ball()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.ball.draw(self.screen)
            self.bar.draw(self.screen)
            self.ball.move(self.bar)
            pygame.display.flip()
            self.clock.tick(60)
