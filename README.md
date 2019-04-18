# GraphsAlgorithms
Graph Algorithms Singles-source shortest path and Minimum Spanning Tree (MST)

In this project, two graph algorithms mentioned below are implemented:

Problem 1:
Find shortest paths in both directed and undirected weighted graphs for a given source vertex. Assume there
is no negative edge in your graph. You will print each path and path cost for a given source.

Problem 2:
Given a connected, undirected, weighted graph, find a spanning tree using edges that minimizes the total
weight𝑤 𝑇 = (),*)∈, 𝑤(𝑢, 𝑣). Use Kruskal or Prims algorithm to find Minimum Spanning Tree (MST).
You will printout the edges of the tree and the total cost of your answer.

Input format:
For each problem, you will take input from a text file. Say you want to run algorithm on the following undirected
graph. The corresponding file format would be:
6 10 U
A B 1
A C 2
B C 1
B D 3
B E 2
C D 1
C E 2
D E 4
D F 3
E F 3
A

Here, the first two numbers represent the number of vertices and edges. The letter U stands for undirected graph
(D for directed). From the second line list all edges and its weight (e.g. 𝑒𝑑𝑔𝑒(𝐴, 𝐵) and its weight is 1. The last line
is optional. If given, it represents the source node.
