# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:03:56 2024

@author: stric
"""

#ajouter tick vert pour satellite creator et une aide qui explique les diffÃ©rents choix et la mission
import pygame
import math
import random

# fonction adaptant les positions en fonction de la taille de l'Ã©cran
# (prend en argument la position x et y initial sur une taille d'Ã©cran de 1066x600)
def px(x=None,y=None):
    if y==None:#si aucune valeur y n'est donnÃ©, calculer seulement x
        return (x*size.width)/1066# produit en croix appelant la class size
    elif x==None:#si aucune valeur x n'est donnÃ©, calculer seulement y
        return (y*size.height)/600# produit en croix appelant la class size
    else:
        return ((x*size.width)/1066,(y*size.height)/600)#sinon renvoyÃ© la nouvelle valeur de x et y
def resize_earth_map_assets():
    earth= pygame.transform.scale(pygame.image.load('Earth_map/Earth_map.png'),px(1066,1066))
    up_button=[pygame.transform.scale(pygame.image.load('orbit/up_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('orbit/up_button2.png'),px(150,150))]
    down_button=[pygame.transform.scale(pygame.image.load('orbit/down_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('orbit/down_button2.png'),px(150,150))]
    ok_button=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'),px(150,150))]
    return earth,up_button,down_button,ok_button
def earth_map():
    run = True
    locations = {'Kourou':[(330,300), True],'Toulouse':[(520,130),False] ,'Elbrouz':[(680,200),False]}
    earth,up_button,down_button,ok_button=resize_earth_map_assets()
    while run and state.game: 
        screen.fill((173, 216, 230))
        screen.blit(earth, px(0,-100))
        screen.blit(up_button[0], px(900,120))
        screen.blit(down_button[0],px(900,250))
        screen.blit(ok_button[0], px(900,400))
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        if pygame.Rect.colliderect(mouse,(px(900,120),px(200,100))):# vÃ©rifie si curseur survol bouton retour
            screen.blit(up_button[1],px(900,120))
        if pygame.Rect.colliderect(mouse,(px(900,250),px(200,100))):# vÃ©rifie si curseur survol bouton retour
            screen.blit(down_button[1],px(900,250))
        if pygame.mouse.get_pressed()[0]== True:
            
        if pygame.Rect.colliderect(mouse, (px(900,400),px(200,100))):
            screen.blit(ok_button[1], px(900,400))
        for i in locations:
            print(locations[i][0][0])
            if locations[i][1]==True:
                pygame.draw.circle(screen,(255,0,0),px(locations[i][0][0],locations[i][0][1]),int(min(px(x=10),px(y=10))))
            else:
                pygame.draw.circle(screen,(0,0,0),px(locations[i][0][0],locations[i][0][1]),int(min(px(x=10),px(y=10))))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth,up_button,down_button,ok_button=resize_earth_map_assets()
                
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio               
class size:
    width, height = pygame.display.get_surface().get_size()
class state:
    game=True
earth_map()
