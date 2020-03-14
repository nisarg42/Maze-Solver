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

def exitMenu(widthMaze, heightMaze):
    pygame.font.init()
    WIDTH,HEIGHT=widthMaze*55+5+100,heightMaze*55+5
    SIZE=(WIDTH, HEIGHT)

    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Maze Solver")

    done=False
    clock=pygame.time.Clock()

    font=pygame.font.Font('freesansbold.ttf', 32)
    RESTART=font.render('RESTART', True, RED, WHITE)
    EXIT=font.render('EXIT', True, RED, WHITE)
    RESTARTRect=RESTART.get_rect()
    EXITRect=EXIT.get_rect()
    RESTARTRect.center=(WIDTH//2,(HEIGHT/7)*1.5)
    EXITRect.center=(WIDTH//2,(HEIGHT/7)*5.5)

    continueSolver=''
    while(not done):
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                done=True

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [(WIDTH/5), (HEIGHT/7), 3*(WIDTH/5), (HEIGHT/7)], 2)
        pygame.draw.rect(screen, GREEN, [(WIDTH/5), 5*(HEIGHT/7), 3*(WIDTH/5), (HEIGHT/7)], 2)

        screen.blit(RESTART, RESTARTRect)
        screen.blit(EXIT, EXITRect)

        for event in events:
            if pygame.mouse.get_pressed()==(1,0,0):
                location=pygame.mouse.get_pos()

                if((location[0]>=(WIDTH/5) and location[0]<4*(WIDTH/5)) and (location[1])>=(HEIGHT/7) and location[1]<2*(HEIGHT/7)):
                    continueSolver=True
                    done=True
                if((location[0]>=(WIDTH/5) and location[0]<4*(WIDTH/5)) and (location[1])>=5*(HEIGHT/7) and location[1]<6*(HEIGHT/7)):
                    ALGO='A_star'
                    continueSolver=False
                    done=True

        screen.blit(RESTART, RESTARTRect)
        screen.blit(EXIT, EXITRect)

        pygame.display.flip()
        clock.tick(60)

    return continueSolver
