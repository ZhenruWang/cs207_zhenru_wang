from P3 import *
import matplotlib.pyplot as plt


x = [10, 20, 50, 100, 200, 500]
naive = timeit(pqclass = NaivePriorityQueue)
heap = timeit(pqclass = HeapPriorityQueue)
python_heap = timeit(pqclass = PythonHeapPriorityQueue)

plt.plot(x,naive, c = 'b', label = 'NaivePriorityQueue')
plt.plot(x,heap, c = 'r', label = 'HeapPriorityQueue')
plt.plot(x,python_heap, c = 'g', label = 'PythonHeapPriorityQueue')
plt.xlabel('Number of Lists Merged')
plt.ylabel('Elapsed time in seconds')
plt.title('Elapsed time in seconds versus Number of Lists Merged')
plt.legend()
plt.show()