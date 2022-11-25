import pygame as pg

pg.init()

# game options/settings/FONT
TITLE = "COOKINGGAME"
WIDTH = 800
HEIGHT = 600
FPS = 60
TIME = pg.time.get_ticks()

#display MODE
MODE = 0
COOKMODE = 0
#select FONT
FONT = pg.font.Font('font/malgun.ttf', 25)
GAMETITLEFONT = pg.font.Font('font/malgun.ttf', 50)
SUBGAMETITLEFONT = pg.font.Font('font/malgun.ttf', 25)
#image/background
OPENINGTURNOFFIMG = pg.image.load('background/opening_turnoff.png')
OPENINGIMG = pg.image.load('background/opening.png')
STARTIMG = pg.image.load('background/start.png')
#image/icon/
GAMESTARTBUTTON = pg.image.load('icon/game_start.png')
GAMESTARTBUTTONPRESSED = pg.image.load('icon/game_start_press.png')
MENUSELECT = pg.image.load('icon/menu_select.png')
MENUSELECTHIGHLIGHT = pg.image.load('icon/menu_select_highlight.png')


# define colors
DARK_GRAY = (122,122,146)
LIGHT_GRAY = (232,233,238)
GRAY = (196,199,208)
BLACK = (0,0,0)
IVORY = (247,247,247)