import pygame

from states.mainScreen import MainScreen
from states.active import ActiveGame

class Game:
    pygame.init()
    active = ActiveGame()
    mainScreen = MainScreen()

    def __init__(self):
        self.running = True
        
    def run(self):
        mainScreen = MainScreen()
        activeGame = ActiveGame()
        while self.running:
            if mainScreen.active:
                mainScreen.run()
            if activeGame.active:
                activeGame.run()
            if activeGame.running == False or mainScreen.running == False:
                self.running = False
        pygame.quit()