class UnionFind:
    def __init__(self):
        self.data = {}
    # END __init__

    def makeSet(self, x):
        self.data[x] = (x, 0)
    # END makeSet

    def find(self, x):
        assert x in self.data, "Use makeSet() to add this item first."
        if self.data[x][0] == x:
            return x
        else:
            self.data[x] = (self.find(self.data[x][0]), self.data[x][1])
        # END if
        return self.data[x][0]
    # END find

    def union(self, x, y):
        assert x in self.data, "Use makeSet() to add this item first."
        assert y in self.data, "Use makeSet() to add this item first."

        (xRoot, xDepth) = self.data[self.find(x)]
        (yRoot, yDepth) = self.data[self.find(y)]

        if xRoot == yRoot:
            return

        if xDepth < yDepth:
            self.data[xRoot] = (yRoot, xDepth)
        elif yDepth < xDepth:
            self.data[yRoot] = (xRoot, yDepth)
        else:
            self.data[yRoot] = (xRoot, yDepth)
            self.data[xRoot] = (xRoot, xDepth + 1)
        # END if
    # END union

    def countGroups(self):
        return sum(k == v[0] for k, v in self.data.iteritems())
    # END countGroups

    def dump(self):
        print self.data
# END UnionFind
