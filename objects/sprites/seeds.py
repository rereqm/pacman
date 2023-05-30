import pygame
import sys
from settings import Settings
from objects.base import BaseObject

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


class Energizer(BaseObject):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 8
        self.score = 50
        self.color = WHITE
        self.pos = (int(self.x+(Settings.IMAGES_PIX_SIZE//2)), int(self.y+(Settings.IMAGES_PIX_SIZE//2)))
        self.width = 0

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.width)


class Seed(BaseObject):
    def __init__(self, x, y):
        self.radius_seed = 3
        self.score = 10
        self.x = x
        self.y = y
        self.pos = (int(self.x + (Settings.IMAGES_PIX_SIZE // 2)), int(self.y + (Settings.IMAGES_PIX_SIZE // 2)))

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, self.radius_seed)


