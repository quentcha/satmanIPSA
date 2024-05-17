import pygame
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def mission_logos():
    comm=[pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite de communication.png'), px(200, 200)),
          pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite de communication.png'), px(300, 300))]
    pos=[pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite de positionnement.png'), px(200, 200)),
         pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite de positionnement.png'), px(300, 300))]
    obs=[pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite d\'observation.png'), px(200, 200)),
         pygame.transform.scale(pygame.image.load('_internal/mission chooser/satellite d\'observation.png'), px(300, 300))]
    return [comm,pos, obs]
def mission_chooser():
    logos =mission_logos()

    rect={(px(55,200),px(200,200)): 'satellite de communication',
          (px(435,200),px(200,200)):'satellite de positionnement',
          (px(805,200),px(200,200)):"satellite d'observation"}
    Mission_name = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(px(20)))
    title=pygame.font.Font('_internal/Grand9K Pixel.ttf', int(px(60)))
    run=True
    while run:# and state.game
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.fill((173, 216, 230))
        screen.blit(title.render('CHOISIS TA MISSION :', True, (0,)*3), (px(10,10),(0,0)))
        for im in range(len(logos)):
            screen.blit(logos[im][0], list(rect.keys())[im])
            screen.blit(Mission_name.render(list(rect.values())[im], True, (0,0,0)), ((list(rect.keys())[im][0][0]+px(x=100-(len(list(rect.values())[im])/2)*11),list(rect.keys())[im][0][1]+px(y=250)),(0,0)))
        #screen.blit(comm[0], px(60,300))
        coll=pygame.Rect.collidedict(mouse,rect)
        if coll:
            screen.blit(logos[list(rect.keys()).index(coll[0])][1], (coll[0][0][0]-50,coll[0][0][1]-50))
            if pygame.mouse.get_pressed()[0]==True:
                run=False
                return coll[1]

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                title=pygame.font.Font('_internal/Grand9K Pixel.ttf', int(px(60)))
                logos =mission_logos()
                Mission_name = pygame.font.Font('_internal/Grand9K Pixel.ttf', int(px(20)))
                rect={(px(55,200),px(200,200)): 'satellite de communication',
                (px(435,200),px(200,200)):'satellite de positionnement',
                (px(805,200),px(200,200)):"satellite d'observation"}
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
check_missions={'satellite de communication': ['orbite géostationnaire', ['panneaux solaires','','grande antenne']],
          "satellite d'observation": ['orbite basse',['générateur nucléaire','senseur optique', 'antenne moyenne']],
            "satellite de positionnement":['orbite moyenne',['réacteur nucléaire','','petite antenne']]}

print(mission_chooser())
