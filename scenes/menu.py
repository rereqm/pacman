import pygame

from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings


class MenuScene(BaseScene):
    PROCESS_ESCAPE = False

    def __init__(self):
        self.hello_text = Text(
            x=Settings.WINDOW_WIDTH // 2 - 315,
            y=Settings.WINDOW_HEIGHT // 2 - 30,
            text='Hello, application',
            size=58,
            color=pygame.Color('yellow')
        )
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)

    def additional_process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            Settings.set_scene(1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            Settings.set_scene(2)
