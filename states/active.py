from gameObjects.ball import Ball
from gameObjects.bar import Bar
from gameObjects.background import Background

import pygame

class ActiveGame:
    pygame.init()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball()
    bar_left = Bar(SCREEN_WIDTH/10,SCREEN_HEIGHT/2, pygame.Color("#D9B400"))
    bar_right = Bar((9/10)*SCREEN_WIDTH,SCREEN_HEIGHT/2, "#B58845")
    background = Background()
    
    def __init__(self):
        self.running = True
        self.active = False

    def run(self):
        while self.running:
            keys = pygame.key.get_pressed()
            self.background.draw(self.screen)
            self.ball.draw(self.screen)
            self.bar_left.draw(self.screen)
            self.bar_left.move(pygame.K_w, pygame.K_s)
            self.bar_right.draw(self.screen)
            self.bar_right.move(pygame.K_UP,pygame.K_DOWN)
            self.bar_left.collision(self.ball)
            self.bar_right.collision(self.ball)
            self.ball.move()
            if self.ball.won() != None:
                if self.ball.won() == "left":
                    self.background.left_won(self.screen, self.bar_left, self.bar_right)
                    if keys[pygame.K_SPACE]:
                        self.active = False
                if self.ball.won() == "right":
                    self.background.right_won(self.screen, self.bar_left, self.bar_right)
                    if keys[pygame.K_SPACE]:
                        self.active = False
            pygame.display.flip()
            self.clock.tick(165)
        pygame.quit()
