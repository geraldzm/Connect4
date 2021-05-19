import pygame

from gameBoard import GameBoard
from inputManager import InputManager
from handler import Handler
from numeration import Numbers
from sound import Sound
from chipGame import Chip
from fileManager import FileManager
from button import Button
from buttonColumns import ButtonColumns
from menu import Menu
from tools import getGame
from ai import AI
from winnerView import WinnerWiew
from score import Score

# S: una matriz de 6 x 7
# crea la matriz con las 46 fichas, todas son rojas por defecto
def getMatrixChips():
    mtz = []
    row = []
    for i in range(6):
        for j in range(7):
            row.append(Chip(i, j))
        mtz.append(row)
        row = []
    return mtz

# S: lista con 6 buttons
def getButtons(handler):
    rs = []
    for i in range(7):
        rs.append(ButtonColumns(150 + 80 * i, 630, 60, 60, i, handler))
    return rs

# inicio letras:
class Game:

    # E: objeto clock, screen y front de pygame
    # constructor del juego
    def __init__(self, clock, screen, font):
        self._clock = clock
        self._screen = screen  # 840, 630 window size
        self._font = font

        self._sound = Sound()
        self._fileManager = FileManager()
        
        self.score = Score(self._fileManager)
        self._menu = Menu(self._fileManager, self, self.score)
        self.winnerWiew = WinnerWiew(self._menu, self, self.score, self._fileManager)
        self._menu.displaying = True
        self._keyInput = InputManager(self._menu)

        self.ai = AI()
        self.setAIMode(False)
        
        
        self._icon_table = pygame.image.load('background.png')  # 576 x 476, fichas 68

    # D: pone el juego en AI mode
    def setAIMode(self, bool):
        self.ai_mode = bool
        self.ai.setMode(bool)

    # S: un objeto de tipo pygame.Surface
    # retorna un objeto que se puede mostrar en pantalla
    # con el numero de fps
    def fps(self):
        frameRate = str(int(self._clock.get_fps()))
        frameRateText = self._font.render(frameRate, 1, pygame.Color('coral'))
        return frameRateText


    # se llama por frame, se encarga de graficar en pantalla
    def render(self):

        if not self._menu.displaying:
            self._screen.fill((253, 235, 208))
            self._handler.render(self._screen)
            self._numeration.render(self._screen)
            self._screen.blit(self._icon_table, (132, 154))
            self.winnerWiew.render(self._screen)
        else:
            self._menu.render(self._screen)

        self._screen.blit(self.fps(), (10, 0))

    # se llama por frame, se encarga de la logica
    def tick(self):
        self._keyInput.tick(pygame.event.get())

        if not self._menu.displaying:
            self._handler.tick()

            if self.ai_mode and not self._handler.getTurn(): # si es turno de AI pedir ficha
                self.ai_turn_request()
            
            self.winnerWiew.tick()
        else:
            self._menu.tick()

    # loop siempre y cuando no hayan precionado la X de la ventana
    def run(self):
        while not self._keyInput.exitButton:
            self.render()
            self.tick()
            self._clock.tick(30)
            pygame.display.update()


    # D: comienza un nuevo juego
    def startNewGame(self):

        self._gameBoard = GameBoard(self._sound)  # LOAD GAME
        
        mtz = getMatrixChips()  # matriz con 46 fichas rojas
        self._handler = Handler(mtz, self._font, self._sound, self._gameBoard)

        if self._fileManager.getNamePlayer2() == 'AI': # enviar modo a AI
            self.setAIMode(True)
        else:
            self.setAIMode(False)

        self.initiateGameGeneralThings()  # inicializa los demas objetos necesarios

    # D: carga un nuevo juego
    def loadGame(self, fileName):

        ls = getGame(fileName)  # Recupera archivo
        self._gameBoard = GameBoard(self._sound, ls[:2])  # LOAD GAME

        mtz = getMatrixChips()  # matriz con 46 fichas rojas
        self._handler = Handler(mtz, self._font, self._sound, self._gameBoard, turn=ls[2])

        self._fileManager.setFileName(fileName)

        self._fileManager.setNamePlayer1(ls[3])
        self._fileManager.setNamePlayer2(ls[4])

        if ls[4] == 'AI': # enviar modo a AI
            self.setAIMode(True)


        self.initiateGameGeneralThings()  # inicializa los demas objetos necesarios

    # D: inicializa las cosas que tienen en comum el loadGame y el newGame
    def initiateGameGeneralThings(self):
        buttons = getButtons(self._handler)

        self._numeration = Numbers(175, 120, 95, 565, 80, -75, self._font)

        self._fileManager.setHandler(self._handler)
        self._fileManager.setGameBoard(self._gameBoard)

        for i in buttons:  # agrega los todos los bototnes
            self._handler.addGameObject(i)

        self._handler.setBoard(self._gameBoard.getBoard())
        self.winnerWiew.setBoard(self._gameBoard)

        if self.ai_mode:
            self.ai.setBoard(self._gameBoard)

        self._keyInput = InputManager(self._menu, self._handler, self._gameBoard, self._numeration, self._fileManager, buttons, self.winnerWiew, self.ai)
        
        self.winnerWiew.checkWinnerLoad()

        


    def ai_turn_request(self):
        coloumn = self.ai.getMove()
        print(coloumn)
        self._handler.displayToken(coloumn)