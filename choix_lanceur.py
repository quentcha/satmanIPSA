import pygame
import random
def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)
def load_rockets():
    rockets={'ArianeV':pygame.transform.scale(pygame.image.load('lanceur/arianeV.png'),px(550,550))
                ,'SLS':pygame.transform.scale(pygame.image.load('lanceur/SLS.png'),px(550,550))
                ,'vega':pygame.transform.scale(pygame.image.load('lanceur/vega.png'),px(550,550))}


    up_button = [pygame.transform.scale(pygame.image.load('orbit/up_button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('orbit/up_button2.png'), px(150, 150))]
    down_button = [pygame.transform.scale(pygame.image.load('orbit/down_button1.png'), px(150, 150)),
                   pygame.transform.scale(pygame.image.load('orbit/down_button2.png'), px(150, 150))]
    ok_button = [pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'), px(150, 150))]
    return rockets,up_button,down_button,ok_button

def rocket_choice():
    run=True
    rockets,up_button,down_button,ok_button=load_rockets()
    stats={'ArianeV':{"Nom":"Ariane V","Constructeur":"ESA","Capacité d'emport en LEO (en tonnes)":[10.35,11],"Capacité d'emport en GTO (en tonnes)":[5,5],"Fiabilité (en %)":[95.7,100],"Réutilisable":'non'},
    'SLS':{"Nom":"Space Launch System (SLS)","Constructeur":"NASA","Capacité d'emport en LEO (en tonnes)":[9,11],"Capacité d'emport en GTO (en tonnes)":[3,5],"Fiabilité (en %)":'inconnu',"Réutilisable":'non'},
    'vega':{"Nom":"Vega","Constructeur":"ESA","Capacité d'emport en LEO (en tonnes)":[2.3,11],"Capacité d'emport en GTO (en tonnes)":[1.5,5],"Fiabilité (en %)":[98,100],"Réutilisable":'non'}}
    index=0
    txt_size=20
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(txt_size)))
    while run and state.game:
        screen.fill(bg_color)
        screen.blit(list(rockets.values())[index],px(400,20))

        #screen.blit(help_button[0],px(5,-50))
        screen.blit(up_button[0], px(900, 60))
        screen.blit(down_button[0], px(900, 190))
        screen.blit(ok_button[0], px(900, 370))

        x=10
        y=size.height//2-(len(stats[list(rockets.keys())[index]])*px(txt_size)*4)//2
        for info in stats[list(rockets.keys())[index]]:
            if type(stats[list(rockets.keys())[index]][info])==type(''):
                screen.blit(font.render(info+' : ',True,(txt_color)),px(x,y))
                y+=px(txt_size)
                screen.blit(font.render(str(stats[list(rockets.keys())[index]][info]),True,(txt_color)),px(x,y))
            else:
                max_val=stats[list(rockets.keys())[index]][info][1]
                val=stats[list(rockets.keys())[index]][info][0]
                max_length=150

                screen.blit(font.render(info+' : ',True,(txt_color)),px(x,y))
                y+=px(txt_size)
                pygame.draw.rect(screen,(txt_color),(px(x,y+txt_size),px(val*max_length/max_val,txt_size)),int(px(y=txt_size)))
                screen.blit(font.render(str(stats[list(rockets.keys())[index]][info][0]),True,(txt_color)),px(20+val*max_length/max_val,y+txt_size-5))

            y+=px(txt_size)*3


        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        if pygame.Rect.colliderect(mouse, (px(900, 120), px(200, 100))):
            screen.blit(up_button[1], px(900, 60))
            if pygame.mouse.get_pressed()[0]:
                if index+1==len(rockets):
                    index=0
                else:index+=1
                pygame.time.wait(200)

        if pygame.Rect.colliderect(mouse, (px(900, 250), px(200, 100))):
            screen.blit(down_button[1], px(900, 190))
            if pygame.mouse.get_pressed()[0]:
                if index==0:
                    index=len(rockets)-1
                else:index-=1
                pygame.time.wait(200)

        if pygame.Rect.colliderect(mouse, (px(900, 370), px(200, 100))):
            screen.blit(ok_button[1], px(900, 370))
            if pygame.mouse.get_pressed()[0]:
                run=False
                pygame.time.wait(200)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                rockets,up_button,down_button,ok_button=load_rockets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(txt_size)))
    return list(rockets.keys())[index]

pygame.init()
screen = pygame.display.set_mode((1066, 600), pygame.RESIZABLE)
txt_color=(0,)*3
bg_color=(173, 216, 230)
class size:
    width, height = pygame.display.get_surface().get_size()

class state:
    game = True
mission='satellite de communication'
check_missions={'satellite de communication': ['orbite géostationnaire','Kourou', 'panneaux solaires','_empty','grande antenne','None', 'SLS'],
          "satellite d'observation": ['orbite basse','Kourou','générateur nucléaire','senseur optique', 'antenne moyenne','None', 'vega'],
            "satellite de positionnement":['orbite moyenne','Kourou','générateur nucléaire','_empty','petite antenne','None', 'arianeV']}

questions={'orbite':0,'map':1,'custom_middle':2, 'custom_bottom':3, 'custom_top':4,'mission_order':5, 'velocity':6}

print(rocket_choice())
