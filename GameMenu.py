import pygame

class GameMenu():
    def __init__(self, font, font_color, menu_list, screen, background, titulo, font_titulo):
        self.font = font
        self.font_color = font_color

        self.font_titulo = font_titulo


        self.menu_list = []
        self.background = pygame.transform.smoothscale(background, screen.get_rect().size)
        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.titulo = font_titulo.render(titulo, True, font_color)

        for index, item in enumerate(menu_list):
            text = font.render(item, True, font_color)


            height = text.get_height()
            width = text.get_width()

            itemx = (self.screen_width / 2) - (width /2)
            menu_h = len(menu_list) * height
            itemy = (self.screen_height /2) - (menu_h /2) + (index*(10 + height))

            self.menu_list.append([item, text, (width, height), (itemx, itemy)])

        titulo_posx = (screen.get_rect().width / 2) - (self.titulo.get_rect().width / 2)
        titulo_posy = self.menu_list[0][3][1] - 200

        self.menu_list.append([titulo, self.titulo, self.titulo.get_rect().size, (titulo_posx, titulo_posy)])
        self.list_size = len(self.menu_list)

    def draw_menu(self):
        #funcao que desenha o menu
        self.screen.fill((255,255,255))
        self.screen.blit(self.background,(0,0))
        
        for inf in self.menu_list:
            self.screen.blit(inf[1], inf[3])


    def mouse_click(self, position_m, x, y, width, height):
        #funcao que "ve" se o rato clicou na figura dada
        return position_m[0] >= x and position_m[0] < (x + width) and position_m[1] >= y and position_m[1] < y + height
