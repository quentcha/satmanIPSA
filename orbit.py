import pygame
import math
from talk import talk
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def resize_assets():
    earth= pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/earth.png'),(px(70),)*2)
    up_button=[pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/up_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/up_button2.png'),px(150,150))]
    down_button=[pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/down_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/orbit/down_button2.png'),px(150,150))]
    ok_button=[pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button2.png'),px(150,150))]
    return earth,up_button,down_button,ok_button
def point_circulaire(angle, rayon):
    # Conversion des coordonnées polaires en coordonnées cartésiennes
    x = rayon * math.cos(math.radians(angle))
    y = rayon * math.sin(math.radians(angle))

    return x, y
def choose_orbit():
    run=True
    earth,up_button,down_button,ok_button=resize_assets()
    angle=0
    #nom:[altitude en pixel,coef vitesse,sélectionné]
    orbite={'':[0,0,True],'orbite basse':[105.99,4,False],'orbite moyenne':[203.68,2,False],'orbite haute':[296.4,1,False]}
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    orbit_choice=0
    while run==True:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.fill((173, 216, 230))

        earth_w,earth_h=pygame.transform.rotate(earth, angle).get_size()
        for circle in orbite:
            if orbite[circle][2]==True:
                pygame.draw.circle(screen, (105,20,14),(size.width/2,size.height/2),px(orbite[circle][0]),int(px(5)))
            else:
                 pygame.draw.circle(screen, (255,255,255),(size.width/2,size.height/2),px(orbite[circle][0]),int(px(5)))

        for sat in orbite:
            x,y=point_circulaire(angle*orbite[sat][1],px(orbite[sat][0]))
            if orbite[sat][2]==True:
                pygame.draw.circle(screen, (255,0,0),(size.width/2+x,size.height/2-y),int(px(5)),int(px(5)))
                screen.blit(font.render(sat, True, (255,0,0)), (size.width/2+x+7,size.height/2-y-7,0,0))

            else:
                pygame.draw.circle(screen, (0,0,0),(size.width/2+x,size.height/2-y),int(px(5)),int(px(5)))

        screen.blit(pygame.transform.rotate(earth, angle),((size.width/2)-(earth_w/2),(size.height/2)-(earth_h/2)))

        angle+=1

        screen.blit(down_button[0],px(900,250))
        screen.blit(up_button[0],px(900,50))
        screen.blit(ok_button[0],px(900,420))
        if pygame.Rect.colliderect(mouse,(px(900,50),px(150,150))):
            screen.blit(up_button[1],px(900,50))
            if pygame.mouse.get_pressed()[0]==True:
                if orbit_choice+1==len(orbite): orbit_choice=0
                else: orbit_choice+=1
                pygame.time.wait(200)
        elif pygame.Rect.colliderect(mouse,(px(900,250),px(150,150))):
            screen.blit(down_button[1],px(900,250))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                if orbit_choice-1<0: orbit_choice=len(orbite)-1
                else: orbit_choice-=1
                pygame.time.wait(200)
        elif pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True and orbit_choice!=0:
                run=False
        for key in orbite:
            if key==list(orbite.keys())[orbit_choice]: orbite[key][2]=True
            else: orbite[key][2]=False
        pygame.time.wait(100)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth,up_button,down_button,ok_button=resize_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))

    return list(orbite.keys())[orbit_choice]

pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
print(choose_orbit())

