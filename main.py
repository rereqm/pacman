import pygame

from application import Application
from settings import Settings
from objects.ghosts.blinky import Blinky
from objects.ghosts.pinky import Pinky
from objects.ghosts.inky import Inky
from objects.ghosts.clyde import Clyde
from logic.field import Field


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])
    app = Application(screen)
    app.run()
if __name__ == '__main__':
    main()
