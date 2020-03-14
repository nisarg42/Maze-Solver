from userInterface.helperFunctions import getKey, mazeNumbering
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

def maze2disp(maze, solution, numberDict, checkPoints):
    WIDTH,HEIGHT=len(maze[0])*55+5+100,len(maze)*55+5
    SIZE=(WIDTH, HEIGHT)

    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Maze Solver")

    done=False
    clock=pygame.time.Clock()

    location=[]
    counter=1
    for element in solution:
            temp=getKey(element, numberDict)
            location.append(temp)

    while(not done):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True

        screen.fill(WHITE)
        for checkPoint in checkPoints:
            pygame.draw.rect(screen, PINK, [5+checkPoint[1]*(55), 5+checkPoint[0]*(55), 50, 50], 0)

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if(maze[i][j]=='#'):
                    pygame.draw.rect(screen, RED, [5+j*(55), 5+i*(55), 50, 50], 0)
                else:
                    pygame.draw.rect(screen, BLACK, [5+j*(55), 5+i*(55), 50, 50], 2)

        if(counter<len(solution)):
            for element in location:
                pygame.draw.rect(screen, GREEN, [5+element[1]*(55), 5+element[0]*(55), 50, 50], 0)
                pygame.display.flip()
                counter+=1
                time.sleep(0.5)

        if(counter==(len(solution)+1)):
            done=True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
