import pygame

from objects.score import ScoreDrawer
from scenes.base import BaseScene
from objects.sprites.pacman import Pacman
from objects.field import FieldDrawer
from settings import Settings
from objects.sprites.seeds import Energizer, Seed
from objects.cherry import Cherry
from objects.ghosts.blinky import Blinky
from objects.ghosts.inky import Inky
from objects.ghosts.pinky import Pinky
from objects.ghosts.clyde import Clyde
from logic.field import Field


class GameScene(BaseScene):
    def __init__(self):
        self.Score = ScoreDrawer(30, 0, 32, pygame.Color('white'))
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.Score)
        field = FieldDrawer(Settings.IMAGES_PIX_SIZE)
        for i in field.get_all_obj():
            self.objects.append(i)
        self.blinky = Blinky()
        self.inky = Inky()
        self.clyde = Clyde()
        self.pinky = Pinky()
        self.objects.append(self.blinky)
        self.objects.append(self.inky)
        self.objects.append(self.clyde)
        self.objects.append(self.pinky)
        self.pacman = Pacman(20*14+50, 20*23+50, Settings.PAC_IMAGE)
        self.objects.append(Cherry(19 * 14 + 58, 15 * 23 + 50, 15, 15))
        self.objects.append(self.pacman)
        self.objects[-2].logic_part_1()
        self.field123 = Field()
        self.blinky.chasef(self.pacman,self.field123.get())
        self.clyde.chasef(self.pacman, self.field123.get())
        self.pinky.chasef(self.pacman, self.field123.get())
        self.inky.chasef(self.pacman, self.field123.get(), self.blinky)
        print(self.blinky.pos_X,self.blinky.pos_Y)

    def process_additional_logic(self):
        for i in range(len(self.objects)):
            if isinstance(self.objects[i],Energizer):
                if self.pacman.rect.collidepoint(self.objects[i].pos):
                    self.Score.add_scores(self.objects[i].score)
                    self.pacman.start_rage()
                    #for ghost in self.ghosts:
                    #    ghost.scare()
                    del self.objects[i]
                    return
            if isinstance(self.objects[i],Seed):
                if self.pacman.rect.collidepoint(self.objects[i].pos):
                    self.Score.add_scores(self.objects[i].score)
                    del self.objects[i]
                    return
            if isinstance(self.objects[i],Cherry):
                if self.pacman.rect.collidepoint(self.objects[i].pos) and self.objects[i].is_Visible:
                    self.Score.add_scores(self.objects[i].score)
                    self.objects[i].timer.cancel()
                    self.objects[i].logic_part_2()
                    return
        if len(self.objects)<=4:
            self.objects[-1].rage_timer.cancel()  # чтобы не зависало приложение
            if isinstance(self.objects[-2], Cherry):
                self.objects[-2].timer.cancel()
                Settings.set_scene(0)
                del self.objects
                self.objects = []
                self.set_up_objects()

            self.blinky.chasef(self.pacman, self.field123.get())
            self.clyde.chasef(self.pacman, self.field123.get())
            self.pinky.chasef(self.pacman, self.field123.get())
            self.inky.chasef(self.pacman, self.field123.get(), self.blinky)

    def process_escape_event(self, event):
        if event.type == pygame.QUIT:
            self.objects[-1].rage_timer.cancel()  #чтобы не зависало приложение
            if isinstance(self.objects[-2],Cherry):
                self.objects[-2].timer.cancel()  # чтобы не зависало приложение
        if not self.PROCESS_ESCAPE:
            return
        if event.type != pygame.KEYDOWN or event.key != pygame.K_ESCAPE:
            return
        Settings.set_scene(0)
