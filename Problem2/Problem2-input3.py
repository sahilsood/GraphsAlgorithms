#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:24:19 2018

@author: sahilsood
"""

import heapq
from collections import defaultdict
import time


def min_spanning_tree(graph, start_node):
    mst = defaultdict(set)
    global totalcost
    # Creating a set of the visited nodes
    visited = set([start_node])
    edges = [
        (cost, start_node, to)
        for to, cost in graph[start_node].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            totalcost = int(cost)
            print('Path cost from '+str(frm)+' To '+str(to)+' : '+str(cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next)) 
    return mst

def main():
    # The below line takes the input from the local drive
    inputfile = open("../Problem2/input3.txt", "r")
    lines = inputfile.readlines()
    edges = []
    for line in lines:
        edges.append(line.split())
    last = list(edges)[-1]
    first = list(edges)[0]
    noofnodes = first[0]
    noofedges = first[1]
    graphtype = first[2]
    
    edges.pop(0)
    
    if(len(last)==1):
        edges.pop()
    di = {}
    for li in edges:
        di.setdefault(li[0],{})[li[1]]=li[2]
    firstnode = list(di)[0]
    # The below line takes the first node as start node
    startnode = firstnode[0]
    print('\nSource vertex: '+str(startnode)+'\n')
    print('Number of Nodes: '+str(noofnodes)+'\n')
    print('Number of Edges: '+str(noofedges)+'\n')
    if graphtype == 'U':
        print('Graph Type: Undirected\n')
    else:
        print('Graph Type: Directed\n')
    print('----------------------------------')
    result = dict(min_spanning_tree(di, startnode))
    print('----------------------------------\n')
    print('Edges of the tree for a Minimum Spanning Tree: \n')
    for key in result:
        print(''+str(key)+' -> '+str(result[key]))
        print('----------------------------------')
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Program Runtime: %s seconds" % (time.time() - start_time))