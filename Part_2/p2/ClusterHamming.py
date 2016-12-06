from collections import defaultdict
from UnionFind import UnionFind
from pUtils import getHamming
from itertools import combinations
from copy import copy

class ClusterHamming:
    def __init__(self, data):
        (nodes, self.bits) = map(int, data.pop(0).split())
        self.uf = UnionFind()
        for n in range(nodes):
            self.uf.makeSet(n)
        # END for

        self.hammingData = defaultdict(list)
        for n in range(nodes):
            s = data[n].replace(' ', '')
            self.hammingData[s].append(n)
        # END for
    # END __init__

    def flip(self, s, flipbits):
        """
        Given an input string (s) and tuple of indices (flipbits), returns a new
        string with bits at specified indices flipped.

        The length of (flipbits) determines the resulting hamming distance.
        """
        result = ''
        for i, c in enumerate(s):
            if i in flipbits:
                if c == '1':
                    result += '0'
                else:
                    result += '1'
            else:
                result += c
        return result
    # END flip

    def getHammingPermutations(self, s, n):
        """
        Generate permutations of s whose distance is less than or equal to n
        """
        result = []
        result.append(s)
        for d in range(1, n+1):
            for flipbits in combinations(range(self.bits), d):
                result.append(self.flip(s, flipbits))
            # END for
        # END for
        return result
    # END getHammingPermutations

    def printSummary(self):
        resultMap = defaultdict(list)
        for k,v in self.hammingData.iteritems():
            cluster = self.uf.find(v)
            resultMap[cluster].append(k)
        # END for

        for k,v in resultMap.iteritems():
            print "\n\nCluster {0}:".format(k)
            for key in v:
                print "\t{0}".format(key)
            # END for
        # END for
    # END printSummary

    def run(self, minDist):
        data = copy(self.hammingData)
        while data:
            (nodeKey, refNodes) = data.popitem()
            if len(refNodes) > 1:
                for i in range(1, len(refNodes)):
                    self.uf.union(refNodes[0], refNodes[i])
                # END for
            # END for

            nearestNodes = self.getHammingPermutations(nodeKey, minDist-1)
            for testNodeKey in nearestNodes:
                if testNodeKey not in data:
                    continue

                testNodes = self.hammingData[testNodeKey]
                for n in testNodes:
                    if self.uf.find(n) == self.uf.find(refNodes[0]):
                        continue
                    self.uf.union(refNodes[0], n)
                # END for
            # END for
        # END while

        return self.uf.countGroups()
    # END run
# END ClusterHamming
