import os
import pygame


def load_textures(folder):
    files = os.listdir(folder)
    textures = []
    for i in files:
        with open(folder+i) as f:
            textures.append(pygame.image.load(f))
    textures.append(textures[1])
    return textures