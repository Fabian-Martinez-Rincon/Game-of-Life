import pygame
import numpy as np
print("Hola mundo")

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)
nxC, nyC = 25, 25
dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))

while True:
    
    for y in range(0, nxC):
        for x in range(0, nyC):
            #Nro de vecinos

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
                gameState[x, y] = 1
            #Regla 2 Caundo la celula viva tiene 2 o mas vecinas vivas, MUERE 
            elif gameState[x, y] == 1 and(n_neigh < 2 or n_neigh > 3):
                gameState[x, y] = 0
            
            poly = [((x) * dimCW, y *dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
    pygame.display.flip()