import pygame


class Settings:
    WINDOW_WIDTH = 560+100
    WINDOW_HEIGHT = 620+100
    MAX_COLLISION_COUNT = 5
    IMAGES_PIX_SIZE = 20
    MAX_WAIT_SECONDS = 3
    BACKGROUND_COLOR = pygame.Color('black')
    PAC_IMAGE = 'textures/pacsprites/20/pac_0_20x20.png'
    scene_changed = True
    scene_index = 0

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index

    @staticmethod
    def set_game_scene():
        Settings.set_scene(1)
