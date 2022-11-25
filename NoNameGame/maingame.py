import pygame as pg
import cv2, random, sys, time
from settings import *

pg.init()
pg.display.set_caption("COOKINGAME")
screen = pg.display.set_mode((WIDTH,HEIGHT))

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

def drawText(text, surface, x, y, font = FONT, color = BLACK):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObject, textRect)
    
def Menu():
    global MODE
    screen.blit(OPENINGTURNOFFIMG,[0,0])
    current_Time = pg.time.get_ticks()
    if current_Time > 2000:
        screen.blit(OPENINGIMG,[0,0])
    if current_Time > 4000:
        menu_trans = pg.transform.scale(MENUSELECT, [330,110])
        menu_highlight_trans = pg.transform.scale(MENUSELECTHIGHLIGHT, [330,110])
        menu_select_trans = pg.transform.scale(GAMESTARTBUTTON, [200,50])
        if MODE == 0:
            screen.blit(STARTIMG,[0,0])
            drawText("오늘은",screen,230,200,SUBGAMETITLEFONT,BLACK)
            drawText("방구석 요리사",screen,230,240,GAMETITLEFONT,BLACK)
            Button(GAMESTARTBUTTON, 250, 310, 300, 63, GAMESTARTBUTTONPRESSED, 250, 310, NextMenuSelectScene)
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
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        Menu()
        pg.display.update()

if __name__ == '__main__':
    main()