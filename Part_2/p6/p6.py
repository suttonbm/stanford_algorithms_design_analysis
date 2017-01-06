from collections import defaultdict
import numpy as np
import random
import time

class TwoSat_SCC:
    def __init__(self, filename):
        self.vertices = set()
        self.edges = []

        with open(filename, 'r') as ifile:
            rawData = ifile.readlines()
        # END with

        self.fGraph = defaultdict(list)
        self.rGraph = defaultdict(list)
        for line in rawData[1:]:
            (v, w) = map(int, line.split())

            # Need to add both the literal and its inverse
            self.vertices.add(v)
            self.vertices.add(-v)
            self.vertices.add(w)
            self.vertices.add(-w)

            # Convert the disjunction (rule) into implication graph links
            self.fGraph[-v].append(w)
            self.fGraph[-w].append(v)
            self.rGraph[w].append(-v)
            self.rGraph[v].append(-w)
        # END for
    # END init

    def __dfsLoop(self, reverse=False, debug=False):
        t = time.clock()
        if reverse:
            vList = list(self.vertices)
            self.__vFinishTimes = []
            self.__vFinished = defaultdict(bool)
            graph = self.rGraph
        else:
            vList = self.__vFinishTimes
            graph = self.fGraph
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
            print "Forward Loop Time: {0}".format(time.clock() - t)
        return result
    # END kosarajuSCC

    def check(self):
        self.kosarajuSCC(debug=True)
        for v in self.vertices:
            v_Parent = self.__sccMap[v]
            nv_Parent = self.__sccMap[-v]
            if v_Parent == nv_Parent:
                return False
            # END if
        # END for
        return True
    # END run2sat
# END AdjList

class TwoSat_Papadimitriou:
    def __a(self, x, y):
        return x or y
    def __b(self, x, y):
        return not x or y
    def __c(self, x, y):
        return x or not y
    def __d(self, x, y):
        return not x or not y

    def __init__(self, f):
        with open(f, 'r') as ifile:
            rawdata = ifile.readlines()
        # END with

        # Set number of variables in the constraint set
        self.nVars = int(rawdata[0])
        self.cList = []
        self.cMap = defaultdict(list)

        for line in rawdata[1:]:
            (x, y) = map(int, line.split())

            if x > 0 and y > 0:
                consFunc = self.__a
            elif x < 0 and y > 0:
                consFunc = self.__b
            elif x > 0 and y < 0:
                consFunc = self.__c
            else:
                consFunc = self.__d
            # END if

            self.cMap[abs(x)-1].append(len(self.cList))
            self.cMap[abs(y)-1].append(len(self.cList))
            self.cList.append((abs(x)-1, abs(y)-1, consFunc))
        # END for
    # END init

    def __genRandBoolAry(self):
        ops = [True, False]
        return np.random.choice(ops, self.nVars)
    # END __genRandBoolAry

    def __checkConstraints(self, xVars):
        result = np.zeros(len(self.cList), dtype=np.dtype(bool))
        for i, c in enumerate(self.cList):
            x = c[0]
            y = c[1]
            fn = c[2]
            result[i] = fn(xVars[x], xVars[y])
        # END for
        return result
    # END __checkConstraints

    def check(self):
        nOuter = int(np.log2(self.nVars))
        nInner = 2*self.nVars**2
        consMapAry = np.arange(len(self.cList))
        for n in range(nOuter):
            xVars = self.__genRandBoolAry()
            consStatus = self.__checkConstraints(xVars)
            m = 0
            while m < nInner:
                #print consStatus
                if np.all(consStatus):
                    return True
                # Choose a random failing test
                failTests = consMapAry[np.invert(consStatus)]
                checkTest = random.choice(failTests)
                flipVar = random.choice([0,1])
                # Flip the value of selected variable
                k = self.cList[checkTest][flipVar]
                xVars[k] = not xVars[k]
                # Update the results of relevant tests
                for consIdx in self.cMap[k]:
                    x = self.cList[consIdx][0]
                    y = self.cList[consIdx][1]
                    fn = self.cList[consIdx][2]
                    consStatus[consIdx] = fn(xVars[x], xVars[y])
                # END for
                m+=1
            # END for
        # END for
        return False
    # END check
# END TwoSat

def run2sat(filename):
    ts = TwoSat_SCC(filename)
    return ts.check()
# END run2sat
