import pygame, math, Utils

class EnemyShip(pygame.sprite.Sprite):
    # Class tha represents the enemy ships
    def __init__(self, picture, speed = 2.5, widht = 50, height = 50):
        # Constructor
        super().__init__()
        self.widht = widht
        self.height = height
        self.picture = pygame.image.load(picture)
        self.image = self.picture
        self.speed = speed
        self.image = pygame.transform.smoothscale(self.image, (self.widht, self.height))
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()

    def change_picture(self, picture):
        self.picture = pygame.image.load(picture)
        self.image = pygame.transform.smoothscale(self.picture, (self.widht, self.height))
        self.image = pygame.transform.rotozoom(self.image, 0, 1)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_angle(self, angle):
        self.image = self.picture
        self.image = pygame.transform.smoothscale(self.image, (self.widht, self.height))
        self.image = pygame.transform.rotozoom(self.image, angle, 1)

    def follow(self, player):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
            # move along this normalized vector towards the player at current speed
            self.rect.x -= dx * self.speed
            self.rect.y -= dy * self.speed
            angle = Utils.get_angle(self.rect, player.rect)
            self.update_angle(angle)
