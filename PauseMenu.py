import pygame, sys
from pygame.locals import *
from GameMenu import GameMenu

class PauseMenu(GameMenu):
    def __init__(self,screen):
        font = pygame.font.Font('font/kenvector_future_thin.ttf', 50)
        font_pause = pygame.font.Font('font/kenvector_future_thin.ttf', 80)
        font_color = (66,196,225)
        menu_list = ("Continue", "Main Menu", "Exit")

        background = pygame.Surface((screen.get_rect().size))
        background.fill((0,0,0))

        super(PauseMenu,self).__init__(font, font_color, menu_list, screen, background, "Game Paused", font_pause)

        self.pause = font_pause.render("Game Paused",True, (66,196,225))
        pause_posx = (screen.get_rect().width / 2) - (self.pause.get_rect().width / 2)
        pause_posy = self.menu_list[0][3][1] - 200
        self.pause_pos = (pause_posx, pause_posy)

    def draw_menu(self):
    #funcao que desanha o menu de pausa

        self.background.set_alpha(100)
        self.screen.blit(self.background,(0,0))

        self.screen.blit(self.pause, self.pause_pos)
        for inf in self.menu_list:
            self.screen.blit(inf[1], inf[3])

        pygame.display.flip()

    def treat_click(self):
        #funcao que trata o evento de quando o rato e clicado
        pos = pygame.mouse.get_pos()

        #verifica se Continue e caregado
        if self.mouse_click(pos, self.menu_list[0][3][0], self.menu_list[0][3][1],
        self.menu_list[0][2][0], self.menu_list[0][2][1]):
            return (True,False)

        #verifica se MainMenu e carregado
        elif self.mouse_click(pos, self.menu_list[1][3][0], self.menu_list[1][3][1],
        self.menu_list[1][2][0], self.menu_list[1][2][1]):
            return (True,True)

        #verifica se Exit e carregado
        elif self.mouse_click(pos, self.menu_list[2][3][0], self.menu_list[2][3][1],
        self.menu_list[2][2][0], self.menu_list[2][2][1]):
            pygame.quit()
            sys.exit()

        return(False, False)

    def treat_event(self):
        #funcao que trata os eventos
        exit = (False,False) #o primeiro boleano premite sair do pause menu, o segundo do jogo

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit = (True,False)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                exit = self.treat_click()
        return exit

    def run_pause_menu(self):
        #funcao que corre o ciclo principal do main menu
        done = (False,False)
        FPS = pygame.time.Clock()

        self.draw_menu()

        while not done[0]:
            done = self.treat_event()


            FPS.tick(60)

        return done[1] #retorna se o jogo termina ou nao
