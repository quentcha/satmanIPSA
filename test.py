import pygame
import sys
import math

# Paramètres physiques
G = 6.67430e-11  # Constante gravitationnelle
M_Terre = 5.972e24  # Masse de la Terre
Rayon_Terre = 6371e3  # Rayon de la Terre en mètres
Altitude_Orbite = 35786e3  # Altitude de l'orbite géostationnaire en mètres
Masse_Satellite = 840  # Masse du satellite en kg

# Paramètres de l'orbite
Demi_Grand_Axe = Rayon_Terre + Altitude_Orbite
Excentricite = 0.0  # Pour une orbite géostationnaire, l'excentricité est nulle

# Initialisation Pygame
pygame.init()

# Paramètres de l'écran
largeur, hauteur = 900, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Simulation de trajectoire satellite")

# Couleurs
couleur_terre = (0, 100, 255)
couleur_satellite = (255, 0, 0)

# Fonction pour convertir les coordonnées polaires en coordonnées cartésiennes
def polaires_vers_cartesiennes(angle, rayon):
    x = rayon * math.cos(angle)
    y = rayon * math.sin(angle)
    return x, y

# Fonction pour calculer la position du satellite en fonction du temps
def position_satellite(temps):
    vraie_anomalie = temps * math.sqrt(G * M_Terre / Demi_Grand_Axe**3)
    x, y = polaires_vers_cartesiennes(vraie_anomalie, Demi_Grand_Axe * (1 - Excentricite**2) / (1 + Excentricite * math.cos(vraie_anomalie)))
    #x=x//100000
    #y=y//100000
    return largeur // 2 + int(x * 1e-5), hauteur // 2 - int(y * 1e-5)

# Boucle principale
horloge = pygame.time.Clock()
temps = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fenetre.fill((0,)*3)

    # Dessiner la Terre
    pygame.draw.circle(fenetre, (0,0,255), (largeur // 2, hauteur // 2), Rayon_Terre // 100000)

    # Calculer la position du satellite
    position = position_satellite(temps)
    print(position)
    # Dessiner le satellite
    pygame.draw.circle(fenetre, (255,0,0), position, 5)

    pygame.display.flip()
    horloge.tick(60)
    temps += 1
