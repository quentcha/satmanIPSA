import pygame
pygame.init()
# colors : (60,21,24)|black bean, (105,20,14)|Blood red, (227,231,211)|Beige, (11,57,84)|Prussian blue, (152,156,148)|Battleship gray, (0,0,0)|black

#créer la fenêtre de jeu
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
asteroid = pygame.image.load("asteroid.png")

#initialiser la boucle
running=True
while running:
    screen.fill((105,20,14))
    font = pygame.font.Font('Space Angel.ttf', int((60*width)/1066))
    text = font.render('Satellite Manager', True, (0,0,0))
    screen.blit(text, (((80*width)/1066,(150*height)/600),(0,0)))
    pygame.display.flip() # refresh l'écran

    for event in pygame.event.get():# voir tout input
        if event.type == pygame.QUIT: # si la croix quitter est cliqué
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = pygame.display.get_surface().get_size()
