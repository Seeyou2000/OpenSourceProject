import pygame as pg

pg.init()

# game options/settings/FONT
TITLE = "COOKINDOOR"
WIDTH = 800
HEIGHT = 600
FPS = 60
TIME = pg.time.get_ticks()

#display MODE
MODE = 0
COOKMODE = 0
#select FONT
FONT = pg.font.Font('font/malgunbd.ttf', 25)
GAMETITLEFONT = pg.font.Font('font/malgunbd.ttf', 50)
SUBGAMETITLEFONT = pg.font.Font('font/malgunbd.ttf', 25)
#image/background
OPENINGTURNOFFIMG = pg.image.load('image/background/opening_turnoff.png')
OPENINGIMG = pg.image.load('image/background/opening.png')
STARTIMG = pg.image.load('image/background/start.png')
STIR = pg.image.load('image/background/stir_background.png')
CUT = pg.image.load('image/background/stir_background.png')
MICRO = pg.image.load('image/background/micro_background.png')
POT = pg.image.load('image/background/pot_background.png')
PAN = pg.image.load('image/background/pan_background.png')
SCORE = pg.image.load('image/background/score_background.png')
#image/icon/
GAMESTARTBUTTON = pg.image.load('image/icon/game_start.png')
GAMESTARTBUTTONPRESSED = pg.image.load('image/icon/game_start_press.png')
MENUSELECT = pg.image.load('image/icon/menu_select.png')
MENUSELECTHIGHLIGHT = pg.image.load('image/icon/menu_select_highlight.png')


# define colors
DARK_GRAY = (122,122,146)
LIGHT_GRAY = (232,233,238)
GRAY = (196,199,208)
BLACK = (0,0,0)
IVORY = (247,247,247)


# captions of recipe
# fried_rice
FRIEDRICE1 = '그릇에 참치, 참치양념을 모두 넣어 잘 섞어주세요.'
FRIEDRICE2 = '양파를 잘게 썰어주세요.'
FRIEDRICE3 = '비빈참치에 다진양파, 밥, 밥양념재료를 넣어 섞어주세요.'
FRIEDRICE4 = '전자레인지에 5분간 돌려 완성합니다.'

# jjajang
JJAJANG1 = '볼에 물, 짜장가루를 넣고 섞어줍니다.'
JJAJANG2 = '전자레인지에 1분간 돌려줍니다.'
JJAJANG3 = '면을 넣고 양념물이 잘 묻을 수 있게 섞어줍니다.'
JJAJANG4 = '전자레인지에 3분간 돌린 후 다시 2분간 돌려 완성합니다.'

# topped_rice
TOPPEDRICE1 = '먼저 대파를 썰어주세요.'
TOPPEDRICE2 = '햄도 썰어줍니다.'
TOPPEDRICE3 = '기름을 두르고 파, 마늘, 햄을 볶아줍니다.'
TOPPEDRICE4 = '양념, 물, 체다치즈 반 장을 넣고 끓여줍니다. 물이 흥건하면 안돼요.'

# potato_pancake
POTATOPANCAKE1 = '감자 2개를 채썰어준다.'
POTATOPANCAKE2 = '팬에 기름을 두르고 약불에서 감자를 얹어줍니다.'