import pygame as pg
from pygame.draw import *

pg.init()

n1 = 8  # кол-во клеток по горизонтали
n2 = 15  # кол-во клеток по вертикали
a = 40  # сторона клетки
n = i = 0
FPS = 60
screen = pg.display.set_mode((a*n1, a*n2))
clock = pg.time.Clock()

while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    # отрисовываем сетку
    for n in range(n1):
        for i in range(n2):
            rect(screen, (40, 40, 40), (n*a, i*a, a, a), 1)

    pg.display.flip()

    clock.tick(FPS)
