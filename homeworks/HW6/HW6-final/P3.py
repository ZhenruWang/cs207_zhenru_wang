from random import sample
from time import time
from heapq import heappush as py_heappush
from heapq import heappop as py_heappop
from P2 import MinHeap

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('put called on a full priority queue')
        self.elements.append(val)

    def get(self):
        res = 0
        for i in range(len(self.elements)):
            if self.elements[res] > self.elements[i]:
                res = i
        
        try:
            removed = self.elements.pop(res)
        except:
            raise IndexError('get called on an empty priority queue')
        return removed

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('peek called on an empty priority queue')
        res = min(self.elements)
        #for i in range(self.max_size):
        #    if res > self.elements[i]:
        #        res = self.elements[i]
        return res
    
class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = MinHeap([])
        self.max_size = max_size
    
    def put(self, val):
        if len(self.elements) == self.max_size:
            raise IndexError('put called on a full priority queue')
        self.elements.heappush(val)

    def get(self):
        try:
            removed = self.elements.heappop()
        except:
            raise IndexError('get called on an empty priority queue')
        return removed

    def peek(self):
        if len(self.elements.elements) == 0:
            raise IndexError('peek called on an empty priority queue')
        res = self.elements.elements[0]
        return res

class PythonHeapPriorityQueue(PriorityQueue):

    def put(self, val):
        if len(self.elements) == self.max_size:
            raise IndexError('put called on a full priority queue')
        py_heappush(self.elements, val)
        
    def get(self):
        try:
            removed = py_heappop(self.elements)
        except:
            raise IndexError('get called on an empty priority queue')
        return removed

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('peek called on an empty priority queue')
        res = self.elements[0]
        return res

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed