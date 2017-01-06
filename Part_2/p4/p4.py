from collections import defaultdict
import numpy as np

# TODO: Implement the other methods of APSP problem and compare speed.

class AdjList:
    def __init__(self, f):
        with open(f, 'r') as ifile:
            rawData = ifile.readlines()
        # END with
        (v, _) = map(int, rawData[0].split())
        self.n = v
        self.vertices = range(self.n)
        self.cost = {}
        self.adj = defaultdict(list)
        for line in rawData[1:]:
            (v, w, c) = map(int, line.split())
            self.adj[v-1].append(w-1)
            self.cost[(v-1, w-1)] = c
        # END for

        self.shortPathData = None
    # END __init__

    def getAllPaths(self):
        oldData = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    oldData[i,j] = 0
                elif j in self.adj[i]:
                    oldData[i,j] = self.cost[(i,j)]
                else:
                    oldData[i,j] = float('inf')
                # END if
            # END for
        # END for

        for k in range(1, self.n):
            data = np.zeros((self.n, self.n))
            for i in range(self.n):
                for j in range(self.n):
                    data[i,j] = min(oldData[i,j], \
                                    oldData[i,k] + oldData[k,j])
                # END for
            # END for
            oldData = data
        # END for

        negCyc = False
        for i in range(self.n):
            if data[i,i] < 0:
                negCyc = True
            # END if
        # END for

        if negCyc:
            self.shortPathData = "NULL"
        else:
            self.shortPathData = data
        # END if
    # END getAllPaths

    def getMinPath(self):
        if self.shortPathData is None:
            print "Run shortest paths first."
        elif self.shortPathData == "NULL":
            return self.shortPathData
        else:
            return np.min(self.shortPathData)
        # END if
    # END getAllPaths
# END AdjList
