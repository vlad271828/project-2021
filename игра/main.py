import pygame as pg
from random import randint
from pygame.draw import *

pg.init()

n1 = 10  # кол-во клеток по горизонтали
n2 = 18  # кол-во клеток по вертикали
a = 40  # сторона клетки
FPS = 60
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
screen = pg.display.set_mode((a*n1, a*n2))
color = COLORS[randint(0, 5)]
clock = pg.time.Clock()
# Массив из координат клеток, из которых состоят фигурки
fig1_pos = [(0, -1), (-1, -1), (-1, 0), (0, 0)]
fig2_pos = [(0, 0), (0, -1), (0, 1), (-1, 0)]
fig3_pos = [(0, 0), (0, -1), (0, 1), (-1, -1)]
fig4_pos = [(0, 0), (0, -1), (0, 1), (-1, -1)]
fig5_pos = [(0, 0), (-1, 0), (0, 1), (-1, -1)]
fig6_pos = [(-1, 0), (-2, 0), (0, 0), (1, 0)]
fig7_pos = [(-1, 0), (-1, 1), (0, 0), (0, -1)]
figure_pos = [fig1_pos, fig2_pos, fig3_pos, fig4_pos, fig5_pos, fig6_pos, fig7_pos]
figures = [[pg.Rect(x + n1 // 2, y + 1, 0, 0) for x, y in fig_pos] for fig_pos in figure_pos]
figure_rect = pg.Rect(0, 0, a - 2, a - 2)
n = randint(0, 6)
figure = figures[n]

while True:
    dx = dy = 0
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                dx = -1
            elif event.key == pg.K_RIGHT:
                dx = 1
            elif event.key == pg.K_DOWN:
                dy = 1
    # перемещение фигурок(вниз, вправо)
    for i in range(4):
        figure[i].x += dx
        if figure[i].x + 1 <= n1 and figure[i].x >= 0:
            break
    # отрисовываем сетку
    for i in range(n1):
        for j in range(n2):
            rect(screen, (40, 40, 40), (i*a, j*a, a, a), 1)

    # отрисовываем фигурки
    for i in range(4):
        figure_rect.x = figure[i].x * a
        figure_rect.y = figure[i].y * a
        rect(screen, color, figure_rect)



    pg.display.flip()

    clock.tick(FPS)
