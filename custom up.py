import pygame
import os
def px(x=None,y=None):
    if y==None:#si aucune valeur y n'est donné, calculer seulement x
        return (x*size.width)/1066# produit en croix appelant la class size
    elif x==None:#si aucune valeur x n'est donné, calculer seulement y
        return (y*size.height)/600# produit en croix appelant la class size
    else:
        return ((x*size.width)/1066,(y*size.height)/600)#sinon renvoyé la nouvelle valeur de x et y
def load_images(part):
    dir={'bottom':'satellite customisation/bottom','middle':'satellite customisation/middle','top':'satellite customisation/top'}[part]
    choices={}
    for f in os.listdir(dir):
        choices[f[:-4]]=pygame.transform.scale(pygame.image.load(str(dir)+'/'+str(f)),px(1500,1500))
    return choices
def resize_buttons():
    left_button=[pygame.transform.scale(pygame.image.load('satellite customisation/left_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/left_button2.png'),px(150,150))]
    right_button=[pygame.transform.scale(pygame.image.load('satellite customisation/right_button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/right_button2.png'),px(150,150))]
    buttons = {(px(0,220),px(150,150)):[left_button,-1],
               (px(750,220),px(150,150)):[right_button,1]}
    ok=[pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'),px(150,150)),pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'),px(150,150))]
    return buttons, ok
def resize_past_choices(past_choices_list):
    for image in range(len(past_choices_list)):
        past_choices_list[image]=pygame.transform.scale(past_choices_list[image],px(1500,1500))
    return past_choices_list
def custom(part):
    run=True
    initialize=True
    choices = load_images(part)
    past_choices_list=resize_past_choices(past_choices)
    arrow_buttons, ok_button=resize_buttons()
    index=len(choices)-1
    while run and state.game:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))

        screen.fill(bg_color)
        for image in past_choices_list:
            screen.blit(image, px(-185,-200))
        screen.blit(list(choices.values())[index], px(-185,-200))
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


        screen.blit(ok_button[0],px(900,420))
        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                pygame.time.wait(200)
                run=False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                state.game=False
                quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                choices = load_images(part)
                past_choices_list=resize_past_choices(past_choices_list)
                arrow_buttons=resize_buttons()
        if initialize==True:
            print(txt)
            initialize=False
    print(list(choices.keys())[index])
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


past_choices=[pygame.image.load('satellite customisation/body.png')]

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('middle')!=check_missions[mission][1]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append(pygame.image.load('satellite customisation/middle/'+check_missions[mission][1]+'.png'))

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('bottom')!=check_missions[mission][2]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append(pygame.image.load('satellite customisation/bottom/'+check_missions[mission][2]+'.png'))

txt=["Construis ton satellite.", "Le satellite doit pouvoir répondre aux besoins de sa mission."]
while state.game and custom('top')!=check_missions[mission][3]:
    txt=["Mauvaise réponse, réessaye !","Tu peux cliquer sur le bouton aide pour chercher  la bonne réponse."]
print('bien joué')
past_choices.append(pygame.image.load('satellite customisation/top/'+check_missions[mission][3]+'.png'))


#print(custom('bottom'))
#past_choices.append('satellite customisation/bottom/'+check_missions[mission][0]+'.png')
