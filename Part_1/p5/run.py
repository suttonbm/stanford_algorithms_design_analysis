from tests import tests, quiz
from p5 import AdjList

def runTest(fname, src, dest, ans=None, debug=False):
    print "Running {0}: {1} -> {2}".format(fname, src, dest)
    al = AdjList(fname)
    result = al.dijkstra(src, dest)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
# END runTest

def main():
    print "Running Tests"
    passed = True
    for test in tests:
        try:
            runTest(test['file'], test['src'], test['dest'], test['ans'], debug=True)
        except AssertionError, e:
            print e.args[0]
            passed = False
        # END try
    # END for
    if not passed:
        print "Some Tests Failed!"
        return -1
    # END if
    print "All Tests Pass!"

    print "Running Quiz"
    for q in quiz:
        runTest(q['file'], q['src'], q['dest'], q['ans'])
    # END for
    print "Quiz Passed."
# END main

if __name__ == '__main__':
    main()
