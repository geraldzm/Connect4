# esta clase sera la encargada de dibujar los numeros ademas de navegar entre ellos
import pygame

from gameObject import GameObject


class Numbers:

    # define la posicion de las filas de numeros y el espacio entre cada numero
    def __init__(self, Xx, Xy, Yx, Yy, spacex, spacey, font, xStart=0, yStart=0):
        self._x_x = Xx
        self._x_y = Xy
        self._y_x = Yx
        self._y_y = Yy
        self._spacex = spacex
        self._spacey = spacey
        self._font = font

        # crea lista logica de x eje: [0, 1, 2, 3, 4, 5, 6]
        self._x = []
        for i in range(xStart, xStart+7):
            self._x.append(i)

        # crea lista logica de y eje: [0, 1, 2, 3, 4, 5]
        self._y = []
        for i in range(yStart, yStart + 6):
            self._y.append(i)

        # se crean 2 listas de GameObject que reprecentan los Xs y Ys a ser graficados
        self._x_numbers = self.createNumbers(self._x, Xx, Xy, spacex, 0)
        self._y_numbers = self.createNumbers(self._y, Yx, Yy, 0, spacey)

    # E: objeto screen de pygame
    # dibuja todos los numeros
    def render(self, screen):
        for i in (self._x_numbers + self._y_numbers):
            i.render(screen)

    # S: lista de numeros
    # retorna la lista de numeros que se muestra en x
    def getXs(self):
        return self._x

    # S: lista de numeros
    # retorna la lista de numeros que se muestra en y
    def getYs(self):
        return self._y

    # E: un numero entero
    # mueve todas las x, 7 * n veces
    def moveX(self, n):
        for i in range(len(self._x)):
            self._x[i] = self._x[i] + 7 * n
        self._x_numbers = self.createNumbers(self._x, self._x_x, self._x_y, self._spacex, 0)

    # E: un numero entero
    # mueve todas las y, 7 * n veces
    def moveY(self, n):
        for i in range(len(self._y)):
            self._y[i] = self._y[i] + 7 * n
            
        self._y_numbers = self.createNumbers(self._y, self._y_x, self._y_y, 0, self._spacey)

    # E: lista de numeros, 4 numeors
    # S: una lista de GameObject
    # cada GameObject reprecenta uno de los numeros en la lista
    # X reprecenta la posicion en x del primer numero, los siguientes se le sumara el spacex
    # igual con y
    def createNumbers(self, ls, x, y, spacex, spacey):
        rs = []
        for i in range(len(ls)):
            txt = self._font.render(str(ls[i]), 1, pygame.Color('black'))
            gameObject = GameObject(x + spacex * i, y + spacey * i, txt)
            rs.append(gameObject)
        return rs
