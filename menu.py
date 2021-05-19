from gameObject import GameObject
from rain import Rain
from buttonMenu import ButtonMenu
import pygame
from os import listdir
from os.path import isfile, join
from inputBox import InputBox
from tools import getImageByName


class Menu(GameObject):

    mainMenuBackground = pygame.transform.scale(pygame.image.load('clouds.png'), (840, 730))

    # ---- main menu ----------
    buttonsMain = []

    # ---- request name ------
    boxes = []

    def __init__(self, fl, game, score):
        super().__init__(0, 0)

        
        self.displaying = False

        # rain
        self.rain = Rain(37)
        self.rain.show()
        
        # modos
        self.mainMenu = True
        self.namesMenu = False
        self.scoreMenu = False

        self.font = pygame.font.SysFont("Purisa", 25)
        self.fileManager = fl
        self.game = game
        self.score = score

        self.buttonsNames = []

        # Crea los objetos button del menu principla
        self.instanseButtonsMainMenu()

    # Tick de cada dia
    def tick(self):
        self.rain.tick()

        if self.mainMenu: # main menu

            self.mainMenuTick()

        elif self.namesMenu: # inputn names menu

            self.namesMenuTick()
            self.backMenuButton.tick()
            self.startMenuButton.tick()

        elif self.scoreMenu: # score menu

            self.backMenuButton.tick()


    # E: objeto screen
    # D: Muestra en pantalla todo lo correspondiente

    def render(self, screen):
        screen.blit(self.mainMenuBackground, (0, 0))
        self.rain.render(screen)

        if self.mainMenu:
            
            self.mainMenuRender(screen)

        elif self.namesMenu:
            self.namesMenuRender(screen)
            self.backMenuButton.render(screen)
            self.startMenuButton.render(screen)
        elif self.scoreMenu:
            self.renderScores(screen)
            self.backMenuButton.render(screen)


    # S: Boolean
    # If true entoces el menu esta mostrandoce o esta activo
    def isDisplaying(self):
        return self.displaying

    # E: evento click
    # D: se llama a este evento cada vez que se hace un click
    # y que displaying sea true

    def menuClick(self, event):

        if self.mainMenu:
            self.buttonsEvents(self.buttonsMain, event)

        elif self.namesMenu:
            self.buttonsEvents(self.buttonsNames +
                               [self.backMenuButton, self.startMenuButton], event)

        elif self.scoreMenu:
            self.buttonsEvents([self.backMenuButton], event)

    # E: evento click
    # D: se llama a este evento cada vez que el click se levanta
    # y que displaying sea true

    def menuClickRised(self, event):
        pass

    # E: evento teclado
    # D: se llama a este evento cada vez se presiona una tecla
    # y que displaying sea true
    def key_pressed(self, event):
        if self.namesMenu:
            for i in self.buttonsNames:
                i.tryToWritte(event)

    # Muestra todos lo del main menu
    def mainMenuRender(self, screen):
        for i in self.buttonsMain:
            i.render(screen)

    # Muestra todos lo del main menu
    def namesMenuRender(self, screen):
        for i in self.buttonsNames:
            i.render(screen)

    def renderScores(self, screen):
        for i in self.socresGameObjects:
            i.render(screen)

    # EL tick de cada dia del main menu
    def mainMenuTick(self):
        for i in self.buttonsMain:
            i.tick()

    # EL tick de cada dia del main menu
    def namesMenuTick(self):
        for i in self.buttonsNames:
            i.tick()

    # D: si boton PVP start PVP mode
    def startPVP(self):
        self.buttonsNames = [InputBox(
            420-250, 375-50-100, 500, 50, self.font), InputBox(420-250, 375-50+50, 500, 50, self.font)]
        self.setNameMenu()

    # D: si boton PVP start PVP mode
    def startPVI(self):
        # PREGUNTAR NOMBRE DE  1 PERSONA
        #self.displaying = False
        self.buttonsNames = [InputBox(420-250, 375-50, 500, 50, self.font)]
        self.setNameMenu()

        print('PVI mode, working on it....')

    # D: Pone el menu en modo score
    def showScore(self):
        self.setScoreMenu()
        self.socresGameObjects = self.score.getTop10()

    # D: Cargar juego previo
    def loadGame(self):
        f = self.fileManager.askForFile()

        if f != '-1':
            self.game.loadGame(f)
            self.displaying = False

    # D: boton continue despues de poner los nombres
    # sirve para los 2 modos
    def startGame(self):
        
        if self.buttonsNames[0].getText().strip() == '':
            return

        self.fileManager.setNamePlayer1(self.buttonsNames[0].getText())

        if len(self.buttonsNames) == 2:
            if self.buttonsNames[1].getText() == '':
                return
            self.fileManager.setNamePlayer2(self.buttonsNames[1].getText())     


        self.fileManager.updateFileName()
        self.game.startNewGame()
        self.displaying = False


    # D: Pone el menu en modo score
    def backMainMenu(self):
        self.fileManager.resetNames()
        self.mainMenu = True
        self.namesMenu = False
        self.scoreMenu = False
        self.displaying = True

    # Crea todos los botones del menu principal

    def instanseButtonsMainMenu(self):

        def m(m): return m.startPVP()  # PVP mode
        def m2(m): return m.startPVI()  # PVI mode
        def m3(m): return m.showScore()  # score mode
        def m4(m): return m.loadGame()  # Load Game mode
        def m5(m): return m.backMainMenu()  # back to main menu
        def m6(m): return m.startGame()  # start the game
        
        self.buttonsMain.append(ButtonMenu(
            420 - 100, 150, 200, 50, 'PVP', m, self, getImageByName('pvpB'), getImageByName('pvpW')))  # PVP

        self.buttonsMain.append(ButtonMenu(
            420 - 100, 250, 200, 50, 'PVI', m2, self, getImageByName('pviB'), getImageByName('pviW')))  # PVI

        self.buttonsMain.append(ButtonMenu(
            420 - 100, 350, 200, 50, 'Score', m3, self, getImageByName('scoreB'), getImageByName('scoreW')))  # score

        self.buttonsMain.append(ButtonMenu(
            420 - 100, 450, 200, 50, 'Load', m4, self, getImageByName('loadB'), getImageByName('loadW')))  # load

        self.backMenuButton = ButtonMenu(
            40, 670, 200, 50, 'Back', m5, self, getImageByName('backB'), getImageByName('backW'))
        
        self.startMenuButton = ButtonMenu(
            600, 670, 200, 50, 'Start', m6, self, getImageByName('startB'), getImageByName('startW'))

    

    # D: activa la vista de names
    def setNameMenu(self):
        self.namesMenu = True
        self.mainMenu = False
        self.scoreMenu = False

    # D: activa la vista de score
    def setScoreMenu(self):
        self.scoreMenu= True
        self.mainMenu = False
        self.namesMenu = False

    # E: una lista de objetos tipo Button
    # D: recorre toda la lista y pregunta si alguno
    # ha sido clickeado
    def buttonsEvents(self, buttons, event):
        for i in buttons:
            if i.inRect(pygame.mouse.get_pos()):
                i.clicked()


  
