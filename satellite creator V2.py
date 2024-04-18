import pygame
import os
def resize_help():
    return [pygame.transform.scale(pygame.image.load('aide/aide-1.png'),px(150,150)),
            pygame.transform.scale(pygame.image.load('aide/aide-2.png'),px(150,150))]
def px(x=None,y=None):
    if y==None:#si aucune valeur y n'est donné, calculer seulement x
        return (x*size.width)/1066# produit en croix appelant la class size
    elif x==None:#si aucune valeur x n'est donné, calculer seulement y
        return (y*size.height)/600# produit en croix appelant la class size
    else:
        return ((x*size.width)/1066,(y*size.height)/600)#sinon renvoyé la nouvelle valeur de x et y
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
    body=pygame.transform.scale(pygame.image.load('satellite customisation/body.png'), px(1500, 1500))
    for image in range(len(past_choices_list)):
        past_choices_list[image]=(pygame.transform.scale(past_choices_list[image][0],px(1500,1500)), pygame.transform.scale(past_choices_list[image][1], px(80,80)),px(past_choices_list[image][2][0],past_choices_list[image][2][1]),past_choices_list[image][3])
    return past_choices_list, body
def custom(part):
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
                screen.blit(font.render(image[3], True, (0,0,0)),(((image[2][0]-(len(image[3])*11),image[2][1]-11)),(0,0)))

        screen.blit(list(choices.values())[index], px(-185,-200))
        if list(choices.keys())[index]!='_empty':
            screen.blit(annotation[1], annotation[0])
            screen.blit(font.render(list(choices.keys())[index], True, (0,0,0)),(((annotation[0][0]-(len(list(choices.keys())[index])*11),annotation[0][1]-11)),(0,0)))

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
                pygame.time.wait(200)

        screen.blit(help_button[0],px(5,-50))
        screen.blit(ok_button[0],px(900,420))
        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False
        elif pygame.Rect.colliderect(mouse,(px(5,-50),px(150,100))):
            screen.blit(help_button[1],px(5,-50))
            if pygame.mouse.get_pressed()[0]:
                pygame.time.wait(200)
                print('help')

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                help_button=resize_help()
                choices, annotation = load_images(part)
                past_choices_list, body=resize_past_choices(past_choices_list)
                arrow_buttons, ok_button=resize_buttons()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
        if initialize==True:
            print(txt)
            initialize=False
    return list(choices.keys())[index]
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class state:
    game=True
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
bg_color=(173, 216, 230)
click=pygame.mixer.Sound("sound/Menu Selection Click.wav")
mission='satellite de positionnement'
check_missions={'satellite de communication': ['orbite géostationnaire', 'panneaux solaires','_empty','grande antenne'],
          "satellite d'observation": ['orbite basse','générateur nucléaire','senseur optique', 'antenne moyenne'],
            "satellite de positionnement":['orbite moyenne','générateur nucléaire','_empty','petite antenne']}


past_choices=[]

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('middle')!=check_missions[mission][1]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append((pygame.image.load('satellite customisation/middle/'+check_missions[mission][1]+'.png'), pygame.image.load('satellite customisation/middle/annotation.png'), (330,210), check_missions[mission][1]))

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('bottom')!=check_missions[mission][2]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append((pygame.image.load('satellite customisation/bottom/'+check_missions[mission][2]+'.png'), pygame.image.load('satellite customisation/bottom/annotation.png'), (330,440), check_missions[mission][2]))

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('top')!=check_missions[mission][3]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append((pygame.image.load('satellite customisation/top/'+check_missions[mission][3]+'.png'), pygame.image.load('satellite customisation/top/annotation.png'), (330,60), check_missions[mission][3]))


#print(custom('bottom'))
#past_choices.append('satellite customisation/bottom/'+check_missions[mission][0]+'.png')
