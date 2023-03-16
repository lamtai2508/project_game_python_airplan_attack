import pygame
import color
from fuc_main_start import *
def main():
    pygame.init()
    screen=pygame.display.set_mode((900,600))
    # tao background cho man hinh
    bg=pygame.image.load("image/bg_main2.png")
    bg=pygame.transform.scale2x(bg)
    #set caption va icon logo
    pygame.display.set_caption("Airplane attack")
    icon_logo=pygame.image.load('image/icon_logo.jpg')
    pygame.display.set_icon(icon_logo)
    #tao Font mac dinh
    base_font=pygame.font.Font(None,40)
    #tao chu level tu 1 toi 10
    level_1_text='Level 1'
    level_2_text='Level 2'
    level_3_text='Level 3'
    level_4_text='Level 4'
    level_5_text='Level 5'
    level_6_text='Level 6'
    level_7_text='Level 7'
    level_8_text='Level 8'
    level_9_text='Level 9'
    level_10_text='Level 10'
    #tao vien cho chu level 1 ->10
    level_1_rect=pygame.Rect(20, 100, 200,50)
    level_1_rect=pygame.Rect(20, 100, 200,50)
    
    
    
    
    #khoi tao cac bien cua chuong trinh
    game_over=False
    bg_x=0
    while not game_over:
        for event in pygame.event.get():
            #su kien bam nut thoat
            if event.type==pygame.QUIT:
                game_over=True
         #tao anh background dong
        bg_x-=1
        screen.blit(bg, (bg_x,0))
        screen.blit(bg, (bg_x+900,0))
        if(bg_x==-900):
            bg_x=0
        #them level 1
        text_true(screen,level_1_text, level_1_rect, base_font)    
        
        pygame.display.update()
    pygame.quit()
    quit()
main()