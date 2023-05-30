import pygame

from objects.ghosts.parent_ghost import Ghost
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

class Pinky(Ghost):

    def __init__(self):
        super().__init__('images/pinky_rect.png',275,325)

    #def activate(self,screen):
    #    self.speed = 1.5
     #   self.objname = "Pinky"
     #   self.chase = True
     #   self.pos_X = 13
     #   self.draw(screen)


    def chasef(self,enemy,field):
        field = convert_field(field)
        if  enemy.shift == [0,1]:
            if (field[enemy.x+4][enemy.y]=="0"):
                self.gotopos(enemy.x,enemy.y+4,field=field)
            else:
                t =1
                while field[enemy.x+t][enemy.y]!="0":
                    t+=1
                self.gotopos(enemy.x,enemy.y+t,field=field)
        elif enemy.shift == [0,-1]:
            if (field[enemy.x-4][enemy.y]=="0"):
                self.gotopos(enemy.x,enemy.y-4,field=field)
            else:
                t =1
                while field[enemy.x-t][enemy.y]!="0":
                    t+=1
                self.gotopos(enemy.x,enemy.y-t,field=field)
        elif enemy.shift == [1,0]:
            if (field[enemy.x][enemy.y+4]):
                if (field[enemy.x][enemy.y+4] == "0"):
                    self.gotopos(enemy.x+4, enemy.y,field=field)
                else:
                    t = 1
                    while field[enemy.x][enemy.y+t] != "0":
                        t += 1
                    self.gotopos(enemy.x+t, enemy.y,field=field )
        elif enemy.shift == [-1,0]:
            if (field[enemy.x][enemy.y-4]):
                if (field[enemy.x][enemy.y-4] == "0"):
                    self.gotopos(enemy.x-4, enemy.y,field=field)
                else:
                    t = 1
                    while field[enemy.x][enemy.y-t] != "0":
                        t += 1
                    self.gotopos(enemy.x+t, enemy.y,field=field)
