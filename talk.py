import pygame
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def resize_images():
    return [pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk0.png'),px(1060,1060)),pygame.transform.scale(pygame.image.load('C:/Users/quent/OneDrive/Documents/GitHub/satmanIPSA/talk/talk1.png'),px(1060,1060))]

def talk(txt):
    run=True
    talking_frames=resize_images()
    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
    written=[]
    for paragraph in range(len(txt)):
        written.append("")
        for letter in range(len(txt[paragraph])):
            written[paragraph]=written[paragraph]+txt[paragraph][letter]
            screen.blit(talking_frames[letter%2], (px(0,390),(0,0)))
            for line in range(len(written)):
                screen.blit(font.render(written[line], True, (0,0,0)), (px(140,450+(line*30)),(0,0)))
                pygame.display.update()
            if pygame.mouse.get_pressed()[0]==True and len(written)+len(written[-1])!=len(txt)+len(txt[-1]):pygame.time.wait(10)
            else:pygame.time.wait(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    return
                elif event.type == pygame.VIDEORESIZE:
                    size.width, size.height = pygame.display.get_surface().get_size()
                    talking_frames=resize_images()
                    font = pygame.font.Font('Grand9K Pixel.ttf', int(px(20)))
    while pygame.mouse.get_pressed()[0]!=True:
        screen.blit(talking_frames[1], (px(0,390),(0,0)))
        for line in range(len(written)):
            screen.blit(font.render(written[line], True, (0,0,0)), (px(140,450+(line*30)),(0,0)))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    return
    return

pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
class size:
    width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
txt=["Choisis l'orbite de ton satellite"," Une orbite haute sera plutôt utilisé pour des satellites géostationnaires","Une orbite moyenne sera généralement utilisé pour des satellites de navigation","Une orbite basse est souvant utilisé pour des satellites de communication"]
#talk(txt)
