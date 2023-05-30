import pygame

from settings import Settings


class BaseScene:
    PROCESS_ESCAPE = True

    def __init__(self):
        self.objects = []
        self.set_up_objects()

    def set_up_objects(self):
        pass

    def activate(self):
        for item in self.objects:
            item.activate()
        self.additional_activate()

    def additional_activate(self):
        pass

    def process_escape_event(self, event):
        if not self.PROCESS_ESCAPE:
            return
        if event.type != pygame.KEYDOWN or event.key != pygame.K_ESCAPE:
            return
        Settings.set_scene(0)

    def process_event(self, event):
        for item in self.objects:
            item.event(event)
        self.additional_process_event(event)
        self.process_escape_event(event)

    def additional_process_event(self, event):
        pass

    def process_logic(self):
        for item in self.objects:
            item.logic()
        self.process_additional_logic()

    def process_additional_logic(self):
        pass

    def process_draw(self, screen):
        for item in self.objects:
            item.draw(screen)
        self.process_additional_draw(screen)

    def process_additional_draw(self, screen):
        pass
