import pygame as pg
import cv2, sys, random, time
import numpy as np
import mediapipe as mp
from settings import *
from cookmode import *

pg.init()
pg.display.set_caption("COOKINDOOR")
screen = pg.display.set_mode((WIDTH, HEIGHT))


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


def backgroud(image):
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
    global MODE, COOKMODE
    if MODE == 11:
        COOKMODE = 1
        Cookmode(1, screen)
        print(COOKMODE)
    elif MODE == 12:
        COOKMODE = 2
        Cookmode(2, screen)
        print(COOKMODE)
    elif MODE == 13:
        COOKMODE = 3
        Cookmode(3, screen)
        print(COOKMODE)
    elif MODE == 14:
        COOKMODE = 4
        Cookmode(4, screen)
        print(COOKMODE)


def draw_text(text, surface, x, y, font=FONT, color=BLACK):
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)


def game():
    global MODE, TIME
    TIME = pg.time.get_ticks()
    if TIME > 4800:
        backgroud(OPENINGTURNOFFIMG)
    if TIME > 5000:
        backgroud(OPENINGIMG)
    if TIME > 7000:
        menu_trans = pg.transform.scale(MENUSELECT, [330, 110])
        menu_highlight_trans = pg.transform.scale(MENUSELECTHIGHLIGHT, [368, 145])
        menu_select_trans = pg.transform.scale(GAMESTARTBUTTON, [200, 50])
        menu_start = pg.transform.scale(STARTIMG, [800, 600])
        if MODE == 0:
            screen.blit(menu_start, [0, 0])
            draw_text("오늘은", screen, 230, 200, SUBGAMETITLEFONT, BLACK)
            draw_text("방구석 요리사", screen, 230, 240, GAMETITLEFONT, BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [300, 63]), 250, 310, 300, 63,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [300, 63]), 250, 310, next_menu_select_scene)
            draw_text("메뉴 선택", screen, 340, 320, FONT, BLACK)
        elif MODE == 1:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50-18, 100-17, first_button_select_scene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 402, 100 - 17, second_button_select_scene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50-18, 300-17, third_button_select_scene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420-18, 300-17, fourth_button_select_scene)
            screen.blit(menu_select_trans, [500, 450])
        elif MODE == 11:
            screen.fill(IVORY)
            Button(menu_highlight_trans, 50-18, 100-17, 330, 110, menu_highlight_trans, 50-18, 100-17, next_menu_select_scene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420-18, 100-17, second_button_select_scene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50-18, 300-17, third_button_select_scene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420-18, 300-17, fourth_button_select_scene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500, 450, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500, 450, cooking_menu_select)
        elif MODE == 12:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50-18, 100-17, first_button_select_scene)
            Button(menu_highlight_trans, 420-18, 100-17, 330, 110, menu_highlight_trans, 420-18, 100-17, next_menu_select_scene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50-18, 300-17, third_button_select_scene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420-18, 300-17, fourth_button_select_scene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500, 450, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500, 450, cooking_menu_select)
        elif MODE == 13:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50-18, 100-17, first_button_select_scene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420-18, 100-17, second_button_select_scene)
            Button(menu_highlight_trans, 50-18, 300-17, 330, 110, menu_highlight_trans, 50-18, 300-17, next_menu_select_scene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420-18, 300-17, fourth_button_select_scene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500, 450, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500, 450, cooking_menu_select)
        elif MODE == 14:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50-18, 100-17, first_button_select_scene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420-18, 100-17, next_menu_select_scene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50-18, 300-17, third_button_select_scene)
            Button(menu_highlight_trans, 420-18, 300-17, 330, 110, menu_highlight_trans, 420-18, 300-17, fourth_button_select_scene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200, 50]), 500, 450, 200, 50,
                   pg.transform.scale(GAMESTARTBUTTONPRESSED, [200, 50]), 500, 450, cooking_menu_select)


def main():
    max_num_hands = 1
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    hands = mp_hands.Hands(max_num_hands=max_num_hands,
                           min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)

    file = np.genfromtxt('data/gesture_train.txt', delimiter=',')
    angle = file[:, :-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    print(angle)
    print(label)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        game()
        
        #cv2.imshow('Game', image) #카메라 나오게하는 코드

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pg.display.update()


if __name__ == '__main__':
    main()
