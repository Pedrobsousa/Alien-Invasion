# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:56:34 2017

@author: Pedro
"""

import sys
from bullet import Bullet
from alien import Alien
import pygame

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
         pygame.quit()
        
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projetil se o limite nao foi alcançado."""
    #Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:    
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e mouse."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

                
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    #Redesenha todos os projéteis atrás da nave e dos aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #Deixa a tela mais recente visível
    pygame.display.flip()
    
    
def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos antigos."""
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        
        
def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número de aliens que cabem na linha."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    #Cria um alien e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
    
    
def create_fleet(ai_settings, screen, aliens):
    """Cria uma frota completa de alienígenas."""
    #Cria Alien e calcula o numero de aliens na linha
    #O espaçamento entre aliens é igual à largura de um alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    
    #Cria a primeira linha de aliens
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
