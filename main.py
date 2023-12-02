import pygame
import random
pygame.init()
# colors : (60,21,24)|black bean, (105,20,14)|Blood red, (227,231,211)|Beige, (11,57,84)|Prussian blue, (152,156,148)|Battleship gray, (0,0,0)|black

#créer la fenêtre de jeu
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')

batiment = pygame.image.load("batiment.png")
batiment=pygame.transform.scale(batiment, (1066, 400))

ciel=[]
for i in range(1,6):
    c=pygame.image.load("ciel"+str(i)+".png")
    c=pygame.transform.scale(c, (1066, 600))
    ciel.append(c)
im=0

def px(x,y=None):
    if y==None:
        return (x*width)/1066
    else:
        return ((x*width)/1066,(y*height)/600)

#initialiser la boucle
running=True
while running:
    screen.fill((105,20,14))
    screen.blit(ciel[int(im)], px(0,0))
    im+=0.1
    if int(im)>=5:
        im=0
    screen.blit(batiment, px(0, 250))
    font = pygame.font.Font('Space Angel.ttf', int(px(60)))
    text = font.render('Satellite Manager', True, (0,0,0))
    screen.blit(text, (px(80,150),(0,0)))
    pygame.display.flip() # refresh l'écran

    for event in pygame.event.get():# voir tout input
        if event.type == pygame.QUIT: # si la croix quitter est cliqué
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = pygame.display.get_surface().get_size()
            asteroid=pygame.transform.scale(asteroid, px(50,50))
