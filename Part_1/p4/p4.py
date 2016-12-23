from collections import defaultdict
import time

class AdjList:
    def __init__(self, filename):
        self.vertices = set()
        self.edges = []

        with open(filename, 'r') as ifile:
            rawData = ifile.readlines()
        # END with

        self.rGraph = defaultdict(list)
        self.fGraph = defaultdict(list)
        for line in rawData:
            (v, w) = map(int, line.split())
            self.vertices.add(v)
            self.vertices.add(w)
            self.rGraph[w].append(v)
            self.fGraph[v].append(w)
        # END for
    # END init

    def __prepareGraph(self, reverse=False):
        if reverse:
            return self.rGraph
        else:
            return self.fGraph
    # END __prepareGraph

    def __dfsLoop(self, reverse=False, debug=False):
        t = time.clock()
        if reverse:
            vList = list(self.vertices)
            self.__vFinishTimes = []
            self.__vFinished = defaultdict(bool)
            graph = self.__prepareGraph(reverse=True)
        else:
            vList = self.__vFinishTimes
            graph = self.__prepareGraph(reverse=False)
        # END if
        if debug:
            print "DFS Loop Setup Time: {0}".format(time.clock() - t)

        self.__explored = defaultdict(bool)
        self.__sccMap = {}
        if debug:
            dfsCalls = 0
            dfsTime = 0
            t1 = time.clock()
        for v in vList:
            if not self.__explored[v]:
                if debug:
                    dfsCalls += 1
                    t2 = time.clock()
                self.__leader = v
                self.__dfs(graph, v)
                if debug:
                    dfsTime += (time.clock() - t2)
            # END if
        # END for
        if debug:
            print "Ran DFS Loop in Time: {0}".format(time.clock() - t1)
            print "Performed DFS Search On {0}/{1} Nodes".format(dfsCalls, len(vList))
            print "Avg Time of DFS Search: {0}".format(dfsTime / dfsCalls)

        return self.__sccMap
    # END dfsLoop

    def __dfs(self, G, v):
        q = [v]
        while q:
            if not self.__explored[q[0]]:
                #print "Exploring {0}".format(q[0])
                self.__explored[q[0]] = True
                self.__sccMap[q[0]] = self.__leader
                for w in G[q[0]]:
                    #print "Checking child {0}".format(w)
                    if not self.__explored[w]:
                        q.insert(0, w)
                    # END if
                # END for
            else:
                u = q.pop(0)
                if not self.__vFinished[u]:
                    self.__vFinishTimes.insert(0,u)
                    self.__vFinished[u] = True
                    #print "Finish Status: {0}".format(self.__vFinishTimes)
                # END if
            # END if
        # END while
    # END _dfs

    def kosarajuSCC(self, debug=False):

        if debug:
            print "Starting reverse loop"
        t = time.clock()
        _ = self.__dfsLoop(reverse=True, debug=debug)
        if debug:
            print "Reverse Loop Time: {0}".format(time.clock() - t)
            print "Starting forward loop"
        t = time.clock()
        result = self.__dfsLoop(debug=debug)
        if debug:
            print "Forward Loop TimeL {0}".format(time.clock() - t)
        return result
    # END kosarajuSCC

    def tarjanSCC(self):
        pass
    # END tarjanSCC
# END AdjList

def getSCCs(filename):
    al = AdjList(filename)
    sccMap = al.kosarajuSCC(debug=True)

    result = defaultdict(int)
    for head in sccMap.itervalues():
        result[head] += 1
    # END for

    return result
# END getSCCs
