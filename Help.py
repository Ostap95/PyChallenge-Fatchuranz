import pygame, sys
from pygame.locals import *

class Help:
    def __init__(self, screen):
        self.background = pygame.image.load("art/space.jpg").convert()
        font = pygame.font.Font('font/kenvector_future_thin.ttf', 50)
        self.screen = screen
        self.text = font.render("Boa", True, (255,255,255))
        x = 500
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            self.text = font.render(str(x), True, (255,255,255))
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.text,(100,100))
            pygame.display.flip()
            
        return
