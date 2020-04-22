import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

# Pintamos el fondo
bg = 25, 25, 25
screen.fill(bg)

# Numero de celdas
nxC, nyC = 25, 25

# Dimensiones de las celdas
dimCW = width/nxC
dimCH = height/nyC

# Estado de las celdas,  vivas =1 muertas=0
gameState = np.zeros((nxC, nyC))


gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

pauseExect = False

while not endGame:
    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    # Eventos de teclado
    ev = pygame.event.get()
   
    for event in ev:
         if event.type == pygame.QUIT:
            endGame = True

        if event.type == pygame.KEYDOWN:
            pauseExec = not pauseExec

        mouseClick = pygame.mouse.get_pressed()
          if sum(mouseClick) > 0:
            # Click del medio pausa / reanuda el juego
            if mouseClick[1]:

                pauseExec = not pauseExec

            else:

                # Obtengo las coordenadas del cursor del mouse en pixeles
                posX, posY, = pygame.mouse.get_pos()

                # Convierto de coordenadas en pixeles a celda clickeada en la grilla
                celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))

                # Click izquierdo y derecho permutan entre vida y muerte
                newGameState[celX, celY] = not gameState[celX, celY]


    for y in range(0, nxC):
        for x in range(0,nyC):
            if not pauseExect:
                n_neigh =   gameState[(x-1)     %nxC, (y - 1)   %nyC] + \
                            gameState[(x)       %nxC, (y - 1)   %nyC] +\
                            gameState[(x + 1)   %nxC, (y - 1)   %nyC] + \
                            gameState[(x - 1)   %nxC, (y)       %nyC] + \
                            gameState[(x + 1)   %nxC, (y)       %nyC] + \
                            gameState[(x - 1)   %nxC, (y + 1)   %nyC] + \
                            gameState[(x)       %nxC, (y + 1)   %nyC] + \
                            gameState[(x + 1)   %nxC, (y + 1)   %nyC]

            # Regla 1: Una celda muerta con 3 vecinas vivas -> revive
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

            # Regla 2: Una celula viva con menos de 2 o mas veceinas vivas -> muere
                elif gameState[x, y] == 1 and (n_neigh <2 or n_neigh >3):
                    newGameState[x,y] = 0

                poly =[ ((x)   * dimCW, y       * dimCH),
                        ((x+1) * dimCW, y       * dimCH),
                        ((x+1) * dimCW, (y+1)  * dimCH),
                        ((x)   * dimCW , (y+1)  * dimCH)]

                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128 ,128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)


    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    pygame.display.flip()
