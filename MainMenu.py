import pygame, ctypes, sys, os.path
from pygame.locals import *
from GameMenu import GameMenu
from Hero import Hero
from NewLevels import NewLevels
from ScoreBoard import ScoreBoard

class MainMenu(GameMenu):
    def __init__(self, screen, CUSTOMEVENT, SPANEVENT):

        self.SPANEVENT = SPANEVENT
        self.CUSTOMEVENT = CUSTOMEVENT
        self.Hero_speed = 6
        self.HeroX_Initial = 300
        self.HeroY_Initial = 250
        self.font_score = pygame.font.Font('font/kenvector_future_thin.ttf', 45)

        font = pygame.font.Font('font/kenvector_future_thin.ttf', 50)
        font_color = (66,196,225)
        menu_list = ("New Game", "God Mode", "Exit")
        background = pygame.image.load("art/space.jpg").convert()
        font_titulo = pygame.font.Font('font/kenvector_future_thin.ttf', 80)

        self.ScoreBoard = ScoreBoard(screen, background)

        if os.path.isfile("savegame"):
            self.ScoreBoard = ScoreBoard.loadScore(self.ScoreBoard)




        super(MainMenu,self).__init__(font, font_color, menu_list, screen, background, "Fatchuranz", font_titulo)


    def draw_menu(self):
        super(MainMenu, self).draw_menu()

        score = self.ScoreBoard.getbestscore()
        text = self.font_score.render(score, True, self.font_color)
        rect = text.get_rect()

        scorex = (self.screen.get_rect().width / 2) - (rect.width / 2)
        scorey = self.menu_list[self.list_size - 2 ][3][1] + 150

        self.screen.blit(text, (scorex, scorey))

        pygame.display.flip()


    def treat_click(self):
        #funcao que trata o evento de quando o rato e clicado
        pos = pygame.mouse.get_pos()

        #verifica se novo jogo e caregado
        if self.mouse_click(pos, self.menu_list[0][3][0], self.menu_list[0][3][1],
        self.menu_list[0][2][0], self.menu_list[0][2][1]):
            self.click_sound()
            Hero_ship = Hero(30, self.Hero_speed, self.HeroX_Initial, self.HeroY_Initial, "art/HeroShips/heroship_level1.png")
            level = NewLevels(Hero_ship, self.screen , self.CUSTOMEVENT, self.SPANEVENT, self.ScoreBoard)
            level.run_game()


        #verifica se Gode Mode e carregado
        elif self.mouse_click(pos, self.menu_list[1][3][0], self.menu_list[1][3][1],
        self.menu_list[1][2][0], self.menu_list[1][2][1]):
            self.click_sound()
            Hero_ship = Hero(25, self.Hero_speed, self.HeroX_Initial, self.HeroY_Initial, "art/HeroShips/heroship_level1.png")
            level = NewLevels(Hero_ship, self.screen , self.CUSTOMEVENT, self.SPANEVENT, self.ScoreBoard)
            Hero_ship.god_mode = True
            level.run_game()

        #verifica se Exit e carregado
        elif self.mouse_click(pos, self.menu_list[2][3][0], self.menu_list[2][3][1],
        self.menu_list[2][2][0], self.menu_list[2][2][1]):
            self.click_sound()
            pygame.quit()
            sys.exit()

    def treat_event(self):
        #funcao que trata os eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.treat_click()
        return False

    def run_main_menu(self):
        #funcao que corre o ciclo principal do main menu
        done = False
        FPS = pygame.time.Clock()

        while not done:
            done = self.treat_event()
            self.draw_menu()

            FPS.tick(60)

        pygame.quit()

    def click_sound(self):
        level_up = pygame.mixer.Sound("sound/click1.wav")
        level_up.set_volume(0.1)
        level_up.play()
