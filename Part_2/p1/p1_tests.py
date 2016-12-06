p1_a_tests = {"Test0.txt": 30, "Test1.txt": 31814, "Test2.txt": 61545, "Test3.txt": 688647}
p1_b_tests = {"Test0.txt": 28, "Test1.txt": 31814, "Test2.txt": 60213, "Test3.txt": 674634}
#p1_c_tests = {"TestPrim1.txt": -236, "TestPrim2.txt": 4, "TestPrim3.txt": 16, "TestPrim4.txt": -3}
p1_c_tests = {"TestPrim1.txt": -236}

p1_a_quiz = {"jobs.txt": 69119377652}
p1_b_quiz = {"jobs.txt": 67311454237}
p1_c_quiz = {"edges.txt": -3612829}

from p1_support import calculateQueueCost, readQueue, AdjList
import p1a_Answer as p1a
import p1b_Answer as p1b
import p1c_Answer as p1c
import timeit

def test_queue(tests, sortFN):
    for filename, answer in tests.iteritems():
        data = readQueue(filename)
        sortedData = sortFN(data)
        result = calculateQueueCost(sortedData)

        if answer is not None:
            if result != answer:
                print "Result: {0}; Expected: {1}".format(result, answer)
                print "FAIL"
            # END if
        else:
            print "Result: {0}".format(result)
        # END if
    # END for
# END  test_queue

def test_prim(tests, fn):
    for filename, answer in tests.iteritems():
        al = AdjList(filename)
        result = fn(al)

        if answer is not None:
            if result != answer:
                print "Result: {0}; Expected: {1}".format(result, answer)
                print "FAIL"
            # END if
        else:
            print "Result: {0}".format(result)
        # END if
    # END for
    pass
# END test_prim

def main():
    #print "Running tests for Part A:"
    test_queue(p1_a_tests, p1a.sortQueue)
    #print "Running tests for Part B:"
    test_queue(p1_b_tests, p1b.sortQueue)
    #print "Running Quiz Problem for Part A:"
    test_queue(p1_a_quiz, p1a.sortQueue)
    #print "Running Quiz Problem for Part B:"
    test_queue(p1_b_quiz, p1b.sortQueue)
    #print "Running tests for Part C (Algo1):"
    test_prim(p1_c_tests, p1c.primMST_Basic)
    test_prim(p1_c_quiz, p1c.primMST_Basic)
    #print "Running tests for Part C (Algo2):"
    test_prim(p1_c_tests, p1c.primMST_Heap1)
    test_prim(p1_c_quiz, p1c.primMST_Heap1)
    #print "Running tests for Part C (Algo3):"
    test_prim(p1_c_tests, p1c.primMST_Heap2)
    test_prim(p1_c_quiz, p1c.primMST_Heap2)

    print ""
    print ""
    print ""

    n = 10
    print "Timing the basic (quadratic) implementation:"
    print timeit.timeit('time1()', 'from p1_tests import time1', number=n)/n
    print "Timing the first heap implementation:"
    print timeit.timeit('time2()', 'from p1_tests import time2', number=n)/n
    print "Timing the second heap implementation:"
    print timeit.timeit('time3()', 'from p1_tests import time3', number=n)/n
    pass
# END __main__

def time1():
    test_prim(p1_c_quiz, p1c.primMST_Basic)
# END time1

def time2():
    test_prim(p1_c_quiz, p1c.primMST_Heap1)
# END time1

def time3():
    test_prim(p1_c_quiz, p1c.primMST_Heap2)
# END time1

if __name__ == "__main__":
    main()
# END if
