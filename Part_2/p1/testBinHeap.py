from BinHeap import BinHeap
import random

def testBinHeap():
    test = [1,2,3,4,5,6,7,8,9]

    #+----------------------------------------------------- Test Insert ---+#
    random.shuffle(test)
    minheap = BinHeap(type='min')
    maxheap = BinHeap(type='max')
    for n in test:
        minheap.push(n)
        maxheap.push(n)
    # END for
    if minheap.heap[1] != 1:
        print "Min Heap Failed Insert Test"
        print minheap.heap
        return -1
    if maxheap.heap[1] != 9:
        print "Max Heap Failed Insert Test"
        print maxheap.heap
        return -1
    # END if

    #+---------------------------------------------------- Test Pop -----+#
    v = minheap.pop()
    if v != 1:
        print "Min Heap Extracted Wrong Value"
        print v
        print minheap
        return -1
    if minheap.heap[1] != 2:
        print "Min Heap Failed to Bubble Up"
        print minheap
        return -1
    # END if
    minheap.push(1)
    v = maxheap.pop()
    if v != 9:
        print "Max Heap Extracted Wrong Value"
        print v
        print maxheap
        return -1
    if maxheap.heap[1] != 8:
        print "Max Heap Failed to Bubble Up"
        print maxheap
        return -1
    # END if
    maxheap.push(9)

    #+---------------------------------------------------- Test PopPush ----+#
    v = minheap.pop_push(0)
    if v != 1:
        print "Min Heap Extracted Wrong Value (poppush)"
        print v
        print minheap
        return -1
    if minheap.heap[1] != 0:
        print "Min Heap Didn't Bubble Correctly (poppush 0)"
        print minheap
        return -1
    v = minheap.pop_push(10)
    if minheap.heap[1] != 2:
        print "Min Heap Didn't Bubble Correctly (poppush 10)"
        print minheap
        return -1
    # END if
    v = maxheap.pop_push(10)
    if v != 9:
        print "Max Heap Extracted Wrong Value (poppush)"
        print v
        print maxheap
        return -1
    if maxheap.heap[1] != 10:
        print "Max Heap Didn't Bubble Correctly (poppush 10)"
        print maxheap
        return -1
    v = maxheap.pop_push(0)
    if maxheap.heap[1] != 8:
        print "Max Heap Didn't Bubble Correctly (poppush 0)"
        print maxheap
        return -1
    # END if

    #+---------------------------------------------------- Test Heapify ----+#
    random.shuffle(test)
    minheap = BinHeap(type='min')
    minheap.heapify(test)
    for k in range(1,10):
        v = minheap.pop()
        if v != k:
            print "Min Heap Didn't Output Sorted List"
            print "Got {0}, Expected {1}".format(v, k)
            print minheap
            return -1
        # END if
    # END for

    random.shuffle(test)
    maxheap = BinHeap(type='max')
    maxheap.heapify(test)
    for k in range(9,0,-1):
        v = maxheap.pop()
        if v != k:
            print "Max Heap Didn't Output Sorted List"
            print "Got {0}, expected {1}".format(v, k)
            print maxheap
            return -1
        # END if
    # END for

    print "All Tests Pass"
    pass
# END testBinHeap

if __name__ == "__main__":
    for k in range(25):
        testBinHeap()
