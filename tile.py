# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 20:47:31 2022

@author: andre
"""

import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)