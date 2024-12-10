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
    bar_left = Bar(SCREEN_WIDTH/10,SCREEN_HEIGHT/2, pygame.Color("#FEFAD4"))
    bar_right = Bar((9/10)*SCREEN_WIDTH,SCREEN_HEIGHT/2, "#FCD0BA")
    background = Background()
    
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False
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
                if self.ball.won() == "right":
                    self.background.right_won(self.screen, self.bar_left, self.bar_right)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
