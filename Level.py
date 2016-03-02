import pygame
class Level(object):
    def __init__(self):
        self.font = pygame.font.Font('font/kenvector_future_thin.ttf', 24)
        self.background = pygame.image.load("art/space.jpg").convert()
        self.score_text = None
        self.life_text = None
        self.level_text = None
        self.speed_text = None
        self.begin_level = 1
        self.level1 = 10 # Number of enemies in level 1
        self.level2 = 10 # Number of enemies in level 2
        self.level3 = 10 # Number of enemies in level 3
        self.level4 = 10
        self.level5 = 10
        self.level6 = 10
        self.level7 = 10
        self.level8 = 15
        self.level9 = 15
        self.level10 = 15
        self.level11 = 15
        self.level12 = 15
        self.level13 = 20
        self.level14 = 20
        self.level15 = 20
        self.level16 = 30
    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
