p1_a_tests = {"Test0.txt": 30, "Test1.txt": 31814, "Test2.txt": 61545, "Test3.txt": 688647}
p1_b_tests = {"Test0.txt": 28, "Test1.txt": 31814, "Test2.txt": 60213, "Test3.txt": 674634}
p1_c_tests = {}

p1_a_quiz = {"jobs.txt": None}
p1_b_quiz = {"jobs.txt": None}

from p1_support import calculateQueueCost, readQueue
import p1a_Answer as p1a
import p1b_Answer as p1b

def test_queue(tests, sortFN):
    for filename, answer in tests.iteritems():
        print "Testing {0}".format(filename)
        data = readQueue(filename)
        sortedData = sortFN(data)
        result = calculateQueueCost(sortedData)

        print "Result: {0}; Expected: {1}".format(result, answer)
        if result == answer:
            print "PASS"
        else:
            print "FAIL"
        # END if
    # END for
# END  test_P1a



def main():
    #print "Running tests for Part A:"
    #test_queue(p1_a_tests, p1a.sortQueue)
    #print "Running tests for Part B:"
    #test_queue(p1_b_tests, p1b.sortQueue)
    print "Running Quiz Problem for Part A"
    test_queue(p1_a_quiz, p1a.sortQueue)
    print "Running Quiz Problem for Part B"
    test_queue(p1_b_quiz, p1b.sortQueue)
    pass
# END __main__

if __name__ == "__main__":
    main()
# END if