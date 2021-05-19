
from buttonMenu import ButtonMenu
from tools import getImageByName
import pygame
from gameObject import GameObject

class WinnerWiew:

    def __init__(self, menu, game, score, fl):
        self.menu = menu
        self.game = game
        self.winner = False
        self.playerWinner = '-1'
        self.fileManager = fl
        self.setUpImageDimensions()
        self.socre = score


        def m5(m): return m.backMainMenu()  # back to main menu
        self.backMenuButton = ButtonMenu(420-100, 500, 200, 50, 'Back', m5, self.menu, getImageByName('backB'), getImageByName('backW'))
        
        

     # E: objeto screen de pygame
    # se hara por frame, se encarga de dibujar en pantalla
    def render(self, screen):
        if self.winner:
            self.backMenuButton.render(screen)
            self.winnerImage.render(screen)

    # se hara por frame, se encarga de la logica (movimientos, ect..)
    def tick(self):
        
        if self.winner:
            self.backMenuButton.tick()
            if self.logoSize < 600:
                self.logoSize += 40
                self.winnerImage.setX(420-(self.logoSize/2))
                self.winnerImage.setY(300 - int(self.logoSize*0.75/2) )
                self.winnerImage.setIcon(pygame.transform.scale(getImageByName('winnerLogo'), (self.logoSize, int(self.logoSize*0.5625))))
        else:
            self.checkWinner()


    # E: evento teclado
    # D: se llama a este evento cada vez se presiona una tecla
    # y que displaying sea true
    def click(self):
        if self.backMenuButton.inRect(pygame.mouse.get_pos()):
            self.backMenuButton.clicked()
            self.winner = False
            self.playerWinner = '-1'
            self.setUpImageDimensions()
    
    # S: boolean
    # D: retorna si hay un winner
    def getWinner(self):
        return self.winner

    # E: objeto board
    def setBoard(self, board):
        self.board = board

    # D: pregunta al board si hay un ganador
    def checkWinner(self):
        if not self.winner and self.board != None:
            if self.board.getWinner() != '-1':
                self.winner = True
                if self.board.getWinner() == '1':
                    self.socre.addToScore(self.fileManager.getNamePlayer1(), 1)
                else:
                    self.socre.addToScore(self.fileManager.getNamePlayer2(), 1)
               
    # D: se llama cada vez que se carga una partida 
    def checkWinnerLoad(self):
        if not self.winner and self.board != None:
            if self.board.verifyWinner() != '-1':
                self.winner = True


    def setUpImageDimensions(self):
        self.logoSize = 50
        self.winnerImage = GameObject(420-25, 300, pygame.transform.scale(getImageByName('winnerLogo'), (self.logoSize, int(self.logoSize*0.5625))))
        