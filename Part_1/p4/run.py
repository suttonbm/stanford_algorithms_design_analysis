from tests import tests
from p4 import getSCCs

quiz = { \
            'file': 'SCC.txt', \
            'ans': [434821,968,459,313,211] \
        }

def runTest(filename, ans=None):
    sccList = getSCCs(filename)
    data = sccList.values()
    data.sort(reverse=True)
    result = data[:5]
    while len(result) < 5:
        result.append(0)
    # END while

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
    # END if
# END runTest

def main():
    passed = True
    for test in tests[10:13]:
        print "Running Test: {0}".format(test['file'])
        try:
            runTest(test['file'], test['ans'])
        except AssertionError, e:
            print e.args[0]
            passed = False
        # END try
    # END for
    if passed:
        print "All tests pass."
    else:
        print "Some tests failed."
        return -1
    # END if

    print "Running quiz."
    runTest(quiz['file'], quiz['ans'])
# END main

if __name__ == "__main__":
    main()
