import pygame, Utils

class Bullet(pygame.sprite.Sprite):

    def __init__(self, png, direction, speed, Figure):
        super().__init__()
        self.angle = Utils.get_angle((Figure.rect.x, Figure.rect.y), direction)
        self.image = pygame.Surface([5,5])
        self.image = pygame.image.load(png)
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        self.rect = self.image.get_rect()
        self.direction = direction
        self.speed = speed


    def update(self):
        self.rect.x += Utils.project(self.angle, self.speed)[0]
        self.rect.y += Utils.project(self.angle, self.speed)[1]
