from userInterface.helperFunctions import mazeNumbering
import pygame
import time
import sys
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (255, 105, 180)

def disp2maze(widthMaze, heightMaze):
    WIDTH,HEIGHT=widthMaze*55+5+100,heightMaze*55+5
    SIZE=(WIDTH, HEIGHT)

    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Maze Solver")

    done=False
    clock=pygame.time.Clock()

    maze=[[0 for i in range(widthMaze)] for j in range(heightMaze)]
    numberDict=mazeNumbering(maze)

    checkPoints,obstacles=[],[]
    while(not done):
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        for i in range(heightMaze):
            for j in range(widthMaze):
                if((i,j) in obstacles):
                    pygame.draw.rect(screen, RED, [5+j*(55), 5+i*(55), 50, 50], 2)
                else:
                    pygame.draw.rect(screen, BLACK, [5+j*(55), 5+i*(55), 50, 50], 2)

                if(len(checkPoints)>0):
                    for checkPoint in checkPoints:
                        pygame.draw.rect(screen, PINK, [5+checkPoint[1]*(55), 5+checkPoint[0]*(55), 50, 50], 2)


        pygame.draw.rect(screen, BLUE, [5+widthMaze*(55), 5, 95, 50], 2)

        for event in events:
            if pygame.mouse.get_pressed()==(1,0,0):
                location=pygame.mouse.get_pos()
                X,Y=location[0]//55,location[1]//55

                if (Y,X) in numberDict and (Y,X) not in obstacles:
                    obstacles.append((Y,X))
                if(((location[0]>=(5*(widthMaze+1)+50*widthMaze) and location[0]<(5*(widthMaze+1)+50*widthMaze+95))\
                and ((location[1]>=5) and (location[1]<55))) and len(checkPoints)==2):
                    done=True

            if pygame.mouse.get_pressed()==(0,0,1):
                location=pygame.mouse.get_pos()
                X,Y=location[0]//55,location[1]//55

                if (Y,X) in obstacles:
                    obstacles.pop(obstacles.index((Y,X)))

            if pygame.mouse.get_pressed()==(0,1,0):
                location=pygame.mouse.get_pos()
                X,Y=location[0]//55,location[1]//55

                if(len(checkPoints)<2 and (Y,X) not in obstacles and (Y,X) not in checkPoints):
                    checkPoints.append((Y,X))

        pygame.display.flip()
        clock.tick(60)

    return obstacles, checkPoints

def renderMaze(widthMaze, heightMaze, obstacles):
    maze=[[' ' for i in range(widthMaze)] for j in range(heightMaze)]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if((i,j) in obstacles):
                maze[i][j]='#'
    return maze
