import pygame
def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)
def mission_order_assets():
    rocket= [pygame.transform.scale(pygame.image.load('lanceur/'+check_missions[mission][questions['velocity']]+'.png'), px(550, 550))]
    sat=[pygame.transform.scale(pygame.image.load('satellite customisation/bin/body.png'), px(700, 700)),
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
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(25)))
    while run: #and state.game:
        screen.fill(bg_color)

        screen.blit(font.render("MISSION : "+mission,True,(0,0,0)),px(10,10))

        screen.blit(rocket[0],px(700,40))
        #pygame.draw.line(screen,(0,0,0),px(700+23*len(check_missions[mission][questions['velocity']]),100),px(900,100),5)
        screen.blit(font.render((check_missions[mission][questions['velocity']]).upper(),True,(0,0,0)),px(850,5))

        pygame.draw.line(screen,(0,0,0),px(800,150),px(900,150),5)
        for im in range(len(sat)):
            screen.blit(sat[im],px(360,-80))

        screen.blit(earth[0], px(70,150))
        pygame.draw.circle(screen,(255,0,0),px(120,200),100,2)
        pygame.draw.circle(screen,(255,0,0),px(218,220),5,5)
        screen.blit(font.render(check_missions[mission][questions['orbite']],True,(0,0,0)),px(230,200))

        screen.blit(map[0], px(500,300))
        pygame.draw.rect(screen,(0,0,0),(px(500,320),px(300,190)),5)
        pygame.draw.rect(screen,bg_color,(px(470,290),px(360,250)),30)
        pygame.draw.circle(screen,(255,0,0),px(600,420),5,5)
        screen.blit(font.render("Kourou",True,(0,0,0)),px(600,510))

        screen.blit(ok_button[0], px(10, 390))
        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        if pygame.Rect.colliderect(mouse, (px(10, 390), px(200, 200))):
            screen.blit(ok_button[1], px(10, 390))
            if pygame.mouse.get_pressed()[0]:
                run=False
                pygame.time.wait(200)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
                #pygame.quit()
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
mission="satellite de communication"
questions={'orbite':0,'map':1,'custom_middle':2, 'custom_bottom':3, 'custom_top':4, 'velocity':5}

mission_order()
