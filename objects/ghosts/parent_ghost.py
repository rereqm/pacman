import pygame


from objects.images import Image
from settings import Settings
from math import sqrt


def convert_field(field):
    field1 = field
    for i in range(31):
        for j in range(28):
            if field1[i][j] == 1:
                field1[i][j] = '1'
            else:
                field1[i][j] = '0'
    return field1


class Ghost(Image):

    def __init__(self,filename,x=Settings.WINDOW_WIDTH//2,y=Settings.WINDOW_HEIGHT//2):
        self.objname = "Ghost"  # Имя призрака
        self.wait_time = 0  # Сколько призрак не двигается с начала игры ( в секундах )
        self.pos_Y = 12
        self.pos_X = 13
        self.chase = False      # Режим преследования
        self.eat = False
        self.scare = False      # Режим страха
        self.speed = 1          # Скорость призрака. Увеличивается в зависимости от очков
        self.shift = [0,0]      # Направление движения [x,y]
        super().__init__(x, y, filename)



    def scare(self,field):
        timer = 0
        field = convert_field(field)
        self.chase,self.scare = self.scare,self.chase
        current_speed = self.speed
        self.speed = 0.5
        while timer!=25:
            self.shift = [self.shift[0]*-1,self.shift[1]*-1]
            self.move(field)
            timer+=1
        if self.eat:
            self.eating_ghost(field)
        else:
            self.chase,self.scare = self.scare,self.chase
            self.speed = current_speed
            del current_speed


    def eating_ghost(self,field):
        field = convert_field(field)
        if self.scare:
            while self.pos_Y!=12 and self.pos_X!=13:
                self.gotopos(13,12,field)
        self.chase = True
        self.eat = False
        self.scare = False

    def move(self,field) -> None:
        field = convert_field(field)
        self.pos_X += self.shift[0] * self.speed
        self.pos_Y += self.shift[1] * self.speed
        self.rect.x += self.shift[0] * self.speed
        self.rect.y += self.shift[1] * self.speed
        if not(self.collision_with_field(self,field)):
            self.rect.x += self.shift[0] * self.speed
            self.rect.y += self.shift[1] * self.speed
        else:
            self.shift = [self.shift[0]*-1,self.shift[1]*-1]
            self.move(field)

    def collision_with_enemy(self,field,enemy):
        field = convert_field(field)
        if (self.distance_between_ghost_and_enemy(self.pos_X,self.pos_Y,enemy)<1):
            return True
        else:
            return False

    def distance_between_ghost_and_enemy(self,self_PosX,self_PosY,enemy):
        distance = sqrt((self_PosX - enemy.x) ** 2 + (self_PosY - enemy.y)**2)
        return distance

    def gotopos(self, endpos_x, endpos_y, field):
        field = convert_field(field)
        if (endpos_x != self.pos_X) and (endpos_y != self.pos_Y):
            if (endpos_x < self.pos_X) and (field[self.pos_Y][self.pos_X - 1] == "0"):
                self.shift = [-1, 0]
                self.move(field)
            elif (endpos_x < self.pos_X) and (field[self.pos_Y][self.pos_X - 1] == "1"):
                if (field[self.pos_Y + 1][self.pos_X - 1] == "0"):
                    self.shift = [0, 1]
                    self.move(field)
                    self.shift = [-1, 0]
                    self.move(field)
                elif (field[self.pos_Y - 1][self.pos_X - 1] == "0"):
                    self.shift = [0, -1]
                    self.move(field)
                    self.shift = [-1, 0]
                    self.move(field)
                else:
                    while field[self.pos_Y][self.pos_X - 1] != "0":
                        if (field[self.pos_Y + 1][self.pos_X] == "0"):
                            self.shift = [0, 1]
                            self.move(field)
                        elif (field[self.pos_Y - 1][self.pos_X] == "0"):
                            self.shift = [0, -1]
                            self.move(field)
            if (endpos_x > self.pos_X) and (field[self.pos_Y][self.pos_X + 1] == "0"):
                self.shift = [1, 0]
                self.move(field)
            elif (endpos_x < self.pos_X) and (field[self.pos_Y][self.pos_X + 1] == "1"):
                if (field[self.pos_Y + 1][self.pos_X + 1] == "0"):
                    self.shift = [0, 1]
                    self.move(field)
                    self.shift = [1, 0]
                    self.move(field)
                elif (field[self.pos_Y - 1][self.pos_X + 1] == "0"):
                    self.shift = [0, -1]
                    self.move(field)
                    self.shift = [1, 0]
                    self.move(field)
                else:
                    while field[self.pos_Y][self.pos_X + 1] != "0":
                        if (field[self.pos_Y + 1][self.pos_X] == "0"):
                            self.shift = [0, 1]
                            self.move(field)
                        elif (field[self.pos_Y - 1][self.pos_X] == "0"):
                            self.shift = [0, -1]
                            self.move(field)
            if (endpos_y < self.pos_Y) and (field[self.pos_Y - 1][self.pos_X] == "0"):
                self.shift = [0, -1]
                self.move(field)
            elif (endpos_y < self.pos_Y) and (field[self.pos_Y - 1][self.pos_X] == "1"):
                if (field[self.pos_Y - 1][self.pos_X + 1] == "0"):
                    self.shift = [1, 0]
                    self.move(field)
                    self.shift = [0, -1]
                    self.move(field)
                elif (field[self.pos_Y - 1][self.pos_X - 1] == "0"):
                    self.shift = [-1, 0]
                    self.move(field)
                    self.shift = [0, -1]
                    self.move(field)
                else:
                    while field[self.pos_Y - 1][self.pos_X] != "0":
                        if (field[self.pos_Y][self.pos_X + 1] == "0"):
                            self.shift = [1, 0]
                            self.move(field)
                        elif (field[self.pos_Y][self.pos_X - 1] == "0"):
                            self.shift = [-1, 0]
                            self.move(field)
            if (endpos_y > self.pos_Y) and (field[self.pos_Y + 1][self.pos_X] == "0"):
                self.shift = [0, 1]
                self.move(field)
            elif (endpos_y > self.pos_Y) and (field[self.pos_Y + 1][self.pos_X] == "1"):
                if (field[self.pos_Y + 1][self.pos_X + 1] == "0"):
                    self.shift = [1, 0]
                    self.move(field)
                    self.shift = [0, 1]
                    self.move(field)
                elif (field[self.pos_Y + 1][self.pos_X - 1] == "0"):
                    self.shift = [-1, 0]
                    self.move(field)
                    self.shift = [0, 1]
                    self.move(field)
                else:
                    while field[self.pos_Y + 1][self.pos_X] != "0":
                        if (field[self.pos_Y][self.pos_X + 1] == "0"):
                            self.shift = [1, 0]
                            self.move(field)
                        elif (field[self.pos_Y][self.pos_X - 1] == "0"):
                            self.shift = [-1, 0]
                            self.move(field)

    @staticmethod
    def collision_with_field(self,field) -> bool:
        field = convert_field(field)
        if (field[self.pos_Y][self.pos_X]=='1'):
            return True
        elif (field[self.pos_Y][self.pos_X]=='0'):
            return False
