import pygame
from talk import talk
def resize_help():
    return [pygame.transform.scale(pygame.image.load('aide/aide-1.png'),px(150,150)),
            pygame.transform.scale(pygame.image.load('aide/aide-2.png'),px(150,150))]
def resize_assets():
    earth= pygame.transform.scale(pygame.image.load('orbit/earth.png'),(px(70),)*2)
    up_button=[pygame.transform.scale(pygame.image.load('orbit/up_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/up_button2.png'),px(150,150))]
    down_button=[pygame.transform.scale(pygame.image.load('orbit/down_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/down_button2.png'),px(150,150))]
    ok_button=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button2.png'),px(150,150))]
    return earth,up_button,down_button,ok_button
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def intro():
    screen.fill((173, 216, 230))
    pygame.display.update()
    talk([f"Bonjour, je suis l'ingénieur en chef du projet SATMAN.",
          "Je vais te guider au cours de cette mission !",
          "Si tu en a marre de m'entendre parler tu peux cliquer n'import où pour accélerer",
          "  ( clique n'importe où )"])
    screen.blit(resize_help()[0], px(10,-30))
    pygame.display.update()
    talk([f"En haut à gauche se trouve le bouton aide.",
          "Tu y trouvera toute les information nécesssaires pour t'aider",
          "  ( clique n'importe où )"])
    screen.blit(resize_assets()[1][0],px(900,50))
    screen.blit(resize_assets()[2][0],px(900,250))
    screen.blit(resize_assets()[3][0],px(700,150))
    pygame.display.update()
    talk([f"Aide toi des flèches pour naviguer le niveau.",
          "Et lorsque tu pense avoir trouver la bonne réponse appuie sur OK",
          "  ( clique n'importe où )"])
    talk([f"Tu es prêt à envoyer un {mission} dans l'espace ?",
          "Alors c'est parti !!!",
          "  ( clique n'importe où )"])


mission='satellite de communication'
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
intro()
