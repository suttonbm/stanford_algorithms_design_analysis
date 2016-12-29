class HeapTypeError(Exception):
    pass
# END HeapTypeError

class DictBinHeap:
    @staticmethod
    def __lt(a, b):
        return (a < b)

    @staticmethod
    def __gt(a, b):
        return (a > b)

    def __debug_inspect(self):
        self.dump()
        raw_input()
    # END debug_inspect

    def __init__(self, type='min'):
        self.heap = [0]
        self.keyMap = dict() # {key: location}
        self.valueMap = dict() # {location: key}
        self.size = 0
        if type=='min':
            self.testInvariant = self.__lt
        elif type=='max':
            self.testInvariant = self.__gt
        else:
            raise HeapTypeError()
        # END if
    # END __init__

    def __swap(self, i, j):
        # Swap the key map pointers
        key_i = self.valueMap[i]
        key_j = self.valueMap[j]
        self.valueMap[i] = key_j
        self.valueMap[j] = key_i
        self.keyMap[key_i] = j
        self.keyMap[key_j] = i

        # Swap the actual heap items
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp
    # END swap

    def __percUp(self, i):
        while i//2 > 0:
            if self.testInvariant(self.heap[i], self.heap[i//2]):
                self.__swap(i, i//2)
            # END if
            i = i//2
        # end while
    # END percUp

    def push(self, key, value):
        self.heap.append(value)
        self.size += 1
        self.keyMap[key] = self.size
        self.valueMap[self.size] = key

        self.__percUp(self.size)
    # END insert

    def __percDown(self, i):
        while (i*2) <= self.size:
            mc = self.__minChild(i)
            if not self.testInvariant(self.heap[i], self.heap[mc]):
                self.__swap(i, mc)
            # END if
            i = mc
        # END while
    # END percDown

    def __minChild(self, i):
        if (i*2+1) > self.size:
            return i*2
        else:
            if self.testInvariant(self.heap[i*2], self.heap[i*2+1]):
                return i*2
            else:
                return i*2+1
            # END if
        # END if
    # END minChild

    def peek(self):
        key = self.valueMap[1]
        value = self.heap[1]
        return (key, value)
    # END peek

    def pop(self):
        value = self.heap[1]
        key = self.valueMap[1]

        self.heap[1] = self.heap[self.size]
        self.valueMap[1] = self.valueMap[self.size]
        self.keyMap[self.valueMap[1]] = 1
        del self.valueMap[self.size]
        del self.keyMap[key]

        self.size -= 1
        self.heap.pop()
        self.__percDown(1)

        return (key, value)
    # END extract

    def pop_push(self, newkey, newvalue):
        oldvalue = self.heap[1]
        oldkey = self.valueMap[1]

        del self.keyMap[oldkey]

        self.keyMap[newkey] = 1
        self.valueMap[1] = newkey
        self.heap[1] = newvalue
        self.__percDown(1)

        return (oldkey, oldvalue)
    # END pop_push

    def heapify(self, l, keyfun = lambda x: x[0], valfun = lambda x: x[1]):
        i = len(l) // 2
        self.size = len(l)
        for k in range(len(l)):
            key = keyfun(l[k])
            value = valfun(l[k])
            self.heap.append(value)
            self.valueMap[k+1] = key
            self.keyMap[key] = k+1
        while (i>0):
            self.__percDown(i)
            i = i-1
        # END while
    # END heapify

    def updateValue(self, key, newval):
        i = self.keyMap[key]
        oldval = self.heap[i]
        self.heap[i] = newval

        if self.testInvariant(newval, oldval):
            self.__percUp(i)
        else:
            self.__percDown(i)
        # END if
    # END updateValue

    def getValue(self, key):
        i = self.keyMap[key]
        return self.heap[i]
    # END getValue

    def dump(self):
        print "Current Heap Size:"
        print self.size
        print "\nCurrent Heap State:"
        print self.heap
        print "\nCurrent Key Map:"
        print self.keyMap
        print "\nCurrent Value Map:"
        print self.valueMap
    # END dump
# END DictBinHeap
