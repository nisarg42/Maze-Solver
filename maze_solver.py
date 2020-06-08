def maze2graph(maze, number_dict):
    graph=[[] for i in number_dict]
    counter=0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(i+1<=len(maze)-1):
                if(maze[i+1][j]==' '):
                    graph[number_dict[(i,j)]].append(number_dict[(i+1,j)])
            if(i-1>=0):
                if(maze[i-1][j]==' '):
                    graph[number_dict[(i,j)]].append(number_dict[(i-1,j)])
            if(j+1<=len(maze[0])-1):
                if(maze[i][j+1]==' '):
                    graph[number_dict[(i,j)]].append(number_dict[(i,j+1)])
            if(j-1>=0):
                if(maze[i][j-1]==' '):
                    graph[number_dict[(i,j)]].append(number_dict[(i,j-1)])

            counter+=1

    return graph

class BFS:
    def __init__(self, adj_list, destination):
        self.graph=adj_list

        vertex_num=len(adj_list)
        self.queue=[]
        self.visited=[0 for i in range(vertex_num)]
        self.solution=[]
        self.iterSolution=[]
        self.destination=destination

    def enqueue(self, value, queue):
        queue.append(value)

    def dequeue(self, queue):
        temp=queue[0]
        queue=queue[1:]
        return temp, queue

    def BFS(self, node):
        # print(self.queue)
        if(self.visited[node]==1):
            return
        self.visited[node]=1
        self.solution.append(node)

        neighbours=self.graph[node]
        self.iterSolution.append(neighbours)
        # temp=sorted(neighbours)
        for neighbour in neighbours:
            self.enqueue(neighbour, self.queue)

        while(self.queue!=[]):
            if(self.visited[self.destination]==1):
                return
            newNode,self.queue=self.dequeue(self.queue)
            self.BFS(newNode)

class DFS:
    def __init__(self, adj_list, destination):
        self.graph=adj_list

        vertex_num=len(adj_list)
        self.visited=[0 for i in range(vertex_num)]
        self.solution=[]
        self.destination=destination

    def DFS(self, node):
        if(self.visited[node]==1):
            return
        self.visited[node]=1
        self.solution.append(node)

        neighbours=self.graph[node]
        # temp=sorted(neighbours)
        for neighbour in neighbours:
            if(self.visited[self.destination]==1):
                return
            self.DFS(neighbour)

class Astar:
    def __init__(self, adj_list, destination):
        pass

    def Astar(self, node):
        pass

def path_tracer(solution, graph):
    solution_rev=solution[::-1]

    path=[]
    path.append(solution_rev[0])
    for i in range(1,len(solution_rev)):
        if(solution_rev[i] in graph[path[-1]]):
            path.append(solution_rev[i])

    return path[::-1]
