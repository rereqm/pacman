import pygame
from objects.base import BaseObject


class Cell(BaseObject):
    def __init__(self, type, x, y, filename):
        self.type = type
        self.filename = filename
        self.image = pygame.image.load(self.filename)
        r = self.image.get_rect()
        super().__init__(x, y, r.width, r.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
