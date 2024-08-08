#!/usr/bin/python3


def bfs(vertices, adjacencies, root):
    """
    Function which takes a graph (in the form of a vertrex list and
    adjacency list of lists) and a root vertex as input and performs
    a breadth-first-search to return the distance between the root and
    every other vetex in the graph.
    """

    distances = [0 if v is root else -1 for v in vertices]
    Q = [root]

    while Q != []:
        w = Q.pop(0)
        for v in adjacencies[w]:
            if distances[v] == -1:
                distances[v] = distances[w] + 1
                Q.append(v)

    return distances


# Example
vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
adjacencies = [[4, 5, 8],
               [9],
               [3, 5, 7],
               [2, 7],
               [0, 6],
               [0, 2, 7],
               [4, 8, 10],
               [5, 2, 3],
               [0, 6],
               [1],
               [6]]
root = 2

print(bfs(vertices, adjacencies, root))
