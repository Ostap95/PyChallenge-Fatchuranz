import pygame
import  random
from Hero import Hero
from EnemyShip import EnemyShip
def LevelSelect(Caller, events):
    if Caller.level == 1:
        for event in events:
            if event.type == Caller.span:
                if Caller.level1 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy1.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level1 = Caller.level1 - 1
            if Caller.level1 == 0 and len(Caller.enemies_group) == 0:
                levelChange(Caller, 2)
                speedChangH(Caller, 1)
                speedChangI(Caller, 1)

    elif Caller.level == 2:
        Caller.hero.change_image("art/HeroShips/heroship_level2.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1160)
        for event in events:
            if event.type == Caller.span:
                if Caller.level2 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy2.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level2 = Caller.level2 - 1
            if Caller.level2 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 3)
                speedChangH(Caller, 1)
                speedChangI(Caller, 1)

    elif Caller.level == 3:
        Caller.hero.change_image("art/HeroShips/heroship_level3.png")
        for event in events:
            if event.type == Caller.span:
                if Caller.level3 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy3.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level3 = Caller.level3 - 1
            if Caller.level3 == 0 and len(Caller.enemies_group) == 0:
                levelChange(Caller, 4)

    elif Caller.level == 4:
        Caller.hero.change_image("art/HeroShips/heroship_level4.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1140)
        for event in events:
            if event.type == Caller.span:
                if Caller.level4 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy4.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level4 = Caller.level4 - 1
            if Caller.level4 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 5)
                speedChangH(Caller, 1)
                speedChangI(Caller, 1)

    elif Caller.level == 5:
        Caller.hero.change_image("art/HeroShips/heroship_level5.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1120)
        for event in events:
            if event.type == Caller.span:
                if Caller.level5 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy5.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level5 = Caller.level5 - 1
            if Caller.level5 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 6)

    elif Caller.level == 6:
        Caller.hero.change_image("art/HeroShips/heroship_level6.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1100)
        for event in events:
            if event.type == Caller.span:
                if Caller.level6 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy6.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level6 = Caller.level6 - 1
            if Caller.level6 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 7)
                speedChangH(Caller, 1)
                speedChangI(Caller, 1)

    elif Caller.level == 7:
        Caller.hero.change_image("art/HeroShips/heroship_level7.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1080)
        for event in events:
            if event.type == Caller.span:
                if Caller.level7 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy7.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level7 = Caller.level7 - 1
            if Caller.level7 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 8)
                speedChangI(Caller, 1)

    elif Caller.level == 8:
        Caller.hero.change_image("art/HeroShips/heroship_level8.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1040)
        for event in events:
            if event.type == Caller.span:
                if Caller.level8 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy8.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level8 = Caller.level8 - 1
            if Caller.level8 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 9)


    elif Caller.level == 9:
        Caller.hero.change_image("art/HeroShips/heroship_level9.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 1000)
        for event in events:
            if event.type == Caller.span:
                if Caller.level9 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy9.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level9 = Caller.level9 - 1
            if Caller.level9 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 10)
                speedChangI(Caller, 1)

    elif Caller.level == 10:
            Caller.hero.change_image("art/HeroShips/heroship_level10.png")
            if Caller.begin_level == 1:
                Caller.begin_level = 0
                change_time(Caller, 950)
            for event in events:
                if event.type == Caller.span:
                    if Caller.level10 > 0:
                        Caller.enemy = EnemyShip("art/EnemyShip/enemy10.png")
                        Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                        Caller.enemies_group.add(Caller.enemy)
                        Caller.all_groups.add(Caller.enemies_group)
                        Caller.level10 = Caller.level10 - 1
                if Caller.level10 == 0 and len(Caller.enemies_group) == 0:
                    Caller.begin_level = 1
                    levelChange(Caller, 11)

    elif Caller.level == 11:
        Caller.hero.change_image("art/HeroShips/heroship_level11.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 850)
        for event in events:
            if event.type == Caller.span:
                if Caller.level11 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy11.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level11 = Caller.level11 - 1
            if Caller.level11 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 12)
                speedChangI(Caller, 1)

    elif Caller.level == 12:
        Caller.hero.change_image("art/HeroShips/heroship_level12.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 800)
        for event in events:
            if event.type == Caller.span:
                if Caller.level12 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy12.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level12 = Caller.level12 - 1
            if Caller.level12 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 13)

    elif Caller.level == 13:
        Caller.hero.change_image("art/HeroShips/heroship_level13.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 760)
        for event in events:
            if event.type == Caller.span:
                if Caller.level13 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy13.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level13 = Caller.level13 - 1
            if Caller.level13 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 14)

    elif Caller.level == 14:
        Caller.hero.change_image("art/HeroShips/heroship_level14.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 740)
        for event in events:
            if event.type == Caller.span:
                if Caller.level14 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy14.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level14 = Caller.level14 - 1
            if Caller.level14 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 15)

    elif Caller.level == 15:
        Caller.hero.change_image("art/HeroShips/heroship_level15.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 720)
        for event in events:
            if event.type == Caller.span:
                if Caller.level15 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy15.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level15 = Caller.level15 - 1
            if Caller.level15 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 16)

    elif Caller.level == 16:
        Caller.hero.change_image("art/HeroShips/heroship_level16.png")
        if Caller.begin_level == 1:
            Caller.begin_level = 0
            change_time(Caller, 650)
        for event in events:
            if event.type == Caller.span:
                if Caller.level16 > 0:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy16.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)
                    Caller.level16 = Caller.level16 - 1
            if Caller.level16 == 0 and len(Caller.enemies_group) == 0:
                Caller.begin_level = 1
                levelChange(Caller, 17)
                speedChangI(Caller, 1)

    elif Caller.level == 17:
        Caller.hero.change_image("art/HeroShips/heroship_level8.png")
        pygame.mixer.music.queue('sound/gamemusic.mp3')
        for event in events:
            if event.type == Caller.span:
                if len(Caller.enemies_group) < 13:
                    Caller.enemy = EnemyShip("art/EnemyShip/enemy17.png")
                    Caller.enemy.set_position(random.randrange(0,Caller.scree_res[0]), random.randrange(0,Caller.scree_res[1]))
                    Caller.enemies_group.add(Caller.enemy)
                    Caller.all_groups.add(Caller.enemies_group)



def levelChange(Caller, new_level):
    # Caller: caller class. new_level: neext level. speed_next: next speed
    pygame.mixer.music.queue('sound/gamemusic.mp3')
    Caller.level = new_level
    Caller.level_upSound()

def speedChangH(Caller, speed_next):
    Caller.hero.speed = Caller.hero.speed + speed_next

def speedChangI(Caller, speed_next):
    Caller.enemy.speed = Caller.enemy.speed + speed_next

def change_time(Caller, time):
    pygame.time.set_timer(Caller.span, time)
