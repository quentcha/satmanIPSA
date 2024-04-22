import pygame
def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)
def news_anchor_assets():
    TV_set = [pygame.transform.scale(pygame.image.load('news_anchor/frame-0.png'), px(1066, 1066)),
                 pygame.transform.scale(pygame.image.load('news_anchor/frame-1.png'), px(1066, 1066))]
    rocket= [pygame.transform.scale(pygame.image.load('lanceur/'+check_missions[mission][questions['velocity']]+'.png'), px(300, 300))]
    sat=[pygame.transform.scale(pygame.image.load('satellite customisation/bin/body.png'), px(500, 500)),
         pygame.transform.scale(pygame.image.load('satellite customisation/bottom/'+check_missions[mission][questions['custom_bottom']]+'.png'), px(500, 500)),
         pygame.transform.scale(pygame.image.load('satellite customisation/middle/'+check_missions[mission][questions['custom_middle']]+'.png'), px(500, 500)),
         pygame.transform.scale(pygame.image.load('satellite customisation/top/'+check_missions[mission][questions['custom_top']]+'.png'), px(500, 500))]
    logo=[pygame.transform.scale(pygame.image.load('menu/title.png'), px(300, 300))]
    return TV_set, rocket, sat, logo
def news_anchor():
    run=True
    i=0
    length=30
    TV_set, rocket, sat, logo=news_anchor_assets()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(60)))
    news=[[f"Aujourd'hui a lieu le lancement historique d'un {mission} à Kourou à l'aide d'une fusée {check_missions[mission][questions['velocity']]}."+" "*length,rocket,(0,0)] ,
          ["Cette mission est opéré par l'agence spatiale privé SATMAN"+" "*length,logo,(0,0)],
    [f"Le satellite sera envoyé en {check_missions[mission][questions['orbite']]}. Vous pouvez voir à l'écran une image du satellite"+" "*length, sat,(0,0)]]
    txt=['',]*length
    print(txt)
    speed=200
    while run and state.game:
        i+=0.1
        screen.fill(bg_color)
        screen.blit(TV_set[int(i)%2],(0,0))
        if len(news[0][0])<=len(txt):
            if len(news)==1:
                run=False
            else:
                news=news[1:]
        for slot in range(len(txt)):
            txt[slot]=news[0][0][slot]
        news[0][0]=news[0][0][1:]
        screen.blit(font.render(''.join(txt),True,(0,0,0)),px(15,470))
        for im in news[0][1]:
            screen.blit(im, news[0][2])
        pygame.time.wait(speed)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
pygame.init()
screen = pygame.display.set_mode((1066, 600), pygame.RESIZABLE)
txt_color=(0,0,0)
bg_color=(173, 216, 230)

class size:
    width, height = pygame.display.get_surface().get_size()

class state:
    game = True

check_missions={'satellite de communication': ['orbite géostationnaire','Kourou', 'panneaux solaires','_empty','grande antenne', 'SLS'],
          "satellite d'observation": ['orbite basse','Kourou','générateur nucléaire','senseur optique', 'antenne moyenne', 'vega'],
            "satellite de positionnement":['orbite moyenne','Kourou','générateur nucléaire','_empty','petite antenne', 'arianeV']}
mission='satellite de positionnement'
questions={'orbite':0,'map':1,'custom_middle':2, 'custom_bottom':3, 'custom_top':4, 'velocity':5}

news_anchor()
