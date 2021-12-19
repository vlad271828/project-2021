import pygame
import Font as f

pygame.init()

size = (700, 800)  # размер общего экрана
end_size = (1126, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
title_tetris = f.main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = f.font.render('score:', True, pygame.Color('green'))
title_record = f.font.render('record:', True, pygame.Color('purple'))
title_pause = f.button_font.render('pause', True, pygame.Color('black'))
title_start = f.main_font.render('start', True, pygame.Color('black'))
title_quit = f.main_font.render('quit', True, pygame.Color('black'))
title_restart = f.main_font.render('restart', True, pygame.Color('black'))


BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
colors = [BLACK, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]