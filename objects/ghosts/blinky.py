import pygame

from math import sqrt
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

class Blinky(Ghost):

    def __init__(self,x=320,y=275):
        super().__init__('images/blinky_rect.png',x,y)

    #def activate(self,screen):
     #   self.objname = "Blinky"
     #   self.chase = True
     #   self.draw(screen)
    def vector(self, enemy, field):
        field = convert_field(field)
        shift = [0, 0]
        if (enemy.x < self.pos_X):
            shift[0] = -1
        else:
            shift[0] = 1
        if (enemy.y < self.pos_Y):
            shift[1] = -1
        else:
            shift[1] = 1
        return shift
    def chasef(self,enemy,field):
        field = convert_field(field)
        if(field[self.pos_Y][self.pos_X-1]=="1") and (field[self.pos_Y][self.pos_X+1]=="1") and (field[self.pos_Y-1][self.pos_X]=="1") and (field[self.pos_Y+1][self.pos_X]=="0"):
            self.shift = [0,1]
        elif (field[self.pos_Y][self.pos_X-1]=="1") and (field[self.pos_Y][self.pos_X+1]=="1") and (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="1"):
            self.shift = [0,-1]
        elif (field[self.pos_Y][self.pos_X-1]=="1") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y-1][self.pos_X]=="1") and (field[self.pos_Y+1][self.pos_X]=="1"):
            self.shift = [1,0]
        elif (field[self.pos_Y][self.pos_X-1]=="0") and (field[self.pos_Y][self.pos_X+1]=="1") and (field[self.pos_Y-1][self.pos_X]=="1") and (field[self.pos_Y+1][self.pos_X]=="1"):
            self.shift = [-1,0]
        elif (field[self.pos_Y][self.pos_X-1]=="0") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y-1][self.pos_X]=="1") and (field[self.pos_Y+1][self.pos_X]=="1"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X+1,enemy)):
                self.shift = [-1,0]
            else:
                self.shift = [1, 0]
        elif (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="0") and (field[self.pos_Y][self.pos_X+1]=="1") and (field[self.pos_Y+1][self.pos_X-1]=="1"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)):
                self.shift = [0,-1]
            else:
                self.shift = [0,1]
        elif (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="0") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y+1][self.pos_X-1]=="1"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)):
                if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X+1,enemy)):
                    self.shift = [0,-1]
                else:
                    self.shift = [1,0]
            else:
                if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X+1,enemy)):
                    self.shift = [0,-1]
                else:
                    self.shift = [1,0]
        elif (field[self.pos_Y-1][self.pos_X]=="1") and (field[self.pos_Y+1][self.pos_X]=="0") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y+1][self.pos_X-1]=="0"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_X+1,self.pos_X,enemy)):
                if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [0,1]
                else:
                    self.shift = [-1,0]
            else:
                if (self.distance_between_ghost_and_enemy(self.pos_X+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [1, 0]
                else:
                    self.shift = [-1,0]
        elif (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="1") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y+1][self.pos_X-1]=="0"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_X+1,self.pos_X,enemy)):
                if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [0,-1]
                else:
                    self.shift = [-1,0]
            else:
                if (self.distance_between_ghost_and_enemy(self.pos_X+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [1, 0]
                else:
                    self.shift = [-1,0]
        elif (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="0") and (field[self.pos_Y][self.pos_X+1]=="1") and (field[self.pos_Y+1][self.pos_X-1]=="0"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)):
                if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [0,1]
                else:
                    self.shift = [-1,0]
            else:
                if (self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    self.shift = [0,-1]
                else:
                    self.shift = [-1,0]
        elif (field[self.pos_Y-1][self.pos_X]=="0") and (field[self.pos_Y+1][self.pos_X]=="0") and (field[self.pos_Y][self.pos_X+1]=="0") and (field[self.pos_Y+1][self.pos_X-1]=="0"):
            if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_X+1,self.pos_X,enemy)):
                if (self.distance_between_ghost_and_enemy(self.pos_Y+1,self.pos_X,enemy)<self.distance_between_ghost_and_enemy(self.pos_Y,self.pos_X-1,enemy)):
                    if (self.distance_between_ghost_and_enemy(self.pos_Y + 1, self.pos_X,enemy) < self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)):
                        self.shift = [0,1]
                    else:
                        self.shift = [0,-1]
                else:
                    if (self.distance_between_ghost_and_enemy(self.pos_Y, self.pos_X-1,enemy) < self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)):
                        self.shift = [-1,0]
                    else:
                        self.shift = [0,-1]
            else:
                if (self.distance_between_ghost_and_enemy(self.pos_X + 1, self.pos_X,enemy) < self.distance_between_ghost_and_enemy(self.pos_Y, self.pos_X - 1,enemy)):
                    if (self.distance_between_ghost_and_enemy(self.pos_X + 1, self.pos_X,enemy) < self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)):
                        self.shift = [1,0]
                    else:
                        self.shift = [0, -1]
                else:
                    if (self.distance_between_ghost_and_enemy(self.pos_Y, self.pos_X - 1,enemy) < self.distance_between_ghost_and_enemy(self.pos_Y-1,self.pos_X,enemy)):
                        self.shift = [-1, 0]
                    else:
                        self.shift = [0, -1]
        self.move(field)
