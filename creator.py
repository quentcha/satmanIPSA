import pygame

def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
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

def satellite_creator(txt):

    p = {'energy':['','panneaux solaires','réacteur nucléaire'],'sensor':['','senseur optique','senseur infrarouge','propulseur'], 'antenna':['','petite antenne', 'antenne moyenne', 'grande antenne']}
    parts = {'body':['body.png'], 'energy':['empty.png','solar panels.png','atomic generator.png'],'sensor':['empty.png','optic sensor.png','infrared sensor.png','small thruster.png'], 'antenna':['empty.png','small antenna.png', 'medium antenna.png', 'big antenna.png']}
    parts=convert_images(parts)
    buttons=resize_buttons()
    game=True
    sat={'body':0,'energy':0,'sensor':0,'antenna':0}
    ok_button=resize_ok()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    annotation=resize_annotation()
    talk(txt)
    while game:
        screen.fill((173, 216, 230))
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))

        if pygame.Rect.colliderect(mouse,(px(900,420),px(150,150))):
            screen.blit(ok_button[1],px(900,420))
            if pygame.mouse.get_pressed()[0]==True:
                game=False
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
            if pygame.mouse.get_pressed()[0]==True:
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
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                parts=resize_images(parts)
                buttons=resize_buttons()
                ok_button=resize_ok()
                annotation=resize_annotation()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    return {"source d'energie":p['energy'][sat['energy']],"senseur":p['sensor'][sat['sensor']],"antenne":p['antenna'][sat['antenna']]}
'''
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
print(satellite_creator())
'''
