class HeapTypeError(Exception):
    pass
# END HeapTypeError

class BinHeap:
    @staticmethod
    def __lt(a, b):
        return (a < b)

    @staticmethod
    def __gt(a, b):
        return (a > b)

    def __init__(self, type='min'):
        self.heap = [0]
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

    def push(self, k):
        self.heap.append(k)
        self.size += 1
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

    def pop(self):
        result = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.__percDown(1)
        return result
    # END extract

    def pop_push(self, k):
        result = self.heap[1]

        self.heap[1] = k
        self.__percDown(1)
        return result
    # END pop_push

    def heapify(self, l):
        i = len(l) // 2
        self.size = len(l)
        self.heap = [0] + l[:]
        while (i>0):
            self.__percDown(i)
            i = i-1
        # END while
    # END heapify
# END BinHeap
