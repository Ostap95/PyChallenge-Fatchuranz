import pygame, sys
from pygame.locals import *
from GameMenu import GameMenu

class GameOver(GameMenu):
    def __init__(self,screen):
        font = pygame.font.Font('font/kenvector_future_thin.ttf', 50)
        font_over = pygame.font.Font('font/kenvector_future_thin.ttf', 80)
        font_color = (66,196,225)
        menu_list = ("Main Menu","Exit")
        background = pygame.image.load("art/space.jpg").convert()
        self.screen = screen

        super(GameOver,self).__init__(font, font_color, menu_list, self.screen, background, "Game Over", font_over)

    def treat_click(self):
        #funcao que trata o evento de quando o rato e clicado
        pos = pygame.mouse.get_pos()

        #verifica se MainMenu e caregado
        if self.mouse_click(pos, self.menu_list[0][3][0], self.menu_list[0][3][1],
        self.menu_list[0][2][0], self.menu_list[0][2][1]):
            return True

        #verifica se Exit e carregado
        elif self.mouse_click(pos, self.menu_list[1][3][0], self.menu_list[1][3][1],
        self.menu_list[1][2][0], self.menu_list[1][2][1]):
            pygame.quit()
            sys.exit()

        return False

    def treat_event(self):
        #funcao que trata os eventos
        exit = False

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                exit = self.treat_click()
        return exit


    def run_gameOver(self):
        #funcao que corre o ciclo principal do main menu
        done = False
        FPS = pygame.time.Clock()

        while not done:
            done = self.treat_event()
            self.draw_menu()

            pygame.display.flip()

            FPS.tick(60)

        return
