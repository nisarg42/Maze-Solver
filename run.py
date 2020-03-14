from userInterface.homePage import homeMenu
from userInterface.dispToMaze import disp2maze, renderMaze
from userInterface.mazeToDisp import maze2disp
from userInterface.finishPage import exitMenu
from userInterface.helperFunctions import mazeNumbering
from mazeSolver import maze2graph, BFS, DFS, pathTracer

continueSolver=True
while(continueSolver):
    algo=homeMenu(10,10)
    obstacles, checkPoints=disp2maze(10,10)
    maze=renderMaze(10,10,obstacles)
    numberDict=mazeNumbering(maze)
    graph=maze2graph(maze, numberDict)
    if(algo=='BFS'):
        bfs=BFS(graph, numberDict[checkPoints[1]])
        bfs.BFS(numberDict[checkPoints[0]])
        path=pathTracer(bfs.solution, graph)
    elif(algo=='DFS'):
        dfs=DFS(graph, numberDict[checkPoints[1]])
        dfs.DFS(numberDict[checkPoints[0]])
        path=pathTracer(dfs.solution, graph)
    elif(algo=='A_STAR'):
        print('No Can Do')
    maze2disp(maze, path, numberDict)
    continueSolver=exitMenu(10,10)
