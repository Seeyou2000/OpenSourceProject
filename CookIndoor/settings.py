import pygame as pg

pg.init()

# game options/settings/FONT
TITLE = "COOKINDOOR"
WIDTH = 800
HEIGHT = 600
FPS = 60
BUFFER = 10
IDX = 15
TIME = 0
JOINTPOS = [0,0]

#display MODE
MODE = 0
INGAMEMODE = 0
COOKMODE = 0
MAKEUPMODE = 1
ENDMODE = 0

#select FONT
FONT = pg.font.Font('font/malgunbd.ttf', 25)
GAMETITLEFONT = pg.font.Font('font/malgunbd.ttf', 50)
SUBGAMETITLEFONT = pg.font.Font('font/malgunbd.ttf', 25)
MENUFONTBIG = pg.font.Font('font/malgunbd.ttf', 15)
MENUFONTSMALL = pg.font.Font('font/malgunbd.ttf', 10)
#image/background
OPENINGTURNOFFIMG = pg.image.load('image/background/opening_turnoff.png')
OPENINGIMG = pg.image.load('image/background/opening.png')
STARTIMG = pg.image.load('image/background/start.png')
STIR = pg.image.load('image/background/stir_background.png')
CUT = pg.image.load('image/background/cut_background.png')
MICRO = pg.image.load('image/background/micro_background.png')
MICRO_FINISH = pg.image.load('image/background/micro_background_finish.png')
POT = pg.image.load('image/background/pot_background.png')
PAN = pg.image.load('image/background/pan_background.png')
SCORE = pg.image.load('image/background/score_background.png')
#image/background/stir_gif
STIR_COUNT = 0
STIR_GIF = [pg.image.load('image/background/stir_gif/0.png'),
            pg.image.load('image/background/stir_gif/1.png'),
            pg.image.load('image/background/stir_gif/2.png'),
            pg.image.load('image/background/stir_gif/3.png'),
            pg.image.load('image/background/stir_gif/4.png'),
            pg.image.load('image/background/stir_gif/5.png'),
            pg.image.load('image/background/stir_gif/6.png'),
            pg.image.load('image/background/stir_gif/7.png'),
            pg.image.load('image/background/stir_gif/8.png'),
            pg.image.load('image/background/stir_gif/9.png'),
            pg.image.load('image/background/stir_gif/10.png'),
            pg.image.load('image/background/stir_gif/11.png'),
            pg.image.load('image/background/stir_gif/12.png'),
            pg.image.load('image/background/stir_gif/13.png'),
            pg.image.load('image/background/stir_gif/14.png'),
            pg.image.load('image/background/stir_gif/15.png'),
            pg.image.load('image/background/stir_gif/16.png'),
            pg.image.load('image/background/stir_gif/17.png'),
            pg.image.load('image/background/stir_gif/18.png'),
            pg.image.load('image/background/stir_gif/19.png'),
            pg.image.load('image/background/stir_gif/20.png'),
            pg.image.load('image/background/stir_gif/21.png'),
            pg.image.load('image/background/stir_gif/22.png'),
            pg.image.load('image/background/stir_gif/23.png'),
            pg.image.load('image/background/stir_gif/24.png'),
            pg.image.load('image/background/stir_gif/25.png'),
            pg.image.load('image/background/stir_gif/26.png'),
            pg.image.load('image/background/stir_gif/27.png'),
            pg.image.load('image/background/stir_gif/28.png'),
            pg.image.load('image/background/stir_gif/29.png'),
            pg.image.load('image/background/stir_gif/30.png'),
            pg.image.load('image/background/stir_gif/31.png'),
            pg.image.load('image/background/stir_gif/32.png'),
            pg.image.load('image/background/stir_gif/33.png'),
            pg.image.load('image/background/stir_gif/34.png'),
            pg.image.load('image/background/stir_gif/35.png'),
            pg.image.load('image/background/stir_gif/36.png'),
            pg.image.load('image/background/stir_gif/37.png'),
            pg.image.load('image/background/stir_gif/38.png'),
            pg.image.load('image/background/stir_gif/39.png'),
            pg.image.load('image/background/stir_gif/40.png'),
            pg.image.load('image/background/stir_gif/41.png'),
            pg.image.load('image/background/stir_gif/42.png'),
            pg.image.load('image/background/stir_gif/43.png'),
            pg.image.load('image/background/stir_gif/44.png'),
            pg.image.load('image/background/stir_gif/45.png'),
            pg.image.load('image/background/stir_gif/46.png'),
            pg.image.load('image/background/stir_gif/47.png'),
            pg.image.load('image/background/stir_gif/48.png'),
            pg.image.load('image/background/stir_gif/49.png'),
            pg.image.load('image/background/stir_gif/50.png'),
            pg.image.load('image/background/stir_gif/51.png'),
            pg.image.load('image/background/stir_gif/52.png'),
            pg.image.load('image/background/stir_gif/53.png'),
            pg.image.load('image/background/stir_gif/54.png'),
            pg.image.load('image/background/stir_gif/55.png'),
            pg.image.load('image/background/stir_gif/56.png'),
            pg.image.load('image/background/stir_gif/57.png'),
            pg.image.load('image/background/stir_gif/58.png'),
            pg.image.load('image/background/stir_gif/59.png'),
            pg.image.load('image/background/stir_gif/60.png')]
#image/icon/
GAMESTARTBUTTON = pg.image.load('image/icon/game_start.png')
GAMESTARTBUTTONPRESSED = pg.image.load('image/icon/game_start_press.png')
MENUSELECT = pg.image.load('image/icon/menu_select.png')
MENUSELECTHIGHLIGHT = pg.image.load('image/icon/menu_select_highlight.png')
GAMEOVER = pg.image.load('image/icon/gameover.png')
GAMEOVERPRESSED = pg.image.load('image/icon/gameoverpressed.png')
#image/pointer
KNIFE_POINTER = pg.image.load('image/pointer/knife_pointer.png')
NORMAL_POINTER = pg.image.load('image/pointer/normal_pointer.png')
#image/dish
FRIED_RICE = pg.transform.scale(pg.image.load('image/dish/fried_rice.png'), [400,400])
JJAJANG = pg.transform.scale(pg.image.load('image/dish/jjajang.png'), [400,400])
TOPPED_RICE = pg.transform.scale(pg.image.load('image/dish/topped_rice.png'), [400,400])
POTATO_PANCAKE = pg.transform.scale(pg.image.load('image/dish/potato_pancake.png'), [400,400])
#image/explanation
STIR_EX = pg.image.load('image/explanation/stir_ex.png')
CUT_EX = pg.image.load('image/explanation/cut_ex.png')
MICRO_EX = pg.image.load('image/explanation/micro_ex.png')
PAN_EX = pg.image.load('image/explanation/pan_ex.png')

# define colors
DARK_GRAY = (122,122,146)
LIGHT_GRAY = (232,233,238)
GRAY = (196,199,208)
BLACK = (0,0,0)
IVORY = (247,247,247)

# explanation of recipe
# fried_rice
FRIEDRICE_NAME = '??????????????????'
FRIEDRICE_INGREDIENT = '?????? : ???(1??????), ??????(1???), ??????(1/4???)'
FRIEDRICE_SEASONING1 = '????????? : ???????????? 1T, ????????? 1T /' 
FRIEDRICE_SEASONING2 = '???????????? : ????????? 3T, ?????? 2T, ?????? 0.5T'
FRIEDRICE_ETC = '1??????, 10??? ????????? ??????'

# jjajang
JJAJANG_NAME = '??????????????????'
JJAJANG_INGREDIENT = '?????? : ???????????? 1???, ???????????? 5T, ??? 400ml'
JJAJANG_ETC = '1??????, 5??? ????????? ??????'

# topped_rice
TOPPEDRICE_NAME = '????????????'
TOPPEDRICE_INGREDIENT = '?????? : ????????? ????????? 8???, ?????? ?????? ??? 1/3???, ??????, ???????????? 1/2???'
TOPPEDRICE_SEASONING = '?????? : ??? 100ml(1/2???), ????????? 1/2T, ???????????? 1/2T, ?????? ?????? 1/2T'
TOPPEDRICE_ETC = '1??????, 30??? ????????? ??????'

# potato_pancake
POTATOPANCAKE_NAME = '?????????'
POTATOPANCAKE_INGREDIENT = '?????? : ?????? 2???, ?????????, ????????? 1T'
POTATOPANCAKE_ETC = '1??????, 30??? ????????? ??????'

# captions of recipe
# fried_rice
FRIEDRICE1 = '????????? ??????, ??????????????? ?????? ?????? ??? ???????????????.'
FRIEDRICE2 = '????????? ?????? ???????????????.'
FRIEDRICE3 = '??????????????? ????????????, ???, ?????????????????? ?????? ???????????????.'
FRIEDRICE4 = '?????????????????? 5?????? ?????? ???????????????.'

# jjajang
JJAJANG1 = '?????? ???, ??????????????? ?????? ???????????????.'
JJAJANG2 = '?????????????????? 1?????? ???????????????.'
JJAJANG3 = '?????? ?????? ???????????? ??? ?????? ??? ?????? ???????????????.'
JJAJANG4 = '?????????????????? 3?????? ?????? ??? ?????? 2?????? ?????? ???????????????.'

# topped_rice
TOPPEDRICE1 = '?????? ????????? ???????????????.'
TOPPEDRICE2 = '?????? ???????????????.'
TOPPEDRICE3 = '????????? ????????? ???, ??????, ?????? ???????????????.'
TOPPEDRICE4 = '??????, ???, ???????????? ??? ?????? ?????? ???????????????. ?????? ???????????? ?????????.'

# potato_pancake
POTATOPANCAKE1 = '?????? 2?????? ??????????????????.'
POTATOPANCAKE2 = '?????? ????????? ????????? ???????????? ????????? ???????????????.'
POTATOPANCAKE3 = 'TIP : ???????????? ????????? ?????? ???????????? ?????????. ????????? ????????? ?????? ???????????????.'

#ingredients cut image
ONION_1 = pg.transform.scale(pg.image.load('image/ingredient/onion_1.png'), [300,300])
ONION_2 = pg.transform.scale(pg.image.load('image/ingredient/onion_2.png'), [300,300])
ONION_3 = pg.transform.scale(pg.image.load('image/ingredient/onion_3.png'), [300,300])

SAUSAGE_1 = pg.transform.scale(pg.image.load('image/ingredient/sausage_1.png'), [300,150])
SAUSAGE_2 = pg.transform.scale(pg.image.load('image/ingredient/sausage_2.png'), [300,150])
SAUSAGE_3 = pg.transform.scale(pg.image.load('image/ingredient/sausage_3.png'), [300,150])

GREEN_ONION_1 = pg.transform.scale(pg.image.load('image/ingredient/green-onion.png'), [300,300])
GREEN_ONION_2 = pg.transform.scale(pg.image.load('image/ingredient/green-onion(0).png'), [300,300])
GREEN_ONION_3 = pg.transform.scale(pg.image.load('image/ingredient/green-onion(1).png'), [300,300])
GREEN_ONION_4 = pg.transform.scale(pg.image.load('image/ingredient/green-onion(2).png'), [300,300])

POTATO_CUT = [pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato.png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(1).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(2).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(3).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(4).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(5).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(6).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(7).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(8).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(9).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(10).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(11).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(12).png'), [300,300]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(13).png'), [300,300]),]

#ingredients pan image
FRYINGPAN = pg.transform.scale(pg.image.load('image/ingredient/pan.png'), [500,500])

BBOKEUM_1 = pg.transform.scale(pg.image.load('image/ingredient/bbokeum(1).png'), [300,300])
BBOKEUM_2 = pg.transform.scale(pg.image.load('image/ingredient/bbokeum(2).png'), [300,300])
BBOKEUM_3 = pg.transform.scale(pg.image.load('image/ingredient/bbokeum(3).png'), [300,300])

POTATO_PAN = [pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(1).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(2).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(3).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(4).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(5).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(6).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(7).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(8).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(9).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(10).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(11).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(12).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(13).png'), [200, 200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_pan/potato(14).png'), [200, 200]),]
#ingredients pot image
FIRE = [pg.transform.scale(pg.image.load('image/ingredient/fire.png'), [100,100]),
        pg.transform.scale(pg.image.load('image/ingredient/fire(1).png'), [100,100]),
        pg.transform.scale(pg.image.load('image/ingredient/fire(2).png'), [100,100])]

#stir bool variable
STIR_OUT = False
#micro bool variable
MICRO_DONE = False
#cut bool variable
CUT_OUT = False
ISCUT = False
#cut int variable
NUMBER_OF_CUT_INGREDIENTS = 1
#cut bool variable
PAN_OUT = False
#pan int variable
NUMBER_OF_PAN_INGREDIENTS = 1
#pot bool variable
ISPOT = False