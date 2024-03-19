import pygame
def px(x=None,y=None):
    if y==None:
        return (x*size.width)/1066
    elif x==None:
        return (y*size.height)/600
    else:
        return ((x*size.width)/1066,(y*size.height)/600)
def load_anim():
    anim=[]
    length=12
    for i in range(length):
        print(i)
        anim.append(pygame.transform.scale(pygame.image.load(f'transition/pixil-frame-{i}.png'),px(1066,1066)))
    return anim
def transition(read):
    anim=load_anim()
    for im in range(read,len(anim)*read,read):#read is -1 backward and else 1
        screen.blit(anim[im], (0,0))
        pygame.display.update()
        pygame.time.wait(100)
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
screen.fill((173, 216, 230))
class size:
    width, height = pygame.display.get_surface().get_size()
transition(-1)
