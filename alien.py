# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:08:04 2017

@author: Pedro
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A classe que representa um único alien da frota."""
    def __init__(self, ai_settings, screen):
        """Inicializa o alien e define a sua posição inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Carrega a imagem do alien e define o seu attr rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        
        #Inicia cada novo alien proximo a parte superior esquerda do monitor
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Armazena a posição exata do alien
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Desenha o alien na sua posição atual."""
        self.screen.blit(self.image, self.rect)