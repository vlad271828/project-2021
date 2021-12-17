import pygame
from copy import deepcopy
from random import randint


n1 = 10
n2 = 18
a = 40
trazmer = n1 * a, n2 * a
razmer = 700, 800
FPS = 60
i = 0

pygame.init()
pygame.mixer.music.load('sounds/тетрисмузыка.mp3')
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode(razmer)
tscreen = pygame.Surface(trazmer)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * a, y * a, a, a) for x in range(n1) for y in range(n2)]

fig1_pos = [(0, -1), (-1, -1), (-1, 0), (0, 0)]
fig2_pos = [(0, 0), (0, -1), (0, 1), (-1, 0)]
fig3_pos = [(0, 0), (0, -1), (0, 1), (-1, -1)]
fig4_pos = [(0, 0), (0, -1), (0, 1), (-1, -1)]
fig5_pos = [(0, 0), (-1, 0), (0, 1), (-1, -1)]
fig6_pos = [(-1, 0), (-2, 0), (0, 0), (1, 0)]
fig7_pos = [(-1, 0), (-1, 1), (0, 0), (0, -1)]
figure_pos = [fig1_pos, fig2_pos, fig3_pos, fig4_pos, fig5_pos, fig6_pos, fig7_pos]

figures = [[pygame.Rect(x + n1 // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figure_pos]
figure_rect = pygame.Rect(0, 0, a - 2, a - 2)
field = [[0 for i in range(n1)] for j in range(n2)]

acount = 0
aspeed = 60
alimit = 2000

bg = pygame.image.load('img/bg.jpg').convert()
game_bg = pygame.image.load('img/bg2.jpg').convert()

main_font = pygame.font.Font('font.ttf', 65)
font = pygame.font.Font('font.ttf', 45)

title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = font.render('score:', True, pygame.Color('green'))
title_record = font.render('record:', True, pygame.Color('purple'))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
figure, next_figure = deepcopy(figures[randint(0, 6)]), deepcopy(figures[randint(0, 6)])
color = COLORS[randint(0, 5)]
next_color = COLORS[randint(0, 5)]

score = 0
lines = 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}  # словарь зачисление очков от кол-ва собранных одновременно линий

def check_borders():
    if figure[i].x < 0 or figure[i].x > n1 - 1:
        return False
    elif figure[i].y > n2 - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')


def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

def move_figure():
    # смещение по горизонтали
    global figure, i,acount, alimit, color, next_color, next_figure
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
    # смещение вниз
    acount += aspeed
    if acount > alimit:
        acount = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(figures[randint(0, 6)]), COLORS[randint(0, 5)]
                alimit = 2000
                break
    # вращение
    center = figure[0]  # центр вращения
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

def end_game():
    global acount, aspeed, alimit, score, field
    for i in range(n1):
        if field[0][i]:
            set_record(record, score)
            field = [[0 for i in range(n1)] for i in range(n2)]
            acount = 0
            aspeed = 60
            alimit = 2000
            score = 0
            # анимация закрашивания экрана
            for i_rect in grid:
                pygame.draw.rect(tscreen, COLORS[randint(0, 5)], i_rect)
                screen.blit(tscreen, (20, 20))
                pygame.display.flip()
                clock.tick(200)


while True:
    record = get_record()
    dx, rotate = 0, False
    screen.blit(bg, (0, 0))
    screen.blit(tscreen, (20, 20))
    tscreen.blit(game_bg, (0, 0))
    # задержка
    for i in range(lines):
        pygame.time.wait(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                alimit = 100
            elif event.key == pygame.K_UP:
                rotate = True
    move_figure()
    # проверка на заполнение линии
    line = n2 - 1
    lines = 0
    for row in range(n2 - 1, -1, -1):
        count = 0
        for i in range(n1):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < n1:
            line -= 1
        else:
            aspeed += 3
            lines += 1
    # кол-во очков
    score += scores[lines]
    # рисует сетку
    [pygame.draw.rect(tscreen, (40, 40, 40), i_rect, 1) for i_rect in grid]
    # рисует следующую фигуру
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * a, y * a
                pygame.draw.rect(tscreen, col, figure_rect)
    # рисует фигурку
    for i in range(4):
        figure_rect.x = figure[i].x * a
        figure_rect.y = figure[i].y * a
        pygame.draw.rect(tscreen, color, figure_rect)
    # рисует на информационной части следующую фигуру, которая появится
    for i in range(4):
        figure_rect.x = next_figure[i].x * a + 380
        figure_rect.y = next_figure[i].y * a + 185
        pygame.draw.rect(screen, next_color, figure_rect)
    # информация про рекорд, кол-во очков
    screen.blit(title_tetris, (435, -10))
    screen.blit(title_score, (485, 480))
    screen.blit(font.render(str(score), True, pygame.Color('green')), (500, 540))
    screen.blit(title_record, (485, 620))
    screen.blit(font.render(record, True, pygame.Color('purple')), (500, 680))
    # конец игры
    end_game()

    pygame.display.flip()
    clock.tick(FPS)

