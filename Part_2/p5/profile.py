import cProfile
from p5 import tsp

def runTest():
    fname = 'tsp.txt'
    with open(fname, 'r') as ifile:
        rawData = ifile.readlines()[1:18]
    # END with
    points = []
    for line in rawData:
        (x, y) = map(float, line.split())
        points.append((x,y))
    # END for

    result = tsp(points)

    print "Result: {0}".format(result)
# END runTest

cProfile.run('runTest()')
