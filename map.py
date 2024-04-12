import pygame

def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)
def resize_help():
    return [pygame.transform.scale(pygame.image.load('aide/aide-1.png'),px(150,150)),
            pygame.transform.scale(pygame.image.load('aide/aide-2.png'),px(150,150))]

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
    locations = {'Kourou':[(335, 305), True],
                 'Pôle Nord':[(400,100), False],
                 'Toulouse':[(470, 190), False],
                 'Himalaya':[(630, 230), False]}
    earth, up_button, down_button, ok_button = resize_earth_map_assets()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
    map_pos=(120,30)
    initialize=True
    while run and state.game:
        screen.fill(bg_color)
        screen.blit(earth, px(map_pos[0],map_pos[1]))
        pygame.draw.rect(screen,bg_color,(px(map_pos[0]-55,map_pos[1]-5),px(810,550)),int(max(px(x=55),px(y=55))))
        pygame.draw.rect(screen,(0,0,0),(px(map_pos[0],map_pos[1]+50),px(700,440)),int(min(px(x=5),px(y=5))))

        screen.blit(help_button[0],px(5,-50))
        screen.blit(up_button[0], px(900, 60))
        screen.blit(down_button[0], px(900, 190))
        screen.blit(ok_button[0], px(900, 370))

        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        if pygame.Rect.colliderect(mouse, (px(900, 120), px(200, 100))):
            screen.blit(up_button[1], px(900, 120))
            if pygame.mouse.get_pressed()[0]:
                #print(locations, list(locations.values()))
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

        if pygame.Rect.colliderect(mouse, (px(900, 250), px(200, 100))):
            screen.blit(down_button[1], px(900, 250))
            if pygame.mouse.get_pressed()[0]:
                #print(locations, list(locations.values()))
                for loc in range(len(locations)):
                    if list(locations.values())[loc][1]==True:
                        locations[list(locations.keys())[loc]][1]=False
                        locations[list(locations.keys())[loc-1]][1]=True
                        break
                pygame.time.wait(200)

        for circles in locations:
            if locations[circles][1]==True:
                screen.blit(font.render(circles,True,(255,0,0)),px(locations[circles][0][0]+10,locations[circles][0][1]+10))
                pygame.draw.circle(screen, (255, 0, 0), px(locations[circles][0][0],locations[circles][0][1]), int(min(px(x=8), px(y=8))))
            else:
                pygame.draw.circle(screen, (0, 0, 0),px(locations[circles][0][0],locations[circles][0][1]), int(min(px(x=8), px(y=8))))
        if pygame.Rect.colliderect(mouse, (px(900, 400), px(200, 100))):
            screen.blit(ok_button[1], px(900, 400))
            if pygame.mouse.get_pressed()[0]:
                run=False
                for loc in range(len(locations)):
                    if list(locations.values())[loc][1]==True:
                        return list(locations.keys())[loc]
                pygame.time.wait(200)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth, up_button, down_button, ok_button = resize_earth_map_assets()
                font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
        if initialize==True:
            earth, up_button, down_button, ok_button = resize_earth_map_assets()
            font = pygame.font.Font('Grand9K Pixel.ttf', int(px(18)))
            initialize=False

pygame.init()
screen = pygame.display.set_mode((1066, 600), pygame.RESIZABLE)
txt_color=(0,0,0)
bg_color=(173, 216, 230)
class size:
    width, height = pygame.display.get_surface().get_size()

class state:
    game = True

print(earth_map())
