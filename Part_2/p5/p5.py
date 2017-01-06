from copy import copy
from itertools import combinations
from math import sqrt, floor
import numpy as np

# TODO: Can I make this faster using simulated annealing or another approximation algorithm?

import operator as op
def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
# END nCr

class AdjList:
    def __init__(self, points):
        self.vertices = set(range(len(points)))
        self.edges = {}
        self.points = {i: pt for i, pt in enumerate(points)}
    # END __init__

    def getDist(self, v, w):
        if (v,w) in self.edges:
            return self.edges[(v,w)]
        elif (w,v) in self.edges:
            return self.edges[(w,v)]
        else:
            dist = sqrt((self.points[w][0] - self.points[v][0])**2 + \
                        (self.points[w][1] - self.points[v][1])**2)
            self.edges[(v,w)] = dist
            return dist
        # END if
    # END getDist

    def __bitmap2Index(self, bitmap):
        pass

    def __heldKarp(self):
        vertices = copy(self.vertices)
        # Get Starting Vertex
        v = max(vertices)
        vertices.remove(v)

        # Initialize array to store subproblem solutions
        nSubproblems = 2**len(vertices)
        subP = np.zeros((nSubproblems, len(vertices)), dtype=np.dtype('f4'))

        # Initialize baseline solutions
        for w in vertices:
            bitmask = 1 << w
            subP[bitmask, w] = self.getDist(v, w)
        # END for

        for n in range(2, len(vertices)+1):
            print "Paths Of {0} Vertices...".format(n)
            newSubP = np.zeros((nSubproblems+1, len(vertices)), dtype=np.dtype('f4'))
            for subset in combinations(vertices, n):
                S = sum([1 << x for x in subset])
                #print "Path Including {0}".format(S)
                for w in subset:
                    P = S - (1 << w)
                    minPath = float("inf")
                    for x in subset:
                        if x == w:
                            continue
                        candidate = subP[P, x] + self.getDist(x, w)
                        if candidate < minPath:
                            minPath = candidate
                    newSubP[S, w] = minPath
                    #print "Min Path has Length {0}".format(min(candidates))
                # END for
            # END for
            subP = newSubP
        # END for

        print "Final Iteration..."
        S = 2**len(vertices)-1
        candidates = []
        for w in vertices:
            candidates.append(subP[S, w] + self.getDist(w, v))
        # END for
        #print "There are {0} candidate paths.".format(len(candidates))
        #print "The shortest path has length {0}".format(min(candidates))

        return min(candidates)
    # END heldKarp

    def runTsp(self, method='held-karp'):
        if method == 'held-karp':
            return self.__heldKarp()
        # END if
    # END runTsp
# END AdjList

def tsp(points):
    al = AdjList(points)
    result = al.runTsp()
    return floor(result)
# END tsp
