import pygame as pg
import time

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
#image/pointer
KNIFE_POINTER = pg.image.load('image/pointer/knife_pointer.png')
NORMAL_POINTER = pg.image.load('image/pointer/normal_pointer.png')
#image/dish
FRIED_RICE = pg.image.load('image/dish/fried_rice.png')
JJAJANG = pg.image.load('image/dish/jjajang.png')
TOPPED_RICE = pg.image.load('image/dish/topped_rice.png')
POTATO_PANCAKE = pg.image.load('image/dish/potato_pancake.png')


# define colors
DARK_GRAY = (122,122,146)
LIGHT_GRAY = (232,233,238)
GRAY = (196,199,208)
BLACK = (0,0,0)
IVORY = (247,247,247)

# explanation of recipe
# fried_rice
FRIEDRICE_NAME = '고추장볶음밥'
FRIEDRICE_INGREDIENT = '재료 : 밥(1공기), 참치(1캔), 양파(1/4개)'
FRIEDRICE_SEASONING1 = '밥양념 : 마요네즈 1T, 식용유 1T /' 
FRIEDRICE_SEASONING2 = '참치양념 : 고추장 3T, 케찹 2T, 설탕 0.5T'
FRIEDRICE_ETC = '1인분, 10분 이내로 완성'

# jjajang
JJAJANG_NAME = '짜파게티범벅'
JJAJANG_INGREDIENT = '재료 : 라면사리 1개, 짜장가루 5T, 물 400ml'
JJAJANG_ETC = '1인분, 5분 이내로 완성'

# topped_rice
TOPPEDRICE_NAME = '부대덮밥'
TOPPEDRICE_INGREDIENT = '재료 : 비엔나 소시지 8알, 스팸 작은 캔 1/3개, 대파, 체다치즈 1/2장'
TOPPEDRICE_SEASONING = '양념 : 물 100ml(1/2컵), 고추장 1/2T, 고춧가루 1/2T, 다진 마늘 1/2T'
TOPPEDRICE_ETC = '1인분, 30분 이내로 완성'

# potato_pancake
POTATOPANCAKE_NAME = '감자전'
POTATOPANCAKE_INGREDIENT = '재료 : 감자 2개, 식용유, 밀가루 1T'
POTATOPANCAKE_ETC = '1인분, 30분 이내로 완성'

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
POTATOPANCAKE3 = 'TIP : 밀가루를 넣으면 서로 들러붙지 않아요. 여유가 된다면 같이 넣어줍니다.'

#ingredients cut image
ONION_1 = pg.transform.scale(pg.image.load('image/ingredient/onion_1.png'), [200,200])
ONION_2 = pg.transform.scale(pg.image.load('image/ingredient/onion_2.png'), [200,200])
ONION_3 = pg.transform.scale(pg.image.load('image/ingredient/onion_3.png'), [200,200])

SAUSAGE_1 = pg.transform.scale(pg.image.load('image/ingredient/sausage_1.png'), [200,100])
SAUSAGE_2 = pg.transform.scale(pg.image.load('image/ingredient/sausage_2.png'), [200,100])
SAUSAGE_3 = pg.transform.scale(pg.image.load('image/ingredient/sausage_3.png'), [200,100])

POTATO_CUT = [pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato.png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(1).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(2).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(3).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(4).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(5).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(6).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(7).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(8).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(9).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(10).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(11).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(12).png'), [200,200]),
              pg.transform.scale(pg.image.load('image/ingredient/potato_cut/peeled_potato(13).png'), [200,200]),]

#stir bool variable
STIR_OUT = False
#micro bool variable
MICRO_DONE = False
#cut bool variable
CUT_OUT = False
ISCUT = False
#cut int variable
NUMBER_OF_CUT_INGREDIENTS = 1