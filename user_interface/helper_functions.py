import copy


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def maze_numbering(maze):
    number_dict = {

    }

    counter = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            number_dict[(i, j)] = counter
            counter += 1

    return number_dict


def output_graph(maze, solution):
    output = copy.deepcopy(maze)
    counter = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(counter in solution):
                output[i][j] = '@'
                # print(counter)
            counter += 1

    return output
