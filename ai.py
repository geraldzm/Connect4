import random


class AI:  # ficha False or 0

    def __init__(self, board=None, active=False, inputManager=None):
        self.board = board
        self.nextMove = [0,0]
        self.mode = active
        self.inputManager = inputManager


    # S: integer
    # D: retorna la columna donde tiene que poner la ficha
    # si no esta en pantalla va a mover la pantalla
    def getMove(self):
        return self.nextMove[0]

    # E: [row, column, rowScreen(0-5)] 
    # S: integer
    # D: retorna la columna donde tiene que poner la ficha
    # si no esta en pantalla va a mover la pantalla
    def enemyMove(self, ls):
        print('movio en : ', ls)
        for i in range(1, 9):
            if self.board.countChipsSides(ls[1], ls[0], '1', i, 2):

                x, y = self.board.moveXYInDireccion(ls[1], ls[0], i, 3)
                print(x, y)

                if self.isPositionEmpty(x, y):
                    print('puede ganar')
                    self.putChipInDireccion(x, y, i)
                    break
        else:
            self.putRandom()

    # E: 2 numeros
    # S: boolean
    # D: retorna false si hay una ficha mia o si la matriz termina
    def isPositionEmpty(self, x, y):
        if len(self.board.getBoard()[0]) <= x or x < 0:
            return True

        if len(self.board.getBoard()) <= y:
            return True

        if self.board.getBoard()[y][x] == '-':
            return True
        
        return False




    # E: integer 1 a 8
    # D: pone una fcha en esa direccion, si es necesario
    # mueve la pantalla
    def putChipInDireccion(self, x, y, direct):
        if x < 0:
            self.inputManager.moveWindow(self.directionToArrow(direct))
            self.nextMove[0] = 6

        elif len(self.board.getBoard()[0]) <= x:
            self.inputManager.moveWindow(self.directionToArrow(direct))
            self.nextMove[0] = 0

        elif len(self.board.getBoard()) <= y:
            self.inputManager.moveWindow(self.directionToArrow(direct))

        else:
            self.nextMove[0] = x


    # D; pone una ficha random 
    def putRandom(self):
        for i in range(7):
            if self.board.canAddChip(i):
                self.nextMove[0] = i
                break
        else:
            self.inputManager.moveWindow(self.directionToArrow(2))
            self.nextMove[0] = 0


    # E: 1 numero
    # S: numero
    # D: transforma la direcicon a direcion de teclado
    # 1 2 3
    # 4 x 5
    # 6 7 8
    def directionToArrow(self, n):
        if n in [1, 4, 6]:
            return 0

        if n in [3, 5, 8]:
            return 2

        if n in [1, 2, 3]:
            return 1

        if n in [6, 7, 8]:
            return 3


    # E: 1 numero entero de [1-8]
    # S: 1 numero natural de  [1-8]
    # retorna la direccion opuesta eje: if 1 -> 8, 2 -> 7, 5 -> 4
    # 1 2 3
    # 4 0 5
    # 6 7 8
    def getOppositeDireccion(self, direccion):
        return abs(9 - direccion)
        
    # E: objeto board
    # D: settea el board
    def setBoard(self, board):
        self.board = board

    # E: objeto board
    # D: settea el board
    def setInputManager(self, inputManager):
        self.inputManager = inputManager


    def getMode(self):
        return self.mode

    def setMode(self, mode):
        self.mode = mode