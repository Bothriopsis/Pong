from gameObjects.ball import Ball
from gameObjects.bar import Bar
from gameObjects.background import Background

import pygame

class ActiveGame:
    pygame.init()
    def __init__(self):
        self.running = True
        self.active = False
    
    def properties(self):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.ball = Ball()
        self.bar_left = Bar(SCREEN_WIDTH/10,SCREEN_HEIGHT/2, pygame.Color("#D9B400"))
        self.bar_right = Bar((9/10)*SCREEN_WIDTH,SCREEN_HEIGHT/2, "#B58845")
        self.background = Background()
        self.active = True


    def run(self, other):
        while self.active:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False
                    self.active = False
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
                        other.active = True
                if self.ball.won() == "right":
                    self.background.right_won(self.screen, self.bar_left, self.bar_right)
                    if keys[pygame.K_SPACE]:
                        self.active = False
                        other.active = True
            pygame.display.flip()
            self.clock.tick(165)
