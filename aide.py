import pygame
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def resize_help_buttons():
    return [pygame.transform.scale(pygame.image.load('aide/retour 1.png'),px(300,300)),
            pygame.transform.scale(pygame.image.load('aide/retour 2.png'),px(300,300))]
def blit(txt):
    help_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(15)))
    Mission_font = pygame.font.Font('Grand9K Pixel.ttf', int(px(30)))
    pygame.draw.rect(screen, (140, 175, 186), (px(30, 30),px(1006,540)))
    screen.blit(Mission_font.render("Objectif : "+missions, True, (0,0,0)), (px(35,35),(0,0)))
    for phrase in range(len(txt.split("\n"))):
        screen.blit(help_font.render(txt.split("\n")[phrase], True, (0,0,0)), (px(35,100+phrase*30),(0,0)))

def help(num):
    back_button=resize_help_buttons()
    blit(help_text[num])
    run=True
    while run:
        mouse=pygame.Rect(pygame.mouse.get_pos(),(20,20))
        screen.blit(back_button[0],(730,430))
        if pygame.Rect.colliderect(mouse,(px(730,430),px(300,300))):
            screen.blit(back_button[1],px(730,430))
            if pygame.mouse.get_pressed()[0]==True:
                run=False
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type == pygame.VIDEORESIZE:
                size.width, size.height = pygame.display.get_surface().get_size()
                back_button=resize_help_buttons()
                blit(help_text[num])

missions='satellite de communication'
help_text=['Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n Maecenas vitae eros quis tellus vehicula convallis quis non dui. Proin interdum non lorem faucibus tincidunt.\n Ut id augue ut massa scelerisque viverra ut vel eros. Sed iaculis purus vitae libero efficitur, at congue nisl blandit.\n Sed fringilla erat nec sollicitudin maximus. Praesent accumsan lacus a elit scelerisque scelerisque.\n In congue porttitor enim. Mauris nisi dui, aliquam ac lorem nec, lobortis aliquet massa.\n Proin luctus orci non rutrum accumsan. Nulla non ex nunc. Cras ac varius velit.\n Aliquam mattis nisi nec libero tincidunt, vel interdum velit accumsan.\n Aliquam bibendum ultricies arcu, vitae hendrerit tortor varius sed.\n \n Suspendisse neque ex, efficitur et condimentum vitae, convallis id neque.',
           '']
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
screen.fill((173, 216, 230))
help(0)

