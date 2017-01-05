from p4 import AdjList
from tests import tests

quiz = [{ \
            'file': 'g1.txt', \
            'ncyc': False, \
            'minPath': None \
        }, { \
            'file': 'g2.txt', \
            'ncyc': False, \
            'minPath': None \
        }, { \
            'file': 'g3.txt', \
            'ncyc': False, \
            'minPath': None \
        }, { \
            'file': 'large.txt', \
            'ncyc': False, \
            'minPath': None \
        }]

def testMinCycle(filename, ans=None):
    print "Running Test: {0}".format(filename)
    al = AdjList(filename)
    al.getAllPaths()
    result = al.getMinPath()

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
    # END if
# END testMinCycle

def testMinPaths(al, ans=[]):
    pass
# END testMinPaths

def main():
    print "Running Tests"
    success = True
    for test in tests:
        try:
            if test['ncyc']:
                _ = testMinCycle(test['file'], ans="NULL")
            else:
                al = testMinCycle(test['file'], ans=test['minPath'])
                if len(test['paths']) > 0:
                    testMinPaths(al, test['paths'])
                # END if
            # END if
        except AssertionError, e:
            print "Assertion Error: {0}".format(e.args[0])
            success = False
        # END try
    # END for
    if not success:
        print "Some Tests Failed"
        return -1
    # END if

    print "Running Quiz"
    for q in quiz:
        testMinCycle(q['file'])
    # END for
# END main

if __name__ == '__main__':
    main()
