import copy

def getKey(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

def mazeNumbering(maze):
    numberDict={

    }

    counter=0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            numberDict[(i,j)]=counter
            counter+=1

    return numberDict

def outputGraph(maze, solution):
    output=copy.deepcopy(maze)
    counter=0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(counter in solution):
                output[i][j]='@'
                # print(counter)
            counter+=1

    return output
