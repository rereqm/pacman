import pygame

from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, x, y, filename):
        self.filename = filename
        self.image = pygame.image.load(filename)
        r = self.image.get_rect()
        super().__init__(x, y, r.width, r.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
