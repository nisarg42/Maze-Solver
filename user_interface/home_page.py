import pygame
import time
import sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)


def home_menu(width_maze, height_maze):
    WIDTH, HEIGHT = width_maze*55+5+100, height_maze*55+5
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Maze Solver")

    done = False
    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 32)
    BFS = font.render('BFS', True, RED, WHITE)
    DFS = font.render('DFS', True, RED, WHITE)
    A_STAR = font.render('A*', True, RED, WHITE)
    BFSRect = BFS.get_rect()
    DFSRect = DFS.get_rect()
    A_STARRect = A_STAR.get_rect()
    BFSRect.center = (WIDTH//2, (HEIGHT/7)*1.5)
    DFSRect.center = (WIDTH//2, (HEIGHT/7)*3.5)
    A_STARRect.center = (WIDTH//2, (HEIGHT/7)*5.5)

    ALGO = ''
    while(not done):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        pygame.draw.rect(
            screen, GREEN, [(WIDTH/5), (HEIGHT/7), 3*(WIDTH/5), (HEIGHT/7)], 2)
        pygame.draw.rect(
            screen, GREEN, [(WIDTH/5), 3*(HEIGHT/7), 3*(WIDTH/5), (HEIGHT/7)], 2)
        pygame.draw.rect(
            screen, GREEN, [(WIDTH/5), 5*(HEIGHT/7), 3*(WIDTH/5), (HEIGHT/7)], 2)

        screen.blit(BFS, BFSRect)

        for event in events:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                location = pygame.mouse.get_pos()

                if((location[0] >= (WIDTH/5) and location[0] < 4*(WIDTH/5)) and (location[1]) >= (HEIGHT/7) and location[1] < 2*(HEIGHT/7)):
                    ALGO = 'BFS'
                    done = True
                if((location[0] >= (WIDTH/5) and location[0] < 4*(WIDTH/5)) and (location[1]) >= 3*(HEIGHT/7) and location[1] < 4*(HEIGHT/7)):
                    ALGO = 'DFS'
                    done = True
                if((location[0] >= (WIDTH/5) and location[0] < 4*(WIDTH/5)) and (location[1]) >= 5*(HEIGHT/7) and location[1] < 6*(HEIGHT/7)):
                    ALGO = 'A_star'
                    done = True

        screen.blit(BFS, BFSRect)
        screen.blit(DFS, DFSRect)
        screen.blit(A_STAR, A_STARRect)

        pygame.display.flip()
        clock.tick(60)
    return ALGO
