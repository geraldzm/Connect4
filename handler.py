import pygame

from gameObject import GameObject
from chipGame import Chip


# contiene todas las fichas y todos los objetos que se grafica
# menos el background y el tablero
# maneja las operaciones con fichas y los turnos
class Handler:
    turn = True

    # E: matriz de fichas, lista de objetos tipo GameObject
    # constructor
    def __init__(self, chips, font, sound, board, ai=False, gameObjects=[], turn=True, AIMODE=False): # turno false o amarillo = AI
        self._gameObjects = gameObjects
        self._chips = chips
        self.turn = turn
        self._sound = sound
        self._board = board
        self.ai_mode = AIMODE

        # ficha que indica el turno
        t = Chip(0, 0, turn, False)
        t._x = 750
        t._y = 70
        t.setDisplaying(True)
        self._gameObjects.append(t)

        self._chip_turn = t

        # texto 'Turno:'
        self._font = font
        turnText = font.render("Turno: ", 1, pygame.Color('coral'))
        self._title = GameObject(750, 20, turnText)
        self._gameObjects.append(self._title)

    # se realiza por frame
    # recorre todos los objetos GameObject y tokens
    # llama a su respectivo metodo tick()
    def tick(self):
        
        for i in self._gameObjects:
            i.tick()
            
        for row in self._chips:
            for column in row:
                column.tick()

    # E: un objeto screen de pygame
    # se realiza por frame
    # recorre todos los objetos GameObject y tokens
    # llama a su respectivo metodo render()
    def render(self, screen):
        for i in self._gameObjects:
            i.render(screen)
        for row in self._chips:
            for column in row:
                column.render(screen)

    # E: lista de objetos GameObject
    # agrega a la lista todos los objetos en gameObjects
    def addGameObjects(self, gameObjects):
        for i in gameObjects:
            self._gameObjects.append(i)

    # E: objeto GameObjet
    # agrega un objeto a la lista
    def addGameObject(self, gameObject):
        self._gameObjects.append(gameObject)

    # E: un GameObject
    # remueve el objeto de la lista
    def removeGameObject(self, gameObject):
        self._gameObjects.remove(gameObject)

    # D: limplia la lista de GameObjects
    def clear(self):
        self._gameObjects.clear()

    # S: boolean
    # D: retorna el turno, True=rojo, False=Amarillo
    def getTurn(self):
        return self.turn

    # E: 1 integers
    # S: lista
    # D: coloca una ficha en esa columna si las filas no estan llenas
    # cambia el estado de la ficha turno
    # [row, column, rowScreen(0-5)] si la puso, [] si no
    def displayToken(self, column):
        row_column = self._board.canAddChip(column)  # verificamos columna

        if row_column == []:  # no se puede agregar en esa columna
            if not self.ai_mode:
                self._sound.playSound('hit')
            return -1

        # se agrega al tablero
        value = '1' if self.turn else '0'
        self._board.addChip(value, row_column[0], row_column[1])

        # se configura la ficha para ser mostrada en pantalla
        self.setUpToDisplay(row_column[2], column)

        # cambia color de la 'ficha turno'
        self.turn = not self.turn

        self._chip_turn.setColor(self.turn)
        
        return row_column

    # E: una matriz 6x7
    # D: recorre toda la matriz si 1=rojo, pone una ficha ahi, 0=amarillo, -= ninguna
    def setBoard(self, mtz):
        self.resetChips()  # reiniciamos todas las fichas

        for row in range(len(mtz)):
            for column in range(len(mtz[row])):
                if mtz[row][column] != '-':
                    chip = self._chips[row][column]
                    chip.setColor(mtz[row][column] == '1')
                    chip.setDisplaying(True)
                    chip.setFalling(True)
                    chip.setY(chip.getFallingLimit())

    # recore todas las fichas y las resetea
    def resetChips(self):
        for row in self._chips:
            for column in row:
                column.reset()

    # E: 2 integers
    # D: configura la ficha para comenzar a ser mostrada en pantalla y que comience a caer
    def setUpToDisplay(self, row, column):
        chip = self._chips[row][column]
        chip.setColor(self.turn)
        chip.setDisplaying(True)
        chip.setFalling(True)

