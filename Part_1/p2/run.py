from tests import tests
from p2 import p2a, p2b, p2c, pivot

quiz = {
    'file': 'QuickSort.txt', \
    'ans1': 162085, \
    'ans2': 164123, \
    'ans3': 138382 \
}

def runTest(filename, fn, ans=None):
    data = []
    with open(filename, 'r') as ifile:
        data = map(int, ifile.readlines())

    result = fn(data)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    # END if

    return result
# END runTest

def main():
    print "Running Tests"
    for test in tests:
        _ = runTest(test['file'], p2a, test['ans1'])
        _ = runTest(test['file'], p2b, test['ans2'])
        _ = runTest(test['file'], p2c, test['ans3'])

    print "Running Quiz A"
    result = runTest(quiz['file'], p2a, quiz['ans1'])
    print "Result: {0}".format(result)

    print "Running Quiz B"
    result = runTest(quiz['file'], p2b, quiz['ans2'])
    print "Result: {0}".format(result)

    print "Running Quiz C"
    result = runTest(quiz['file'], p2c, quiz['ans3'])
    print "Result: {0}".format(result)

    print "All Tests Pass"
# END main

if __name__ == '__main__':
    main()
