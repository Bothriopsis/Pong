from gameObjects.ball import Ball
from gameObjects.bar import Bar
from gameObjects.background import Background

import pygame

class Game:
    pygame.init()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball()
    bar_left = Bar(SCREEN_WIDTH/10,SCREEN_HEIGHT/2, "green")
    bar_right = Bar((9/10)*SCREEN_WIDTH,SCREEN_HEIGHT/2, "red")
    bakcground = Background()
    
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False
            self.bakcground.draw(self.screen)
            self.ball.draw(self.screen)
            self.bar_left.draw(self.screen)
            self.bar_left.move(pygame.K_w, pygame.K_s)
            self.bar_right.draw(self.screen)
            self.bar_right.move(pygame.K_UP,pygame.K_DOWN)
            self.ball.move(self.bar_right)
            self.ball.move(self.bar_left)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
