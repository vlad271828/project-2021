import pygame.mouse
import pygame
from pygame.draw import *
from pygame.mixer import *
from Sounds import *
from parametry import *




class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            rect(screen, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1:
                Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    if action == exit:
                        exit()
                    else:
                         action()
        else:
            rect(screen, self.inactive_color, (x, y, self.width, self.height))

        screen.blit(message, (x, y - 5))