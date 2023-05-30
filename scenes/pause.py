import pygame

from objects.texts import Text
from scenes.base import BaseScene


class PauseScene(BaseScene):
    def __init__(self):
        self.header_text = Text(10, 10, 'This is pause!', 42, pygame.Color('red'))
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.header_text)
