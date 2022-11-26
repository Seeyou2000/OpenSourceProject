import pygame as pg
import cv2, sys, random, time
import numpy as np
import mediapipe as mp
from settings import *

pg.init()
pg.display.set_caption("COOKINGAME")
screen = pg.display.set_mode((WIDTH,HEIGHT))

class Button():
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(0.1)
                action()
        else:
            screen.blit(img_in,(x,y))

def NextMenuSelectScene():            #MODE : 1
    global MODE
    MODE = 1
    
def FirstButtonSelectScene():         #MODE : 11
    global MODE
    MODE = 11

def SecondButtonSelectScene():        #MODE : 12
    global MODE
    MODE = 12
    
def ThirdButtonSelectScene():         #MODE : 13
    global MODE
    MODE = 13
    
def FourthButtonSelectScene():        #MODE : 14
    global MODE
    MODE = 14

def CookingMenuSelect():
    global MODE, COOKMODE
    if MODE == 11:
        COOKMODE = 1
        print(COOKMODE)
    elif MODE == 12:
        COOKMODE = 2
        print(COOKMODE)
    elif MODE == 13:
        COOKMODE = 3
        print(COOKMODE)
    elif MODE == 14:
        COOKMODE = 4
        print(COOKMODE)

def drawText(text, surface, x, y, font = FONT, color = BLACK):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObject, textRect)
    
def Game():
    global MODE, TIME
    TIME = pg.time.get_ticks()
    if TIME > 4800:
        screen.blit(pg.transform.scale(OPENINGTURNOFFIMG, [800,600]),[0,0])
    if TIME > 5000:
        screen.blit(pg.transform.scale(OPENINGIMG, [800,600]),[0,0])
    if TIME > 7000:
        menu_trans = pg.transform.scale(MENUSELECT, [330,110])
        menu_highlight_trans = pg.transform.scale(MENUSELECTHIGHLIGHT, [330,110])
        menu_select_trans = pg.transform.scale(GAMESTARTBUTTON, [200,50])
        menu_start = pg.transform.scale(STARTIMG, [800,600])
        if MODE == 0:
            screen.blit(menu_start,[0,0])
            drawText("오늘은",screen,230,200,SUBGAMETITLEFONT,BLACK)
            drawText("방구석 요리사",screen,230,240,GAMETITLEFONT,BLACK)
            Button(pg.transform.scale(GAMESTARTBUTTON, [300, 63]), 250, 310, 300, 63, pg.transform.scale(GAMESTARTBUTTONPRESSED, [300,63]), 250, 310, NextMenuSelectScene)
            drawText("메뉴 선택",screen,340,320,FONT,BLACK)
        elif MODE == 1:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50, 100, FirstButtonSelectScene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420, 100, SecondButtonSelectScene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50, 300, ThirdButtonSelectScene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420, 300, FourthButtonSelectScene)
            screen.blit(menu_select_trans, [500,450])
        elif MODE == 11:
            screen.fill(IVORY)
            Button(menu_highlight_trans, 50, 100, 330, 110, menu_highlight_trans, 50, 100, NextMenuSelectScene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420, 100, SecondButtonSelectScene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50, 300, ThirdButtonSelectScene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420, 300, FourthButtonSelectScene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200,50]), 500, 450, 200, 50, pg.transform.scale(GAMESTARTBUTTONPRESSED, [200,50]), 500, 450, CookingMenuSelect)
        elif MODE == 12:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50, 100, FirstButtonSelectScene)
            Button(menu_highlight_trans, 420, 100, 330, 110, menu_highlight_trans, 420, 100, NextMenuSelectScene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50, 300, ThirdButtonSelectScene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420, 300, FourthButtonSelectScene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200,50]), 500, 450, 200, 50, pg.transform.scale(GAMESTARTBUTTONPRESSED, [200,50]), 500, 450, CookingMenuSelect)
        elif MODE == 13:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50, 100, FirstButtonSelectScene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420, 100, SecondButtonSelectScene)
            Button(menu_highlight_trans, 50, 300, 330, 110, menu_highlight_trans, 50, 300, NextMenuSelectScene)
            Button(menu_trans, 420, 300, 330, 110, menu_highlight_trans, 420, 300, FourthButtonSelectScene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200,50]), 500, 450, 200, 50, pg.transform.scale(GAMESTARTBUTTONPRESSED, [200,50]), 500, 450, CookingMenuSelect)
        elif MODE == 14:
            screen.fill(IVORY)
            Button(menu_trans, 50, 100, 330, 110, menu_highlight_trans, 50, 100, FirstButtonSelectScene)
            Button(menu_trans, 420, 100, 330, 110, menu_highlight_trans, 420, 100, NextMenuSelectScene)
            Button(menu_trans, 50, 300, 330, 110, menu_highlight_trans, 50, 300, ThirdButtonSelectScene)
            Button(menu_highlight_trans, 420, 300, 330, 110, menu_highlight_trans, 420, 300, FourthButtonSelectScene)
            Button(pg.transform.scale(GAMESTARTBUTTON, [200,50]), 500, 450, 200, 50, pg.transform.scale(GAMESTARTBUTTONPRESSED, [200,50]), 500, 450, CookingMenuSelect)

def main():
    max_num_hands = 1
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    
    hands = mp_hands.Hands(max_num_hands = max_num_hands,
                           min_detection_confidence = 0.5,
                           min_tracking_confidence = 0.5)
    
    file = np.genfromtxt('data/gesture_train.txt', delimiter=',')
    angle = file[:,:-1].astype(np.float32)
    label = file[:,-1].astype(np.float32)
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
        
        Game()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pg.display.update()

if __name__ == '__main__':
    main()