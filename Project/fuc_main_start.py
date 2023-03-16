import pygame
from color import *
#tao su kien khi tro vao chu 
#hien 
def text_true(screen,text,rect,base_font):
    pygame.draw.rect(screen,gray,rect)
    surface=base_font.render(text, True,red)
    screen.blit(surface,(rect.x+60,rect.y+10))
#an
def text_false(screen,text,rect,base_font):
    pygame.draw.rect(screen,white, rect,2)
    surface=base_font.render(text, True,white)
    screen.blit(surface,(rect.x+60,rect.y+10))

