#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 22:19:31 2018

@author: sahilsood
"""

import collections
import heapq
import time

def shortestPath(edges, source, dnode):
    # The below if-else condition checks whether the input graph is an undirected or directed graph and adds the nodes in the set accordingly
    if graphtype == 'U':
        graph = collections.defaultdict(set)
        for l,r,c in edges:
            graph[l].add((c, r))
            graph[r].add((c, l))
            
    else:
        graph = collections.defaultdict(set)
        for l,r, c in edges:
            graph[l].add((c, r))
            
    # Here we are creating a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    # Now we traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # Visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # Compare the dnode value
            if node == dnode:
                return (cost, path)
            # Visit the neighbours
            for c, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+int(c), neighbour, path))
    return float("inf")



def main():
    # The below line takes the input from the local drive
    inputfile = open("../Problem1/input3.txt", "r")
    lines = inputfile.readlines()
    edges = []
    global graphtype
    for line in lines:
        edges.append(line.split())
    last = list(edges)[-1]
    first = list(edges)[0]
    noofnodes = first[0]
    noofedges = first[1]
    graphtype = first[2]
    
    edges.pop(0)
    # The below if condition checks if the startnode is present at the last line
    if(len(last)==1):
        startnode=''.join(last)
        edges.pop()
    # If the start node is not present, the below else condition takes the first node as start node
    else:
        print("\nStart node is not present in the input file. Choosing the first node as Start node")
        firstnode = list(edges)[0]
        startnode = firstnode[0]
    print('\nSource vertex: '+str(startnode)+'\n')
    print('Number of Nodes: '+str(noofnodes)+'\n')
    print('Number of Edges: '+str(noofedges)+'\n')
    if graphtype == 'U':
        print('Graph Type: Undirected\n')
    else:
        print('Graph Type: Directed\n')
    print ("Shortest paths from the source vertex to each vertex in the weighted graphs: ")
    
    n = [x[0] for x in edges]
    n.extend(y[1] for y in edges)
    destnode = list((set(n)))
    print('----------------------------------')
    for i in destnode:
        print (str(startnode)+" -> "+str(i)+":")
        result = shortestPath(edges, startnode, i)
        print('Path Cost: '+str(result[0]))
        print('Path: '+str(result[1]))
        print('----------------------------------')



if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Program Runtime: %s seconds" % (time.time() - start_time))