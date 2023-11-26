import sys
from heapq import heapify, heappush, heappop

def dijkstra(graph,start,goal,t):
    shortest_distance={}
    track_predecessors={}
    unseen_nodes=graph
    infinity=9999
    track_path=[]

    for node in unseen_nodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0

    while unseen_nodes:
        min_distance_node=None

        for node in unseen_nodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortest_distance[node]<shortest_distance[min_distance_node]:
                min_distance_node=node

        path_options=graph[min_distance_node].items()

        for child_node,weight in path_options:
            if weight+shortest_distance[min_distance_node]<shortest_distance[child_node]:
                shortest_distance[child_node]=weight+shortest_distance[min_distance_node]
                track_predecessors[child_node]=min_distance_node
        unseen_nodes.pop(min_distance_node)
    currNode=goal
    while currNode!=start:
        try:
            track_path.insert(0,currNode)
            currNode=track_predecessors[currNode]
        except KeyError:
            print("no path found")
            break
    track_path.insert(0,start)
    if shortest_distance[goal]!=infinity:
        print("optimal path is "+str(track_path))
        print("Time taken "+str(shortest_distance[goal]))
    if shortest_distance[goal]>t:
        print("EXPECTD TIME IS GREATER THEN THRESHOLD")
        # exit()
    else:
        print("********Congratulations YOUR TRIP WILL B COMPLECTED IN TIME***********")
    
#shortest path finding using dijkastra ends here

#kanpasck for shopping is starts from here

# W IS CAPACITY
# N NUMBER OF ITMES
# ITEMS KI ARRAY       
def printknapSack(W,item, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    #stores the result of Knapsack
    res = K[n][W]
    print("Maximum profit earned is given by: ")
    print(res)
     
    w = W
    print("Selected items and their cost")
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            
            print(item[i-1],"-",wt[i - 1])
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
            
            
def prims():
    INF = 9999999
    V=int(input("Enter the total number of places to be visited: "))
    #print("Enter the adjacency matrix representing the distance of one place from another\n")
    #G=[]
    #for x in range(V):
    #    a=[]
    #    for y in range(V):
    #        a.append(int(input()))
    #    G.append(a)
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
    G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
    selected = [0, 0, 0, 0, 0]
# set number of edge to 0
    no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
    selected[0] = True
# print for edge and weight
    print("\nthe travel itinerary is as followes\n")
    print("Edge : Weight\n")
    while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + " - " + str(y) + " : " + str(G[x][y]))
        selected[y] = True
        no_edge += 1
    
    


if __name__ == "__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
    }
    # graph = {}

    # size = int(input("Enter the total number of cities "))
    # for i in range(size):
    
    #     dict_name = input("Enter the name of the starting city: ")
    #     graph[dict_name] = {}
    #     n=int(input("Enter number of cities connected to the starting city: "))
    #     for j in range(n):
    #         city=input("Enter the vertex: ")
    #         time=int(input("Time taken to reach from the start city: "))
    #         graph[dict_name][city]=time
    
    src = input("Enter starting point: ")
    dest = input("Enter destination city: ")
    t=int(input("expected time :\n"))
    dijkstra(graph,src,dest,t)

    prims()
    W=int(input("\nEnter maximum weight can : "))
    x=int(input("Enter the number of available items: "))
    items=[]
    print("Enter the items: ")
    for i in range(x):
        items.append(input())
    print(items)
    print("Enter the weight of items: ")
    wt=[]
    for i in range(x):
        wt.append(int(input()))
    print(wt)
    print("enter the max discount of items")
    val=[]
    for i in range(x):
        val.append(int(input()))
    print(val)
    n = len(val)
    printknapSack(W,items, wt, val, n)