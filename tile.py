import pygame as pg

class Tile:
    def __init__(self, size, x, y, color):
        self._size = size
        self._x = x
        self._y = y
        self._color = color

    def draw(self, screen, row, column):
        rect = pg.Rect(self._size * row, self._size * column, self._size, self._size)
        pg.draw.rect(screen, self._color, rect)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, xval):
        self._x = xval

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, yval):
        self._y = yval
