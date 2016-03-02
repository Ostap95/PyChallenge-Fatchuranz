import pygame, math, Utils, ctypes
from pygame.locals import *
from Hero import Hero
from EnemyShip import EnemyShip
from Bullet import Bullet
from NewLevels import NewLevels
from MainMenu import MainMenu

CUSTOMEVENT = USEREVENT + 1
SPANEVENT = USEREVENT + 1

def main():
    global FPSClOCK, DISPLAYSURF, CUSTOMEVENT
    pygame.init() # Pygame initialization
    pygame.mixer.init()

    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Fatchuranz")

    pygame.mixer.music.load('sound/gamemusic.mp3')
    pygame.mixer.music.play(100)
    pygame.mixer.music.set_volume(0.1)

    mainmenu = MainMenu(DISPLAYSURF, CUSTOMEVENT, SPANEVENT)
    mainmenu.run_main_menu()

if __name__ == '__main__':
    main()
