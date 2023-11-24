import pygame
# colors : (60,21,24)|black bean, (105,20,14)|Blood red, (227,231,211)|Beige, (11,57,84)|Prussian blue, (152,156,148)|Battleship gray
#créer la fenêtre de jeu
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
width, height = pygame.display.get_surface().get_size()

screen.fill((105,20,14))
#initialiser la boucle
running=True
while running:
    pygame.display.flip() # refresh l'écran

    for event in pygame.event.get():# voir tout input
        if event.type == pygame.QUIT: # si la croix quitter est cliqué
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = pygame.display.get_surface().get_size()
            screen.fill((105,20,14))
