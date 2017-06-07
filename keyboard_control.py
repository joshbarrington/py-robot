__author__ = 'joshuabarrington'

import pygame
from pygame.locals import *

pygame.init()


class KeyboardInput:
    def read_command(self):
        pygame.init()
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            return "w"
        elif key[pygame.K_a]:
            return "a"
        elif key[pygame.K_s]:
            return "s"
        elif key[pygame.K_d]:
            return "d"
