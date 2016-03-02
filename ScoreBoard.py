import pygame
from pygame.locals import *
import pickle
from eztext import Input
from GameOver import GameOver

class ScoreBoard():
    def __init__(self, screen, background):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.font = pygame.font.Font('font/kenvector_future_thin.ttf', 20)
        self.font_gameover = pygame.font.Font('font/kenvector_future_thin.ttf', 60)
        self.color = (66,196,225)
        self.bestscore = 0
        self.bestplayer = "None"
        self.value = 0
        self.background = background
        self.gameover = GameOver(self.screen)
        

    def saveScore(self, scoreBoard):
        with open("savegame", "wb") as f:
            pickle.dump(scoreBoard, f)

    @staticmethod
    def loadScore(scoreBoard):
        with open("savegame", "rb") as f:
            score = pickle.load(f)
            scoreBoard.bestscore = score[0]
            scoreBoard.bestplayer = score[1]
        return scoreBoard

    def getbestscore(self):
        return "#1" + " " + self.bestplayer + "   " + str(self.bestscore) + " " +"pts"


    def drawback(self):
        self.screen.blit(self.background,(0,0))
        text = self.font_gameover.render("New Record!", True, self.color)
        posx = self.screen_width / 2 - (text.get_rect().width / 2)
        self.screen.blit(text, (posx, 200))



    def newName(self, score):
        if score > self.bestscore:
            self.bestscore = score
            self.bestplayer = self.getname()
            self.saveScore((self.bestscore,self.bestplayer));
        else:
            self.gameover.run_gameOver()


    def getname(self):

        posx = ((self.screen_width / 2) - len("Escreva o seu nome:") * 10)
        posy = self.screen_height / 2


        ez = Input(x = posx, y = posy, font = self.font,
                   color = self.color, maxlength = 10,
                   prompt = "Escreva o seu nome:")

        clock = pygame.time.Clock()

        while 1:
            # make sure the program is running at 30 fps
            clock.tick(30)

            # events for txtbx
            events = pygame.event.get()
            # process other events
            for event in events:
                # close it x button si pressed
                if event.type == QUIT: return ez.value

                # update txtbx
                self.value = ez.update(events)
                # blit txtbx on the sceen
                self.drawback()
                ez.draw(self.screen)
                # refresh the display
                pygame.display.flip()
            if self.value == 1:
                return ez.value
