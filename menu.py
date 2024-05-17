import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def menu_images():
    title=pygame.transform.scale(pygame.image.load('/satmanIPSA/_internal/menu/title.png'), px(800, 800))
    scientifique1=[[],
    [pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 1.png'), px(280, 280)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 2.png'), px(280, 280)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 3.png'), px(280, 280))],
    [pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 1 M.png'), px(280, 280)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 2 M.png'), px(280, 280)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist/ssiantifique 3 M.png'), px(280, 280))]
    ]
    scientifique2=[[],
    [pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 1.png'), px(300, 300)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 2.png'), px(300, 300)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 3.png'), px(300, 300))],
    [pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 1 M.png'), px(300, 300)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 2 M.png'), px(300, 300)),
     pygame.transform.scale(pygame.image.load('_internal/menu/scientist2/ssiantifique 3 M.png'), px(300, 300))]
    ]
    background=[pygame.transform.scale(pygame.image.load('_internal/menu/pixil-layer-0.png'), px(1066, 600)),
                pygame.transform.scale(pygame.image.load('_internal/menu/pixil-layer-1.png'), px(1066, 600)),
                pygame.transform.scale(pygame.image.load('_internal/menu/pixil-layer-2.png'), px(1066, 600)),
                pygame.transform.scale(pygame.image.load('_internal/menu/pixil-layer-3.png'), px(1066, 600))]
    return title,scientifique1, scientifique2, background
def move(x_scientists):
    for i in range(len(x_scientists)):
        if x_scientists[i][0]>x_scientists[i][1]-10 and x_scientists[i][0]<x_scientists[i][1]+10:
            x_scientists[i][1]=random.randint(0,int(px(x=900)))
        x_scientists[i][0]+=(x_scientists[i][1]-x_scientists[i][0])*x_scientists[i][3]/abs(x_scientists[i][1]-x_scientists[i][0])
        x_scientists[i][2]=int((x_scientists[i][1]-x_scientists[i][0])/abs(x_scientists[i][1]-x_scientists[i][0]))
def menu():
    play_button=(px(x=300),px(y=250),px(x=465),px(y=100))
    run=True
    title_font = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(min(px(y=70), px(x=70))))
    credit_font = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(min(px(x=20), px(y=20))))
    pygame.mixer.music.load("_internal/sound/awesomeness.wav")
    pygame.mixer.music.play(-1)
    show_play=False
    title, scientifique0,scientifique1,background=menu_images()
    #x_scientists=[[0,random.randint(0,int(px(x=700))),1,3],[900,random.randint(0,int(px(x=900))),1,5]]
    x_scientists=[[0,random.randint(0,int(px(x=700))),1,3]]
    i=0
    while run:
        i+=0.8
        move(x_scientists)
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.fill((173, 216, 230))
        for image in range(len(background)):
            screen.blit(background[image],px(0,-image+(mouse[1]/100*(image))))
        screen.blit(title,px(130,50))

        if int(i)%4 and show_play:screen.blit(title_font.render("", True, (0, 0, 0)), (play_button[0] + 10, play_button[1] - 5))
        else:screen.blit(title_font.render("DECOLLAGE", True, (0, 0, 0)), (play_button[0] + 10, play_button[1] - 5))

        screen.blit(scientifique0[x_scientists[0][2]][int(i)%3],(x_scientists[0][0],px(y=385-3+(mouse[1]/100*(3)))))
        #screen.blit(scientifique1[x_scientists[1][2]][int(i+1)%3],(5,px(y=366)))
        pygame.draw.rect(screen, (255,0,0),play_button,5,True)
        screen.blit(credit_font.render("Un jeu créer par AéroKids IPSA",True,(0,0,0)),px(720,570))

        pygame.display.flip() # refresh l'écran
        pygame.time.wait(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if pygame.Rect.colliderect(mouse,play_button):
                show_play=True
                if pygame.mouse.get_pressed()[0]==True:
                    pygame.time.wait(200)
                    run=False
            else: show_play=False
            if event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                title_font = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(min(px(y=70), px(x=70))))
                credit_font = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(min(px(x=20), px(y=20))))
                play_button=(px(x=300),px(y=250),px(x=465),px(y=100))
                title, scientifique0,scientifique1, background=menu_images()


menu()
