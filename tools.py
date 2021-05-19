import datetime
import pygame
# E: 3 numeros
# S: un numero
# retorna un numero entre [min, max]
def clamp(n, min, max):
    if n < min:
        return min
    if n > max:
        return max
    return n

# E: numero entero positivo
# S: numero
# retorna la posicion que debe tomar en x para estar en esa columna
def getXPosition(column):
    return 147 + column * (68 + 12)


# E: 2 numeros
# S: un numero
# calcula hasta donde tiene que caer una ficha de acuerdo con su fila
def getFallLimit(row):
    return 630 - 15 - 68 - row * 76


# E: nombre del archivo, string
# S:
# Crear un archivo, sobrescribe si ya existe y guarda el string qu
def save(name, strValue):
    file = open(name, 'w')
    file.write(strValue)
    file.close()


# E: un string
# S: una lista
# carga el archivo en una lista, si hay algun problema devuelve []
def getGame(name):
    result = []
    try:
        file = open(name, "r")
        result = eval(file.read())
        file.close()
    finally:
        if type(result) != list:
            return []
        return result

def noZero(n):
    if n == 0:
        return 1
    return n

# S: string
# retorna yyy-mm-dd hh:mm:ss
def getTime():
    return str(datetime.datetime.now()).split('.')[0]

# E: string
# S: icon
# D: carga y devuelve un icon
def getImageByName(name):
    return pygame.image.load(name+'.png')