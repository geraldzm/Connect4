from button import Button
import pygame
import time


class InputBox(Button):

    def __init__(self, x, y, width, height, font):
        super().__init__(x, y, width, height)

        self.setIcon(pygame.transform.scale(
            pygame.image.load('inputBox.png'), (width, height)))

        self._font = font
        self.label = self._font.render('Digite el nombre', 1, pygame.Color('black'))
        
        self.focouse = False

        self.text = [] # estas son las letras que ha escrito
        self.txtRender = self._font.render('', 1, (48, 63, 159))
        self._cursor_time = 1

    # E: objeto screen de pygame
    # se hara por frame, se encarga de dibujar en pantalla
    def render(self, screen):
        screen.blit(self._icon, (self._x, self._y))
        screen.blit(self.txtRender, (self._x + 20, self._y + 8))
        screen.blit(self.label, (self._x+150, self._y - 40))

    # E: poitn(x,y)
    # S: boolean
    # D: true si x, y estan dentro de el rectangulo
    def inRect(self, point):
        rs = self._rect.collidepoint(point)
        self.focouse = rs
        return rs

    # se hara por frame, se encarga de la logica (movimientos, ect..)
    def tick(self):
        pass

    # D: si click entonces pasa a este metodo
    def clicked(self):
        self.focouse = True
    
    def tryToWritte(self, event):
        if self.focouse:
            if event.key == 8: #borrar
                self.text = self.text[:-1]
                self.renderLetters()
            elif  64 < event.key < 91 or 96 < event.key < 123: # letra
                if len(self.text) < 25: # maximo letras
                    self.text.append(event.unicode)
                    self.renderLetters()

    # S: String
    # D: retorna el texto escrito
    def getText(self):
        return ''.join(self.text)


    # D: Renderisa las letras para ser mostradas, 
    # esto se hace cuando se modifica el texto
    def renderLetters(self):
        self.txtRender = self._font.render(self.getText(), 1, (48, 63, 159))
    


    # D: Se encarga de hacer la animacion del cursor
    def cursor(self, screen, x, y):

        cursor = pygame.Rect(( x, y, 2, 40))

        start_pos = (x, y)
        end_pos = (x, y + 40)

        time_since = time.time() * 1000.0 - self._cursor_time

        if time_since <= 500:
            pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, 3)

        elif 500 < time_since and time_since <= 1000:
            pygame.draw.line(screen, (0,0,0), start_pos, end_pos, 3)

        else:
            self._cursor_time = time.time() * 1000

