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
def resize_talking_frames():
    return [pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk0.png'),px(1060,1060)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk1.png'),px(1060,1060))]

def talk(txt):
    speed=50
    run=True
    talking_frames=resize_talking_frames()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
    written=[]
    for paragraph in range(len(txt)):
        written.append("")
        for letter in range(len(txt[paragraph])):
            written[paragraph]=written[paragraph]+txt[paragraph][letter]
            screen.blit(talking_frames[letter%2], (px(0,390),(0,0)))
            for line in range(len(written)):
                screen.blit(font.render(written[line], True, (0,0,0)), (px(140,450+(line*30)),(0,0)))
                pygame.display.update()
            if pygame.mouse.get_pressed()[0]==True and len(written)+len(written[-1])!=len(txt)+len(txt[-1]):pygame.time.wait(10)
            else:pygame.time.wait(speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
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
                    run=False
                    quit()
    return
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
    orbite={'':[0,0,True],'orbite basse':[105.99,4,False],'orbite moyenne':[203.68,2,False],'orbite géostationnaire':[296.4,1,False]}
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    orbit_choice=0
    initialize=True
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
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth,up_button,down_button,ok_button=resize_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
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
    game=True
    sat={'body':0,'energy':0,'sensor':0,'antenna':0}
    ok_button=resize_ok()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    annotation=resize_annotation()
    initialize=True
    while game:
        screen.fill((173, 216, 230))
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))

        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                game=False
                pygame.time.wait(200)
        else :
            screen.blit(ok_button[0],px(900,420))

        for element in sat:
            screen.blit(parts[element][sat[element]], px(-185,-200))

        for element in annotation:
            if p[element][sat[element]]!='':
                screen.blit(annotation[element][1], annotation[element][0])
                screen.blit(font.render(p[element][sat[element]], True, (0,0,0)),(((annotation[element][0][0]-(len(p[element][sat[element]])*annotation[element][2]),annotation[element][0][1]-annotation[element][2])),(0,0)))

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
                game=False
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                parts=resize_images(parts)
                buttons=resize_buttons()
                ok_button=resize_ok()
                annotation=resize_annotation()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
        if initialize==True:
            initialize=False
            talk(txt)

    return [p['energy'][sat['energy']],p['sensor'][sat['sensor']],p['antenna'][sat['antenna']]]

def random_mission():
    return list(check_missions.keys())[random.randint(0,len(check_missions.keys())-1)]



pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')

#missions={nom de la mission:           [orbite nécessaire       , [source d'énergie    , senseur        , antenne         ]]
check_missions={'satellite de communication': ['orbite géostationnaire', ['panneaux solaires','','grande antenne']],
          "satellite d'observation": ['orbite basse',['générateur nucléaire','senseur optique', 'antenne moyenne']],
            "satellite de positionnement":['orbite moyenne',['réacteur nucléaire','','petite antenne']]}
#textes_erreurs={nom de la mission :          [[texte explicatif orbite],[texte explicatif composition satelllite]]
textes_erreurs={'satellite de communication': [["Bien joué !","Un satellite de communication doit constamment être au dessus du même point","pour faciliter le calibrage des antennes relais,","c'est-à-dire a un orbite géostationnaire."],
                                               ["Bien joué !","Un satellite de communication a besoin d'une antenne conséquente", "afin d'augmenter la bande passante, en orbite haute une source d'énergie", "présente en abondance est le rayonnement solaire."]],
        "satellite d'observation":[["Bien joué !","Un satellite d'observation doit avoir des images clairs","et pour cela il doit se trouver au plus proche de la Terre."],
                                    ["Bien joué !","Un satellite d'observation nécessite un senseur optique afin de photographier,", "d'une antenne moyenne pour les transmettre en bonne qualité", "et d'une source d'énergie constante même lorsqu'il se trouve à l'ombre de la Terre."]],

        "satellite de positionnement":[["Bien joué !","Un satellite de positionnement doit couvrir un large espace","pour cela une altitude idéale et une période orbitale moyenne est nécessaire"],
                                       ["Bien joué !","Un satellite de positionnement nécessite une horloge atomique","afin d'être le plus précis possible pour l'heure d'envoi du signal","et une petite antenne car les informations doivent-être envoyés rapidement"]]}
#textes_explicatifs=[[texte explicatif orbite],[texte explicatif customisation satellite]]
textes_explicatifs=[["Choisi l'orbite du satellite","L'orbite basse permet au satellite d'être au plus près de la Terre"," L'orbite moyen est idéal pour avoir une période orbitale moyenne.","En orbite géostationnaire les satellites restent au même point par rapport au sol"],
                    ["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]]
#ne pas expliquer mauvais choix mais expliquer bon choix
mission=random_mission()
screen.fill((173, 216, 230))
screen.blit(pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/menu/title.png'),px(800,800)),(130,50))
talk(["Bonjour ! J'ai besoin de ton aide pour cette mission très importante","L'agence SATMAN aimerai envoyer un "+mission,"et nous avons besoin de ton expertise pour cela","clique n'importe où pour commencer"])
txt=textes_explicatifs[0]
while choose_orbit()!=check_missions[mission][0]:
    txt=["Mauvaise réponse, réessaye !"]
talk(textes_erreurs[mission][0])
txt=textes_explicatifs[1]
while satellite_creator()!=check_missions[mission][1]:
    txt=["Mauvaise réponse, réessaye !"]
talk(textes_erreurs[mission][1])


