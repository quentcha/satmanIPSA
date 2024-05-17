import pygame
import random
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def resize_help():
    return [pygame.transform.scale(pygame.image.load('_internal/aide/aide-1.png'), px(150, 150)),
            pygame.transform.scale(pygame.image.load('_internal/aide/aide-2.png'), px(150, 150))]
def load_space_velocity_assets():
    clouds=[pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud0.png'), px(200, 200)),
            pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud1.png'), px(200, 200)),
            pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud2.png'), px(200, 200)),
            pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud3.png'), px(200, 200)),
            pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud4.png'), px(200, 200)),
            pygame.transform.scale(pygame.image.load('_internal/space velocity/cloud5.png'), px(200, 200))]
    speedometer=pygame.transform.scale(pygame.image.load('_internal/space velocity/speedometer.png'), px(400, 400))
    liberation_button=[pygame.transform.scale(pygame.image.load('_internal/space velocity/lancement0.png'), px(250, 250)),
                       pygame.transform.scale(pygame.image.load('_internal/space velocity/lancement1.png'), px(250, 250)),
                       pygame.transform.scale(pygame.image.load('_internal/space velocity/lancement2.png'), px(250, 250))]
    return clouds, speedometer, liberation_button
def load_space_vehicles():
    arianeV=pygame.transform.scale(pygame.image.load('_internal/lanceur/arianeV.png'), px(400, 400))
    sls=pygame.transform.scale(pygame.image.load('_internal/lanceur/SLS.png'), px(400, 400))
    vega=pygame.transform.scale(pygame.image.load('_internal/lanceur/vega.png'), px(400, 400))
    booster_arianeV=[pygame.transform.scale(pygame.image.load('_internal/lanceur/Feu booster Ariane 1.png'), px(400, 400)),
                     pygame.transform.scale(pygame.image.load('_internal/lanceur/Feu booster Ariane 2.png'), px(400, 400)),
                     366,265]
    booster_sls=[pygame.transform.scale(pygame.image.load('_internal/lanceur/Feu booster SLS 1.png'), px(400, 400)),
                 pygame.transform.scale(pygame.image.load('_internal/lanceur/Feu booster SLS 2.png'), px(400, 400)),
                 343,265]
    return {'arianeV':[arianeV,booster_arianeV],'SLS':[sls, booster_sls], 'vega':[vega, booster_arianeV]}
def second_space_velocity():
    run=True
    clock=pygame.time.Clock()
    clock.tick(70)
    clouds, speedometer, liberation_button=load_space_velocity_assets()
    lanceur=load_space_vehicles()[check_missions[mission][2]][0]
    booster=load_space_vehicles()[check_missions[mission][2]][1]
    help_button=resize_help()
    layers=[[None, [0,0], 0],]*(len(clouds)+1)
    layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
    time=2000
    i=0
    initialize=True
    while run:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        clock.tick(70)#maintien 70 fps quel que soit la taille de l'écran et donc la vitesse de rafraichissement
        i+=0.3
        if i>= time:
            run = False
            return False
        screen.fill(bg_color)
        for slots in range(len(layers)-int((i*((len(clouds)+1)//2))/time)):#diminue le nombre de nuages au fil du temps
            if layers[slots]==[None, [0,0], 0]:
                layers[slots]=[clouds[random.randint(0,len(clouds)-1)], [random.randint(-200,int(size.width)),random.randint(int(px(y=-200)),int(px(y=-110)))], random.randint(int(px(y=1)),int(px(y=5)))+(i%time/100)]
            else:
                screen.blit(layers[slots][0], (layers[slots][1][0], layers[slots][1][1]))
                if layers[slots][1][1]>=size.height+100:
                    layers[slots]=[None, [0,0], 0]
                if layers[slots][0]!=lanceur:
                    layers[slots][1][1]+=layers[slots][2]
                else:
                    layers[slots][1][0]=px(x=350+i%3)
                    screen.blit(booster[int(i)%2], px(booster[2]+i%3,booster[3]))

        screen.blit(speedometer, px(-150,100))
        #max 446,min 110
        pygame.draw.rect(screen, ((0,0,0)), (px(190,495-(i*385)/time),px(56,5)))
#775-1295
        pos_button=px(745,200)
        if i>(time*775)/2000 and i<(time*1295)/2000:
            screen.blit(liberation_button[int(i/5)%2], pos_button)
        else:
            screen.blit(liberation_button[0], pos_button)

        screen.blit(help_button[0],px(5,-50))
        if pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                print('help')
        if pygame.Rect.colliderect(mouse,(pos_button,px(250,250))):
            if i>(time*775)/2000 and i<(time*1295)/2000:
                screen.blit(liberation_button[(int(i/5)%2)+1], pos_button)
                if pygame.mouse.get_pressed()[0]:
                    run=False
                    return True
            else:
                screen.blit(liberation_button[2], pos_button)
                if pygame.mouse.get_pressed()[0]:
                    run=False
                    return False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                clouds, speedometer, liberation_button=load_space_velocity_assets()
                lanceur=load_space_vehicles()[check_missions[mission][2]][0]
                booster=load_space_vehicles()[check_missions[mission][2]][1]
                help_button=resize_help()
                layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
        if initialize==True:
            print('talk')
            initialize=False


pygame.init()
bg_color=(173, 216, 230)
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
check_missions={'satellite de communication': ['orbite géostationnaire', ['panneaux solaires','','grande antenne'], 'vega'],
          "satellite d'observation": ['orbite basse',['générateur nucléaire','senseur optique', 'antenne moyenne'], 'SLS'],
            "satellite de positionnement":['orbite moyenne',['générateur nucléaire','','petite antenne'], 'arianeV']}
mission="satellite de positionnement"


print(second_space_velocity())
