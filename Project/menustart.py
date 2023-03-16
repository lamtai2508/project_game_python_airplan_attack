import pygame
import color
from fuc_main_start import *
def main():
    pygame.init()
    #tao man hinh voi do rong 1000 va dai 6000
    screen=pygame.display.set_mode((900,600))
    # tao background cho man hinh
    bg=pygame.image.load("image/bg_main2.png")
    bg=pygame.transform.scale2x(bg)
    #set caption va icon logo
    pygame.display.set_caption("Airplane attack")
    icon_logo=pygame.image.load('image/icon_logo.jpg')
    pygame.display.set_icon(icon_logo)
    #them may bay chien dau
    pl=pygame.image.load("image/icon_plane.png")
    pl=pygame.transform.scale2x(pl)
    pl_rect=pl.get_rect(center=(450,100))
    #tao Font mac dinh
    base_font=pygame.font.Font(None,80)
    #tao cho bam bat dau
    start_text='Start'
    #tao chu Score
    score_text='Score'
    #tao vien cho chu start
    start_rect=pygame.Rect(325, 150, 250,70)
    #tao vien cho chu score
    score_rect=pygame.Rect(325, 240, 250,70)
    bg_x=0
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            #su kien bam nut thoat
            if event.type==pygame.QUIT:
                game_over=True
        #lay vi tri con tro chuot
        if event.type==pygame.MOUSEBUTTONDOWN:...
        # print(pygame.mouse.get_pos())
        cur=pygame.mouse.get_pos()
        #tao anh background dong
        bg_x-=1
        screen.blit(bg, (bg_x,0))
        screen.blit(bg, (bg_x+900,0))
        if(bg_x==-900):
            bg_x=0
        #the may bay vao
        screen.blit(pl,pl_rect)
        #them chu start va them vien vao chu start
        #su kien khi tro vao chu start
        if 325+250 > cur[0] >325 and 220 > cur[1] >150:
            text_true(screen,start_text,start_rect,base_font)
            text_false(screen, score_text, score_rect, base_font)
        elif 325+250 > cur[0] >325 and 310 > cur[1] >240:
            text_true(screen, score_text, score_rect, base_font)
            text_false(screen,start_text,start_rect,base_font)
        else:
            text_false(screen,start_text,start_rect,base_font)
            text_false(screen, score_text, score_rect, base_font) 
        pygame.display.update()
    pygame.quit()
    quit()
main()