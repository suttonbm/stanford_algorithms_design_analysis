from tests import tests
from p1 import getInversions

quiz = { \
            'file': 'IntegerArray.txt', \
            'ans': 2407905288 \
        }

def runTest(filename, ans=None):
    data = []
    with open(filename, 'r') as ifile:
        data = map(int, ifile.readlines())
    # END with

    try:
        _, result = getInversions(data)
    except RuntimeError:
        print "Exception Raised in Execution."

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    # END if

    return result
# END runTest

def main():
    for test in tests:
        _ = runTest(test['file'], ans=test['ans'])
    # END for

    result = runTest(quiz['file'], ans=quiz['ans'])

    print "Quiz Result: {0}".format(result)
    print "Passed All Tests"
# END main

if __name__ == '__main__':
    main()
