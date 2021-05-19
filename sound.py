import pygame


# Esta clase se encarga de reproduccir todos los sonidos
class Sound:

    # constructor, crea un diccionario con todos los sonidos del juego
    def __init__(self):
        self._sounds = {'hit': pygame.mixer.Sound('Micrhit.wav'), 'win': pygame.mixer.Sound('YouWin.wav')}

    # E: sting
    # reproduce el sonido en el diccionario con la clave key
    def playSound(self, key):
        s = self._sounds.get(key)
        if s is not None:
            s.play()
