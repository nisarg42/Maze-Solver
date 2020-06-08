from user_interface.helper_functions import maze_numbering
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


def disp2maze(width_maze, height_maze):
    WIDTH, HEIGHT = width_maze*55+5+100, height_maze*55+5
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Maze Solver")

    done = False
    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 32)
    NEXT = font.render('NEXT', True, RED, WHITE)
    NEXTRect = NEXT.get_rect()
    NEXTRect.center = (5+width_maze*55+47.5, 32.5)

    maze = [[0 for i in range(width_maze)] for j in range(height_maze)]
    number_dict = maze_numbering(maze)

    check_points, obstacles = [], []
    while(not done):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        for i in range(height_maze):
            for j in range(width_maze):
                if((i, j) in obstacles):
                    pygame.draw.rect(
                        screen, RED, [5+j*(55), 5+i*(55), 50, 50], 0)
                else:
                    pygame.draw.rect(
                        screen, BLACK, [5+j*(55), 5+i*(55), 50, 50], 2)

                if(len(check_points) > 0):
                    for check_point in check_points:
                        pygame.draw.rect(
                            screen, PINK, [5+check_point[1]*(55), 5+check_point[0]*(55), 50, 50], 0)

        pygame.draw.rect(screen, BLUE, [5+width_maze*(55), 5, 95, 50], 2)
        screen.blit(NEXT, NEXTRect)

        for event in events:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                location = pygame.mouse.get_pos()
                X, Y = location[0]//55, location[1]//55

                if (Y, X) in number_dict and (Y, X) not in obstacles:
                    obstacles.append((Y, X))
                if(((location[0] >= (5*(width_maze+1)+50*width_maze) and location[0] < (5*(width_maze+1)+50*width_maze+95))
                        and ((location[1] >= 5) and (location[1] < 55))) and len(check_points) == 2):
                    done = True

            if pygame.mouse.get_pressed() == (0, 0, 1):
                location = pygame.mouse.get_pos()
                X, Y = location[0]//55, location[1]//55

                if (Y, X) in obstacles:
                    obstacles.pop(obstacles.index((Y, X)))

            if pygame.mouse.get_pressed() == (0, 1, 0):
                location = pygame.mouse.get_pos()
                X, Y = location[0]//55, location[1]//55

                if(len(check_points) < 2 and (Y, X) not in obstacles and (Y, X) not in check_points):
                    check_points.append((Y, X))

        pygame.display.flip()
        clock.tick(60)

    return obstacles, check_points


def render_maze(width_maze, height_maze, obstacles):
    maze = [[' ' for i in range(width_maze)] for j in range(height_maze)]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if((i, j) in obstacles):
                maze[i][j] = '#'
    return maze
