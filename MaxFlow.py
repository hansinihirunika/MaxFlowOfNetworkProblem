class Graph:

    def __init__(residual, graph):
        residual.graph = graph  # create the residual graph
        residual.ROW = len(graph)

    def bFS(residual, s, t, parent):

        visited = [False] * (residual.ROW)  # Mark all the vertices as not visited

        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:


            u = queue.pop(0)



            for ind, va in enumerate(residual.graph[u]):
                if visited[ind] == False and va > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def FordFulkerson(residual, source, sink):

        parent = [-1] * (residual.ROW)  # array is filled by BFS and store path

        maxFlow = 0

        # find a Augment flow that has path from source to sink
        while residual.bFS(source, sink, parent):

            pathFlow = float("Inf")
            s = sink
            while (s != source):
                pathFlow = min(pathFlow, residual.graph[parent[s]][s])
                s = parent[s]

            # get the residual capacities  and reverse edges
            v = sink
            while (v != source):
                u = parent[v]
                residual.graph[u][v] -= pathFlow
                residual.graph[v][u] += pathFlow
                v = parent[v]


            maxFlow += pathFlow

        return maxFlow




user = 0
while user < 6:
    user = int(input("What's your choise 1/2/3/4/5?"
                     "**1- 1st graph** "
                     "**2- 2nd graph**"
                     "**3- 3rd graph**"
                     "**4- 4th graph**"
                     "**5- Exit**"))

    if user == 1:

        graph = [[0, 10, 8, 0, 0, 0],
                 [0, 0, 6, 5, 0, 0],
                 [0, 4, 0, 0, 10, 0],
                 [0, 0, 7, 0, 6, 3],
                 [0, 0, 0, 10, 0, 14],
                 [0, 0, 0, 0, 0, 0]]

        g = Graph(graph)

        source = 0
        sink = 5

        print("The maximum possible flow is = %d " % g.FordFulkerson(source, sink))

    elif user == 2:
        graph = [[0, 16, 8, 21, 11, 11, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 20, 0, 0, 0, 0, 0],
                 [0, 5, 0, 3, 0, 0, 7, 9, 0, 0, 0, 0],
                 [0, 0, 9, 0, 4, 0, 0, 8, 7, 0, 0, 0],
                 [0, 0, 0, 0, 0, 6, 0, 0, 6, 6, 0, 0],
                 [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0],
                 [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4],
                 [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 9],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                 [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        g = Graph(graph)

        source = 0
        sink = 5

        print("The maximum possible flow is = %d " % g.FordFulkerson(source, sink))



    elif user == 3:
        graph = [[0, 7, 8, 5, 7, 20, 3, 25, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 13, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 21, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 13, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0],
                 [0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 20],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 11, 0, 0, 0, 18],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 23],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        g = Graph(graph)

        source = 0
        sink = 5

        print("The maximum possible flow is = %d " % g.FordFulkerson(source, sink))

    elif user == 4:
        graph = [[0, 80, 0, 80, 0, 0],
                 [0, 0, 32, 16, 64, 0],
                 [0, 0, 0, 0, 0, 80],
                 [0, 0, 0, 0, 72, 0],
                 [0, 0, 48, 0, 0, 80],
                 [0, 0, 0, 0, 0, 0]]

        g = Graph(graph)

        source = 0
        sink = 5

        print("The Max Flow is = %d " % g.FordFulkerson(source, sink))

    elif user == 5:
        print("Exit!!!")

        break

else:
    print("incorrect Entry...Try Again!!!!")
