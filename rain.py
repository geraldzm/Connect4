import pygame
from chipGame import Chip
from numpy import random
from tools import noZero
import math


class Rain:
    # imagen de ficha roja
    red_icon = pygame.image.load('red.png')
    # imagen de ficha amarilla
    yellow_icon = pygame.image.load('yellow.png')
    

    def __init__(self, n):
        self.ls = []
        sizes = [10, 15, 20, 25, 30, 35]

        for i in range(n):
            s = self.getSize(n, sizes)

            x = 830 * random.rand()

            y = -1*(random.rand()*700) - 80

            chip = Chip(0, 0)

            chip.setX(x)
            chip.setY(y)
            chip.setAcelerarcion(0.2 * s)
            chip.setVelocidad(0)
            chip.hasToBounds(False)

            if i % 2 == 0:
                chip.setIcon(pygame.transform.scale(self.red_icon, (s, s)))
            else:
                chip.setIcon(pygame.transform.scale(self.yellow_icon, (s, s)))


            chip.setFalling(True)
            self.ls.append(chip)


    def tick(self):
        for i in self.ls:
            i.tick()
            i.setVelocidad(0)
            self.goUpAgain(i)


    def render(self, screen):
        for i in self.ls:
            i.render(screen)

    # D: pone cada ficha en display 
    def show(self):
        for i in self.ls:
            i.setDisplaying(True)


    # si la ficha llego a su limite, la vuleve a poner arriba
    def goUpAgain(self, chip):
        if 800 <= chip.getY():
            chip.setX( 900 * random.rand())
            chip.setY( -1*(random.rand()*50) - 80)
            chip.setDisplaying(True)
            chip.setFalling(True)


    anterior = -1
    # E: 1 numero positivo entero, una lista de numeros naturales
    # S: un numero natural
    # calcula el tama;o de la siguiente ficha en base a la anterior
    def getSize(self, n, sizes):
        cada = math.ceil(n / len(sizes))
        
        
        self.anterior += 1
        return sizes[self.anterior // cada]