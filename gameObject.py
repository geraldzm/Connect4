# Todos los objetos que se muestren en pantalla seran de este tipo
class GameObject:

    # E: 2 numeros reales, objeto de tipo pygame.Surface
    # constructor, icon sera lo que grafique
    def __init__(self, x, y, icon=None):
        self._x = x
        self._y = y
        self._icon = icon

    # S: numero
    # retorna la posicion en x de este objeto
    def getX(self):
        return self._x

    # S: numero
    # retorna la posicion en y de este objeto
    def getY(self):
        return self._y

    # E: numero real
    # posicion en x de este objeto = x
    def setX(self, x):
        self._x = x

    # E: numero real
    # posicion en y de este objeto = y
    def setY(self, y):
        self._y = y

    # E: objeto de tipo pygame.Surface
    # setea el icon
    def setIcon(self, icon):
        self._icon = icon

    # E: objeto screen de pygame
    # se hara por frame, se encarga de dibujar en pantalla
    def render(self, screen):
        if self._icon is not None:
            screen.blit(self._icon, (self._x, self._y))

    # se hara por frame, se encarga de la logica (movimientos, ect..)
    def tick(self):
        pass
