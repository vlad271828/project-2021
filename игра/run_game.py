from pygame.draw import *
from tetris import *
from parametry import *
import Sounds
import Img
import Font as f
from button import *
import loose

fps = 60
game = Tetris(18, 10)
pygame.mixer.music.play(-1)
counter = 0
pressing_down = False

def run_game():
    rgame = True
    pause_button = Button(100, 50)
    global counter, pressing_down
    while rgame:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(18, 10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False
        # фон главного экрана
        screen.blit(Img.bg, (0, 0))
        # рисует сетку
        for i in range(game.n2):
            for j in range(game.n1):
                rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    rect(screen, colors[game.field[i][j]],
                         [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                          game.zoom - 1])
        # рисует кнопку паузу
        pause_button.draw(485, 280, title_pause)

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        rect(screen, colors[game.figure.color],
                             [game.x + game.zoom * (j + game.figure.x) + 1,
                              game.y + game.zoom * (i + game.figure.y) + 1,

                              game.zoom - 2, game.zoom - 2])

        screen.blit(title_tetris, (435, -10))
        screen.blit(title_score, (485, 70))
        screen.blit(f.font.render(str(game.score), True, pygame.Color('green')), (500, 130))
        screen.blit(title_record, (485, 190))

        if game.state == "gameover":
            loose.show_loose()


        pygame.display.flip()
        clock.tick(fps)