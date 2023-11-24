import pygame
import random
pygame.init()
# colors : (60,21,24)|black bean, (105,20,14)|Blood red, (227,231,211)|Beige, (11,57,84)|Prussian blue, (152,156,148)|Battleship gray, (0,0,0)|black

#créer la fenêtre de jeu
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')

earth = pygame.image.load("earth.png")
earth=pygame.transform.scale(earth, (600, 600))

asteroid = pygame.image.load("asteroid.png")
asteroid=pygame.transform.scale(asteroid, (50, 50))
posx, posy=-10,random.randint(0, width)
movx, movy=random.choice([-1,1]), 1

def px(x,y=None):
    if y==None:
        return (x*width)/1066
    else:
        return ((x*width)/1066,(y*height)/600)

#initialiser la boucle
running=True
while running:
    posx, posy = posx+movx, posy+movy
    screen.fill((105,20,14))
    screen.blit(asteroid, px(posx,posy))
    screen.blit(earth, px(200,400))
    font = pygame.font.Font('Space Angel.ttf', int(px(60)))
    text = font.render('Satellite Manager', True, (0,0,0))
    screen.blit(text, (px(80,150),(0,0)))
    pygame.display.flip() # refresh l'écran

    if posy > height+10:
        posx,posy =random.randint(0, width), -10
        movx, movy = random.choice([-1,1]),1
    if posx < 0 or posx > width:
        posx,posy =random.randint(0, width), -10
        movx, movy = random.choice([-1,1]),1

    for event in pygame.event.get():# voir tout input
        if event.type == pygame.QUIT: # si la croix quitter est cliqué
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = pygame.display.get_surface().get_size()
            asteroid=pygame.transform.scale(asteroid, px(50,50))
