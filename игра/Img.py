import pygame

pygame.init()

bckg = pygame.image.load('img/bg1.jpg')
bg_end = pygame.image.load('img/bg_end.jpg')
bg_menu = pygame.image.load('img/bg_menu.jpg')
themeimage = pygame.image.load('img/choose_theme.jpg')
levelimage = pygame.image.load('img/choose_level.jpg')

def set_theme(num):
    global bckg
    bckg = pygame.image.load(r'img/bg{}.jpg'.format(num))