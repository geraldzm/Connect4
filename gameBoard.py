from tools import save


# esta clase se encarga de la matriz logica
# 1=red, 0=yellow, - = none
class GameBoard:

    # E: una lista si se quiere comenzar ese juego, nada si es un nuevo juego
    # ls tiene que tener [matrizLogica, int] donde int es la posicion abstracta del 0
    def __init__(self, sound, ls=[]):
        self.sound = sound
        self.index = 0  # se puede ver 7 columnas en pantalla, esta reprecenta la menor
        self.indexy = 0  # se puede ver 6 filas

        self.winner = '-1' # winner

        if not ls:  # juego nuevo

            self.boardHeight = 6
            self.boardWidth = 7
            self.zero = 0  # puede creser para la izquierda, esto mantiene esa posicion de 0 inicial
            self.board = []
            self.setBoard()
        else:  # juego previo

            self.board = ls[0]
            self.zero = int(ls[1])
            self.index += self.zero
            self.boardHeight = len(self.board)
            self.boardWidth = len(self.board[0])

    # D: crea una matriz (board) todo en '-', con boardHeight * boardWidth
    def setBoard(self):
        for i in range(6):
            self.board.append(['-'] * 7)

    # D: quita todas las fichas de la matriz
    def resetBoard(self):
        for row in range(self.boardHeight):
            for column in range(self.boardWidth):
                self.board[row][column] = '-'

    # D: imprime el estado actual de la matriz
    def printBoard(self):
        for i in range(self.boardWidth):
            print("|  ", end="")
            print(i, sep="  | ", end="")
        print('')
        for i in range(self.boardHeight):
            print("| ", end="")
            print(*self.board[i], sep=" | ", end="")
            print(" |\n")

    # S: lista
    # D: una lista con el board
    def getMatrixGuardar(self):
        return [self.board, self.zero]

    # E: integer
    # S: lista
    # D: [] si no se puede agregar otra ficha en esa columna, si si se puede, retorna [row, column, rowScreen(0-5)]
    def canAddChip(self, column):

        # si no tiene nada abajo no puede poner
        if self.indexy != 0 and self.board[self.indexy - 1][column + self.index] == '-':
            return []

        # validar 7 espacios derecha izquierda
        if self.index < self.zero:  
            if not self.isChipInRango(self.index+7+column, self.index+column, -1):
                return []
            
        # validar 7 espacios izquierda derecha
        if self.zero+6 < self.index:  
            if not self.isChipInRango(self.index-7+column, self.index+column):
                return []

        # recorre las 6 filas de arriba a abajo
        for i in range(self.indexy, self.indexy + 6):

            if self.board[i][column + self.index] == '-':
                return [i, column + self.index, i % 6]

        return []

    # E: 2 integers naturales dentro de la matriz y un uno positovo o negativo
    # S: boolean
    # D: pregunta en ese rango si hay una ficha
    def isChipInRango(self, fro, to, steps=1):
        for i in range(fro, to, steps):
            if self.isChipInColoumn(i):
                return True
        return False


    # E: integer
    # S: boolean
    # D: true si hay una ficha en la columna

    def isChipInColoumn(self, coloumn):
        return self.board[0][coloumn] != '-'

    # E: un string, 2 integers
    # D: el string puede ser 1, 0, o -
    # ANTES DE USAR ESTE METODO TIENE QUE COMPROBAR LA COLUMNA CON canAddChip
    # ademas la row y column debe ser la que canAddChip retorna

    def addChip(self, chip, row, column):
        self.board[row][column] = chip

        if self.isWinner(chip, column, row):
            self.winner = chip


    # E: 2 integers
    # S: string
    # S: si la posicion existe retorna lo que este ahi, sino retorna -
    def getChip(self, row, column):
        if not self.isPositionInBoard(column):
            return '-'
        return self.board[row][column]

    # S: numero entero
    # D: retorna la primera posicion de la matris eje [-2,-1,0,1] retorna -2
    def getFirstPosition(self):
        return self.zero * - 1

    # E: numero entero
    # S: boolean
    # D: determina si la columna esta en la matriz logica
    # tomando como cero el self.zero eje [-2,-1,0,1] no tiene posicion 2
    def isPositionInBoard(self, column):
        return self.getFirstPosition() <= column < self.boardWidth

    # S: un numero
    # D: retorna el index x
    def getIndex(self):
        return self.index

    # S: un numero
    # D: retorna el index y
    def getIndeY(self):
        return self.indexy

    # S: una matriz de 6x7
    # devuelve la matriz de 6x7 dentro de la matriz logica infinita en base a los index
    def getBoard(self):
        result = []
        temp = []
        for row in range(self.indexy, self.indexy + 6):
            for column in range(self.index, self.index + 7):
                temp.append(self.getChip(row, column))
            result.append(temp)
            temp = []
        return result

    # S: matriz
    # D: retorna toda la matriz logica
    def getMatriz(self):
        return self.board

    # D: actualiza el width y height por el de la matrix actual
    # guarda la matrix en el archivo
    def updateBoardDimensions(self):
        self.boardWidth = len(self.board[0])
        self.boardHeight = len(self.board)

    # E: numero entero
    # S: boolean
    # true si la matrix necesita crecer, false si no
    def needToGrowY(self, index):
        return index >= self.boardHeight

    # S: string
    # D: retorna el winner, -1 no winner, 1 rojo, 0 amarillo
    def getWinner(self):
        return self.winner

    # E: numero entero
    # S: boolean (true si se mueve, false si no)
    # D: mueve el indey n veces, cada n reprecenta 6 campos
    # indexY nunca va a ser menor que 0, si se intenta esto se reproducira el sonido de hit
    def moveIndexY(self, n):
        temp = self.indexy + n * 6
        if temp < 0:  # trata bajar de 0
            self.sound.playSound('hit')
            return False
        elif self.needToGrowY(temp):  # creser hacia arriba
            self.growUp()

        self.indexy = temp
        self.updateBoardDimensions()

        return True

    # E: numero entero
    # S: boolean
    # true si la matrix necesita crecer, false si no
    def needToGrowX(self, index):
        return 0 > index or index >= self.boardWidth

    # E: numero entero
    # D: mueve el index n veces, cada n reprecenta 7 campos a la derecha o izquierda
    def moveIndex(self, n):
        self.index += n * 7

        # si la matriz necesita crecer
        if self.needToGrowX(self.index):

            if n < 0:  # crese a la izquierda
                self.growLeft()
                self.zero += 7
                self.index += 7
            else:
                self.growRight()

        self.updateBoardDimensions()

    # E: string, 2 enteros naturales dentro de la matriz
    # S: boolean
    # D: se llama cada vez que se agrega una nueva ficha
    # boolean jugador chip gano
    def isWinner(self, chip, x, y):
        for i in range(1, 9):
            if self.countChipsSides(x, y, chip, i, 3):
                return True
        return False
        
    # S: string (-1, 0, 1)
    # 1 = gana rojo, 0 = gana amarillo, -1 = ninguno
    # busca en toda la matriz un ganador
    def verifyWinner(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):

                if self.board[y][x] != '-':
                    if self.isWinner(self.board[y][x], x, y):
                        self.winner = self.board[y][x]
                        return self.board[y][x]
        return '-1'
    

    # E: 5 enteros naturales, 1 string Chip con el tipo de ficha
    # S: boolean
    # D: en base a una posicion x,y, determina si en el board hay una sucession de 'n' para una ficha 'chip'
    # x y deben ser posiciones dentro del board
    # chip: 1=Rojo, 0=Amarillo
    # direcciones:
    # 123
    # 4x5
    # 678
    def countChipsSides(self, x, y, chip, direct, n, counter=0):
        if n == counter:
            return True

        x, y = self.moveXYInDireccion(x, y, direct)

        if self.needToGrowX(x) or self.needToGrowY(y): # se sale de los limites
            return False
            
        if self.board[y][x] != chip:
            return False

        return self.countChipsSides(x, y, chip, direct, n, counter+1)


    # D: incrementa la matriz en 7 nuevos espacios hacia la derecha para cada columna
    def growRight(self):
        for i in range(len(self.board)):
            self.board[i] += ['-', '-', '-', '-', '-', '-', '-']

    # D: incrementa la matriz en 7 nuevos espacios hacia la derecha para cada columna
    def growLeft(self):
        for i in range(len(self.board)):
            self.board[i] = ['-', '-', '-', '-', '-', '-', '-'] + self.board[i]

    # D: incrementa la matriz en 6 nuevos espacios hacia arriba
    def growUp(self):
        length = len(self.board[0])
        for i in range(6):
            self.board.append(['-'] * length)


    # E: 3 numeros naturales
    # S: Lista
    # D: las direcciones puden ser desde [1-8]
    # mueve las coordenadas para esa direccion
    # Direcciones
    # 1 2 3
    # 4 x 5
    # 6 7 8
    def moveXYInDireccion(self, x, y, direct, n=1):
        if direct in [1, 4, 6]:
            x -= n

        if direct in [3, 5, 8]:
            x += n

        if direct in [1, 2, 3]:
            y += n

        if direct in [6, 7, 8]:
            y -= n

        return x, y