from tools import save
import tkinter as tk
from tkinter import filedialog
from tools import getTime

class FileManager:

    def __init__(self, handler=None, gameBoard=None, file='new'):
        self._handler = handler
        self._gameBoard = gameBoard

        self._gameMode = True # True = PVP, Flase = PVI
        self.resetNames()

        self._file = file
        self._socreFile = 'score.sc'        

    # D: guarda el juego en el archivo
    def saveGame(self):
        if self._gameBoard == None:
            return

        ls = self._gameBoard.getMatrixGuardar()

        ls.append(self._handler.getTurn())
        ls.append(self._player1)
        ls.append(self._player2)

        save(self._file, str(ls))


    # S: string con la direccion de una archivo
    # D: retorna la direccion de un archivo en forma de string, '-1' si cancelar
    def askForFile(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfile()

        if file_path == None:
            return '-1'
            
        return file_path.name

    # E: GameBoard
    # D: settea el board que se guarda 
    def setGameBoard(self, board):
        self._gameBoard = board

    # E: GameBoard
    # D: settea el board que se guarda 
    def setHandler(self, handler):
        self._handler = handler

    # E: string
    # D: establece el nombre del player 1
    def setNamePlayer1(self, name):
        self._player1 = name

    # E: string
    # D: establece el nombre del player 2
    def setNamePlayer2(self, name):
        self._player2 = name

    # S: string
    # D: retorna el nombre del player 2
    def getNamePlayer1(self):
        return self._player1

    # S: string
    # D: retorna el nombre del player 2
    def getNamePlayer2(self):
        return self._player2
        
    # D: actualiza el nombre de la funcion
    def updateFileName(self):
        self._file = self.generateFileName()

    # D: reinicia los nombres a los genericos
    def resetNames(self):
        self._player1 = 'player1'
        self._player2 = 'AI'

    # S: string
    # D: genera un nombre para el archivo
    def generateFileName(self):
        return 'games/'+self._player1+'vs'+self._player2+getTime()+'.game'


    # E: string
    # D: establece el nombre del file que cargo
    def setFileName(self, name):
        self._file = name

    # E: String
    # S: lista
    # D: retorna el los scores almacenados
    def getFileScores(self, name):
        result = []
        try:
            file = open(name, "r")
            result = eval(file.read())
            file.close()
        finally:
            if type(result) != list:
                return []
            return result
