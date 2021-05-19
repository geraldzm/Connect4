import pygame
from game import Game


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((840, 730))  # WIDTH = 940, HEIGHT = WIDTH / 12* 9;, esta en 840, 630
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 25)
    pygame.display.set_caption("4 en linea")

    game = Game(clock, screen, font)
    game.run()  # run

    pygame.quit()
