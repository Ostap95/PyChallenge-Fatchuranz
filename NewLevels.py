import pygame, Utils, sys, random, LevelSelection
from EnemyShip import EnemyShip
from pygame.locals import *
from Hero import Hero
from EnemyShip import EnemyShip
from Bullet import Bullet
from Level import Level
from PauseMenu import PauseMenu
from ScoreBoard import ScoreBoard


class NewLevels(Level):
    def __init__(self, Hero, screen, custom_event, span_event, scoreBoard):
        super().__init__()
        self.level = 1
        self.scree_res = screen.get_rect().size
        self.background = pygame.transform.smoothscale(self.background, self.scree_res)
        self.hero_bullets = pygame.sprite.Group()
        self.enemy = EnemyShip("art/EnemyShip/enemy1.png")
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.all_groups = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
        self.hero = Hero
        self.hero_group.add(self.hero)
        self.all_groups.add(self.hero_group)
        self.bulletevent = custom_event
        self.span = span_event
        self.screen = screen
        self.pause = PauseMenu(self.screen)
        self.heart = pygame.image.load("art/life.png")
        self.heart = pygame.transform.smoothscale(self.heart, (30, 30))
        self.ScoreBoard = scoreBoard

        pygame.time.set_timer(self.bulletevent, 100)
        pygame.time.set_timer(self.span, 1200)


    def render(self):
        self.text_update()
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.score_text, (120,5))
        self.screen.blit(self.life_text, (50,5))
        self.screen.blit(self.level_text, (350,5))
        self.screen.blit(self.speed_text, (500,5))
        self.screen.blit(self.heart, (10, 5))
        self.all_groups.draw(self.screen)

    def update(self):
        self.hero_bullets.update()
        self.enemy_bullets.update()

        for enemy in self.enemies_group:
            enemy.follow(self.hero) # All enemies must follow the hero

        for bullet in self.enemy_bullets:
            if self.hero.life <= 0:
                self.ScoreBoard.newName(self.hero.score)
                return True

            if bullet.rect.x < -5 or bullet.rect.x > self.scree_res[0]:
                self.enemy_bullets.remove(bullet)
                self.all_groups.remove(bullet)
            elif bullet.rect.y < -5 or bullet.rect.y > self.scree_res[1]:
                self.enemy_bullets.remove(bullet)
                self.all_groups.remove(bullet)
            hit_block = pygame.sprite.spritecollide(bullet, self.hero_group, False)
            for hit in hit_block:
                if not self.hero.god_mode:
                    self.hero.life = self.hero.life - 1
                self.enemy_bullets.remove(bullet)
                self.all_groups.remove(bullet)

        for bullet in self.hero_bullets:
            if bullet.rect.x < -5 or bullet.rect.x > self.scree_res[0]:
                self.hero_bullets.remove(bullet)
                self.all_groups.remove(bullet)
            elif bullet.rect.y < -5 or bullet.rect.y > self.scree_res[1]:
                self.hero_bullets.remove(bullet)
                self.all_groups.remove(bullet)
            hit_block = pygame.sprite.spritecollide(bullet, self.enemies_group, True)
            for hit in hit_block:
                self.hero.score = self.hero.score + 5

        return False

    def handle_events(self, events):
        self.level_call(events)
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return self.pause.run_pause_menu()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_Coordinate = pygame.mouse.get_pos()
                bullet = Bullet("art/laser_hero.png", mouse_Coordinate, 15,  self.hero)
                bullet.rect.x = self.hero.rect.x + 25
                bullet.rect.y = self.hero.rect.y + 10
                self.hero_bullets.add(bullet)
                self.all_groups.add(self.hero_bullets)
                laser_sound = pygame.mixer.Sound("sound/sfx_laser1.ogg")
                laser_sound.set_volume(0.1)
                laser_sound.play()
            elif event.type == self.bulletevent:
                for enemy in self.enemies_group:
                    bullet = Bullet("art/laser_enemy.png", (self.hero.rect.x, self.hero.rect.y), 8, enemy)
                    bullet.rect.x = enemy.rect.x + 25
                    bullet.rect.y = enemy.rect.y + 10
                    self.enemy_bullets.add(bullet)
                    self.all_groups.add(self.enemy_bullets)
                    laser_sound = pygame.mixer.Sound("sound/sfx_laser2.ogg")
                    laser_sound.set_volume(0.1)
                    laser_sound.play()


        (MouseX, MouseY) = pygame.mouse.get_pos() # Gets mouse position
        angle = Utils.get_angle((self.hero.rect.x, self.hero.rect.y),(MouseX-25,MouseY)) # Calculates the angle between surface and the mouse
        self.hero.update_angle(angle) # Update the rotation of the ship

        # --------------------------- KEYBOARD BUTTONS CONTROL ----------------------------------
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] or keys_pressed[K_a]:
            self.hero.move_Left(self.hero.speed, self.scree_res)
        if keys_pressed[K_RIGHT] or keys_pressed[K_d]:
            self.hero.move_Right(self.hero.speed, self.scree_res)
        if keys_pressed[K_UP] or keys_pressed[K_w]:
            self.hero.move_Up(self.hero.speed, self.scree_res)
        if keys_pressed[K_DOWN] or keys_pressed[K_s]:
            self.hero.move_Down(self.hero.speed, self.scree_res)
        # ------------------------- END OF KEYBOARD BUTTONS CONTROL -----------------------------
        return False

    def level_call(self, events):
        LevelSelection.LevelSelect(self, events)

    def level_upSound(self):
        level_up = pygame.mixer.Sound("sound/level_up.ogg")
        level_up.set_volume(0.1)
        level_up.play()

    def text_update(self):
        self.score_text = self.font.render("Score: " + str(self.hero.score), True, (255,255,255))
        self.life_text = self.font.render(str(self.hero.life), True, (255,255,255))
        self.level_text = self.font.render("Level: " + str(self.level), True, (255,255,255))
        self.speed_text = self.font.render("Hero Speed: " + str(self.hero.speed), True, (255,255,255))



    def run_game(self):
        done = False
        FPS = pygame.time.Clock()
        while not done:

            if self.handle_events(pygame.event.get()) or self.update():
                break
            self.render()
            pygame.display.flip()

            FPS.tick(60)
