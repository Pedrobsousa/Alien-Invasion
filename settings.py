# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:34:04 2017

@author: Pedro
"""

class Settings():
    """Uma classe para armazenar todas as configurações da alien_invasion."""
    
    def __init__(self):
        """Inicializa as configurações do jogo."""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        
        #Configurações da nave
        self.ship_speed_factor = 1.5
        
        #Configurações dos projeteis
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4