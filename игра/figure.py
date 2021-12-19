import pygame
from random import randint

pygame.init()

class Figure:
    # массив из разных положений фигурок(поворотов)
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = randint(0, 6)
        self.color = randint(1, 6)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]
    # формула по которой определяется поворот
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])