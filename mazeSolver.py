def maze2graph(maze, numberDict):
    graph=[[] for i in numberDict]
    counter=0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(i+1<=len(maze)-1):
                if(maze[i+1][j]==' '):
                    graph[numberDict[(i,j)]].append(numberDict[(i+1,j)])
            if(i-1>=0):
                if(maze[i-1][j]==' '):
                    graph[numberDict[(i,j)]].append(numberDict[(i-1,j)])
            if(j+1<=len(maze[0])-1):
                if(maze[i][j+1]==' '):
                    graph[numberDict[(i,j)]].append(numberDict[(i,j+1)])
            if(j-1>=0):
                if(maze[i][j-1]==' '):
                    graph[numberDict[(i,j)]].append(numberDict[(i,j-1)])

            counter+=1

    return graph

class BFS:
    def __init__(self, adjList, destination):
        self.graph=adjList

        vertexNum=len(adjList)
        self.queue=[]
        self.visited=[0 for i in range(vertexNum)]
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
    def __init__(self, adjList, destination):
        self.graph=adjList

        vertexNum=len(adjList)
        self.visited=[0 for i in range(vertexNum)]
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
    def __init__(self, adjList, destination):
        pass

    def Astar(self, node):
        pass

def pathTracer(solution, graph):
    solutionRev=solution[::-1]

    path=[]
    path.append(solutionRev[0])
    for i in range(1,len(solutionRev)):
        if(solutionRev[i] in graph[path[-1]]):
            path.append(solutionRev[i])

    return path[::-1]
