import pygame
import numpy as np
import time
import os

# iniciamos el juego
pygame.init()

# ponemos el titulo a la ventana
pygame.display.set_caption("Juego de la vida - JSC")

# Cargamos el icono, si lo hay
icon ='./icono.ico'
if os.path.exists(icon):
    icono = pygame.image.load(icon)

    pygame.display.set_icon(icono)

# Definimos el ancho y alto de  la ventana
width, height = 1000, 1000

#Creamos una ventana 
screen = pygame.display.set_mode((height, width))

# Seleccionamos el color  de fondo
bg = 25, 25, 25
screen.fill(bg)

# Seleccionamos el numero de celulas por fila y columna
nxC, nyC = 100, 100

# Seleccionamos el ancho y el alto de cada celula
dimCW = width / nxC
dimCH = height / nyC

# Matriz con los estados de las celulas del juego,
# Iniciamos todas las celulas a cero
# Estados de las celulas: Vivas -> 1 ; Muertas -> 0
gameState = np.zeros((nxC, nyC))

# Variable que controla la pausa,
# iniciamos el juego pausado para disponer nuestras celulas
pauseMode = True

# Controla si se debe pausar un segundo por iteracion, ni idea
pauseOneSec = False

# Controla la finalizacion del juego:
endGame = False

# Bucle de ejecución
while not endGame:
    newGameState = np.copy(gameState)

    # Coloreamos la pantalla del color seleccionado, reset del state anterior
    screen.fill(bg)
    
    # Pausa entre interaciones
    time.sleep(0.1)

    # Eventos inputs teclado y mouse
    ev = pygame.event.get()

    for event in ev:
        # Si cerramos la ventana
        if event.type == pygame.QUIT:
            endGame = True

        # Si pulsamos el teclado entramos en pausa
        if event.type == pygame.KEYDOWN:
            pauseMode = not pauseMode
        
        # Pulsaciones del mouse
        Click = pygame.mouse.get_pressed()
        if sum(Click) >0:
            # Obtenemos las coordenadas del cursor
            clickPosX, clickPosY = pygame.mouse.get_pos()

            # Buscamos la celula pulsada en funcion de las coordenadas
            cellX, cellY = int(np.floor(clickPosX / dimCW)), int(np.floor(clickPosY / dimCH))
            # Cambiamos el estado de la celula pulsada
            newGameState[cellX, cellY] = not gameState[cellX, cellY]
    
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseMode:
                neighCells = (
                    gameState[(x - 1) % nxC, (y - 1) % nyC]
                    + gameState[x % nxC, (y - 1) % nyC]
                    + gameState[(x + 1) % nxC, (y - 1) % nyC]
                    + gameState[(x - 1) % nxC, y % nyC]
                    + gameState[(x + 1) % nxC, y % nyC]
                    + gameState[(x - 1) % nxC, (y + 1) % nyC]
                    + gameState[x % nxC, (y + 1) % nyC]
                    + gameState[(x + 1) % nxC, (y + 1) % nyC]
                )

                # Regla 1º: Una célula muerta con exactamente 3 vecinas vivas: "revive"
                if gameState[x, y] == 0 and neighCells == 3:
                    newGameState[x, y] = 1
                
                # Regla 2ª: Una célula viva con menos de 2 o más de 3 vecinas vivas : "muere"

                elif gameState[x, y] == 1 and (neighCells < 2 or neighCells > 3):
                    newGameState[x, y] = 0
                
            # Puntos que componen el poligono o celula
            poly = [
                (int(x * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int((y + 1) * dimCH)),
                (int(x * dimCW), int((y + 1) * dimCH)),
            ]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                if pauseMode:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    # Muestro y actualizo los fotogramas en cada iteración del bucle principal
    pygame.display.flip()
