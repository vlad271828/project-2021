import pygame

pygame.init()

button_sound = pygame.mixer.Sound('sounds/button.wav')

def set_sound(num):
    global game_sound
    game_sound = pygame.mixer.music.load('sounds/8bit{}.mp3'.format(num))
