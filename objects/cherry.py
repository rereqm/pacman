import pygame as pg
from threading import Timer
from objects.base import BaseObject


class Cherry(BaseObject):
    def __init__(self, x, y, width, height):
        super(Cherry, self).__init__(x, y, width, height)
        self.rect = pg.Rect(x, y, width, height)
        self.pos = (x,y)
        self.start_logic = True
        self.is_Visible = True
        self.score = 100
        self.color = "red"
        self.timer = Timer(1,self.logic_part_1)

    def show(self):
        self.is_Visible = True

    def hide(self):
        self.is_Visible = False

    def logic_part_1(self):
        self.show()
        self.timer = Timer(10,self.logic_part_2)
        self.timer.start()
    def logic_part_2(self):
        self.hide()
        self.timer = Timer(10,self.logic_part_1)
        self.timer.start()
    def draw(self, screen):
        if self.is_Visible:
            pg.draw.ellipse(screen, self.color, self.rect, width=0)