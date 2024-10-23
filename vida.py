import pygame
import numpy as np

pygame.init()

grid = (200, 120)
cellDim = 5

screen = pygame.display.set_mode((grid[0]*cellDim,grid[1]*cellDim))

bg = (25, 24, 25)

screen.fill(bg)

gameState = np.zeros(grid)

game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            else:
                play = not play
                print(play)
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            cellX , CellY = int(np.floor(posX/cellDim)), int(np.floor(posY/cellDim))
            if mouseClick[0]:
                gameState[cellX, CellY] = 1
            else: gameState[cellX, CellY] = 0
            print(cellX, CellY)
    
    newGameState = np.copy(gameState)

    screen.fill(bg)
    pygame.time.wait(100)

    for y in range(0, grid[1]):
        for x in range(0, grid[0]):
            if play:

                n_neigh =   gameState[(x-1) % grid[0], (y-1) % grid[1]] + \
                            gameState[(x-1) % grid[0], (y) % grid[1]] + \
                            gameState[(x-1) % grid[0], (y+1) % grid[1]] + \
                            gameState[(x) % grid[0], (y-1) % grid[1]] + \
                            gameState[(x) % grid[0], (y+1) % grid[1]] + \
                            gameState[(x+1) % grid[0], (y-1) % grid[1]] + \
                            gameState[(x+1) % grid[0], (y) % grid[1]] + \
                            gameState[(x+1) % grid[0], (y+1) % grid[1]]
                            
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                if gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                
            cell = (x * cellDim, y * cellDim, cellDim, cellDim)

            if newGameState[x, y] == 0:
                pygame.draw.rect(screen, (100, 0, 100), cell, 1)
            if newGameState[x, y] == 1:
                pygame.draw.rect(screen,(200,200,255), cell)
    
    gameState = np.copy(newGameState)
    pygame.display.flip()
