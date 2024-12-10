from gameObjects.background import Background

import pygame

class MainScreen:
    pygame.init()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background = Background()
    
    def __init__(self):
        self.running = True
        self.active = True

    def run(self):
        while self.running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False
            self.background.draw(self.screen)
            self.background.starting_screeen(self.screen)
            pygame.display.flip()
            self.clock.tick(165)
        pygame.quit()
