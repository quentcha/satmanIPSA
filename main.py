# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:23:42 2024

@author: stric
"""



#ajouter tick vert pour satellite creator et une aide qui explique les différents choix et la mission
import pygame
import math
import random
import os

# fonction adaptant les positions en fonction de la taille de l'écran
# (prend en argument la position x et y initial sur une taille d'écran de 1066x600)
def px(x=None,y=None):
    if y==None:#si aucune valeur y n'est donné, calculer seulement x
        return (x*size.width)/1066# produit en croix appelant la class size
    elif x==None:#si aucune valeur x n'est donné, calculer seulement y
        return (y*size.height)/600# produit en croix appelant la class size
    else:
        return ((x*size.width)/1066,(y*size.height)/600)#sinon renvoyé la nouvelle valeur de x et y
def resize_help():
    return [pygame.transform.scale(pygame.image.load('aide/aide-1.png'),px(150,150)),
            pygame.transform.scale(pygame.image.load('aide/aide-2.png'),px(150,150))]
#fonction pour chargé les sons dans le programme (appelé une seule fois)
def load_sound():
    cl=pygame.mixer.Sound("sound/Menu Selection Click.wav")
    tr=pygame.mixer.Sound("sound/transition.wav")
    ty=''
    return cl, tr, ty


# charge et adapte la taille des images pour l'animation
def load_anim():
    anim=[]
    length=12 #nombre d'images dans l'animation
    for i in range(length):
        anim.append(pygame.transform.scale(pygame.image.load(f'transition/pixil-frame-{i}.png'),px(1066,1066)))
    return anim
#fonction jouant l'animation (prend en argument la direction de lecture -1 ou 1)
def transition(read):
    anim=load_anim()# charge les animations
    pygame.mixer.Sound.play(transition_sound)#joue le son de transition
    for im in range(read,len(anim)*read,read):
        screen.blit(anim[im], (0,0))# affiche l'image nr.im aux coordonnées 0,0
        pygame.display.update()# raffraichis l'écran
        pygame.time.wait(100)# attendre 100ms


#charge et adapte la taille des images du boutons retour
def resize_return_help_buttons():
    return [pygame.transform.scale(pygame.image.load('aide/retour 1.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('aide/retour 2.png'),px(200,200))]
#affiche le texte de la fenêtre aide (le met en forme)
def blit(txt):
    help_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(15)))
    Mission_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(30)))
    pygame.draw.rect(screen, (140, 175, 186), (px(30, 30),px(1006,540)))
    screen.blit(Mission_font.render("Objectif : "+mission, True, txt_color), (px(35,35),(0,0)))
    for phrase in range(len(txt.split("\n"))):
        screen.blit(help_font.render(txt.split("\n")[phrase], True, txt_color), (px(35,100+phrase*30),(0,0)))
#fonction gérant la fenêtre aide
def help(num):
    back_button=resize_return_help_buttons()#charge les images du bouton retour
    blit(help_text[num])#afficher le texte
    run=True
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))#résupère la position du curseur sous forme de rect
        screen.blit(back_button[0],px(35,475))
        if pygame.Rect.colliderect(mouse,(px(35,475),px(200,100))):# vérifie si curseur survol bouton retour
            screen.blit(back_button[1],px(35,475))
            if pygame.mouse.get_pressed()[0]==True:#si un clique est enregistré
                pygame.mixer.Sound.play(click)# jouer le son "click"
                run=False# arrêter la fonction
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:# si le joueur ferme le programme
                run=False# arrêter la fonction
                state.game=False#arrêter le jeu
            elif event.type == pygame.VIDEORESIZE:# si le joueur change la taille de la fenêtre
                size.width, size.height = pygame.display.get_surface().get_size()# mettre à jour la class size avec la nouvelle taille de l'écran
                back_button=resize_return_help_buttons()# charger le bouton retour avec la nouvelle taille
                blit(help_text[num])# afficher le texte avec la nouvelle taille


#charge et adapte la taille des images du dialogue
def resize_talking_frames():
    return [pygame.transform.scale(pygame.image.load('talk/talk0.png'),px(1060,1060)),pygame.transform.scale(pygame.image.load('talk/talk1.png'),px(1060,1060))]
# fonction affichant et gérant les dialogues
def talk(txt):
    if state.game:#si le jeu n'a pas été arrêté
        speed=30#vitesse d'affichage des lettres
        talking_frames=resize_talking_frames()#charger images
        font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))#police d'écriture
        written=[]#texte déjà écrit (sera afficher directement)
        for paragraph in range(len(txt)):
            written.append("")
            for letter in range(len(txt[paragraph])):#afficher chaque letter
                written[paragraph]=written[paragraph]+txt[paragraph][letter]#ajouter cette lettre au texte d"jà écrit
                screen.blit(talking_frames[(letter%6)//3], (px(0,390),(0,0)))#avancer d'une image dans l'animation du scientifique qui parle
                for line in range(len(written)):#affiche les lignes déjà écrites
                    screen.blit(font.render(written[line], True, txt_color), (px(140,450+(line*30)),(0,0)))
                    pygame.display.update()
                #si un clique est enregistré et que l'on est pas à la fin du texte alors accéléré la vitesse d'affichage
                if pygame.mouse.get_pressed()[0]==True and len(written)+len(written[-1])!=len(txt)+len(txt[-1]):pygame.time.wait(10)
                else:pygame.time.wait(speed)#sinon afficher à la vitesse choisi en début de fonction

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:# si le joueur ferme le programme
                        state.game=False# mettre à jour la class game
                        return
                    elif event.type == pygame.VIDEORESIZE:# si le joueur change la taille de la fenêtre
                        size.width, size.height = pygame.display.get_surface().get_size()# mettre à jour la class size avec la nouvelle taille de l'écran
                        talking_frames=resize_talking_frames()# charger les images avec les nouvelles tailles
                        font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))# charger la police d'écriture avec une nouvelle taille
        #le texte est maintenant entièrement affiché
        while pygame.mouse.get_pressed()[0]!=True:#tant que l'on ne clique pas
            screen.blit(talking_frames[1], (px(0,390),(0,0)))# afficher l'image du scientifique
            for line in range(len(written)):#afficher toute les lignes du texte d'un coup
                screen.blit(font.render(written[line], True, txt_color), (px(140,450+(line*30)),(0,0)))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:# si le programme est fermé
                        state.game=False# mettre à jour la class
        #le joueur a cliquer donc quitter le dialogue
        return


#charge les images du menu (sous forme de liste pour certains à cause des animations)
def menu_images():
    title=pygame.transform.scale(pygame.image.load('menu/title.png'),px(800,800))
    scientifique1=[[],
    [pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 1.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 2.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 3.png'),px(280,280))],
    [pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 1 M.png'),px(280,280)),
     pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 2 M.png'),px(280,280)),
    pygame.transform.scale(pygame.image.load('menu/scientist/ssiantifique 3 M.png'),px(280,280))]
    ]
    scientifique2=[[],
    [pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 1 M.png'),px(300,300)),
     pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 2 M.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 3 M.png'),px(300,300))],
    [pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 1.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 2.png'),px(300,300)),
    pygame.transform.scale(pygame.image.load('menu/scientist2/ssiantifique fou 3.png'),px(300,300))]]
    background=[pygame.transform.scale(pygame.image.load('menu/pixil-layer-0.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-1.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-2.png'),px(1066,600)),
                pygame.transform.scale(pygame.image.load('menu/pixil-layer-3.png'),px(1066,600))]
    scientifique3=[pygame.transform.scale(pygame.image.load('menu/scientist3/scientifique femme 1.png'),px(300,300)),
                pygame.transform.scale(pygame.image.load('menu/scientist3/scientifique femme 2.png'),px(300,300))]
    play=[pygame.transform.scale(pygame.image.load('menu/play.png'),px(500,500)),
          pygame.transform.scale(pygame.image.load('menu/empty button.png'),px(500,500))]
    return title,scientifique1, scientifique2, background, scientifique3, play
#changer la position horizontale des scientifiques
def move(x_scientists):
    for i in range(len(x_scientists)):
        # si le scientifique est à plus ou moins 10px de son objectif
        if x_scientists[i][0]>x_scientists[i][1]-15 and x_scientists[i][0]<x_scientists[i][1]+15:
            x_scientists[i][1]=random.randint(0,int(px(x=900)))# fixer un nouvel objectif
        #fait la différence entre l'objectif et la position et le converti en veceur unitaire multipplié par 3 pour
        #changer la position horizontale du scientifique par 3 ou -3
        x_scientists[i][0]+=(x_scientists[i][1]-x_scientists[i][0])*x_scientists[i][3]/abs(x_scientists[i][1]-x_scientists[i][0])
        x_scientists[i][2]=int((x_scientists[i][1]-x_scientists[i][0])/abs(x_scientists[i][1]-x_scientists[i][0]))
def menu():
    credit_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=20),px(y=20))))#police des credits
    show_play=False
    title, scientifique0,scientifique1,background, scientifique3, play=menu_images()#charger les images
    #x_scientists=[[0,random.randint(0,int(px(x=700))),1,3],[900,random.randint(0,int(px(x=900))),1,5]]
    #x_scientists=[[position, objectif, nr.image, vitesse de déplacement]]
    x_scientists=[[0,random.randint(0,int(px(x=700))),1,3],[900,random.randint(0,int(px(x=900))),1,11]]# liste des positions horizontales des scientifiques
    i=0#initialiser l'horloge du programme
    run=True
    while run and state.game:
        i+=0.8#ajouter 0.8 a l'horloge a chaque itération
        move(x_scientists)# mettre a jour la position des scientifiques
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))#récupérer la position du curseur sous forme de Rect
        screen.fill(bg_color)
        for image in range(len(background)):# itérer à travers les images de l'animation
            screen.blit(background[image],px(0,-image+(mouse[1]/100*(image))))

        if int(i%20):
            screen.blit(credit_font.render('.'*int(i%15)+'|'*int(i%2), True, (100,100,100)), px(220,490+(mouse[1]/100*(3))))
            screen.blit(credit_font.render('ALERTE'*int(i%2), True, (100,100,100)), px(900,45+(mouse[1]/100*(3))))
            screen.blit(credit_font.render('SCIENTIFIQUE FOU'*int(i%2), True, (100,100,100)), px(847,75+(mouse[1]/100*(3))))
            screen.blit(credit_font.render('/!\\'*int(i%2), True, (100,100,100)), px(930,105+(mouse[1]/100*(3))))

        screen.blit(title,px(130,50))
        if int(i)%4 and show_play: screen.blit(play[1],px(300,250))
        else:screen.blit(play[0],px(300,250))
        #if int(i)%4 and show_play:screen.blit(title_font.render("", True, txt_color), (0,0))
        #else:screen.blit(title_font.render("DECOLLAGE", True, txt_color), (play_button[0] + px(x=10), play_button[1] - px(y=5)))

        screen.blit(scientifique3[int(i%2)], (px(x=450),px(y=362+(mouse[1]/100*(3)))))
        screen.blit(scientifique0[x_scientists[0][2]][int(i)%3],(x_scientists[0][0],px(y=382+(mouse[1]/100*(3)))))
        screen.blit(scientifique1[x_scientists[1][2]][int(i+1)%3],(x_scientists[1][0],px(y=365+(mouse[1]/100*(3)))))
        screen.blit(credit_font.render("Un jeu créé par AéroKids IPSA",True,txt_color),px(720,570))

        pygame.display.flip() # refresh l'écran
        pygame.time.wait(80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
            if pygame.Rect.colliderect(mouse,(px(300,250), px(500,150))):
                show_play=True
                if pygame.mouse.get_pressed()[0]==True:
                    pygame.mixer.Sound.play(click)
                    run=False
            else: show_play=False
            if event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                credit_font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=20),px(y=20))))
                title, scientifique0,scientifique1, background, scientifique3, play=menu_images()
def mission_logos():
    comm=[pygame.transform.scale(pygame.image.load('mission chooser/satellite de communication.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('mission chooser/satellite de communication.png'),px(300,300))]
    pos=[pygame.transform.scale(pygame.image.load('mission chooser/satellite de positionnement.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('mission chooser/satellite de positionnement.png'),px(300,300))]
    obs=[pygame.transform.scale(pygame.image.load('mission chooser/satellite d\'observation.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('mission chooser/satellite d\'observation.png'),px(300,300))]
    return [comm,pos, obs]
def mission_chooser():
    logos =mission_logos()

    rect={(px(55,200),px(200,200)): 'satellite de communication',
          (px(435,200),px(200,200)):'satellite de positionnement',
          (px(805,200),px(200,200)):"satellite d'observation"}
    Mission_name = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
    title=pygame.font.Font('Grand9K Pixel.ttf', int(px(60)))
    run=True
    init=True
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.fill(bg_color)
        screen.blit(title.render('CHOISIS TA MISSION :', True, txt_color), (px(10,10),(0,0)))
        for im in range(len(logos)):
            screen.blit(logos[im][0], list(rect.keys())[im])
            screen.blit(Mission_name.render(list(rect.values())[im], True, txt_color), ((list(rect.keys())[im][0][0]+px(x=100-(len(list(rect.values())[im])/2)*11),list(rect.keys())[im][0][1]+px(y=250)),(0,0)))
        #screen.blit(comm[0], px(60,300))
        coll=pygame.Rect.collidedict(mouse,rect)
        if coll and init==False:
            screen.blit(logos[list(rect.keys()).index(coll[0])][1], (coll[0][0][0]-50,coll[0][0][1]-50))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.mixer.Sound.play(click)
                run=False
                return coll[1]
        if init==True: init=False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game=False
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                title=pygame.font.Font('Grand9K Pixel.ttf', int(px(60)))
                logos =mission_logos()
                Mission_name = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
                rect={(px(55,200),px(200,200)): 'satellite de communication',
                (px(435,200),px(200,200)):'satellite de positionnement',
                (px(805,200),px(200,200)):"satellite d'observation"}
def intro():
    screen.fill(bg_color)
    pygame.display.update()
    talk([f"Bonjour, je suis l'ingénieur en chef du projet SATMAN.",
          "Je vais te guider au cours de cette mission !",
          "Si tu en a marre de m'entendre parler tu peux cliquer n'importe où pour accélerer",
          "  ( clique n'importe où )"])
    screen.fill(bg_color)
    screen.blit(resize_help()[0], px(10,-30))
    pygame.display.update()
    talk([f"En haut à gauche se trouve le bouton aide.",
          "Tu y trouveras toutes les informations nécessaires pour t'aider",
          "  ( clique n'importe où )"])
    screen.fill(bg_color)
    screen.blit(resize_help()[0], px(10,-30))
    screen.blit(resize_assets()[1][0],px(900,50))
    screen.blit(resize_assets()[2][0],px(900,250))
    screen.blit(resize_assets()[3][0],px(700,150))
    pygame.display.update()
    talk([f"Aide toi des flèches pour naviguer le niveau.",
          "Et lorsque tu penses avoir trouver la bonne réponse appuie sur OK",
          "  ( clique n'importe où )"])
    screen.fill(bg_color)
    screen.blit(resize_help()[0], px(10,-30))
    screen.blit(resize_assets()[1][0],px(900,50))
    screen.blit(resize_assets()[2][0],px(900,250))
    screen.blit(resize_assets()[3][0],px(700,150))
    pygame.display.update()
    talk(["Tu es prêt à envoyer un satellite dans l'espace ?",
          "Alors c'est parti !!!",
          "  ( clique n'importe où )"])
def resize_assets():
    earth= pygame.transform.scale(pygame.image.load('orbit/earth.png'),(min(px(x=70),px(y=70)),)*2)
    up_button=[pygame.transform.scale(pygame.image.load('orbit/up_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('orbit/up_button2.png'),px(150,150))]
    down_button=[pygame.transform.scale(pygame.image.load('orbit/down_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('orbit/down_button2.png'),px(150,150))]
    ok_button=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'),px(150,150))]
    return earth,up_button,down_button,ok_button
def point_circulaire(angle, rayon):
    # Conversion des coordonnées polaires en coordonnées cartésiennes
    x = rayon * math.cos(math.radians(angle))
    y = rayon * math.sin(math.radians(angle))

    return x, y
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
        screen.fill(bg_color)

        earth_w,earth_h=pygame.transform.rotate(earth, angle).get_size()
        for circle in orbite:
            if orbite[circle][2]==True:
                pygame.draw.circle(screen, (105,20,14),(size.width/2,size.height/2),min(px(x=orbite[circle][0]),px(y=orbite[circle][0])),int(min(px(x=5),px(y=5))))
            else:
                 pygame.draw.circle(screen, (255,255,255),(size.width/2,size.height/2),min(px(x=orbite[circle][0]),px(y=orbite[circle][0])),int(min(px(x=5),px(y=5))))

        for sat in orbite:
            x,y=point_circulaire(angle*orbite[sat][1],min(px(x=orbite[sat][0]),px(y=orbite[sat][0])))
            if orbite[sat][2]==True:
                pygame.draw.circle(screen, (255,0,0),(size.width/2+x,size.height/2-y),int(min(px(x=5),px(y=5))),int(min(px(x=5),px(y=5))))
                screen.blit(font.render(sat, True, (255,0,0)), (size.width/2+x+7,size.height/2-y-7,0,0))

            else:
                pygame.draw.circle(screen, (0,)*3,(size.width/2+x,size.height/2-y),int(min(px(x=5),px(y=5))),int(min(px(x=5),px(y=5))))

        screen.blit(pygame.transform.rotate(earth, angle),((size.width/2)-(earth_w/2),(size.height/2)-(earth_h/2)))

        angle+=1

        screen.blit(help_button[0],px(5,-50))
        screen.blit(down_button[0],px(900,250))
        screen.blit(up_button[0],px(900,50))
        screen.blit(ok_button[0],px(900,420))
        
        if pygame.Rect.colliderect(mouse,(px(900,50),px(150,150))):
            screen.blit(up_button[1],px(900,50))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.mixer.Sound.play(click)
                if orbit_choice+1==len(orbite): orbit_choice=0
                else: orbit_choice+=1
                pygame.time.wait(200)
        elif pygame.Rect.colliderect(mouse,(px(900,250),px(150,150))):
            screen.blit(down_button[1],px(900,250))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.mixer.Sound.play(click)
                pygame.time.wait(200)
                if orbit_choice-1<0: orbit_choice=len(orbite)-1
                else: orbit_choice-=1
                pygame.time.wait(200)
        elif pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True and orbit_choice!=0:
                pygame.mixer.Sound.play(click)
                run=False
        elif pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                pygame.mixer.music.pause()
                help(questions['orbite'])
                earth,up_button,down_button,ok_button=resize_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                help_button=resize_help()
                pygame.mixer.music.unpause()
        for key in orbite:
            if key==list(orbite.keys())[orbit_choice]: orbite[key][2]=True
            else: orbite[key][2]=False

        pygame.time.wait(100)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth,up_button,down_button,ok_button=resize_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                help_button=resize_help()
        if initialize==True:
            talk(txt)
            earth,up_button,down_button,ok_button=resize_assets()
            font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
            help_button=resize_help()
            initialize=False
    return list(orbite.keys())[orbit_choice]

def load_images(part):
    dir={'bottom':['satellite customisation/bottom', px(330,440)],'middle':['satellite customisation/middle', px(330,210)],'top':['satellite customisation/top', px(330,60)]}[part]
    choices={}
    for f in os.listdir(dir[0]):
        if f!='annotation.png':
            choices[f[:-4]]=pygame.transform.scale(pygame.image.load(str(dir[0])+'/'+str(f)),px(1500,1500))
    annotation=[dir[1],pygame.transform.scale(pygame.image.load(dir[0]+'/annotation.png'),px(80,80))]

    return choices, annotation

def resize_buttons():
    left_button=[pygame.transform.scale(pygame.image.load('satellite customisation/left_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/left_button2.png'),px(150,150))]
    right_button=[pygame.transform.scale(pygame.image.load('satellite customisation/right_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/right_button2.png'),px(150,150))]
    buttons = {(px(0,220),px(150,150)):[left_button,-1],
               (px(750,220),px(150,150)):[right_button,1]}
    ok=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'),px(150,150))]
    return buttons, ok
def resize_past_choices(past_choices_list):
    new_list=[]
    body=pygame.transform.scale(pygame.image.load('satellite customisation/body.png'),px(1500,1500))
    for image in range(len(past_choices_list)):
        new_list.append((pygame.transform.scale(past_choices_list[image][0],px(1500,1500)), pygame.transform.scale(past_choices_list[image][1], px(80,80)),px(past_choices_list[image][2][0],past_choices_list[image][2][1]),past_choices_list[image][3]))
    return new_list, body
def custom(part, num):
    run=True
    initialize=True
    choices,annotation = load_images(part)
    past_choices_list, body=resize_past_choices(past_choices)
    arrow_buttons, ok_button=resize_buttons()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    help_button=resize_help()
    index=len(choices)-1
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))

        screen.fill(bg_color)
        screen.blit(body, px(-185,-200))
        for image in past_choices_list:
            if image[3]!='_empty':
                screen.blit(image[0], px(-185,-200))
                screen.blit(image[1], image[2])
                screen.blit(font.render(image[3], True, (0,0,0)),((image[2][0]-len(image[3])*px(x=11),image[2][1]-px(y=11)),(0,0)))

        screen.blit(list(choices.values())[index], px(-185,-200))
        if list(choices.keys())[index]!='_empty':
            screen.blit(annotation[1], annotation[0])
            screen.blit(font.render(list(choices.keys())[index], True, (0,0,0)),((annotation[0][0]-px(x=len(list(choices.keys())[index])*11),annotation[0][1]-px(y=11)),(0,0)))

        for element in arrow_buttons:
            screen.blit(arrow_buttons[element][0][0], element)
        colliding=pygame.Rect.collidedict(mouse, arrow_buttons)
        if colliding:
            screen.blit(colliding[1][0][1], colliding[0][0])
            if pygame.mouse.get_pressed()[0]==True:
                if index+colliding[1][1]==len(choices):
                    index=0
                elif index+colliding[1][1]<0:
                    index=len(choices)-1
                else:index+=colliding[1][1]
                pygame.mixer.Sound.play(click)
                pygame.time.wait(200)

        screen.blit(help_button[0],px(5,-50))
        screen.blit(ok_button[0],px(900,420))
        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.mixer.Sound.play(click)
                pygame.time.wait(200)
                run=False
        elif pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                pygame.time.wait(200)
                pygame.mixer.music.pause()
                help(num)
                help_button=resize_help()
                choices, annotation = load_images(part)
                past_choices_list, body=resize_past_choices(past_choices)
                arrow_buttons, ok_button=resize_buttons()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                pygame.mixer.music.unpause()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                help_button=resize_help()
                choices, annotation = load_images(part)
                past_choices_list, body=resize_past_choices(past_choices)
                arrow_buttons, ok_button=resize_buttons()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
        if initialize==True:
            talk(txt)
            help_button=resize_help()
            choices, annotation = load_images(part)
            past_choices_list, body=resize_past_choices(past_choices)
            arrow_buttons, ok_button=resize_buttons()
            font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
            initialize=False
    return list(choices.keys())[index]
def load_space_velocity_assets():
    clouds=[pygame.transform.scale(pygame.image.load('space velocity/cloud0.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('space velocity/cloud1.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('space velocity/cloud2.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('space velocity/cloud3.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('space velocity/cloud4.png'),px(200,200)),
            pygame.transform.scale(pygame.image.load('space velocity/cloud5.png'),px(200,200))]
    speedometer=pygame.transform.scale(pygame.image.load('space velocity/speedometer.png'),px(400,400))
    liberation_button=[pygame.transform.scale(pygame.image.load('space velocity/lancement0.png'),px(250,250)),
        pygame.transform.scale(pygame.image.load('space velocity/lancement1.png'),px(250,250)),
        pygame.transform.scale(pygame.image.load('space velocity/lancement2.png'),px(250,250))]
    return clouds, speedometer, liberation_button
def load_space_vehicles():
    arianeV=pygame.transform.scale(pygame.image.load('lanceur/arianeV.png'),px(400,400))
    sls=pygame.transform.scale(pygame.image.load('lanceur/SLS.png'),px(400,400))
    vega=pygame.transform.scale(pygame.image.load('lanceur/vega.png'),px(400,400))
    booster_arianeV=[pygame.transform.scale(pygame.image.load('lanceur/Feu booster Ariane 1.png'),px(400,400)),
                     pygame.transform.scale(pygame.image.load('lanceur/Feu booster Ariane 2.png'),px(400,400)),
                     366,265]
    booster_sls=[pygame.transform.scale(pygame.image.load('lanceur/Feu booster SLS 1.png'),px(400,400)),
                 pygame.transform.scale(pygame.image.load('lanceur/Feu booster SLS 2.png'),px(400,400)),
                 343,265]
    return {'arianeV':[arianeV,booster_arianeV],'SLS':[sls, booster_sls], 'vega':[vega, booster_arianeV]}
def second_space_velocity():
    run=True
    clock=pygame.time.Clock()
    #clock.tick(70)
    clouds, speedometer, liberation_button=load_space_velocity_assets()
    lanceur=load_space_vehicles()[check_missions[mission][questions['velocity']]][0]
    booster=load_space_vehicles()[check_missions[mission][questions['velocity']]][1]
    help_button=resize_help()
    layers=[[None, [0,0], 0],]*(len(clouds)+1)
    layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
    time=1000
    i=0
    initialize=True
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        clock.tick(70)#maintien 70 fps quel que soit la taille de l'écran et donc la vitesse de rafraichissement
        i+=0.3
        if i>= time:
            run = False
        screen.fill(bg_color)
        for slots in range(len(layers)-int((i*((len(clouds)+1)//2))/time)):#diminue le nombre de nuages au fil du temps
            if layers[slots]==[None, [0,0], 0]:
                layers[slots]=[clouds[random.randint(0,len(clouds)-1)], [random.randint(-200,int(size.width)),random.randint(int(px(y=-200)),int(px(y=-110)))], random.randint(int(px(y=1)),int(px(y=5)))+(i%time/(time/200))]
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
                pygame.mixer.Sound.play(click)
                pygame.mixer.music.pause()
                help(questions['velocity'])
                clouds, speedometer, liberation_button=load_space_velocity_assets()
                lanceur=load_space_vehicles()[check_missions[mission][questions['velocity']]][0]
                booster=load_space_vehicles()[check_missions[mission][questions['velocity']]][1]
                help_button=resize_help()
                layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
                pygame.mixer.music.unpause()
        if pygame.Rect.colliderect(mouse,(pos_button,px(250,250))):
            if i>(time*775)/2000 and i<(time*1295)/2000:
                screen.blit(liberation_button[(int(i/5)%2)+1], pos_button)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click)
                    return True
            else:
                screen.blit(liberation_button[2], pos_button)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click)
                    pygame.time.wait(200)
                    run=False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game=False
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                clouds, speedometer, liberation_button=load_space_velocity_assets()
                lanceur=load_space_vehicles()[check_missions[mission][questions['velocity']]][0]
                booster=load_space_vehicles()[check_missions[mission][questions['velocity']]][1]
                help_button=resize_help()
                layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
        if initialize==True:
            talk(txt)
            pygame.mixer.music.load("space velocity/Rocket-SoundBible.com-941967813.mp3")
            pygame.mixer.music.play(1)
            clouds, speedometer, liberation_button=load_space_velocity_assets()
            lanceur=load_space_vehicles()[check_missions[mission][questions['velocity']]][0]
            booster=load_space_vehicles()[check_missions[mission][questions['velocity']]][1]
            help_button=resize_help()
            layers[(len(clouds)+1)//2]=[lanceur, [px(x=350),px(y=50)]]
            initialize=False
def resize_earth_map_assets():
    earth = pygame.transform.scale(pygame.image.load('Earth_map/Earth_map.png'), px(700, 700))
    up_button = [pygame.transform.scale(pygame.image.load('orbit/up_button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('orbit/up_button2.png'), px(150, 150))]
    down_button = [pygame.transform.scale(pygame.image.load('orbit/down_button1.png'), px(150, 150)),
                   pygame.transform.scale(pygame.image.load('orbit/down_button2.png'), px(150, 150))]
    ok_button = [pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'), px(150, 150))]
    return earth, up_button, down_button, ok_button

def earth_map():
    run = True
    help_button=resize_help()
    locations = {'Kourou':[(335, 305), False],
                 'Pôle Nord':[(400,100), False],
                 'Toulouse':[(470, 190), True],
                 'Himalaya':[(630, 230), False]}
    earth, up_button, down_button, ok_button = resize_earth_map_assets()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    initialize=True
    map_pos=(120,30)
    while run and state.game:
        screen.fill(bg_color)
        screen.blit(earth, px(map_pos[0],map_pos[1]))
        pygame.draw.rect(screen,bg_color,(px(map_pos[0]-55,map_pos[1]-5),px(810,550)),int(max(px(x=55),px(y=55))))
        pygame.draw.rect(screen,(0,0,0),(px(map_pos[0],map_pos[1]+50),px(700,440)),int(max(px(x=5),px(y=5))))


        screen.blit(up_button[0], px(900, 60))
        screen.blit(down_button[0], px(900, 190))
        screen.blit(ok_button[0], px(900, 370))
        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))

        if pygame.Rect.colliderect(mouse, (px(900, 60), px(200, 100))):
            screen.blit(up_button[1], px(900, 60))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                for loc in range(len(locations)):
                    if list(locations.values())[loc][1]==True:
                        if loc+1==len(locations):
                            locations[list(locations.keys())[loc]][1]=False
                            locations[list(locations.keys())[0]][1]=True
                        else:
                            locations[list(locations.keys())[loc]][1]=False
                            locations[list(locations.keys())[loc+1]][1]=True
                        break
                pygame.time.wait(200)

        if pygame.Rect.colliderect(mouse, (px(900, 190), px(200, 100))):
            screen.blit(down_button[1], px(900, 190))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                for loc in range(len(locations)):
                    if list(locations.values())[loc][1]==True:
                        locations[list(locations.keys())[loc]][1]=False
                        locations[list(locations.keys())[loc-1]][1]=True
                        break
                pygame.time.wait(200)

        for circles in locations:
            if locations[circles][1]==True:
                screen.blit(font.render(circles,True,(255,0,0)),px(locations[circles][0][0]+10,locations[circles][0][1]+10))
                pygame.draw.circle(screen, (255, 0, 0), px(locations[circles][0][0],locations[circles][0][1]), int(min(px(x=10), px(y=10))))
            else:
                pygame.draw.circle(screen, (0, 0, 0),px(locations[circles][0][0],locations[circles][0][1]), int(min(px(x=10), px(y=10))))

        if pygame.Rect.colliderect(mouse, (px(900, 370), px(200, 100))):
            screen.blit(ok_button[1], px(900, 370))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                run=False
                pygame.time.wait(200)

        screen.blit(help_button[0],px(5,-50))
        if pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                help(questions['map'])
                earth, up_button, down_button, ok_button = resize_earth_map_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                help_button=resize_help()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth, up_button, down_button, ok_button = resize_earth_map_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
                help_button=resize_help()
        if initialize==True:
            earth, up_button, down_button, ok_button = resize_earth_map_assets()
            font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
            help_button=resize_help()
            talk(txt)
            initialize=False
    for loc in range(len(locations)):
        if list(locations.values())[loc][1]==True:
            return list(locations.keys())[loc]
def mission_order_assets():
    rocket= [pygame.transform.scale(pygame.image.load('lanceur/'+check_missions[mission][questions['velocity']]+'.png'), px(550, 550))]
    sat=[pygame.transform.scale(pygame.image.load('satellite customisation/body.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/bottom/'+check_missions[mission][questions['custom_bottom']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/middle/'+check_missions[mission][questions['custom_middle']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/top/'+check_missions[mission][questions['custom_top']]+'.png'), px(700, 700))]
    earth=[pygame.transform.scale(pygame.image.load('orbit/earth.png'), px(100, 100))]
    map=[pygame.transform.scale(pygame.image.load('Earth_map/Earth_map.png'), px(300, 300))]
    ok_button=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(200,200)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/satellite customisation/button2.png'),px(200,200))]

    return rocket, sat, earth, map, ok_button
def mission_order():
    run=True
    rocket, sat,earth, map, ok_button=mission_order_assets()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=25),px(y=25))))
    initialize=True
    while run and state.game:
        screen.fill(bg_color)

        screen.blit(font.render("MISSION : "+mission,True,(0,0,0)),px(10,10))

        screen.blit(rocket[0],px(700,40))
        screen.blit(font.render((check_missions[mission][questions['velocity']]).upper(),True,(0,0,0)),px(850,5))

        pygame.draw.line(screen,(0,0,0),px(800,150),px(900,150),5)
        for im in range(len(sat)):
            screen.blit(sat[im],px(360,-80))

        screen.blit(earth[0], px(70,150))
        pygame.draw.circle(screen,(255,0,0),px(120,200),px(100),2)
        pygame.draw.circle(screen,(255,0,0),px(218,220),px(5),5)
        screen.blit(font.render(check_missions[mission][questions['orbite']],True,(0,0,0)),px(230,200))

        screen.blit(map[0], px(500,300))
        pygame.draw.rect(screen,(0,0,0),(px(500,320),px(300,190)),int(min(px(x=5),px(y=5))))
        pygame.draw.rect(screen,bg_color,(px(470,290),px(360,250)),int(max(px(x=30),px(y=30))))
        pygame.draw.circle(screen,(255,0,0),px(600,420),px(5),int(px(5)))
        screen.blit(font.render("Kourou",True,(0,0,0)),px(600,510))

        screen.blit(ok_button[0], px(10, 390))
        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        if pygame.Rect.colliderect(mouse, (px(10, 390), px(200, 200))):
            screen.blit(ok_button[1], px(10, 390))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(click)
                run=False
                pygame.time.wait(200)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                rocket, sat,earth, map, ok_button=mission_order_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=25),px(y=25))))
        if initialize==True:
            talk(txt)
            rocket, sat,earth, map, ok_button=mission_order_assets()
            font = pygame.font.Font('Grand9K Pixel.ttf', int(min(px(x=25),px(y=25))))
            initialize=False
def credit_assets():
    replay=[pygame.transform.scale(pygame.image.load('credits/replay.png'),px(700,700)),
            pygame.transform.scale(pygame.image.load('credits/empty button.png'),px(700,700))]
    quit=[pygame.transform.scale(pygame.image.load('credits/quit.png'),px(700,700)),
            pygame.transform.scale(pygame.image.load('credits/empty button.png'),px(700,700))]
    sat=[pygame.transform.scale(pygame.image.load('satellite customisation/body.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/bottom/'+check_missions[mission][questions['custom_bottom']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/middle/'+check_missions[mission][questions['custom_middle']]+'.png'), px(700, 700)),
         pygame.transform.scale(pygame.image.load('satellite customisation/top/'+check_missions[mission][questions['custom_top']]+'.png'), px(700, 700))]
    logo_ipsa=pygame.transform.scale(pygame.image.load('credits/ipsa.png'),px(400,400))
    logo_git=pygame.transform.scale(pygame.image.load('credits/github.png'),px(150,100))
    txt=pygame.transform.scale(pygame.image.load('credits/texte.png'),px(520,125))
    title=pygame.transform.scale(pygame.image.load('menu/title.png'),px(400,400))
    share=[pygame.transform.scale(pygame.image.load('credits/partage0.png'),px(800,800)), pygame.transform.scale(pygame.image.load('credits/partage1.png'),px(800,800))]
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
         '',
         'SATMAN',
         'Une création IPSA',
         'sous licence blablabla',
         logo_ipsa,
         'PARTICIPANTS :',
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
    font = pygame.font.Font('Grand9K Pixel.ttf', font_size)
    i=0
    stars=[]
    for star in range(100):
        stars.append((random.randint(0,int(size.width)),random.randint(0,int(size.height))))
    start,y=300,10
    j=0
    clock=pygame.time.Clock()
    pygame.time.wait(200)
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        clock.tick(70)
        i+=px(0.1)
        j+=px(0.05)
        screen.fill((28, 41, 81))
        for star in stars:
            pygame.draw.rect(screen,(random.randint(0,255),random.randint(100,255),255),(star, (5,5)),5)

        if y>=0:
            y=start
            for line in range(len(txt)):
                if type(txt[line])==type(''):
                    x=(px(x=1066)-(px(x=1066)//4))-(font.size(txt[line])[0]//2)
                    screen.blit(font.render(txt[line],True,(255,255,255)),(x,y))
                    y+=2*font_size
                else:
                    x=(px(x=1066)-(px(x=1066)//4))-(txt[line].get_width()//2)
                    screen.blit(txt[line],(x,y))
                    y+=txt[line].get_height()
        if int(i%2):
            i=0
            start-=(font_size)//2


        if pygame.Rect.colliderect(mouse,(px(10,150), px(400,100))):
            if int(j)%2: screen.blit(replay[1],px(10,150))
            else:screen.blit(replay[0],px(10,150))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
        else:screen.blit(replay[0],px(10,150))

        if pygame.Rect.colliderect(mouse,(px(10,300), px(400,100))):
            if int(j%2): screen.blit(quit[1],px(10,300))
            else:screen.blit(quit[0],px(10,300))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
                state.game=False
        else:screen.blit(quit[0],px(10,300))

        screen.blit(texte_missions, px(10,50))
        screen.blit(share[int(j%2)], px(10,450))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                font_size=int(min(px(x=25),px(y=25)))
                replay,quit,sat, logo_ipsa, logo_git,share,texte_missions,title=credit_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', font_size)
                stars=[]
                for star in range(100):
                    stars.append((random.randint(0,int(size.width)),random.randint(0,int(size.height))))
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
pygame.display.set_icon(pygame.image.load('SATMAN logo.ico'))
class state:
    game=True
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
click,transition_sound, typing=load_sound()
bg_color=(173, 216, 230)
txt_color=(0,0,0)

#missions={nom de la mission:           [orbite nécessaire       , [source d'énergie    , senseur        , antenne         ]]
check_missions={'satellite de communication': ['orbite géostationnaire','Kourou', 'panneaux solaires','_empty','grande antenne','None', 'SLS'],
          "satellite d'observation": ['orbite basse','Kourou','générateur nucléaire','senseur optique', 'antenne moyenne','None', 'vega'],
            "satellite de positionnement":['orbite moyenne','Kourou','générateur nucléaire','_empty','petite antenne','None', 'arianeV']}


menu()
if state.game:transition(1)

if state.game:intro()
if state.game:transition(1)

#textes_erreurs={nom de la mission :          [[texte explicatif orbite],[texte explicatif composition satelllite]]
textes_fin_niveau={'satellite de communication': [["Bien joué !", "Un satellite de communication doit constamment être au dessus du même point", "pour faciliter le calibrage des antennes relais,", "c'est-à-dire a un orbite géostationnaire."],
                                                  ["Bien joué !","Kourou, est, parmi les propositions","le meilleur site de lancement pour","  profiter de l'effet de fronde."],
                                                  ["Bien joué !","En orbite haute une source d'énergie présente en abondance"," est le rayonnement solaire."],
                                                  ["Bien joué !","Un satellite de communication n'a besoin d'aucun senseur car,","il ne transmet que les informations captés par son antenne"],
                                                  ["Bien joué !","Un satellite de communication a besoin d'une antenne conséquente", "afin d'augmenter la bande passante."],
                                                  ["Très bien alors on peux procéder au décollage !"],
                                                  ["Bien joué !", "La vitesse de libération est la vitesse à laquelle la fusée est","assez rapide pour ne pas retomber sur Terre, la vitesse minimale est de 7km/s.","Mais la fusée ne doit pas être trop rapide où elle sortirait de l'orbite terrestre."]],
        "satellite d'observation":[["Bien joué !","Un satellite d'observation doit avoir des images clairs","et pour cela il doit se trouver au plus proche de la Terre."],
                                   ["Bien joué !","Kourou, est, parmi les propositions","le meilleur site de lancement pour","  profiter de l'effet de fronde."],
                                   ["Bien joué !","Un satellite d'observation a besoin d'une source d'énergie constante,","même lorsqu'il se trouve à l'ombre de la Terre."],
                                    ["Bien joué !","Un satellite d'observation nécessite un senseur optique afin de photographier","la Terre"],
                                    ["Bien joué !","Une antenne moyenne permet de transmettre les images en bonne qualité"],
                                   ["Très bien alors on peux procéder au décollage !"],
                                    ["Bien joué !", "La vitesse de libération est la vitesse à laquelle la fusée est","assez rapide pour ne pas retomber sur Terre, la vitesse minimale est de 7km/s.","Mais la fusée ne doit pas être trop rapide où elle sortirait de l'orbite terrestre."]],

        "satellite de positionnement":[["Bien joué !","Un satellite de positionnement doit couvrir un large espace","pour cela une altitude idéale et une période orbitale moyenne est nécessaire"],
                                       ["Bien joué !","Kourou, est, parmi les propositions","le meilleur site de lancement pour","  profiter de l'effet de fronde."],
                                       ["Bien joué !","Un satellite de positionnement nécessite une horloge atomique","afin d'être le plus précis possible pour l'heure d'envoi du signal"],
                                       ["Bien joué !","Un satellite de positionnement n'a besoin d'aucun capteur car","sa source d'énergie est son capteur"],
                                       ["Bien joué !","Un satellite de positionnement doit se contenter d'une petite antenne car","les informations doivent-être envoyés rapidement"],
                                       ["Très bien alors on peux procéder au décollage !"],
                                        ["Bien joué !", "La vitesse de libération est la vitesse à laquelle la fusée est","assez rapide pour ne pas retomber sur Terre, la vitesse minimale est de 7km/s.","Mais la fusée ne doit pas être trop rapide ou elle sortirait de l'orbite terrestre."]]
                   }



#textes_explicatifs=[[texte explicatif orbite],[texte explicatif customisation satellite]]
textes_explicatifs=[[f"Choisi l'orbite du satellite","L'orbite basse permet au satellite d'être au plus près de la Terre"," L'orbite moyen est idéal pour avoir une période orbitale moyenne.","En orbite géostationnaire les satellites restent au même point par rapport au sol"],
                    ["Choisis le bon site de lancement", "Il n'y a qu'une seule bonne réponse", "N'oublie pas le bouton aide qui est là pour t'aider"],
                    ["Construis ton satellite.", "Choisis la source d'énergie adéquate."],
                    ["Construis ton satellite.", "Choisis le senseur adapté.", "Il est possible qu'il n'y ais besoin d'aucun senseur"],
                    ["Construis ton satellite.", "Choisis le bon moyen de communication", "Il est possible qu'il n'y ais besoin d'aucun moyen de communication"],
                    ["Vérifie les paramètres de mission","Appuis sur OK pour lancer le décollage"],
                    ["Libère le satellite à la bonne vitesse et au bon moment pour qu'il aille en orbite"]]
help_text=["Les satellites sont généralement placés en orbite géostationnaire pour assurer \nune couverture constante d'une région spécifique de la Terre.\n \nLes satellites sont souvent déployés \nen orbite basse ou moyenne terrestre pour une résolution spatiale plus élevée \net une revisite plus fréquente des zones d'intérêt.\n \nEnfin, les satellites,\ncomme ceux utilisés dans les systèmes de navigation GPS, \nsont souvent placés en orbite moyenne terrestre pour une couverture globale.",
           "txt explicatif blablabla",
           'Tout les satellites ont besoin d\'une source d\'alimentation,\nen orbite basse, les satellites sont parfois à l\'ombre de la Terre, \nils ne peuvent donc être alimenté par des panneaux solaires.\n\nParfois les satellites doivent-être très précis, c\'est pourquoi on utilise alors une horloge atomique,\nle \'capteur\' et la source d\'énergie sont alors les mêmes.',
           'Il est nécessaire d\'avoir des capteurs adaptés à la mission, certains satellites ne nécessitent aucun capteur.',
           "Afin de communiquer, il est nécessaire d\'avoir \nune antenne parabolique pour la transmission et la réception des signaux \nde taille nécessaire pour qu’ils effectuent une grande distance, \net qu\'ils puisse transmettre une quantité de données suffisante.",
           "",
           "La vitesse de satellisation est la vitesse que notre satellite doit atteindre \npour se mettre en orbite au tour de la Terre.\nCette vitesse doit être assez élevée pour que notre vaisseau spatial ne retombe pas sur la surface de la Terre,\nelle doit donc être supérieure à 7,8 km/s.\n \nLa vitesse de libération est la vitesse que le satellite a besoin pour échapper à la gravitation de notre planète, \nelle dépend de son volume, pour la Terre, elle est de 11km/s.\n\nA noter que cette vitesse dépend des différentes planètes et de leur volume,  \nau plus elles sont volumineuses au plus la vitesse de libération sera grande." ]

questions={'orbite':0,'map':1,'custom_middle':2, 'custom_bottom':3, 'custom_top':4,'mission_order':5, 'velocity':6}
while state.game:

    mission=mission_chooser()
    if state.game:transition(1)

    txt=textes_explicatifs[questions['orbite']]
    while choose_orbit()!=check_missions[mission][questions['orbite']] and state.game:
        txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
    talk(textes_fin_niveau[mission][questions['orbite']])
    if state.game:transition(1)

    txt=textes_explicatifs[questions['map']]
    while earth_map()!=check_missions[mission][questions['map']] and state.game:
        txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
    talk(textes_fin_niveau[mission][questions['map']])
    if state.game:transition(1)
    past_choices=[]

    txt=textes_explicatifs[questions['custom_middle']]
    while state.game and custom('middle',questions['custom_middle'])!=check_missions[mission][questions['custom_middle']]:
        txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
    talk(textes_fin_niveau[mission][questions['custom_middle']])
    past_choices.append((pygame.image.load('satellite customisation/middle/'+check_missions[mission][questions['custom_middle']]+'.png'), pygame.image.load('satellite customisation/middle/annotation.png'), (330,210), check_missions[mission][questions['custom_middle']]))

    txt=textes_explicatifs[questions['custom_bottom']]
    while state.game and custom('bottom',questions['custom_bottom'])!=check_missions[mission][questions['custom_bottom']]:
        txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse.", "Il est possible qu'il ne faille rien mettre"]
    talk(textes_fin_niveau[mission][questions['custom_bottom']])
    past_choices.append((pygame.image.load('satellite customisation/bottom/'+check_missions[mission][questions['custom_bottom']]+'.png'), pygame.image.load('satellite customisation/bottom/annotation.png'), (330,440), check_missions[mission][questions['custom_bottom']]))

    txt=textes_explicatifs[questions['custom_top']]
    while state.game and custom('top',questions['custom_top'])!=check_missions[mission][questions['custom_top']]:
        txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse.", "Il est possible qu'il ne faille rien mettre"]
    talk(textes_fin_niveau[mission][questions['custom_top']])
    past_choices.append((pygame.image.load('satellite customisation/top/'+check_missions[mission][questions['custom_top']]+'.png'), pygame.image.load('satellite customisation/top/annotation.png'), (330,60), check_missions[mission][questions['custom_top']]))
    if state.game:transition(1)

    txt=textes_explicatifs[questions['mission_order']]
    if state.game: mission_order()
    talk(textes_fin_niveau[mission][questions['mission_order']])
    if state.game:transition(1)

    txt=textes_explicatifs[questions['velocity']]
    while second_space_velocity()!=True and state.game:
        txt=["Raté, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
    talk(textes_fin_niveau[mission][questions['velocity']])
    if state.game:transition(1)

    if state.game: credits()
    if state.game:transition(1)


pygame.quit()
