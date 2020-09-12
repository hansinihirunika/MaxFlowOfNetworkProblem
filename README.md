# MaxFlowOfNetworkProblem
Designed and implemented an efficient algorithm to find the maximum flow in a network. Used Ford Fulkerson Algorithm to find maximum flow of the network based on Python.

Algorithmic Approach

The max flow problems are the problems that we used to find the maximum flow of the network. So, how does it work? In this problem we are going to find the maximum amount of data which we can pass through the entire graph. To solve this max flow problem, we use the algorithm called “Ford Fulkerson”  algorithms.
The “Ford Fulkerson”  algorithm finds the maximum flow from start vertex to end vertex of a graph. The way of this work is first we create the adjacency matrix of the given graph. Then we calculate the minimum number of flow and towards the graph we put “Breadth First Search” method. Then we take the different minimum amounts of flows through the “Breadth First Search”. Then we do this staff over again and again. 


 
In the graph there are two main nodes. 0 is the starting vertex/source of this graph. 5 is the ending vertex/ sink of this graph. Nodes are connected with edges. The edges have an amount, so therefore the graph this called as a weighted graph. Not only that the edges are directed also, therefore the graph called as directed graph. 
The “Ford Fulkerson”  algorithm has a several step to follow. So, in this first we create the adjacency matrix of the graph.

0	1	2	3	4	5

0	0	10	8	0	0	0

1	0	0	10	12	0	0

2	0	4	0	0	14	0

3	0	0	9	0	0	20
  
4	0	0	0	7	0	4

5	0	0	0	0	0	0
                                   
Next step of this process, first we need to do Bread First Search to the entire graph. In the Bread First Search we use a queue. Then we need to have a parent array and a visited array. The parent array basically stores the nodes and the visited array basically store the track of which element was visited.

Queue
	
  0	1	2	3	4	5

Parent Queue						

Visited Queue						

First thing in this method we start with the source node. In the above graph the source node is 0. So, in the queue the first element is also 0.Therfore we put 0 node is visited (T) and also the 0 node has not a parent node, so we put -1 there. Then the next step is in the queue, what are possible paths are open from node 0. We can find 1 and 2 nodes are open from 0. Therefore, we put 1 and 2 in the queue and then called them as visited nodes. They know their parent node, it is 0. The next step is 1 element in queue because in the queue there is a rule first in first out. So, that why 1 came before the 2 comes. Like that we must visit the all possible paths that we can visit in the graph.
	
  0	1	2	3	4	5
  
Parent Queue	-1	0	0	1	2	3

Visited Queue	T	T	T	T	T	T

After this process we can find the augmenting path of the flow. That is 0-1, 1-3, 3-5. In this path we calculate the minimum amount that we can pass through is flow. 0-1 has 10, 1-3 has 5,3-5 has 3. So, among those values the minimum amount is 3. Therefore 3 is the minimum amount that we can pass through this path. Like this method we find the all the possible path that we can reach source to sink. 
 

pseudo-code

bFS Function- we input the residual graph, source, sink, parent
Begin
   Mark all vertices as not visited
   Create a queue for bFS   
   Put start node is 0
   insert start into the queue 
   while queue is not empty, do
      delete element from queue and set to vertex u
      for all vertices v, in the residual graph, do
         if u and v are connected, and  v is unvisited, then
            add vertex v into the queue
            mark v as visited
         End if
   End while
   return true if the sink vertex is visited
End

Ford Fulkerson Function- we input source, sink, parent 

Begin
   Create a residual graph and copy given graph into it
   while bFS(parent, source, sink) is true, do
      pathFlow = float(“INFINITE”)
      s= sink vertex
      while s != source, do
         pathFlow = minimum of pathFlow and residual graph[s], [s]
         s = parent[s]
      End while

      v = sink vertex
      while v != source, do
         u = parent[v]
         residual graph[u],[v] = residual graph[u],[v] – pathFlow
         residualGraph[v],[u] = residual graph[v],[u] + pathFlow
         v = parent[ v]
      End while

     maxFlow = maxFlow + pathFlow
   End while
   return maxFlow
End


Methodology

In this max flow problem, we use source and the sink node. In the code I use source =0 and sink = 5 because in the graph the source that means the start is 0. The end node is 5. In the code I use the same adjacency matrix  as an array that we use above discus.  

graph = [[0, 80, 0, 80, 0, 0],

            [0, 0, 32, 16, 64, 0],
            [0, 0, 0, 0, 0, 80],
            [0, 0, 0, 0, 72, 0],
            [0, 0, 48, 0, 0, 80],
             [0, 0, 0, 0, 0, 0]]

Then I use the print function. In this I use %d formatter. After that called the Ford Fulkerson function, it is passing the source and sink into it. Sink and source are going to be our pointers of each node in the graph.
print("The Max Flow is = %d " % g.FordFulkerson(source, sink))

In the code we declare some thing called a residual graph. We don’t want anything change in the original graph so, we use this residual graph for that purpose.


maxFlow = 0 

There is something called maxflow. It’s kept the track of everything. That means the all the track of the minimum amount of flows in the graph. 


while residual.bFS(source, sink, parent):

We basically called this function “Bread First Search” function. This will return either True or False. It is depending on that execute the next point. It is augmenting the flow while there is a path from source to sink.



def bFS(residual, s, t, parent):
    
    visited = [False] * (residual.ROW)
    
    queue = []
    
    queue.append(s)
    
    visited[s] = True
    

In bFS function we define visited, queue and parent arrays. In here we mark all the vertices as not visited. Then we create a queue for bFS function and append the (s) in the queue and set the visited[s] as True.
u = queue.pop(0)

In here we pop the queue basically pop off the first element because the first in first out.


for ind, va in enumerate(residual.graph[u]):
    
    if visited[ind] == False and va > 0:
        
        queue.append(ind)
        
        visited[ind] = True
        
        parent[ind] = u
        

In this part we get all adjacency vertices of the dequeued vertex u. Then if an adjacency node has not been visited the mark it visited and enqueue it.  

queue.append(ind)

visited[ind] = True

parent[ind] = u


If we find any of satisfy above for condition it add them to the queue. Then makes the visited array as True and put that parent array value in there.
return True if visited[t] else False
Then we check if the sink is visited. As we know we always have to be visited the sink node. If the edges are not 0, we must find the path again and again to solve this problem. Therefore, if visited[t] is not True returns False. So, if we return True only then the while loop will run.


pathFlow = float("INFINITE")

s = sink

while (s != source):

    pathFlow = min(pathFlow, residual.graph[parent[s]][s])
    
    s = parent[s]
    
    
In here we create a variable called pathFlow. S goes to sink. In the while loop s is not the source.


while (v != source):

    u = parent[v]
    
    residual.graph[u][v] -= pathFlow
    
    residual.graph[v][u] += pathFlow
    
    v = parent[v]
    
    
In here also we do the same but the change of this this  residual.graph[u][v] -= pathFlow and
    residual.graph[v][u] += pathFlow 
This pathFlow is the minimum range in the entire path we use. We use adding operation for opposite directions in the graph and we use minus operation for correct directions in the graph.

maxFlow += pathFlow

End of the entire path we basically say maxflow += pathFlow. Because the collection of pathFlow values add and it returns the max Flow of the graph. 


algorithmic performance in terms of Big-O

Big O notation is used to describe the performance or the complexity of an algorithm. So, in our algorithm, O(1) shows an algorithm that will always execute in the same time regardless of the size of the input dataset. E.g.-: user = int(input("What's your choise 1/2/3/4/5? "))
O(N)shows an algorithm whose performance will grow linearly. 
E.g.-: for ind, va in enumerate(residual.graph[u]):
    if visited[ind] == False and va > 0:
        queue.append(ind)
        visited[ind] = True
        parent[ind] = u

O(N2) shows whose performance is directly proportional to the square of the size of the input data set. 
E.g.-: while residual.bFS(source, sink, parent):

     pathFlow = float("INFINITE")
    s = sink
    while (s != source):
        pathFlow = min(pathFlow, residual.graph[parent[s]][s])
        s = parent[s]
    v = sink
    while (v != source):
        u = parent[v]
        residual.graph[u][v] -= pathFlow
        residual.graph[v][u] += pathFlow
        v = parent[v] 
    maxFlow += pathFlow

return maxFlow
