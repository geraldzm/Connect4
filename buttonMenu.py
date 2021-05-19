from button import Button
import pygame


class ButtonMenu(Button):

    balckBox = pygame.image.load('balckbox.png')
    whiteBox = pygame.image.load('whitebox.png')


    def __init__(self, x, y, width, height, title, lamb, menu, bTxt, wTxt, icon=None):
        super().__init__(x, y, width, height, wTxt)
        self._title = title
        self.lamb = lamb
        self.menu = menu

        self.blackTxt = bTxt
        self.whiteTxt = wTxt

        self.box = self.balckBox

    # D: solo llamar si inRect is true

    def clicked(self):
        self.lamb(self.menu)

   
  # E: objeto screen de pygame
  # se hara por frame, se encarga de dibujar en pantalla
    def render(self, screen):
        screen.blit(self.box, (self._x, self._y))
        screen.blit(self._icon, (self._x, self._y))
        

    # if mouse over button cambia color
    def tick(self):
        if self.inRect(pygame.mouse.get_pos()):
            self.box = self.whiteBox
            self.setIcon(self.blackTxt)
        else:
            self.box = self.balckBox
            self.setIcon(self.whiteTxt)

    def setTextAndColor(self, txt, color):
        self.setIcon(self.font.render(txt, 1, color))