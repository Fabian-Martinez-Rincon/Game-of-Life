import pygame
import numpy as np
import time


width, height = 700, 700
nxC, nyC = 70, 70
dimCW = width / nxC
dimCH = height / nyC
bg = 10, 10, 10 #Color
viva = (255,255,255)
muerta = (128,128,128)
pauseExect = False
run = True



pygame.init()
screen = pygame.display.set_mode([height, width])


screen.fill(bg)


gameState = np.zeros((nxC, nyC))


while run:
    
    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    #Registramos teclas
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mauseClick = pygame.mouse.get_pressed()

        if sum(mauseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX,celY] = not mauseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):
            #Nro de vecinos

            if not pauseExect:

                n_neigh =   gameState[(x-1) % nxC, (y-1) % nyC] + \
                            gameState[(x)   % nxC, (y-1) % nyC] + \
                            gameState[(x+1) % nxC, (y-1) % nyC] + \
                            gameState[(x-1) % nxC, (y) % nyC] + \
                            gameState[(x+1) % nxC, (y) % nyC] + \
                            gameState[(x-1) % nxC, (y+1) % nyC] + \
                            gameState[(x) % nxC, (y+1) % nyC] + \
                            gameState[(x+1) % nxC, (y+1) % nyC] 
                #Regla 1 Cuando la celula muerta tiene exactamente 3 vecinas vivas, REVIVE
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                #Regla 2 Caundo la celula viva tiene 2 o mas vecinas vivas, MUERE 
                elif gameState[x, y] == 1 and(n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                
            poly = [((x) * dimCW, y *dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            #Dibujamos las celdas
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen,(255, 255, 255), poly, 0)
        #actualizamos
    gameState = np.copy(newGameState)

    pygame.display.flip()

pygame.quit()
