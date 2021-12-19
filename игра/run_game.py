from pygame.draw import *
from tetris import *
from parametry import *
import Sounds
import Img
import Font as f
from button import *
from tetris import *
from states import *
import menu

fps = 60
game = Tetris(18, 10)
game_state = GameState()
counter = 0
pressing_down = False

def start():
    global pause
    while True:
        if game_state.check(State.MENU):
            menu.show_menu()
        elif game_state.check(State.START):
            choose_level()
            chose_music()
            pygame.mixer.music.play(-1)
            choose_theme()
            run_game()
        elif game_state.check(State.QUIT):
            break

def choose_theme():
    theme1 = Button(300, 70)
    theme2 = Button(300, 70)
    theme3 = Button(300, 70)
    theme4 = Button(300, 70)
    theme5 = Button(300, 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.set_caption("Выбор фона")
        screen.blit(Img.themeimage, (0, 0))

        if theme1.draw(70, 50, title_theme1):
            Img.set_theme(1)
            return
        if theme2.draw(70, 200, title_theme2):
            Img.set_theme(2)
            return
        if theme3.draw(70, 350, title_theme3):
            Img.set_theme(3)
            return
        if theme4.draw(70, 500, title_theme4):
            Img.set_theme(4)
            pygame.mixer.music.play(-1)
            return
        if theme5.draw(70, 650, title_theme5):
            Img.set_theme(5)
            return

        pygame.display.update()
        clock.tick(60)

def choose_level():
    global level
    level1 = Button(300, 70)
    level2 = Button(300, 70)
    level3 = Button(300, 70)
    level4 = Button(300, 70)
    level5 = Button(300, 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.set_caption("Выбор уровня")
        screen.blit(Img.levelimage, (0, 0))

        if level1.draw(70, 100, title_level1):
            level = 1
            return
        if level2.draw(70, 200, title_level2):
            level = 2
            return
        if level3.draw(70, 300, title_level3):
            level = 3
            return
        if level4.draw(70, 400, title_level4):
            level = 4
            return
        if level5.draw(70, 500, title_level5):
            level = 5
            return

        pygame.display.update()
        clock.tick(60)

def chose_music():
    global level
    music1 = Button(300, 70)
    music2 = Button(300, 70)
    music3 = Button(300, 70)
    music4 = Button(300, 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.set_caption("Выбор музыки")
        screen.blit(Img.soundimage, (0, 0))

        if music1.draw(70, 100, title_music1):
            Sounds.set_sound(1)
            return
        if music2.draw(70, 200, title_music2):
            Sounds.set_sound(2)
            return
        if music3.draw(70, 300, title_music3):
            Sounds.set_sound(3)
            return
        if music4.draw(70, 400, title_music4):
            Sounds.set_sound(4)
            return

        pygame.display.update()
        clock.tick(60)



def paused():
    global pause
    pause = True
    resume_button = Button(260, 100)
    quit_button = Button(200, 100)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.set_caption("Пауза")
        screen.blit(Img.bg_menu, (0, 0))
        resume_button.draw(250, 250, title_resume, "resume")
        quit_button.draw(250, 500, title_quit, exit)

        pygame.display.update()
        clock.tick(15)


def run_game():
    global level
    rgame = True
    pause_button = Button(100, 50)
    global counter, pressing_down
    while rgame:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // level // 2) == 0 or pressing_down:
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
        pygame.display.set_caption("Tetris")
        screen.blit(Img.bckg, (0, 0))
        # рисует кнопку паузу
        pause_button.draw(485, 280, title_pause, paused)
        # рисует сетку
        for i in range(game.n2):
            for j in range(game.n1):
                rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    rect(screen, colors[game.field[i][j]],
                         [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                          game.zoom - 1])

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

        if game.state == "gameover":
            screen.blit(Img.bg_end, (0, 0))



        pygame.display.flip()
        clock.tick(fps)