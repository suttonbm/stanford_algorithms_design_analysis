from tests import tests
from p3_answer import run_A, run_B

def testKnapsack(filename, fn, ans=None):
    print "Testing {0}".format(filename)
    result = fn(filename)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
    # END if
    return

def main():
    print "Testing Solution A"
    for test in tests:
        try:
            if 'p08' in test['file']:
                continue
            testKnapsack(test['file'], run_A, ans=test['soln'])
        except AssertionError as err:
            print "Failed Test: {0}".format(err)
    # END for
    print "Testing Solution B"
    for test in tests:
        try:
            testKnapsack(test['file'], run_B, ans=test['soln'])
        except AssertionError as err:
            print "Failed Test: {0}".format(err)
    # END for

    print "Part A:"
    testKnapsack('knapsack1.txt', run_A)
    print "Part B:"
    testKnapsack('knapsack_big.txt', run_B)
# END main

if __name__=='__main__':
    main()
