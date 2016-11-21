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