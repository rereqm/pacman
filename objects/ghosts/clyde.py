import pygame

from objects.ghosts.parent_ghost import Ghost
from settings import Settings
from objects.ghosts.blinky import Blinky

def convert_field(field):
    field1 = field.copy()
    for i in range(31):
        for j in range(28):
            if field1[i][j] == 1:
                field1[i][j] = '1'
            else:
                field1[i][j] = '0'
    return field1

class Clyde(Ghost):

    def __init__(self):
        super().__init__('images/clyde_rect.png',400,325)


    #def activate(self,screen):
    #    self.objname = "Clyde"
    #    self.chase = True
    #    self.pos_X =15
    #    self.draw(screen)

    def chasef(self,enemy,field):
        field = convert_field(field)
        t = 0
        if (self.distance_between_ghost_and_enemy(self.pos_X,self.pos_Y,enemy)<8):
            if not t:

                self.gotopos(endpos_x=9,endpos_y=24,field=field)
                t = 1
            else:
                self.gotopos(endpos_x=7,endpos_y=30,field=field)
                t = 0
        else:
            ghost_blinky = Blinky()
            ghost_blinky.pos_X = self.pos_X
            ghost_blinky.pos_Y = self.pos_Y
            ghost_blinky.chasef(enemy,field)
            self.shift = ghost_blinky.shift
            self.move(field)
