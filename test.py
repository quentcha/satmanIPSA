from creator import satellite_creator
import pygame
pygame.init()
screen = pygame.display.set_mode((1066,600), pygame.RESIZABLE) #16:9 ratio
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('SATMAN')
print(satellite_creator())

