import random
from collections import defaultdict
from copy import copy
import time

class AdjacencyList:
    def __init__(self, filename):
        self.vertices = []
        self.edges = defaultdict(list)

        with open(filename, 'r') as ifile:
            rawData = ifile.readlines()

        for line in rawData:
            tokens = map(int, line.split())
            vertex = tokens[0]
            self.vertices.append(vertex)

            for adj in tokens[1:]:
                if adj > vertex:
                    self.edges[vertex].append(adj)
            # END for
        # END for
    # END __init__
# END AdjacencyList

def runKarger(al, nIter=50, seed=0):
    result = float('inf')
    random.seed(seed)

    for n in range(nIter):
        candidate = karger(al)
        if candidate < result:
            result = candidate
        # END if
    # END for
    return result
# END runKarger

def karger(al):
    # Initialize copy of edges in adjacency list
    edges = []

    # Create copy of edges and vertices
    vertices = set(al.vertices[:])
    for v, adjList in al.edges.iteritems():
        for adj in adjList:
            edges.append((v, adj))
        # END for
    # END for

    # Iteratively contract until two "vertices" are left
    while len(vertices) > 2:
        # Choose index of a random edge to select
        e = random.choice(edges)

        # "Child" vertex
        v = e[0]
        # "Parent" vertex
        w = e[1]

        tmp = []
        for edge in edges:
            if v in edge:
                if w in edge:
                    continue
                elif edge[0] == v:
                    tmp.append((w, edge[1]))
                else:
                    tmp.append((edge[0], w))
            elif w in edge:
                if v in edge:
                    continue
                else:
                    tmp.append(edge)
            else:
                tmp.append(edge)
            # END if
        # END for
        edges = tmp

        # Remove the selected vertex
        vertices.remove(v)
    # END while

    return len(edges)
# END karger
