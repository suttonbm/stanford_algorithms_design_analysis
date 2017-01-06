from test import tests
from p6 import run2sat

quizzes = [{
                'f': '2sat1.txt', \
            }, {
                'f': '2sat2.txt', \
            }, {
                'f': '2sat3.txt', \
            }, {
                'f': '2sat4.txt', \
            }, {
                'f': '2sat5.txt', \
            }, {
                'f': '2sat6.txt', \
            }]

def runTest(f, ans=None):
    print "Running 2Sat on {0}".format(f)
    result = run2sat(f)

    if ans is not None:
        assert result == ans, "Got {0}, Expected {1}".format(result, ans)
    else:
        print "Result: {0}".format(result)
        return result
    # END if
# END runTest

def main():
    failed = False
    for test in tests:
        try:
            runTest(test['f'], test['ans'])
            print "Success"
        except AssertionError, e:
            print "Failed: {0}".format(e.args[0])
            failed = True
        # END try
    # END for
    if failed:
        print "Some Tests Failed."
        return -1
    # END if

    ans = ""
    for quiz in quizzes:
        if runTest(quiz['f']):
            ans += "1"
        else:
            ans += "0"
    # END for
# END main

if __name__ == '__main__':
    main()
