import pygame as pg
import cv2, sys, random, time
import numpy as np
import mediapipe as mp
from settings import *

# 종료시 초기화 시켜야되는것들
# global INGAMEMODE, MODE, COOKMODE
# INGAMEMODE = 0
# MODE = 0
# COOKMODE = 0
# MAKEUPMODE = 1
# ENDMODE = 0
# STIR_OUT = False
# MICRO_DONE = False
# CUT_OUT = False
# ISCUT = False
# ISPOT = False
# PAN_OUT = False
# NUMBER_OF_CUT_INGREDIENTS = 1
# NUMBER_OF_PAN_INGREDIENTS = 1
# STIR_COUNT = 0

pg.init()
pg.display.set_caption("COOKINDOOR")
screen = pg.display.set_mode((WIDTH, HEIGHT))
EXPLANATION = True


class Button():
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        self.img_in = img_in
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img_act = img_act
        self.x_act = x_act
        self.y_act = y_act
        self.action = action

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action is not None:
                time.sleep(0.1)
                action()
        else:
            screen.blit(img_in, (x, y))


class Cookmode():
    def __init__(self, COOKMODE, surface):
        self.surface = surface

        if COOKMODE == 1:
            self.fried_rice()
        elif COOKMODE == 2:
            self.jjajang()
        elif COOKMODE == 3:
            self.topped_rice()
        elif COOKMODE == 4:
            self.potato_pancake()

    def caption_in(self, caption, font=FONT):
        self.caption = font.render(caption, False, IVORY, BLACK)
        self.caption_position = self.caption.get_rect()
        self.caption_position.centerx = 400
        self.caption_position.y = 500
        self.surface.blit(self.caption, self.caption_position)

    def explain(self, image):
        background(image)
        pg.display.update()
        pg.time.delay(1500)

    def stir(self, caption):  # 재료만 변경 매개변수에 ingredient
        global STIR_OUT, MAKEUPMODE, STIR_COUNT, MICRO_DONE
        MICRO_DONE = False

        background(STIR)
        self.caption_in(caption)

        self.stir_ground = pg.Rect((200, 0, 400, 200))
        if self.stir_ground.collidepoint(JOINTPOS) and IDX == 0:
            background(STIR_GIF[STIR_COUNT])
            STIR_COUNT += 1
            if STIR_COUNT >= 60:
                STIR_COUNT = 0
            STIR_OUT = True
        if JOINTPOS[1] > 200:
            STIR_OUT = False
        if (JOINTPOS[0] < 200 or JOINTPOS[0] > 600) and STIR_OUT and IDX == 0:
            time.sleep(1)
            STIR_COUNT = 0
            MAKEUPMODE += 1

    def caption_two(self, caption, font=FONT):
        self.caption = font.render(caption, False, IVORY, BLACK)
        self.surface.blit(self.caption, (100, 700))

    def cut(self, caption):  # 재료만 변경 매개변수에 ingredient
        global CUT_OUT, MAKEUPMODE, NUMBER_OF_CUT_INGREDIENTS, ISCUT

        ISCUT = True
        background(CUT)
        self.caption_in(caption)

        if COOKMODE == 1:
            self.onion_ground = pg.Rect((350, 200, 200, 200))
            if NUMBER_OF_CUT_INGREDIENTS == 1:
                self.surface.blit(ONION_1, [300, 150])
            if NUMBER_OF_CUT_INGREDIENTS == 2:
                self.surface.blit(ONION_2, [300, 150])
            if NUMBER_OF_CUT_INGREDIENTS == 3:
                self.surface.blit(ONION_3, [300, 150])
            if self.onion_ground.collidepoint(JOINTPOS) and (IDX == 9 or IDX == 3 or IDX == 1):
                CUT_OUT = True
            if (JOINTPOS[1] > 400 or JOINTPOS[1] < 200) and CUT_OUT and (IDX == 9 or IDX == 3 or IDX == 1):
                NUMBER_OF_CUT_INGREDIENTS += 1
                time.sleep(1)
                CUT_OUT = False
                if NUMBER_OF_CUT_INGREDIENTS > 3:
                    ISCUT = False
                    NUMBER_OF_CUT_INGREDIENTS = 1
                    MAKEUPMODE += 1

        if COOKMODE == 3 and MAKEUPMODE == 1:
            self.green_onion_ground = pg.Rect((350, 250, 200, 100))
            if NUMBER_OF_CUT_INGREDIENTS == 1:
                self.surface.blit(GREEN_ONION_1, [300, 200])
            if NUMBER_OF_CUT_INGREDIENTS == 2:
                self.surface.blit(GREEN_ONION_2, [300, 200])
            if NUMBER_OF_CUT_INGREDIENTS == 3:
                self.surface.blit(GREEN_ONION_3, [300, 200])
            if NUMBER_OF_CUT_INGREDIENTS == 4:
                self.surface.blit(GREEN_ONION_4, [300, 200])
            if self.green_onion_ground.collidepoint(JOINTPOS) and (IDX == 9 or IDX == 3 or IDX == 1):
                CUT_OUT = True
            if (JOINTPOS[1] > 400 or JOINTPOS[1] < 200) and CUT_OUT and (IDX == 9 or IDX == 3 or IDX == 1):
                NUMBER_OF_CUT_INGREDIENTS += 1
                time.sleep(1)
                CUT_OUT = False
                if NUMBER_OF_CUT_INGREDIENTS > 4:
                    ISCUT = False
                    NUMBER_OF_CUT_INGREDIENTS = 1
                    MAKEUPMODE += 1

        if COOKMODE == 3 and MAKEUPMODE == 2:
            self.sausage_ground = pg.Rect((300, 250, 200, 100))
            if NUMBER_OF_CUT_INGREDIENTS == 1:
                self.surface.blit(SAUSAGE_1, [300, 250])
            if NUMBER_OF_CUT_INGREDIENTS == 2:
                self.surface.blit(SAUSAGE_2, [300, 250])
            if NUMBER_OF_CUT_INGREDIENTS == 3:
                self.surface.blit(SAUSAGE_3, [300, 250])
            if self.sausage_ground.collidepoint(JOINTPOS) and (IDX == 9 or IDX == 3 or IDX == 1):
                CUT_OUT = True
            if (JOINTPOS[1] > 300 or JOINTPOS[1] < 250) and CUT_OUT and (IDX == 9 or IDX == 3 or IDX == 1):
                NUMBER_OF_CUT_INGREDIENTS += 1
                time.sleep(1)
                CUT_OUT = False
                if NUMBER_OF_CUT_INGREDIENTS > 3:
                    ISCUT = False
                    NUMBER_OF_CUT_INGREDIENTS = 1
                    MAKEUPMODE += 1

        if COOKMODE == 4:
            self.potato_ground = pg.Rect((350, 200, 200, 200))
            self.idx = NUMBER_OF_CUT_INGREDIENTS
            if NUMBER_OF_CUT_INGREDIENTS == self.idx:
                self.surface.blit(POTATO_CUT[self.idx - 1], [300, 150])
            if self.potato_ground.collidepoint(JOINTPOS) and (IDX == 9 or IDX == 3 or IDX == 1):
                CUT_OUT = True
            if (JOINTPOS[1] > 400 or JOINTPOS[1] < 200) and CUT_OUT and (IDX == 9 or IDX == 3 or IDX == 1):
                NUMBER_OF_CUT_INGREDIENTS += 1
                time.sleep(1)
                CUT_OUT = False
                if NUMBER_OF_CUT_INGREDIENTS > 14:
                    ISCUT = False
                    NUMBER_OF_CUT_INGREDIENTS = 1
                    MAKEUPMODE += 1

    def micro(self, caption):
        global MICRO_DONE, MAKEUPMODE

        background(MICRO)
        self.caption_in(caption)
        self.micro_ground = pg.Rect((200, 150, 400, 300))
        if self.micro_ground.collidepoint(JOINTPOS) and rock_motion():
            MICRO_DONE = True
            background(MICRO_FINISH)
        if MICRO_DONE and IDX == 5:
            time.sleep(1)
            MAKEUPMODE += 1

        self.caption_in(caption)

    def pan(self, caption):
        global NUMBER_OF_PAN_INGREDIENTS, PAN_OUT, MAKEUPMODE
        background(PAN)
        self.caption_in(caption)

        if COOKMODE == 3:
            self.surface.blit(FRYINGPAN, [100, 50])
            self.pan_handle = pg.Rect((100, 250, 200, 100))
            if NUMBER_OF_PAN_INGREDIENTS == 1:
                self.surface.blit(BBOKEUM_1, [260, 150])
            if NUMBER_OF_PAN_INGREDIENTS == 2:
                self.surface.blit(BBOKEUM_2, [260, 150])
            if NUMBER_OF_PAN_INGREDIENTS == 3:
                self.surface.blit(BBOKEUM_3, [260, 150])
            if self.pan_handle.collidepoint(JOINTPOS) and (IDX == 0 or IDX == 6):
                PAN_OUT = True
            if (JOINTPOS[1] > 350 or JOINTPOS[1] < 250) and PAN_OUT and (IDX == 0 or IDX == 6):
                NUMBER_OF_PAN_INGREDIENTS += 1
                time.sleep(1)
                PAN_OUT = False
                if NUMBER_OF_PAN_INGREDIENTS > 3:
                    NUMBER_OF_PAN_INGREDIENTS = 1
                    MAKEUPMODE += 1

    def pan2(self, caption1, caption2):
        global NUMBER_OF_PAN_INGREDIENTS, PAN_OUT, MAKEUPMODE

        background(PAN)
        self.caption_in(caption1)
        self.caption_two(caption2)

        if COOKMODE == 4:
            self.surface.blit(FRYINGPAN, [100, 50])
            self.pan_handle = pg.Rect((100, 250, 200, 100))
            self.idx = NUMBER_OF_PAN_INGREDIENTS
            if NUMBER_OF_PAN_INGREDIENTS == self.idx:
                self.surface.blit(POTATO_PAN[self.idx - 1], [300, 200])
            if self.pan_handle.collidepoint(JOINTPOS) and (IDX == 0 or IDX == 6):
                PAN_OUT = True
            if (JOINTPOS[1] > 350 or JOINTPOS[1] < 250) and PAN_OUT and (IDX == 0 or IDX == 6):
                NUMBER_OF_PAN_INGREDIENTS += 1
                time.sleep(1)
                PAN_OUT = False
                if NUMBER_OF_PAN_INGREDIENTS > 14:
                    NUMBER_OF_PAN_INGREDIENTS = 1
                    MAKEUPMODE += 1

    def pot(self, caption):
        global MAKEUPMODE, ISPOT
        self.caption_in(caption)
        background(POT)
        if COOKMODE == 3:
            for idx in range(0, 3):
                self.surface.blit(FIRE[idx], [300, 360 - 10 * idx])
                self.surface.blit(FIRE[idx], [350, 360 - 10 * idx])
                self.surface.blit(FIRE[idx], [400, 360 - 10 * idx])
                pg.display.update()
                pg.time.delay(1500)
            MAKEUPMODE += 1

    def finish(self):
        global ENDMODE
        ENDMODE = 1
        background(SCORE)

        Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 550, 300, 200, 50,
               pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 550, 300, end)
        draw_text("게임 종료하기", screen, 600, 315, MENUFONTBIG, BLACK)

        Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 550, 390, 200, 50,
               pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 550, 390, reset)
        draw_text("게임 다시하기", screen, 600, 405, MENUFONTBIG, BLACK)

        if COOKMODE == 1:
            self.surface.blit(FRIED_RICE, [100, 100])
        if COOKMODE == 2:
            self.surface.blit(JJAJANG, [100, 100])
        if COOKMODE == 3:
            self.surface.blit(TOPPED_RICE, [100, 100])
        if COOKMODE == 4:
            self.surface.blit(POTATO_PANCAKE, [100, 100])

    def fried_rice(self):
        global EXPLANATION
        if EXPLANATION:
            self.explain(STIR_EX)
            self.explain(CUT_EX)
            self.explain(MICRO_EX)
            EXPLANATION = False
        if MAKEUPMODE == 1:
            self.stir(FRIEDRICE1)
        elif MAKEUPMODE == 2:
            self.cut(FRIEDRICE2)
        elif MAKEUPMODE == 3:
            self.stir(FRIEDRICE3)
        elif MAKEUPMODE == 4:
            self.micro(FRIEDRICE4)
        else:
            self.finish()

    def jjajang(self):
        global EXPLANATION
        if EXPLANATION:
            self.explain(STIR_EX)
            self.explain(MICRO_EX)
            EXPLANATION = False
        if MAKEUPMODE == 1:
            self.stir(JJAJANG1)
        elif MAKEUPMODE == 2:
            self.micro(JJAJANG2)
        elif MAKEUPMODE == 3:
            self.stir(JJAJANG3)
        elif MAKEUPMODE == 4:
            self.micro(JJAJANG4)
        else:
            self.finish()

    def topped_rice(self):
        global EXPLANATION
        if EXPLANATION:
            self.explain(CUT_EX)
            self.explain(PAN_EX)
            EXPLANATION = False
        if MAKEUPMODE == 1:
            self.cut(TOPPEDRICE1)
        elif MAKEUPMODE == 2:
            self.cut(TOPPEDRICE2)
        elif MAKEUPMODE == 3:
            self.pan(TOPPEDRICE3)
        elif MAKEUPMODE == 4:
            self.pot(TOPPEDRICE4)
        else:
            self.finish()

    def potato_pancake(self):
        global EXPLANATION
        if EXPLANATION:
            self.explain(CUT_EX)
            self.explain(PAN_EX)
            EXPLANATION = False
        if MAKEUPMODE == 1:
            self.cut(POTATOPANCAKE1)
        elif MAKEUPMODE == 2:
            self.pan2(POTATOPANCAKE2, POTATOPANCAKE3)
        else:
            self.finish()


def reset():
    global INGAMEMODE, MODE, COOKMODE, MAKEUPMODE, ENDMODE, STIR_OUT, MICRO_DONE, CUT_OUT, ISCUT, \
        ISPOT, PAN_OUT, NUMBER_OF_CUT_INGREDIENTS, NUMBER_OF_PAN_INGREDIENTS, STIR_COUNT, EXPLANATION
    INGAMEMODE = 0
    MODE = 0
    COOKMODE = 0
    MAKEUPMODE = 1
    ENDMODE = 0
    EXPLANATION = True
    STIR_OUT = False
    MICRO_DONE = False
    CUT_OUT = False
    ISCUT = False
    ISPOT = False
    PAN_OUT = False
    NUMBER_OF_CUT_INGREDIENTS = 1
    NUMBER_OF_PAN_INGREDIENTS = 1
    STIR_COUNT = 0


def end():
    sys.exit()


def background(image):
    screen.blit(pg.transform.scale(image, (800, 600)), (0, 0))


def next_menu_select_scene():  # MODE : 1
    global MODE
    MODE = 1


def first_button_select_scene():  # MODE : 11
    global MODE
    MODE = 11


def second_button_select_scene():  # MODE : 12
    global MODE
    MODE = 12


def third_button_select_scene():  # MODE : 13
    global MODE
    MODE = 13


def fourth_button_select_scene():  # MODE : 14
    global MODE
    MODE = 14


def cooking_menu_select():
    global MODE, COOKMODE, INGAMEMODE
    INGAMEMODE = 1
    if MODE == 11:
        COOKMODE = 1
    elif MODE == 12:
        COOKMODE = 2
    elif MODE == 13:
        COOKMODE = 3
    elif MODE == 14:
        COOKMODE = 4


def draw_text(text, surface, x, y, font=FONT, color=BLACK):
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)


def scissors_motion():
    global BUFFER, IDX
    if (BUFFER == 9 or BUFFER == 1 or BUFFER == 3) and (IDX == 6 or IDX == 5 or IDX == 0):
        return True
    else:
        BUFFER = IDX
        return False


def rock_motion():
    global BUFFER, IDX
    if (BUFFER == 5) and (IDX == 0 or IDX == 6):
        return True
    else:
        BUFFER = IDX
        return False


def paper_motion():
    global BUFFER, IDX
    if (BUFFER == 0 or BUFFER == 6) and (IDX == 5):
        return True
    else:
        BUFFER = IDX
        return False


def game():
    global MODE, TIME
    TIME = pg.time.get_ticks()
    if TIME > 4800:
        background(OPENINGTURNOFFIMG)
    if TIME > 5000:
        background(OPENINGIMG)
    if TIME > 7000:
        menu_trans = pg.transform.scale(MENUSELECT, [336, 150])
        menu_highlight_trans = pg.transform.scale(MENUSELECTHIGHLIGHT, [366, 185])
        menu_select_trans = pg.transform.scale(GAMESTARTBUTTON, [200, 50])
        menu_start = pg.transform.scale(STARTIMG, [800, 600])
        if MODE == 0:
            screen.blit(menu_start, [0, 0])
            draw_text("오늘은", screen, 230, 200, SUBGAMETITLEFONT, BLACK)
            draw_text("방구석 요리사", screen, 230, 240, GAMETITLEFONT, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [300, 63]), 250, 310, 300, 63,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [300, 63]), 250, 310, next_menu_select_scene)
            Button(pg.transform.scale(GAMEOVER, [50, 50]), 740, 540, 100, 100,
                   pg.transform.scale(GAMEOVER, [50, 50]), 740, 540, end)
            draw_text("메뉴 선택", screen, 340, 320, FONT, BLACK)
        elif MODE == 1:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 150, menu_highlight_trans, 50 - 16, 100 - 17, first_button_select_scene)
            draw_text(FRIEDRICE_NAME, screen, 160, 110, MENUFONTBIG, BLACK)
            draw_text(FRIEDRICE_INGREDIENT, screen, 60, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING1, screen, 60, 150 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING2, screen, 60, 170 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_ETC, screen, 60, 190 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 100, 330, 150, menu_highlight_trans, 404, 100 - 17, second_button_select_scene)
            draw_text(JJAJANG_NAME, screen, 530 + 20, 110, MENUFONTBIG, BLACK)
            draw_text(JJAJANG_INGREDIENT, screen, 430, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(JJAJANG_ETC, screen, 430, 150 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 50, 300, 330, 150, menu_highlight_trans, 50 - 16, 300 - 17, third_button_select_scene)
            draw_text(TOPPEDRICE_NAME, screen, 160 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(TOPPEDRICE_INGREDIENT, screen, 55, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_SEASONING, screen, 55, 350 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_ETC, screen, 55, 370 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 300, 330, 150, menu_highlight_trans, 420 - 16, 300 - 17, fourth_button_select_scene)
            draw_text(POTATOPANCAKE_NAME, screen, 530 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(POTATOPANCAKE_INGREDIENT, screen, 430, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(POTATOPANCAKE_ETC, screen, 430, 350 + 20, MENUFONTSMALL, BLACK)
            screen.blit(menu_select_trans, [500 + 56, 450 + 40])
            draw_text("게임 시작하기", screen, 550 + 56, 465 + 40, MENUFONTBIG, BLACK)
        elif MODE == 11:
            screen.fill(IVORY)
            Button(menu_highlight_trans, 50 - 16, 100 - 17, 330, 150, menu_highlight_trans, 50 - 16, 100 - 17,
                   next_menu_select_scene)
            draw_text(FRIEDRICE_NAME, screen, 160, 110, MENUFONTBIG, BLACK)
            draw_text(FRIEDRICE_INGREDIENT, screen, 60, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING1, screen, 60, 150 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING2, screen, 60, 170 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_ETC, screen, 60, 190 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 100, 330, 150, menu_highlight_trans, 420 - 16, 100 - 17, second_button_select_scene)
            draw_text(JJAJANG_NAME, screen, 530 + 20, 110, MENUFONTBIG, BLACK)
            draw_text(JJAJANG_INGREDIENT, screen, 430, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(JJAJANG_ETC, screen, 430, 150 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 50, 300, 330, 150, menu_highlight_trans, 50 - 16, 300 - 17, third_button_select_scene)
            draw_text(TOPPEDRICE_NAME, screen, 160 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(TOPPEDRICE_INGREDIENT, screen, 55, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_SEASONING, screen, 55, 350 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_ETC, screen, 55, 370 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 300, 330, 150, menu_highlight_trans, 420 - 16, 300 - 17, fourth_button_select_scene)
            draw_text(POTATOPANCAKE_NAME, screen, 530 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(POTATOPANCAKE_INGREDIENT, screen, 430, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(POTATOPANCAKE_ETC, screen, 430, 350 + 20, MENUFONTSMALL, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500 + 56, 450 + 40, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500 + 56, 450 + 40, cooking_menu_select)
            draw_text("게임 시작하기", screen, 550 + 56, 465 + 40, MENUFONTBIG, BLACK)
        elif MODE == 12:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 150, menu_highlight_trans, 50 - 16, 100 - 17, first_button_select_scene)
            draw_text(FRIEDRICE_NAME, screen, 160, 110, MENUFONTBIG, BLACK)
            draw_text(FRIEDRICE_INGREDIENT, screen, 60, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING1, screen, 60, 150 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING2, screen, 60, 170 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_ETC, screen, 60, 190 + 20, MENUFONTSMALL, BLACK)
            Button(menu_highlight_trans, 420 - 16, 100 - 17, 330, 150, menu_highlight_trans, 420 - 16, 100 - 17,
                   next_menu_select_scene)
            draw_text(JJAJANG_NAME, screen, 530 + 20, 110, MENUFONTBIG, BLACK)
            draw_text(JJAJANG_INGREDIENT, screen, 430, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(JJAJANG_ETC, screen, 430, 150 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 50, 300, 330, 150, menu_highlight_trans, 50 - 16, 300 - 17, third_button_select_scene)
            draw_text(TOPPEDRICE_NAME, screen, 160 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(TOPPEDRICE_INGREDIENT, screen, 55, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_SEASONING, screen, 55, 350 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_ETC, screen, 55, 370 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 300, 330, 150, menu_highlight_trans, 420 - 16, 300 - 17, fourth_button_select_scene)
            draw_text(POTATOPANCAKE_NAME, screen, 530 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(POTATOPANCAKE_INGREDIENT, screen, 430, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(POTATOPANCAKE_ETC, screen, 430, 350 + 20, MENUFONTSMALL, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500 + 56, 450 + 40, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500 + 56, 450 + 40, cooking_menu_select)
            draw_text("게임 시작하기", screen, 550 + 56, 465 + 40, MENUFONTBIG, BLACK)
        elif MODE == 13:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 150, menu_highlight_trans, 50 - 16, 100 - 17, first_button_select_scene)
            draw_text(FRIEDRICE_NAME, screen, 160, 110, MENUFONTBIG, BLACK)
            draw_text(FRIEDRICE_INGREDIENT, screen, 60, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING1, screen, 60, 150 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING2, screen, 60, 170 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_ETC, screen, 60, 190 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 100, 330, 150, menu_highlight_trans, 420 - 16, 100 - 17, second_button_select_scene)
            draw_text(JJAJANG_NAME, screen, 530 + 20, 110, MENUFONTBIG, BLACK)
            draw_text(JJAJANG_INGREDIENT, screen, 430, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(JJAJANG_ETC, screen, 430, 150 + 20, MENUFONTSMALL, BLACK)
            Button(menu_highlight_trans, 50 - 16, 300 - 17, 330, 150, menu_highlight_trans, 50 - 16, 300 - 17,
                   next_menu_select_scene)
            draw_text(TOPPEDRICE_NAME, screen, 160 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(TOPPEDRICE_INGREDIENT, screen, 55, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_SEASONING, screen, 55, 350 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_ETC, screen, 55, 370 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 300, 330, 150, menu_highlight_trans, 420 - 16, 300 - 17, fourth_button_select_scene)
            draw_text(POTATOPANCAKE_NAME, screen, 530 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(POTATOPANCAKE_INGREDIENT, screen, 430, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(POTATOPANCAKE_ETC, screen, 430, 350 + 20, MENUFONTSMALL, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500 + 56, 450 + 40, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500 + 56, 450 + 40, cooking_menu_select)
            draw_text("게임 시작하기", screen, 550 + 56, 465 + 40, MENUFONTBIG, BLACK)
        elif MODE == 14:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 150, menu_highlight_trans, 50 - 16, 100 - 17, first_button_select_scene)
            draw_text(FRIEDRICE_NAME, screen, 160, 110, MENUFONTBIG, BLACK)
            draw_text(FRIEDRICE_INGREDIENT, screen, 60, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING1, screen, 60, 150 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_SEASONING2, screen, 60, 170 + 20, MENUFONTSMALL, BLACK)
            draw_text(FRIEDRICE_ETC, screen, 60, 190 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 420, 100, 330, 150, menu_highlight_trans, 420 - 16, 100 - 17, next_menu_select_scene)
            draw_text(JJAJANG_NAME, screen, 530 + 20, 110, MENUFONTBIG, BLACK)
            draw_text(JJAJANG_INGREDIENT, screen, 430, 130 + 20, MENUFONTSMALL, BLACK)
            draw_text(JJAJANG_ETC, screen, 430, 150 + 20, MENUFONTSMALL, BLACK)
            Button(menu_trans, 50, 300, 330, 150, menu_highlight_trans, 50 - 16, 300 - 17, third_button_select_scene)
            draw_text(TOPPEDRICE_NAME, screen, 160 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(TOPPEDRICE_INGREDIENT, screen, 55, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_SEASONING, screen, 55, 350 + 20, MENUFONTSMALL, BLACK)
            draw_text(TOPPEDRICE_ETC, screen, 55, 370 + 20, MENUFONTSMALL, BLACK)
            Button(menu_highlight_trans, 420 - 16, 300 - 17, 330, 150, menu_highlight_trans, 420 - 16, 300 - 17,
                   fourth_button_select_scene)
            draw_text(POTATOPANCAKE_NAME, screen, 530 + 30, 310, MENUFONTBIG, BLACK)
            draw_text(POTATOPANCAKE_INGREDIENT, screen, 430, 330 + 20, MENUFONTSMALL, BLACK)
            draw_text(POTATOPANCAKE_ETC, screen, 430, 350 + 20, MENUFONTSMALL, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500 + 56, 450 + 40, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500 + 56, 450 + 40, cooking_menu_select)
            draw_text("게임 시작하기", screen, 550 + 56, 465 + 40, MENUFONTBIG, BLACK)


def main():
    global JOINTPOS, IDX, ISCUT, ENDMODE
    max_num_hands = 1
    mp_hands = mp.solutions.hands
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_drawing = mp.solutions.drawing_utils

    rps_gesture = {6: 'rock', 5: 'paper', 9: 'scissors', 1: 'scissors', 0: 'rock', 3: 'scissors'}

    hands = mp_hands.Hands(max_num_hands=max_num_hands,
                           min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)

    file = np.genfromtxt('data/gesture_train.txt', delimiter=',')
    angle = file[:, :-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
        image = cv2.flip(image, 1)

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if INGAMEMODE == 0:
            game()
        if INGAMEMODE == 1:
            Cookmode(COOKMODE, screen)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                joint = np.zeros([21, 3])

                for i, lm in enumerate(hand_landmarks.landmark):
                    joint[i] = [lm.x, lm.y, lm.z]

                v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :]
                v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :]
                v = v2 - v1
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                angle = np.arccos(np.einsum('nt,nt->n',
                                            v[[0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18], :],
                                            v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]))

                angle = np.degrees(angle)

                data = np.array([angle], dtype=np.float32)
                success, result, near, dist = knn.findNearest(data, 3)
                IDX = int(result[0][0])

                if IDX in rps_gesture.keys():
                    cv2.putText(image, text=rps_gesture[IDX].upper(),
                                org=(int(hand_landmarks.landmark[0].x * image.shape[1]),
                                     int(hand_landmarks.landmark[0].y * image.shape[0] + 20)),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(125, 125, 125), thickness=2)

                px = joint[7][0] * (WIDTH) + 0
                py = joint[7][1] * (HEIGHT) + 0
                JOINTPOS = [px, py]

                if INGAMEMODE == 1 and ENDMODE == 0:
                    if IDX == 9 or IDX == 3 or IDX == 1:
                        screen.blit(pg.transform.scale(KNIFE_POINTER, [79, 93]), JOINTPOS)
                    else:
                        screen.blit(pg.transform.scale(NORMAL_POINTER, [79, 93]), JOINTPOS)

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        #cv2.imshow('Game', image) #카메라 나오게하는 코드

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # 함수 만들기 update
        pg.display.update()

        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()


if __name__ == '__main__':
    main()