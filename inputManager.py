import pygame


# se encarga de todos los eventos de mouse y teclado
class InputManager: # NOTA CUANDO COLOCO UNA FICHA CON LOS BOTONES NO SE ESTA GUARDANDO

    # E: objeto TokenSammer
    # constructor
    def __init__(self, menu, handler=None, board=None, numbers=None, fileManager=None, buttons=None, winner=None, ai=None):
        self.exitButton = False  # si True -> el juego se cierra
        self._handler = handler
        self._board = board
        self._numbers = numbers
        self._fileManager = fileManager
        self._buttons = buttons
        self._menu = menu
        self._winner_view = winner
        self.ai = ai
        if self.ai != None:
            self.ai.setInputManager(self)

    # E: un array de con objetos de tipo event
    # se realiza por frame, maneja todos los eventos
    def tick(self, events):
        for event in events:
            # x window, (close window)
            if event.type == pygame.QUIT:
                self.exitButton = True

            # if a key is pressed
            if event.type == pygame.KEYDOWN:  # key pressed
                self._key_pressed(event)
            elif event.type == pygame.KEYUP:  # key released
                self._key_released(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Click
                self.clicked(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.riseClick(event)


    # E: objeto de tipo event
    # si precionan una tecla el evento debe venir aqui
    def clicked(self, event):

        if self._menu.isDisplaying():  # para menu
            self._menu.menuClick(event)

        elif self._board.getWinner() == '-1':  # juego
            for i in self._buttons:
                if i.inRect((pygame.mouse.get_pos())):
                    i.clicked()
                    self._fileManager.saveGame()

        elif self._winner_view.getWinner():
            self._winner_view.click()

    # si se levanta el click
    def riseClick(self, event):
        if self._menu.isDisplaying():  # para menu
            self._menu.menuClickRised(event)
        else: 
            for i in self._buttons:
                if i.isClick():
                    i.riseClick()
                    


    # E: objeto de tipo event
    # si precionan una tecla el evento debe venir aqui
    def _key_pressed(self, event):

        if self._menu.isDisplaying(): # para menu
            self._menu.key_pressed(event)
            return

        if self._board.getWinner() != '-1': # si hay ganador
            # llamar lo del boton para ir a menu principal, o algo asi
            return

        row = {
            pygame.K_0: 0,
            pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 4,
            pygame.K_5: 5,
            pygame.K_6: 6,
        }

        key = row.get(event.key)
        
        if key is not None:
            rs = self._handler.displayToken(key)
            self._fileManager.saveGame()

            if self.ai.getMode() and rs != []:
                self.ai.enemyMove(rs)

            return

        arrow = {
            pygame.K_LEFT: 0,
            pygame.K_UP: 1,
            pygame.K_RIGHT: 2,
            pygame.K_DOWN: 3,
        }

        key = arrow.get(event.key)
        if key is not None:
            self.moveWindow(key)


    def moveWindow(self, n):
        if n == 0:
            self._board.moveIndex(-1)
            self._numbers.moveX(-1)
        elif n == 2:
            self._board.moveIndex(1)
            self._numbers.moveX(1)
        elif n == 1:
            if self._board.moveIndexY(1):
                self._numbers.moveY(1)
        elif n == 3:
            if self._board.moveIndexY(-1):
                self._numbers.moveY(-1)

        self._handler.setBoard(self._board.getBoard())


    # E: objeto de tipo event
    # si precionan una tecla y la sueltan el evento debe venir aqui
    def _key_released(self, event):
        pass
