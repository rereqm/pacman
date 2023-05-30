import pygame
from objects.images import Image
from settings import Settings
from logic.field import Field
from objects.sprites.load_textures import load_textures
from threading import Timer

class Pacman(Image):
    def __init__(self, x, y, filename):
        self.x = 14
        self.y = 23
        self.initial = {
            'x': x,
            'y': y,
            'shift': [0, 0]
        }
        super().__init__(x, y, filename)
        self.shift = [0, 0]
        self.speed_multiplier = 0.5  # for test
        self.field = Field().get()
        self.last_press_key = ''


        self.rage = False
        self.rage_time = 10 # время рейджа в секундах
        self.rage_timer = Timer(self.rage_time, self.end_rage)


        self.arr_of_textures_simp = load_textures(folder='textures/pacsprites/20/')      # спасибо тому кто это сделал, теперь бы понять как это работает
        # сюда бы ещё текстуры для режима ярости, но нет так нет

        self.anim_tik = 0

        self.last_shift = [0, 0]  # направление прошлого движения, необходимо для поворота при остановке
        self.image_to_draw = self.arr_of_textures_simp[0]  # необходимо для анимаций "сыра"



    def activate(self):
        pass
        #self.rect.x = self.initial['x']
        #self.rect.y = self.initial['y']
        #self.x = self.initial['x'] // Settings.IMAGES_PIX_SIZE
        #self.y = self.initial['y'] // Settings.IMAGES_PIX_SIZE
        #self.shift = [0,0]
        #self.last_press_key = ''

    def step(self):
        self.rect.x += self.shift[0]
        self.rect.y += self.shift[1]
        if self.shift != [0,0]:
            self.anim_tik+=1
            self.anim_tik%=40

    def change_shift(self):
        if self.last_press_key == 'w' and not self.collision([0, -1]):
            self.last_shift = self.shift
            self.shift = [0, -1]
        elif self.last_press_key == 's' and not self.collision([0, 1]):
            self.last_shift = self.shift
            self.shift = [0, 1]
        elif self.last_press_key == 'a' and not self.collision([-1, 0]):
            self.last_shift = self.shift
            self.shift = [-1, 0]
        elif self.last_press_key == 'd' and not self.collision([1, 0]):
            self.last_shift = self.shift
            self.shift = [1, 0]
        if not self.collision(self.shift):
            self.x += self.shift[0]
            self.y += self.shift[1]
        else:
            self.shift = [0, 0]

    def teleport(self):
        if self.x == 27 and self.y == 14:
            self.x = 0
            self.rect.x = 50
            self.last_press_key = 'd'
        elif self.x == 0 and self.y == 14:
            self.x = 27
            self.rect.x = (27 * Settings.IMAGES_PIX_SIZE)+50
            self.last_press_key = 'a'

    def move(self):
        if (self.rect.x-50) % Settings.IMAGES_PIX_SIZE == 0 and (self.rect.y-50) % Settings.IMAGES_PIX_SIZE == 0:
            self.teleport()
            self.change_shift()
        self.step()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.last_press_key = 'w'
            elif event.key == pygame.K_s:
                self.last_press_key = 's'
            elif event.key == pygame.K_d:
                self.last_press_key = 'd'
            elif event.key == pygame.K_a:
                self.last_press_key = 'a'

    def collision(self, shift):
        return self.field[self.y + shift[1]][self.x + shift[0]] == 1

    def logic(self):
        self.move()
        self.animation()
    def draw(self, screen):
        screen.blit(self.image_to_draw, self.rect)

    def animation(self):
        self.eating_animation()
        self.rotation()
    def start_rage(self):
        self.rage = True
        self.rage_timer.cancel()
        self.rage_timer = Timer(self.rage_time, self.end_rage) #почему-то без этого не работает
        self.rage_timer.start()
    def end_rage(self):
        self.rage = False

    def eating_animation(self):  # эта функция отвечает за кадр рта
        #if self.rage == True:   #проверка ярости
           #self.image = self.arr_of_textures_rage[(self.anim_tik // 10)] # для этого куска нехватает текстур и режима ярости
        #else:
            self.image = self.arr_of_textures_simp[(self.anim_tik // 10)]

    def rotation(self):  # эта функция отвечает за направление взгляда "сыра"
        if self.shift == [0, 0]:  # если стоит на месте
            direction = self.last_shift  # смотрим куда двигался в прошлый раз
        else:  # иначе
            direction = self.shift  # куда двигается сейчас

        if direction == [0, -1]:  # относительно вектора движения поварачиваем текстуру в нужную сторону
            self.image_to_draw = pygame.transform.rotate(self.image, 90)
        elif direction == [0, 1]:
            self.image_to_draw = pygame.transform.rotate(self.image, -90)
        elif direction == [-1, 0]:
            self.image_to_draw = pygame.transform.rotate(self.image, 180)
        else:
            self.image_to_draw = self.image
