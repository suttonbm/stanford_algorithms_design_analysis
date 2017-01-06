from collections import defaultdict
import numpy as np
import random

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
    ts = TwoSat(filename)
    return ts.check()
# END run2sat
