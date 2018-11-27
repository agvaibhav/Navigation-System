import sys

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def dijkstra(self, src, dest, loc):

        dist = [sys.maxsize]*self.V
        dist[src]=0
        sptSet = [False]*self.V
        parent = [-1] * self.V

        for out in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v]==False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        self.printSolution(dist, parent, dest, loc)
                    
    def minDistance(self,dist,sptSet):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def printSolution(self,dist, parent, dest,loc):
        print("Destination \tDistance From {} \tPath".format(loc[src]))
        print()
        print(loc[dest], "\t\t", dist[dest], "\t\t\t",end=" ")
        self.printPath(parent,dest, loc)


    def printPath(self, parent, node, loc):
        if parent[node]==-1:
            print(loc[node],end=" ")
            return
        self.printPath(parent, parent[node],loc)
        print("-->",loc[node],end=" ")
                                                                         
                                                                         
g  = Graph(15) 
g.graph = [[0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
           [0, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 2, 2, 0, 3, 0, 0, 0, 0, 0, 1, 0, 3, 0],
           [0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 5, 0, 2, 0, 7, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 2, 0, 8, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 15, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 0, 15, 0, 1, 8, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 6, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 6, 0, 4, 0],
           [0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 3],
           [0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]
          ]; 

loc=['thapar university','mini secreteriat','columbia asia','jaggi sweets','leela bhavan',
     'easy day','ajanta hospital','mocha','lifeplus hospital','anand hospital',
     'YPS market','fountain chowk','urban estate','bus stand','gurudwara sahib']

src = input("write the source location:")
dest = input("write the destination:")
src = src.lower()
dest = dest.lower()
print(src)
print(dest)
for i in range(len(loc)):
    if loc[i]==src:
        src=i
    if loc[i]==dest:
        dest=i
        
g.dijkstra(src, dest, loc)
