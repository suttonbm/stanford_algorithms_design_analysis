from tests import tests
from p3 import AdjacencyList, runKarger

quiz = { \
            'file': 'kargerMinCut.txt', \
            'ans': 17 \
        }

def runTest(filename, ans=None):
    print "Running Test {0}".format(filename)
    al = AdjacencyList(filename)
    result = runKarger(al)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
# END runTest

def main():
    print "Running Tests"
    for test in tests:
        runTest(test['file'], test['ans'])
    print "All Tests Pass"

    print "Running Quiz"
    runTest(quiz['file'], quiz['ans'])
# END main

if __name__ == '__main__':
    main()
