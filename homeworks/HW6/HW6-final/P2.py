from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array.copy()
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError
        
    def heapify(self, idx: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        ### min-heap
        small = idx
        l = self.left(idx)
        r = self.right(idx)
        if l < self.size and self.compare(idx, l):
            small = l
        if r < self.size and self.compare(small, r):
            small = r
        
        if small != idx:
            self.swap(idx,small)
            self.heapify(small)

    def build_heap(self) -> None:
        for i in range(int(self.size / 2)-1 ,-1,-1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        self.size += 1
        self.elements.append(key)
        idx = self.size - 1
        while idx != 0 and self.compare(self.parent(idx), idx):
            self.swap(idx,self.parent(idx))
            idx = self.parent(idx)

    def heappop(self) -> int:
        if len(self.elements) < 1:
            raise IndexError ('heap is empty')
        self.size -= 1
        removed = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        self.heapify(0)
        return removed

class MinHeap(Heap):
    # TODO: complete implementation
    def compare(self, a: int, b: int) -> bool:
        return self.elements[a] > self.elements[b]

class MaxHeap(Heap):
    # TODO: complete implementation
    def compare(self, a: int, b: int) -> bool:
        return self.elements[a] < self.elements[b]


#h = MinHeap([1,9,8,2,3,10,14,7]) # The heap tree will be built during initialization
#print(h)
#h.heappush(27)
#print(h)
#h.heappop()
#print(h)
#h.heappop()
#print(h)