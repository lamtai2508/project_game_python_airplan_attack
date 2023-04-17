import pygame
from question import Question
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import functions as gf
from alien import Alien
from gameStats import GameStats
from button import Button
from scoreboard import ScoreBoard
import pygame

pygame.init()
game_settings = Settings() 
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  

game_end=False
while not game_end:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True
    question=Question(game_settings, screen, "Cau hoi 1:","dap an 1","dap an 2","dap an 3","dap an 4")
    question.draw_button()
    pygame.display.update()

pygame.quit()
quit()