import pygame
import random
def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)
def credit_assets():
    replay=[pygame.transform.scale(pygame.image.load('_internal/credits/replay.png'), px(700, 700)),
            pygame.transform.scale(pygame.image.load('_internal/credits/empty button.png'), px(700, 700))]
    quit=[pygame.transform.scale(pygame.image.load('_internal/credits/quit.png'), px(700, 700)),
          pygame.transform.scale(pygame.image.load('_internal/credits/empty button.png'), px(700, 700))]
    sat=[pygame.transform.scale(pygame.image.load('_internal/satellite customisation/bin/body.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/bottom/'+check_missions[mission][questions['custom_bottom']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/middle/'+check_missions[mission][questions['custom_middle']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/top/'+check_missions[mission][questions['custom_top']]+'.png'), px(700, 700))]
    logo_ipsa=pygame.transform.scale(pygame.image.load('_internal/credits/ipsa.png'), px(400, 400))
    logo_git=pygame.transform.scale(pygame.image.load('_internal/credits/github.png'), px(150, 100))
    txt=pygame.transform.scale(pygame.image.load('_internal/credits/texte.png'), px(520, 125))
    title=pygame.transform.scale(pygame.image.load('_internal/menu/title.png'), px(400, 400))
    share=[pygame.transform.scale(pygame.image.load('_internal/credits/partage0.png'), px(800, 800)), pygame.transform.scale(pygame.image.load(
        '_internal/credits/partage1.png'), px(800, 800))]
    return replay,quit, sat, logo_ipsa, logo_git,share,txt,title

def credits():
    replay,quit,sat, logo_ipsa, logo_git,share,texte_missions,title=credit_assets()
    txt=[title,
         'FELICITATION',
         'TU AS COMPLETE LA MISSION',
         mission.upper()+ ' !',
         '',
         '',
         '',
         '',
         'SATMAN',
         'Une création IPSA',
         'sous licence blablabla',
         logo_ipsa,
         'PARTICPANTS :',
         '',
         'Professeur Referent : ',
         'M.BOSS',
          '',
          'Chef du projet SATMAN : ',
          'Pierre GAUTRON',
          '',
          'Pole Recherche :',
          'Eva SARZETAKIS',
          'Charlotte LEAUTEAUD',
          'Alexandra GENDREL',
          'Sarah WISZNIAK',
          '',
          'Pole Programmation : ',
          'Marc STRICKER',
          'Gabriel GOOSENS',
          'Quentin CHAMBON',
         '',
         '',
         'RETROUVE LE PROJET EN ENTIER SUR',
         logo_git,
         'GITHUB']
    run=True
    font_size=int(min(px(x=25),px(y=25)))
    font = pygame.font.Font('_internal/Grand9K Pixel.ttf', font_size)
    '''
    sat_pos=(0,0)
    sat_dir=(0,-1)
    '''
    i=0
    stars=[]
    for star in range(100):
        stars.append((random.randint(0,int(size.width)),random.randint(0,int(size.height))))
    start,y=300,10
    j=0
    clock=pygame.time.Clock()
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        clock.tick(70)
        i+=px(0.1)
        j+=px(0.05)
        screen.fill(bg_color)
        for star in stars:
            pygame.draw.rect(screen,(random.randint(0,255),random.randint(100,255),255),(star, (5,5)),5)
        '''
        if sat_pos[0]<=int(px(x=-200)):
            sat_pos=(sat_pos[0]+15,sat_pos[1])
            sat_dir=(random.randint(0,1),random.randint(-1,1))
        elif sat_pos[0]>=int(px(x=650)):
            sat_pos=(sat_pos[0]-15,sat_pos[1])
            sat_dir=(random.randint(-1,0),random.randint(-1,1))
        elif sat_pos[1]<=int(px(y=-130)):
            sat_pos=(sat_pos[0],sat_pos[1]+15)
            sat_dir=(random.randint(-1,1),random.randint(0,1))
        elif sat_pos[1]>=int(px(y=200)):
            sat_pos=(sat_pos[0],sat_pos[1]-15)
            sat_dir=(random.randint(-1,1),random.randint(-1,0))
        while sat_dir==(0,0):sat_dir=(random.randint(-1,1),random.randint(-1,1))
        sat_pos=(sat_pos[0]+sat_dir[0]*2,sat_pos[1]+sat_dir[1]*2)

        for im in sat:
            screen.blit(im, sat_pos)
        
        if start+((len(txt))*2)*font_size>=0:
            for line in range(len(txt)):
                x=(size.width//2)-(font.size(txt[line])[0]//2)
                screen.blit(font.render(txt[line],True,txt_color),(x,start+(line*2)*font_size))
        
        pygame.draw.rect(screen,(255,0,0),(px(740,490), px(300,100)), 10)
        screen.blit(button_font.render(replay_txt,True,(255,0,0)),px(770,500))
        replay_txt='REJOUER'
        if pygame.Rect.colliderect(mouse,(px(740,490), px(300,100))):
            if int(j)%2: replay_txt=''
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                print('replay')

        pygame.draw.rect(screen,(255,0,0),(px(20,490), px(300,100)), 10)
        screen.blit(button_font.render(quit_txt,True,(255,0,0)),px(50,500))
        quit_txt='QUITTER'
        if pygame.Rect.colliderect(mouse,(px(20,490), px(300,100))):
            if int(j%2): quit_txt=''
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
                state.game=False
                pygame.quit()

        '''
        #print(start,y)
        if y>=0:
            y=start
            for line in range(len(txt)):
                if type(txt[line])==type(''):
                    x=(px(x=650)//2)-(font.size(txt[line])[0]//2)
                    screen.blit(font.render(txt[line],True,txt_color),(x,y))
                    y+=2*font_size
                else:
                    x=(px(x=650)//2)-(txt[line].get_width()//2)
                    screen.blit(txt[line],(x,y))
                    y+=txt[line].get_height()
        if int(i%2):
            i=0
            start-=(font_size)//2


        if pygame.Rect.colliderect(mouse,(px(650,150), px(400,100))):
            if int(j)%2: screen.blit(replay[1],px(650,150))
            else:screen.blit(replay[0],px(650,150))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
        else:screen.blit(replay[0],px(650,150))

        if pygame.Rect.colliderect(mouse,(px(650,300), px(400,100))):
            if int(j%2): screen.blit(quit[1],px(650,300))
            else:screen.blit(quit[0],px(650,300))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
                state.game=False
                pygame.quit()
        else:screen.blit(quit[0],px(650,300))

        screen.blit(texte_missions, px(650,50))
        screen.blit(share[int(j%2)], px(650,450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                font_size=int(min(px(x=25),px(y=25)))
                sat_pos=(0,0)
                sat_dir=(0,-1)
                replay,quit,sat, logo_ipsa, logo_git,share,texte_missions,title=credit_assets()
                button_font = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(min(px(x=50), px(y=50))))
                font = pygame.font.Font('_internal/Grand9K Pixel.ttf', font_size)
                stars=[]
                for star in range(100):
                    stars.append((random.randint(0,int(size.width)),random.randint(0,int(size.height))))
pygame.init()
screen = pygame.display.set_mode((1066, 600), pygame.RESIZABLE)
txt_color=(255,)*3
bg_color=(28, 41, 81)
class size:
    width, height = pygame.display.get_surface().get_size()

class state:
    game = True
mission='satellite de communication'
check_missions={'satellite de communication': ['orbite géostationnaire','Kourou', 'panneaux solaires','_empty','grande antenne','None', 'SLS'],
          "satellite d'observation": ['orbite basse','Kourou','générateur nucléaire','senseur optique', 'antenne moyenne','None', 'vega'],
            "satellite de positionnement":['orbite moyenne','Kourou','générateur nucléaire','_empty','petite antenne','None', 'arianeV']}

questions={'orbite':0,'map':1,'custom_middle':2, 'custom_bottom':3, 'custom_top':4,'mission_order':5, 'velocity':6}
credits()
