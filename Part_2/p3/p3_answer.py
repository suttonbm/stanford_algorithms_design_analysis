from p3_support import readData
import sys
from collections import defaultdict

def printData(x, i, data):
    sys.stdout.write('+' + '-'*(2*i-1) + '+\n')
    for n in range(1, x+1):
        sys.stdout.write('| ')
        for m in range(i):
            v = data[(n, m)]
            sys.stdout.write(' {0}'.format(v))
        # END for
        sys.stdout.write('|\n')
    # END for
    sys.stdout.write('+' + '-'*(2*i-1) + '+\n\n\n')
    sys.stdout.flush()


def run_A(filename):
    (c, values, weights) = readData(filename)
    data = defaultdict(int)
    for x in range(min(weights), c+1):
        for i in range(len(values)):
            if x >= weights[i]:
                data[(x, i)] = max(data[(x, i-1)], \
                                    data[(x-weights[i], i-1)] + values[i])
            else:
                data[(x, i)] = data[(x, i-1)]
            # END if
        # END for
    # END for

    #printData(c, len(values), data)

    return data[(c, len(values)-1)]

def findRelevantCells(c, weights):
    data = defaultdict(list)
    data[len(weights)-1].append(c)
    count = 1

    for i in range(len(weights)-1, -1, -1):
        cells = set()
        for x in data[i]:
            cells.add(x)
            if (x-weights[i]) > 0:
                cells.add(x-weights[i])
            # END if
        # END for
        data[i-1] = sorted(list(cells))
        count += len(data[i-1])
    # END for

    print "Found {0} relevant cells.".format(count)
    print "Compressed Problem by {0}%.".format(1 - float(count)/(c*len(weights)))

    return data

def run_B(filename):
    (c, values, weights) = readData(filename)
    relevantCells = findRelevantCells(c, weights)
    data = defaultdict(int)
    for i in range(len(weights)):
        for x in relevantCells[i]:
            if x >= weights[i]:
                data[(x, i)] = max(data[(x, i-1)], \
                                    data[(x-weights[i], i-1)] + values[i])
            else:
                data[(x, i)] = data[(x, i-1)]
            # END if
        # END for
    # END for

    return data[(c, len(values)-1)]
