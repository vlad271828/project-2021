import pygame
import Img
import parametry as p
from button import *
import run_game

def show_menu():

    start_button = Button(200, 100)
    quit_button = Button(200, 100)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        p.screen.blit(Img.bg_menu, (0, 0))
        start_button.draw(250, 250, title_start, run_game.run_game)
        quit_button.draw(250, 500, title_quit, exit)

        pygame.display.update()
        clock.tick(60)
