from gameObject import GameObject
from pygame import Rect


# Maneja todos los botones
class Button(GameObject):

    def __init__(self, x, y, width, height, icon=None):
        super().__init__(x, y, icon)
        self._rect = Rect(x, y, width, height)
        self.width = width
        self.height = height


    # E: poitn(x,y)
    # S: boolean
    # D: true si x, y estan dentro de el rectangulo
    def inRect(self, point):
        return self._rect.collidepoint(point)

    # D: si click entonces pasa a este metodo
    def clicked(self):
        pass

    # S: Rect
    # D: retorna el rectangulo que compone el boton
    def getRect(self):
        return self._rect
