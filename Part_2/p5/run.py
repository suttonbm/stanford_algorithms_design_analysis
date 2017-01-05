from tests import tests
from p5 import tsp

def runTest(lines=-1, ans=None):
    fname = 'tsp.txt'
    with open(fname, 'r') as ifile:
        if lines == -1:
            print "Running Quiz."
            rawData = ifile.readlines()[1:]
        else:
            print "Running Test on First {0} Lines".format(lines)
            rawData = ifile.readlines()[1:(lines+1)]
        # END if
    # END with
    points = []
    for line in rawData:
        (x, y) = map(float, line.split())
        points.append((x,y))
    # END for

    result = tsp(points)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
    # END if
# END runTest

def main():
    failTest = False
    for test in tests[:4]:
        try:
            runTest(test['npts'], test['ans'])
            print "Test OK"
        except AssertionError, e:
            print "Assertion Error: {0}".format(e.args[0])
            failTest = True
        # END try
    # END for
    if failTest:
        print "Some Tests Failed!"
        return -1
    # END if

    runTest()
# END main

if __name__ == '__main__':
    main()
