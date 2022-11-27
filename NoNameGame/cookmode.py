import pygame as pg
from settings import *
import time


class Cookmode():
    def __init__(self, COOKMODE, surface):
        self.COOKMODE = COOKMODE
        self.surface = surface
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.start_time = time.time()
        self.timer = 0
        self.score = 100

        if COOKMODE == 1:
            self.fried_rice()
        elif COOKMODE == 2:
            self.jjajang()
        elif COOKMODE == 3:
            self.topped_rice()
        elif COOKMODE == 4:
            self.potato_pancake()

    def background(self, image):
        self.screen.blit(pg.transform.scale(image, (800, 600)), (0, 0))

    def caption_in(self, caption, font=FONT):
        self.caption = font.render(caption, False, IVORY, BLACK)
        self.surface.blit(self.caption, (400, 500))

    def stir(self, caption):  # 재료만 변경 매개변수에 ingredient
        # self.ingredient = ingredient  # 섞는 과정이 달라서
        self.present_time = time.time() - self.start_time
        self.timer = 5000
        if self.present_time < self.timer:
            self.caption_in(caption)
            self.background(CUT)
            pg.display.flip()

    def cut(self, timer, caption):  # 재료만 변경 매개변수에 ingredient
        self.present_time = time.time() - self.start_time
        self.timer = timer
        if self.present_time < self.timer:
            self.caption_in(caption)
            self.background(CUT)
            pg.display.flip()

    def micro(self, timer, caption):
        self.present_time = time.time() - self.start_time
        self.caption_in(caption)
        self.timer = timer
        self.background(MICRO)
        if self.present_time > self.timer:
            return 0

    def pan(self, caption):
        self.present_time = time.time() - self.start_time
        self.caption_in(caption)
        self.timer = 5000  # 임시
        self.background(PAN)
        if self.present_time > self.timer:
            return 0

    def pot(self, caption):
        self.present_time = time.time() - self.start_time
        self.caption_in(caption)
        self.timer = 2000  # 임시
        self.background(POT)
        if self.present_time > self.timer:
            return 0

    def finish(self):
        pass

    def fried_rice(self):
        self.stir(FRIEDRICE1)
        self.cut(5000, FRIEDRICE2)
        self.stir(FRIEDRICE3)
        self.micro(5000, FRIEDRICE4)

    def jjajang(self):
        pass

    def topped_rice(self):
        pass

    def potato_pancake(self):
        pass
