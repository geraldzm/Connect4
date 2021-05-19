import pygame
from button import Button


# estos son los botoens que ponen fichas
class ButtonColumns(Button):
    iconButton = pygame.transform.scale(pygame.image.load('button.png'), (60, 60))
    iconButtonClicked = pygame.transform.scale(pygame.image.load('buttonClicked.png'), (60, 60))

    def __init__(self, x, y, width, height, column, handler):
        super().__init__(x, y, width, height, self.iconButton)

        self._column = column
        self._handler = handler
        self.click = False

    # D: si click entonces pasa a este metodo
    def clicked(self):
        self._handler.displayToken(self._column)
        self.setIcon(self.iconButtonClicked)
        self.click = True

    def riseClick(self):
        self.setIcon(self.iconButton)
        self.click = False

    # se hara por frame, se encarga de la logica (movimientos, ect..)
    def tick(self):
        pass

    # E: boolean
    # D: retorna si el boton esta clickeado
    def isClick(self):
        return self.click