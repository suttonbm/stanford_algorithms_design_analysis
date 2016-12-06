from UnionFind import UnionFind
from operator import itemgetter

class Kruskal:
    def __init__(self, data):
        nodes = int(data[0].split()[0])
        self.ufSet = UnionFind()
        for n in range(nodes):
            self.ufSet.makeSet(n)
        # END for

        self.edges = []
        for k in data[1:]:
            row = map(int, k.strip().split())
            self.edges.append((row[0]-1, row[1]-1, row[2]))
        # END for

        self.edges.sort(key=itemgetter(2))
    # END __init__

    def mstKruskal(self):
        mst = []
        l = 0
        for edge in self.edges:
            s1 = self.ufSet.find(edge[0])
            s2 = self.ufSet.find(edge[1])
            if s1 == s2:
                continue
            # END if

            self.ufSet.union(edge[0], edge[1])
            mst.append(edge)
            l += edge[2]
        # END for

        self.mst = mst
        return l
    # END mstKruskal

    def clusterKruskal(self, k):
        print "Running Clustering, k={0}".format(k)
        done = False
        for edge in self.edges:
            s1 = self.ufSet.find(edge[0])
            s2 = self.ufSet.find(edge[1])
            if s1 == s2:
                continue
            # END if
            if not done:
                self.ufSet.union(edge[0], edge[1])
            else:
                print "Smallest unallocated edge: {0}".format(edge)
                return edge[2]
            # END if

            if self.ufSet.countGroups() == k:
                done = True
            # END if
        # END for
    # END clusterKruskal
# END AdjList
