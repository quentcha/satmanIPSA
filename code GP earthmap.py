import pygame

def px(x=None, y=None):
    if y == None:
        return (x * size.width) / 1066
    elif x == None:
        return (y * size.height) / 600
    else:
        return ((x * size.width) / 1066, (y * size.height) / 600)

def resize_earth_map_assets():
    earth = pygame.transform.scale(pygame.image.load('Earth_map/Earth_map.png'), px(1066, 1066))
    up_button = [pygame.transform.scale(pygame.image.load('orbit/up_button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('orbit/up_button2.png'), px(150, 150))]
    down_button = [pygame.transform.scale(pygame.image.load('orbit/down_button1.png'), px(150, 150)),
                   pygame.transform.scale(pygame.image.load('orbit/down_button2.png'), px(150, 150))]
    ok_button = [pygame.transform.scale(pygame.image.load('satellite customisation/button1.png'), px(150, 150)),
                 pygame.transform.scale(pygame.image.load('satellite customisation/button2.png'), px(150, 150))]
    return earth, up_button, down_button, ok_button

def earth_map():
    run = True
    locations = {'Kourou':[(330, 300), True],
                 'Toulouse':[(520, 130), False],
                 'Elbrouz':[(680, 200), False]}
    current_location = 'Kourou'
    earth, up_button, down_button, ok_button = resize_earth_map_assets()
    while run and state.game: 
        screen.fill((173, 216, 230))
        screen.blit(earth, px(0, -100))
        screen.blit(up_button[0], px(900, 120))
        screen.blit(down_button[0], px(900, 250))
        screen.blit(ok_button[0], px(900, 400))
        mouse = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        if pygame.Rect.colliderect(mouse, (px(900, 120), px(200, 100))):
            screen.blit(up_button[1], px(900, 120))
        if pygame.Rect.colliderect(mouse, (px(900, 250), px(200, 100))):
            screen.blit(down_button[1], px(900, 250))
        if pygame.mouse.get_pressed()[0]:
            current_location = handle_click(pygame.mouse.get_pos(), locations, current_location)

        for location, (pos, _) in locations.items():
            if location == current_location:
                pygame.draw.circle(screen, (255, 0, 0), px(pos[0], pos[1]), int(min(px(x=10), px(y=10))))
            else:
                pygame.draw.circle(screen, (0, 0, 0), px(pos[0], pos[1]), int(min(px(x=10), px(y=10))))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                state.game = False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                earth, up_button, down_button, ok_button = resize_earth_map_assets()

def handle_click(pos, locations, current_location):
    x, y = pos
    button_up_pos = (900, 120)
    button_down_pos = (900, 250)
    if button_up_pos[0] <= x <= button_up_pos[0] + 80 and button_up_pos[1] <= y <= button_up_pos[1] + 40:
        keys = list(locations.keys())
        index = keys.index(current_location)
        next_index = (index - 1) % len(locations)
        current_location = keys[next_index]
    elif button_down_pos[0] <= x <= button_down_pos[0] + 80 and button_down_pos[1] <= y <= button_down_pos[1] + 40:
        keys = list(locations.keys())
        index = keys.index(current_location)
        next_index = (index + 1) % len(locations)
        current_location = keys[next_index]

    # Mettre à jour l'état des positions dans le dictionnaire
    for location in locations:
        locations[location][1] = False
    locations[current_location][1] = True

    return current_location


pygame.init()
screen = pygame.display.set_mode((1066, 600), pygame.RESIZABLE)

class size:
    width, height = pygame.display.get_surface().get_size()

class state:
    game = True

earth_map()
