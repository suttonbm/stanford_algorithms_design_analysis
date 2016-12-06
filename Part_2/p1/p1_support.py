from collections import defaultdict

def calculateQueueCost(l):
    result = 0
    time = 0
    for job in l:
        time += job[1]
        result += time * job[0]
    # END for
    return result
# END calculateQueueCost

def readQueue(filename):
    data = []
    with open(filename, 'r') as ifile:
        njobs = int(ifile.readline())
        for k in range(njobs):
            row = ifile.readline().strip().split()
            data.append((int(row[0]), int(row[1])))
        # END for
    # END with
    return data
# END readQueue

class AdjList:
    def __init__(self, filename):
        with open(filename, 'r') as ifile:
            fileInfo = map(int, ifile.readline().strip().split())
            self.nodes = set(range(fileInfo[0]))
            self.edges = defaultdict(list)
            for k in range(fileInfo[1]):
                row = map(int, ifile.readline().strip().split())
                self.edges[row[0]-1].append((row[1]-1, float(row[2])))
                self.edges[row[1]-1].append((row[0]-1, float(row[2])))
            # END for
        # END with
    # END __init__
# END AdjList
