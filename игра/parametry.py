import pygame
import Font as f

pygame.init()

size = (700, 800)  # размер общего экрана
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
title_tetris = f.main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = f.font.render('score:', True, pygame.Color('green'))
title_pause = f.button_font.render('pause', True, pygame.Color('black'))
title_start = f.main_font.render('start', True, pygame.Color('black'))
title_quit = f.main_font.render('quit', True, pygame.Color('black'))
title_restart = f.main_font.render('restart', True, pygame.Color('black'))
title_resume = f.main_font.render('resume', True, pygame.Color('black'))
title_theme1 = f.button_font.render('BLUE SPACE', True, pygame.Color('black'))
title_theme2 = f.button_font.render('BLACK SPACE', True, pygame.Color('black'))
title_theme3 = f.button_font.render('NATURE', True, pygame.Color('black'))
title_theme4 = f.button_font.render('CAT', True, pygame.Color('black'))
title_theme5 = f.button_font.render('GAMEBOY', True, pygame.Color('black'))
title_level1 = f.button_font.render('level 1', True, pygame.Color('purple'))
title_level2 = f.button_font.render('level 2', True, pygame.Color('purple'))
title_level3 = f.button_font.render('level 3', True, pygame.Color('purple'))
title_level4 = f.button_font.render('level 4', True, pygame.Color('purple'))
title_level5 = f.button_font.render('level 5', True, pygame.Color('purple'))
title_music1 = f.button_font.render('Korobeiniki', True, pygame.Color('purple'))
title_music2 = f.button_font.render('guitar 8bit', True, pygame.Color('purple'))
title_music3 = f.button_font.render('8bit', True, pygame.Color('purple'))
title_music4 = f.button_font.render('soundless', True, pygame.Color('purple'))



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