import pygame

from gameObject import GameObject
from tools import clamp, getXPosition, getFallLimit


# esta es la ficha
class Chip(GameObject):
    
    # imagen de ficha roja
    red_icon = pygame.image.load('red.png')
    # imagen de ficha amarilla
    yellow_icon = pygame.image.load('yellow.png')

    # E: 3 numeros enteros, opcionales: 2 boolean
    # constructor de la clase, color: True = Red, False=Yellow
    # row = fila y column = columna NUNCA CAMBIA
    # fall_animation True anima la caida, False no
    def __init__(self, row, column, color=True, fall_animation=True):
        super().__init__(getXPosition(column), row * -80)

        # nunca cambian, son para resetear la posicion
        self._origin_x = getXPosition(column)
        self._origin_y = row * -80

        # variables para el movimiento
        self._fall_limit = getFallLimit(row)
        if not fall_animation:  # para que aparesca en su pocicion sin caer
            self._y = self._fall_limit
        self._fall = False
        self._bound = False
        self._vel = -8
        self._ac = 1.5
        self._row = row
        self._column = column
        self._hasToBounds = True
        self._velMax = 50

        # variables para mostrar en pantalla
        self._display = False
        if color:
            self._icon = self.red_icon
        else:
            self._icon = self.yellow_icon

    # este metodo se llama cada frame
    # se encarga del movimiento de la ficha y su logica
    def tick(self):
        if self._fall:
            self._vel = clamp(self._vel + self._ac, -8, self._velMax)
            self._y += self._vel
            if self._hasToBounds:
                self.boundes()

    def boundes(self):
        if not self._bound and self._y > self._fall_limit:
            self._bound = True
            self._vel *= -1
            self._y = self._fall_limit
        elif self._bound and self._y > self._fall_limit:
            self._y = self._fall_limit
            self._fall = False

    def hasToBounds(self, htb):
        self._hasToBounds = htb


    # E: Objeto screan de pygame
    # este metodo se llama cada frame, se encarga del lo grafico
    # si display = False no se muestra, o si no hay imagen asignada
    def render(self, screen):
        if self._display and self._icon is not None:
            screen.blit(self._icon, (self._x, self._y))

    # S: boolean
    # dice si esta cayendo o no
    def isFalling(self):
        return self._fall

    # S: boolean
    # dice si se esta mostrando en pantalla o no
    def isDisplaying(self):
        return self._display

    # E: boolean
    # para que se comienze a mostrar en pantalla
    def setDisplaying(self, display):
        self._display = display

    # E: boolean
    # para que comience a caer
    def setFalling(self, fall):
        self._fall = fall

    # S: numero
    # retorna el limite de caida en Y
    def getFallingLimit(self):
        return self._fall_limit


    def setAcelerarcion(self, n):
        self._ac = n


    def setVelocidad(self, n):
        self._vel = n


    def setBound(self, bound):
        self._bound = bound


    def setVelMaximo(self, n):
        self._velMax = n


    def setOriginX(self, n):
        self._origin_x = n


    def setOriginY(self, n):
        self._origin_y = n


    def getOriginX(self):
        return self._origin_x


    def getOriginY(self):
        return self._origin_y

    # E: boolean
    # cambia el color de la ficha, True = Red, False=Yellow
    def setColor(self, color):
        if color:
            self._icon = self.red_icon
        else:
            self._icon = self.yellow_icon

    # S: Numero
    # retorna la columna a la que pertenece
    def getColumn(self):
        return self._column

    # S: Numero
    # retorna la fila a la que pertenece
    def getRow(self):
        return self._row

    # D: retorna todo a su estado inicial
    def reset(self):
        self._x = self._origin_x
        self._y = self._origin_y
        self._fall = False
        self._bound = False
        self._display = False
        self._vel = -8
