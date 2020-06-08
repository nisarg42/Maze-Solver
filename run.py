from user_interface.home_page import home_menu
from user_interface.disp_to_maze import disp2maze, render_maze
from user_interface.maze_to_disp import maze2disp
from user_interface.finish_page import exit_menu
from user_interface.helper_functions import maze_numbering
from maze_solver import maze2graph, BFS, DFS, Astar, path_tracer
from sys import exit

if __name__ == '__main__':
    continueSolver=True
    while(continueSolver):
        algo=home_menu(10,10)

        if algo=='A_star':
            print('A* is under construction')
            exit()

        obstacles,checkPoints=disp2maze(10,10)
        maze=render_maze(10,10,obstacles)
        numberDict=maze_numbering(maze)
        graph=maze2graph(maze, numberDict)
        if(algo=='BFS'):
            bfs=BFS(graph, numberDict[checkPoints[1]])
            bfs.BFS(numberDict[checkPoints[0]])
            path=pathTracer(bfs.solution, graph)
            # print(bfs.iterSolution)
        elif(algo=='DFS'):
            dfs=DFS(graph, numberDict[checkPoints[1]])
            dfs.DFS(numberDict[checkPoints[0]])
            path=pathTracer(dfs.solution, graph)
        elif(algo=='A_star'):
            astar=Astar(graph, numberDict[checkPoints[1]])
            astar.Astar(numberDict[checkPoints[0]])
            path=pathTracer(astar.solution, graph)
        maze2disp(maze, path, numberDict, checkPoints)
        continueSolver=exit_menu(10,10)
