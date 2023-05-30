import pygame

from objects.ghosts.parent_ghost import Ghost
from objects.ghosts.blinky import Blinky
from settings import Settings

def convert_field(field):
    field1 = field.copy()
    for i in range(31):
        for j in range(28):
            if field1[i][j] == 1:
                field1[i][j] = '1'
            else:
                field1[i][j] = '0'
    return field1

class Inky(Ghost):

    def __init__(self):
        super().__init__('images/inky_rect.png',0,0)

   # def activate(self,screen):
    #    self.objname = "Inky"
    #    self.chase = True
     #   self.pos_X = 14
     #   self.draw(screen)



    def chasef(self,enemy,field,blinky):
        field = convert_field(field)
        ghost_bliky = blinky
        if  enemy.shift == [0,1]:
            if (field[enemy.y+2][enemy.x]=="0"):
                ghost_bliky.pos_Y = enemy.pos_Y+2
                ghost_bliky.chasef(field,enemy)
            else:
                t =1
                while field[enemy.y+t][enemy.x]!="0":
                    t+=1
                ghost_bliky.pos_Y = enemy.pos_Y+t
                ghost_bliky.chasef(field, enemy)
        elif enemy.shift == [0,-1]:
            if (field[enemy.y + 2][enemy.x] == "0"):
                ghost_bliky.pos_Y = enemy.pos_Y-2
                ghost_bliky.chasef(field, enemy)
            else:
                t = 1
                while field[enemy.y - t][enemy.x] != "0":
                    t += 1
                ghost_bliky.pos_Y = enemy.pos_Y-t
                ghost_bliky.chasef(field, enemy)
        elif enemy.shift == [1,0]:
            if (field[enemy.y][enemy.x+2] == "0"):
                ghost_bliky.pos_X = enemy.pos_X+2
                ghost_bliky.chasef(field, enemy)
            else:
                t = 1
                while field[enemy.y][enemy.x+t] != "0":
                    t += 1
                ghost_bliky.pos_X = enemy.pos_X+t
                ghost_bliky.chasef(field, enemy)
        elif enemy.shift == [-1,0]:
            if (field[enemy.y][enemy.x - 2] == "0"):
                ghost_bliky.pos_X = enemy.pos_X-2
                ghost_bliky.chasef(field, enemy)
            else:
                t = 1
                while field[enemy.y][enemy.x - t] != "0":
                    t += 1
                ghost_bliky.pos_X = enemy.pos_X-t
                ghost_bliky.chasef(field, enemy)
        self.gotopos(int(ghost_bliky.pos_X+((4*(blinky.vector(enemy,field)[0])))),ghost_bliky.pos_Y+(4*blinky.vector(enemy,field)[1]),field)
