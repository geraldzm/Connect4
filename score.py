from gameObject import GameObject
import pygame
from tools import save

# Maneja todos los scores
class Score:

    # E: lista de score [name, score] # agregar el score
    def __init__(self, fileManager):
        self._font = pygame.font.SysFont("Purisa", 35)
        
        self.fileManager = fileManager
        self.updateScore()

    # S: lista
    # D: retorna los scores
    def getScore(self):
        return self.score 

    # S: lista de GameObjects
    # D: retorna una lista de letras para renderisar
    def getTop10(self):
        self.updateScore() # actualizamos los puntajes

        color = (0,0,0)
        title = 'Posicion       nombre      puntaje'

        x, y = self._font.size(title)
        rs = []
        rs.append(GameObject(420 - x / 2, y-20, self._font.render(title, 1, color) )) # titulo


        for i in range(len(self.score)):
                        
            txt = f'{self.score[i][0]}'
            x, y = self._font.size(txt)

            rs.append(GameObject(100, 100+y*i, self._font.render(f'#{i+1}', 1, color)) ) # numero
            rs.append(GameObject(420 - x / 2, 100+y*i, self._font.render(txt, 1, color) )) # nombre
            rs.append(GameObject(700, 100+y*i, self._font.render(f'{self.score[i][1]}', 1, color) )) # Puntaje

            if i == 9:
                return rs 
            
        return rs 


    # actualizaoms los puntajes
    def updateScore(self):
        self.score = self.sortList(self.fileManager.getFileScores('games/scores.game'))

    # E: string, ints
    # D: actualiza el score con estos datos
    def addToScore(self, name, pts):
        for i in range(len(self.score)):
            if self.score[i][0].upper().strip() == name.upper().strip():
                print('es igual a', name)
                self.score[i][1] += pts
                break
        else:
            self.score.append([name, pts]) 

        self.saveScore()

    # D: guarda el score en el archivo
    def saveScore(self):
        save('games/scores.game', str(self.score))


    # D: ordena la lista de scores de mayor a menor
    def sortList(self, lista):

        #caso base
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]

            #llamada recursiva
            izquierda = self.sortList(izquierda)
            derecha = self.sortList(derecha)

            #iteradores para recorrer las dos sublistas
            i = 0
            j = 0

            #Iterador para la lista principal
            k = 0

            while i < len(izquierda) and j < len(derecha): # mientras podamos seguir comparando
                if izquierda[i][1] > derecha[j][1]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k+= 1

            #copiar los pedazos de las listas que quedaron
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i+=1
                k += 1

            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1

        return lista