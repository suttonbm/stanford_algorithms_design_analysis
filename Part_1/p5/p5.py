from collections import defaultdict
from DictBinHeap import DictBinHeap

# TODO: Implement heap-based version of this algorithm

class AdjList:
    def __init__(self, filename):
        self.vertices = set()

        with open(filename, 'r') as ifile:
            rawData = ifile.readlines()
        # END with

        self.fGraph = defaultdict(list)
        for line in rawData:
            vData = line.split()
            v = int(vData[0])
            self.vertices.add(v)
            for tok in vData[1:]:
                (w,d) = map(int, tok.split(','))
                self.fGraph[v].append((w,d))
            # END for
        # END for
    # END init

    def dijkstra(self, src, dest):
        assert src in self.vertices, "Specified source not in graph."
        assert dest in self.vertices, "Specified destination not in graph."

        if src == dest:
            return 0

        heap = DictBinHeap()
        for v in self.vertices:
            heap.push(v, float('inf'))
        # END for
        heap.updateValue(src, 0)
        visited = set([src])

        minV = src; minDist = 0
        while dest not in visited:
            if minDist == float('inf'):
                print "No Path Exists."
                return -1
            # END if
            if minV == dest:
                return minDist

            #print "Exploring adjacent vertices for {0}".format(minV)
            for w, d in self.fGraph[minV]:
                if w in visited:
                    continue
                # END if

                tDist = heap.getValue(w)
                pDist = minDist + d

                #print "Adjacent vertex {0}".format(w)
                #print "Tentative Distance {0}".format(tDist)
                #print "Potential Distance {0}".format(pDist)

                if pDist < tDist:
                    #print "Updating Distance"
                    heap.updateValue(w, pDist)
                # END if
            # END if
            visited.add(minV)
            minV, minDist = heap.pop()
        # END while
    # END djikstra
