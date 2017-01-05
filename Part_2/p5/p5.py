from copy import copy
from itertools import combinations
from math import sqrt, floor

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

    def __heldKarp(self):
        vertices = copy(self.vertices)
        # Get Starting Vertex
        v = vertices.pop()
        #print "Starting from Vertex {0}".format(v)

        # Initialize dictionary of sub-problems
        subP = {}
        # Initialize solutions
        for w in vertices:
            subP[(frozenset([w]), w)] = self.getDist(v, w)
        # END for

        for n in range(2, len(vertices)+1):
            print "Paths Of {0} Vertices...".format(n)
            newSubP = {}
            for subset in combinations(vertices, n):
                S = frozenset(subset)
                #print "Path Including {0}".format(S)
                for w in subset:
                    l = frozenset([w])
                    candidates = []
                    for x in S-l:
                        candidates.append(subP[(S-l, x)] + self.getDist(x, w))
                    # END for
                    #print "{0} Candidate Paths".format(len(candidates))
                    newSubP[(S, w)] = min(candidates)
                    #print "Min Path has Length {0}".format(min(candidates))
                # END for
            # END for
            subP = newSubP
        # END for

        print "Final Iteration..."
        S = frozenset(vertices)
        candidates = []
        for w in vertices:
            candidates.append(subP[(S, w)] + self.getDist(w, v))
        # END for
        #print "There are {0} candidate paths.".format(len(candidates))
        print "The shortest path has length {0}".format(min(candidates))

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
