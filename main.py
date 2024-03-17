#ajouter tick vert pour satellite creator et une aide qui explique les différents choix et la mission
import pygame
import math
import random
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def resize_return_help_buttons():
    return [pygame.transform.scale(pygame.image.load('aide/retour 1.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('aide/retour 2.png'),px(200,200))]
def blit(txt):
    help_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(15)))
    Mission_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(30)))
    pygame.draw.rect(screen, (140, 175, 186), (px(30, 30),px(1006,540)))
    screen.blit(Mission_font.render("Objectif : "+mission, True, (0,0,0)), (px(35,35),(0,0)))
    for phrase in range(len(txt.split("\n"))):
        screen.blit(help_font.render(txt.split("\n")[phrase], True, (0,0,0)), (px(35,100+phrase*30),(0,0)))

def help(num):
    back_button=resize_return_help_buttons()
    blit(help_text[num])
    run=True
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.blit(back_button[0],px(35,475))
        if pygame.Rect.colliderect(mouse,(px(35,475),px(200,100))):
            screen.blit(back_button[1],px(35,475))
            if pygame.mouse.get_pressed()[0]==True:
                run=False
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                back_button=resize_return_help_buttons()
                blit(help_text[num])
def resize_talking_frames():
    return [pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk0.png'),px(1060,1060)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk1.png'),px(1060,1060))]

def talk(txt):
    if state.game:
        speed=30
        talking_frames=resize_talking_frames()
        font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
        written=[]
        for paragraph in range(len(txt)):
            written.append("")
            for letter in range(len(txt[paragraph])):
                written[paragraph]=written[paragraph]+txt[paragraph][letter]
                screen.blit(talking_frames[(letter%6)//3], (px(0,390),(0,0)))
                for line in range(len(written)):
                    screen.blit(font.render(written[line], True, (0,0,0)), (px(140,450+(line*30)),(0,0)))
                    pygame.display.update()
                if pygame.mouse.get_pressed()[0]==True and len(written)+len(written[-1])!=len(txt)+len(txt[-1]):pygame.time.wait(10)
                else:pygame.time.wait(speed)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state.game=False
                        return
                    elif event.type == pygame.VIDEORESIZE:
                        size.width, size.height = pygame.display.get_surface().get_size()
                        talking_frames=resize_talking_frames()
                        font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
        while pygame.mouse.get_pressed()[0]!=True:
            screen.blit(talking_frames[1], (px(0,390),(0,0)))
            for line in range(len(written)):
                screen.blit(font.render(written[line], True, (0,0,0)), (px(140,450+(line*30)),(0,0)))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state.game=False
                        quit()
        return
def menu_images():
    title=pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/menu/title.png'),px(800,800))
    scientifique1=[[],
    [pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 1.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 2.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 3.png'),px(280,280))],
    [pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 1 M.png'),px(280,280)),
     pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 2 M.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 3 M.png'),px(280,280))]
    ]
    scientifique2=[[],
    [pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 1.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 2.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 3.png'),px(300,300))],
    [pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 1 M.png'),px(300,300)),
     pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 2 M.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique 3 M.png'),px(300,300))]
    ]
    background=[pygame.transform.scale(pygame.image.load('menu/pixil-layer-0.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-1.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-2.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-3.png'),px(1066,600))]
    return title,scientifique1, scientifique2, background
def move(x_scientists):
    for i in range(len(x_scientists)):
        if x_scientists[i][0]>x_scientists[i][1]-10 and x_scientists[i][0]<x_scientists[i][1]+10:
            x_scientists[i][1]=random.randint(0,int(px(x=900)))
        x_scientists[i][0]+=(x_scientists[i][1]-x_scientists[i][0])*x_scientists[i][3]/abs(x_scientists[i][1]-x_scientists[i][0])
        x_scientists[i][2]=int((x_scientists[i][1]-x_scientists[i][0])/abs(x_scientists[i][1]-x_scientists[i][0]))
def menu():
    play_button=(px(x=300),px(y=250),px(x=465),px(y=100))
    title_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(y=70),px(x=70))))
    credit_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=20),px(y=20))))
    pygame.mixer.music.load("sound/awesomeness.wav")
    pygame.mixer.music.play(-1)
    show_play=False
    title, scientifique0,scientifique1,background=menu_images()
    #x_scientists=[[0,random.randint(0,int(px(x=700))),1,3],[900,random.randint(0,int(px(x=900))),1,5]]
    x_scientists=[[0,random.randint(0,int(px(x=700))),1,3]]
    i=0
    run=True
    while run and state.game:
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
                state.game=False
            if pygame.Rect.colliderect(mouse,play_button):
                show_play=True
                if pygame.mouse.get_pressed()[0]==True:
                    pygame.time.wait(200)
                    run=False
            else: show_play=False
            if event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                title_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(y=70),px(x=70))))
                credit_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=20),px(y=20))))
                play_button=(px(x=300),px(y=250),px(x=465),px(y=100))
                title, scientifique0,scientifique1, background=menu_images()
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
def resize_help():
    return [pygame.transform.scale(pygame.image.load('aide/aide-1.png'),px(150,150)),
            pygame.transform.scale(pygame.image.load('aide/aide-2.png'),px(150,150))]
def choose_orbit():
    earth,up_button,down_button,ok_button=resize_assets()
    help_button=resize_help()
    angle=0
    #nom:[altitude en pixel,coef vitesse,sélectionné]
    orbite={'':[0,0,True],'orbite basse':[105.99,4,False],'orbite moyenne':[203.68,2,False],'orbite géostationnaire':[296.4,1,False]}
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    orbit_choice=0
    initialize=True
    run=True
    while run and state.game:
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

        screen.blit(help_button[0],px(5,-50))
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
        elif pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                help(0)
        for key in orbite:
            if key==list(orbite.keys())[orbit_choice]: orbite[key][2]=True
            else: orbite[key][2]=False

        pygame.time.wait(100)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth,up_button,down_button,ok_button=resize_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                help_button=resize_help()
        if initialize==True:
            talk(txt)
            initialize=False
    return list(orbite.keys())[orbit_choice]
def convert_images(parts):
    for category in parts:
        for l in range(len(parts[category])):
            parts[category][l]=pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/'+str(parts[category][l])),px(1500,1500))
    return parts
def resize_images(parts):
    for category in parts:
        for l in range(len(parts[category])):
            parts[category][l]=pygame.transform.scale(parts[category][l],px(1500,1500))
    return parts
def resize_buttons():
    left_button=[pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/left_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/left_button2.png'),px(150,150))]
    right_button=[pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/right_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/right_button2.png'),px(150,150))]
    buttons = {(px(0,20),px(150,150)):[left_button,['antenna',-1]],(px(0,220),px(150,150)):[left_button,['energy',-1]],(px(0,420),px(150,150)):[left_button,['sensor',-1]],
               (px(750,20),px(150,150)):[right_button,['antenna',1]],(px(750,220),px(150,150)):[right_button,['energy',1]],(px(750,420),px(150,150)):[right_button,['sensor',1]]}
    return buttons
def resize_ok():
    return [pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button2.png'),px(150,150))]
def resize_annotation():
    return {'energy':[px(330,210),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/annotation1.png'),px(80,80)),px(11)],
                'sensor':[px(330,440),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/annotation2.png'),px(80,80)),px(10)],
                'antenna':[px(330,60),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/annotation1.png'),px(80,80)),px(11)]}

def satellite_creator():

    p = {'energy':['','panneaux solaires','générateur nucléaire'],'sensor':['','senseur optique','senseur infrarouge','propulseur'], 'antenna':['','petite antenne', 'antenne moyenne', 'grande antenne']}
    parts = {'body':['body.png'], 'energy':['empty.png','solar panels.png','atomic generator.png'],'sensor':['empty.png','optic sensor.png','infrared sensor.png','small thruster.png'], 'antenna':['empty.png','small antenna.png', 'medium antenna.png', 'big antenna.png']}
    parts=convert_images(parts)
    buttons=resize_buttons()
    sat={'body':0,'energy':0,'sensor':0,'antenna':0}
    ok_button=resize_ok()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    annotation=resize_annotation()
    help_button=resize_help()
    initialize=True
    run=True
    while run and state.game:
        screen.fill((173, 216, 230))
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))

        screen.blit(help_button[0],px(911,-50))
        screen.blit(ok_button[0],px(900,420))
        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                run=False
                pygame.time.wait(200)
        elif pygame.Rect.colliderect(mouse,(px(911,-50),px(150,100))):
            screen.blit(help_button[1],px(911,-50))
            if pygame.mouse.get_pressed()[0]:
                help(1)

        for element in sat:
            screen.blit(parts[element][sat[element]], px(-185,-200))

        for element in annotation:
            if p[element][sat[element]]!='':
                screen.blit(annotation[element][1], annotation[element][0])
                if p[element][sat[element]] in check_missions[mission][1]:
                    screen.blit(font.render(p[element][sat[element]], True, (2,107,2)),(((annotation[element][0][0]-(len(p[element][sat[element]])*annotation[element][2]),annotation[element][0][1]-annotation[element][2])),(0,0)))
                else: screen.blit(font.render(p[element][sat[element]], True, (0,0,0)),(((annotation[element][0][0]-(len(p[element][sat[element]])*annotation[element][2]),annotation[element][0][1]-annotation[element][2])),(0,0)))


        for pos in buttons:
            screen.blit(buttons[pos][0][0], (pos[0][0],pos[0][1]))

        colliding=pygame.Rect.collidedict(mouse, buttons)
        if colliding:
            screen.blit(buttons[colliding[0]][0][1], colliding[0][0])
            if pygame.mouse.get_pressed()[0] == True:
                if sat[buttons[colliding[0]][1][0]]+buttons[colliding[0]][1][1]<0:
                    sat[buttons[colliding[0]][1][0]]=len(parts[buttons[colliding[0]][1][0]])-1
                elif sat[buttons[colliding[0]][1][0]]+buttons[colliding[0]][1][1]>len(parts[buttons[colliding[0]][1][0]])-1:
                    sat[buttons[colliding[0]][1][0]]=0
                else: sat[buttons[colliding[0]][1][0]]+=buttons[colliding[0]][1][1]
                pygame.time.wait(200)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                parts=resize_images(parts)
                buttons=resize_buttons()
                ok_button=resize_ok()
                annotation=resize_annotation()
                help_button=resize_help()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
        if initialize==True:
            initialize=False
            talk(txt)

    return [p['energy'][sat['energy']],p['sensor'][sat['sensor']],p['antenna'][sat['antenna']]]
def random_mission():
    return list(check_missions.keys())[random.randint(0,len(check_missions.keys())-1)]



pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class state:
    game=True
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')

#missions={nom de la mission:           [orbite nécessaire       , [source d'énergie    , senseur        , antenne         ]]
check_missions={'satellite de communication': ['orbite géostationnaire', ['panneaux solaires','','grande antenne']],
          "satellite d'observation": ['orbite basse',['générateur nucléaire','senseur optique', 'antenne moyenne']],
            "satellite de positionnement":['orbite moyenne',['réacteur nucléaire','','petite antenne']]}

mission=random_mission()

#textes_erreurs={nom de la mission :          [[texte explicatif orbite],[texte explicatif composition satelllite]]
textes_erreurs={'satellite de communication': [["Bien joué !","Un satellite de communication doit constamment être au dessus du même point","pour faciliter le calibrage des antennes relais,","c'est-à-dire a un orbite géostationnaire."],
                                               ["Bien joué !","Un satellite de communication a besoin d'une antenne conséquente", "afin d'augmenter la bande passante, en orbite haute une source d'énergie", "présente en abondance est le rayonnement solaire."]],
        "satellite d'observation":[["Bien joué !","Un satellite d'observation doit avoir des images clairs","et pour cela il doit se trouver au plus proche de la Terre."],
                                    ["Bien joué !","Un satellite d'observation nécessite un senseur optique afin de photographier,", "d'une antenne moyenne pour les transmettre en bonne qualité", "et d'une source d'énergie constante même lorsqu'il se trouve à l'ombre de la Terre."]],

        "satellite de positionnement":[["Bien joué !","Un satellite de positionnement doit couvrir un large espace","pour cela une altitude idéale et une période orbitale moyenne est nécessaire"],
                                       ["Bien joué !","Un satellite de positionnement nécessite une horloge atomique","afin d'être le plus précis possible pour l'heure d'envoi du signal","et une petite antenne car les informations doivent-être envoyés rapidement"]]}
#textes_explicatifs=[[texte explicatif orbite],[texte explicatif customisation satellite]]
textes_explicatifs=[[f"Choisi l'orbite du {mission}","L'orbite basse permet au satellite d'être au plus près de la Terre"," L'orbite moyen est idéal pour avoir une période orbitale moyenne.","En orbite géostationnaire les satellites restent au même point par rapport au sol"],
                    ["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]]
help_text=['Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n Maecenas vitae eros quis tellus vehicula convallis quis non dui. Proin interdum non lorem faucibus tincidunt.\n Ut id augue ut massa scelerisque viverra ut vel eros. Sed iaculis purus vitae libero efficitur, at congue nisl blandit.\n Sed fringilla erat nec sollicitudin maximus. Praesent accumsan lacus a elit scelerisque scelerisque.\n In congue porttitor enim. Mauris nisi dui, aliquam ac lorem nec, lobortis aliquet massa.\n Proin luctus orci non rutrum accumsan. Nulla non ex nunc. Cras ac varius velit.\n Aliquam mattis nisi nec libero tincidunt, vel interdum velit accumsan.\n Aliquam bibendum ultricies arcu, vitae hendrerit tortor varius sed.\n \n Suspendisse neque ex, efficitur et condimentum vitae, convallis id neque.',
           '']

menu()
#ne pas expliquer mauvais choix mais expliquer bon choix
if state.game:
    screen.fill((173, 216, 230))
    talk(["Bonjour ! J'ai besoin de ton aide pour cette mission très importante","L'agence SATMAN aimerai envoyer un "+mission,"et nous avons besoin de ton expertise pour cela","clique n'importe où pour commencer"])

txt=textes_explicatifs[0]
while choose_orbit()!=check_missions[mission][0] and state.game:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
talk(textes_erreurs[mission][0])
txt=textes_explicatifs[1]
while satellite_creator()!=check_missions[mission][1] and state.game:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
talk(textes_erreurs[mission][1])


