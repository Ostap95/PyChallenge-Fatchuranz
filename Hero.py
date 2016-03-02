import pygame
class Hero(pygame.sprite.Sprite):
    # This class represents the SpaceShip
    def __init__(self, lifes, speed, x_initial, y_initial, picture, score = 0, widht = 50, height = 50):
        # Constructor
        # lifes: life of the hero | score: score of the hero
        super().__init__()
        self.height = height
        self.widht = widht
        self.picture = pygame.image.load(picture)
        self.image = self.picture
        self.image = pygame.transform.smoothscale(self.image, (widht, height))
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()
        self.life = lifes
        self.score = score
        self.speed = speed
        self.rect.x = x_initial
        self.rect.y = y_initial
        self.angle = 0
        self.god_mode = False
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_angle(self, angle):
        self.image = self.picture
        self.image = pygame.transform.smoothscale(self.image, (self.widht, self.height))
        self.image = pygame.transform.rotozoom(self.image, angle, 1)
        self.angle = angle

    def change_image(self, image):
        self.picture = pygame.image.load(image)
        self.image = self.picture
        self.image = pygame.transform.smoothscale(self.image, (self.widht, self.height))
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)

    def move_Up(self, speed, dimension):
        if self.rect.y > 0:
            self.rect.y -= speed

    def move_Down(self, speed, dimension):
        if self.rect.y < dimension[1] - 50:
            self.rect.y += speed

    def move_Right(self, speed, dimension):
        if self.rect.x < dimension[0] - 50:
            self.rect.x += speed

    def move_Left(self, speed, dimension):
        if self.rect.x > 0:
            self.rect.x -= speed

