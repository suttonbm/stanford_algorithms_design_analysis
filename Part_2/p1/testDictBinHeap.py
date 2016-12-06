import random
from DictBinHeap import DictBinHeap

class FAIL(Exception):
    pass

def fail(testid, desc, got, expected):
    print "Test ID {0}".format(testid)
    print desc
    print "Got {0}, Expected {1}".format(got, expected)
    raise FAIL()
# END fail

def test():
    test = [('a',1), ('b',2), ('c',3), ('d',4), ('e',5)]
    answer = test[:]

    #+------------------------------------------------------ Test Insert --+#
    random.shuffle(test)
    minheap = DictBinHeap()
    maxheap = DictBinHeap(type='max')
    for item in test:
        minheap.push(item[0], item[1])
        maxheap.push(item[0], item[1])
    # END for
    if minheap.heap[1] != 1:
        fail(1,"Min Heap Failed Insert Test (Value)", minheap.heap[1] , 1)
    if minheap.valueMap[1] != 'a':
        fail(2,"Min Heap Failed Insert Test (Value Map)", minheap.valueMap[1], 'a')
    if minheap.keyMap['a'] != 1:
        fail(3,"Min Heap Failed Insert Test (Key Map)", minheap.keyMap[1], 1)
    if maxheap.heap[1] != 5:
        fail(4,"Max Heap Failed Insert Test (Value)", maxheap.heap[1], 5)
    if maxheap.valueMap[1] != 'e':
        fail(5,"Max Heap Failed Insert Test (Value Map)", maxheap.valueMap[1], 'e')
    if maxheap.keyMap['e'] != 1:
        fail(6,"Max Heap Failed Insert Test (Key Map)", maxheap.keyMap['e'], 1)
    # END if

    #+----------------------------------------------------- Test Pop -----+#
    (k, v) = minheap.pop()
    if v != 1:
        fail(7,"Min Heap Popped Wrong Value", v, 1)
    if k != 'a':
        fail(8,"Min Heap Popped Wrong Key", k, 'a')
    if minheap.heap[1] != 2:
        fail(9,"Min Heap Failed to Bubble Value", minheap.heap[1], 2)
    if minheap.valueMap[1] != 'b':
        fail(10,"Min Heap Failed to Bubble ValMap", minheap.valueMap[1], 'b')
    if minheap.keyMap['b'] != 1:
        fail(11,"Min Heap Failed to Bubble KeyMap", minheap.keyMap['b'], 1)

    (k, v) = maxheap.pop()
    if v != 5:
        fail(12,"Max Heap Popped Wrong Value", v, 5)
    if k != 'e':
        fail(13,"Max Heap Popped Wrong Value", k, 'e')
    if maxheap.heap[1] != 4:
        fail(14,"Max Heap Failed to Bubble Value", maxheap.heap[1], 4)
    if maxheap.valueMap[1] != 'd':
        fail(15,"Max Heap Failed to Bubble ValMap", maxheap.valueMap[1], 'd')
    if maxheap.keyMap['d'] != 1:
        fail(16,"Max Heap Failed to Bubble KeyMap", maxheap.keyMap['d'], 1)

    #+------------------------------------------------ Test PopPush -----+#
    (k, v) = minheap.pop_push('0', 0)
    if v != 2:
        fail(17,"Min Heap Popped Wrong Value (pushpop)", v, 2)
    if k != 'b':
        fail(18,"Min Heap Popped Wrong Key (pushpop)", k, 'b')
    if minheap.heap[1] != 0:
        fail(19,"Min Heap Failed to Bubble Value (pushpop)", minheap.heap[1], 0)
    if minheap.valueMap[1] != '0':
        fail(20,"Min Heap Failed to Bubble ValMap (pushpop)", minheap.valueMap[1], '0')
    if minheap.keyMap['0'] != 1:
        fail(21,"Min Heap Failed to Bubble KeyMap (pushpop)", minheap.keyMap['0'], 1)
    (k, v) = minheap.pop_push('f',6)
    if v != 0:
        fail(22,"Min Heap Popped Wrong Value (pushpop)", v, 0)
    if k != '0':
        fail(23,"Min Heap Popped Wrong Key (pushpop)", k, '0')
    if minheap.heap[1] != 3:
        fail(24,"Min Heap Failed to Bubble Value (pushpop)", minheap.heap[1], 3)
    if minheap.valueMap[1] != 'c':
        fail(25,"Min Heap Failed to Bubble ValMap (pushpop)", minheap.valueMap[1], 'c')
    if minheap.keyMap['c'] != 1:
        fail(26,"Min Heap Failed to Bubble KeyMap (pushpop)", minheap.keyMap['c'], 1)

    (k, v) = maxheap.pop_push('f', 6)
    if v != 4:
        fail(27,"Max Heap Popped Wrong Value (pushpop)", v, 4)
    if k != 'd':
        fail(28,"Max Heap Popped Wrong Value (pushpop)", k, 'd')
    if maxheap.heap[1] != 6:
        fail(29,"Max Heap Failed to Bubble Value (pushpop)", maxheap.heap[1], 6)
    if maxheap.valueMap[1] != 'f':
        fail(30,"Max Heap Failed to Bubble ValMap (pushpop)", maxheap.valueMap[1], 'f')
    if maxheap.keyMap['f'] != 1:
        fail(31,"Max Heap Failed to Bubble KeyMap (pushpop)", maxheap.keyMap['f'], 1)
    (k, v) = maxheap.pop_push('0', 0)
    if v != 6:
        fail(32,"Max Heap Popped Wrong Value (pushpop)", v, 6)
    if k != 'f':
        fail(33,"Max Heap Popped Wrong Value (pushpop)", k, 'f')
    if maxheap.heap[1] != 3:
        fail(34,"Max Heap Failed to Bubble Value (pushpop)", maxheap.heap[1], 3)
    if maxheap.valueMap[1] != 'c':
        fail(35,"Max Heap Failed to Bubble ValMap (pushpop)", maxheap.valueMap[1], 'c')
    if maxheap.keyMap['c'] != 1:
        fail(36,"Max Heap Failed to Bubble KeyMap (pushpop)", maxheap.keyMap['c'], 1)

    #+--------------------------------------------------------- Test Heapify -+#
    random.shuffle(test)
    minheap = DictBinHeap()
    minheap.heapify(test, lambda x: x[0], lambda x: x[1])
    for item in answer:
        (k, v) = minheap.pop()
        if k != item[0]:
            fail(37,"Min Heap Didn't Output Keys Correctly", k, item[0])
        if v != item[1]:
            fail(38,"Min Heap Didn't Output Values Correctly", v, item[1])
        # END if
    # END for

    random.shuffle(test)
    maxheap = DictBinHeap(type='max')
    maxheap.heapify(test, lambda x: x[0], lambda x: x[1])
    answer.reverse()
    for item in answer:
        (k, v) = maxheap.pop()
        if k != item[0]:
            fail(39,"Max Heap Didn't Output Keys Correctly", k, item[0])
        if v != item[1]:
            fail(40,"Max Heap Didn't Output Values Correctly", v, item[1])
        # END if
    # END for
    
    
    #+---------------------------------------------------- Test Update Value ----+#
    random.shuffle(test)
    minheap = DictBinHeap()
    minheap.heapify(test, lambda x: x[0], lambda x: x[1])

    minheap.updateValue('c', 0)
    if minheap.heap[1] != 0:
        fail(41,"Min Heap Failed Update (Value)", minheap.heap[1] , 0)
    if minheap.valueMap[1] != 'c':
        fail(42,"Min Heap Failed Update (Value Map)", minheap.valueMap[1], 'c')
    if minheap.keyMap['c'] != 1:
        fail(43,"Min Heap Failed Update (Key Map)", minheap.keyMap['c'], 1)
    
    minheap.updateValue('c', 6)
    if minheap.heap[1] != 1:
        fail(44,"Min Heap Failed Update (Value)", minheap.heap[1] , 1)
    if minheap.valueMap[1] != 'a':
        fail(45,"Min Heap Failed Update (Value Map)", minheap.valueMap[1], 'a')
    if minheap.keyMap['a'] != 1:
        fail(46,"Min Heap Failed Update (Key Map)", minheap.keyMap['a'], 1)
    
    random.shuffle(test)
    maxheap = DictBinHeap(type='max')
    maxheap.heapify(test, lambda x: x[0], lambda x: x[1])

    maxheap.updateValue('c', 6)
    if maxheap.heap[1] != 6:
        fail(47,"Max Heap Failed Update (Value)", maxheap.heap[1] , 6)
    if maxheap.valueMap[1] != 'c':
        fail(48,"Max Heap Failed Update (Value Map)", maxheap.valueMap[1], 'c')
    if maxheap.keyMap['c'] != 1:
        fail(49,"Max Heap Failed Update (Key Map)", maxheap.keyMap['c'], 1)
    
    maxheap.updateValue('c', 0)
    if maxheap.heap[1] != 5:
        fail(50,"Max Heap Failed Update (Value)", maxheap.heap[1] , 1)
    if maxheap.valueMap[1] != 'e':
        fail(51,"Max Heap Failed Update (Value Map)", maxheap.valueMap[1], 'e')
    if maxheap.keyMap['e'] != 1:
        fail(52,"Max Heap Failed Update (Key Map)", maxheap.keyMap['e'], 1)
# END test

def main():
    for k in range(25):
        try:
            test()
        except(FAIL):
            return -1
    print "Passed All Tests"
# END main

if __name__ == "__main__":
    main()
