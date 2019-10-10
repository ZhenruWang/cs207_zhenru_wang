import numpy as np
import time

# below the timer function is adopted from the code in lecture5
def timer(f):
    def inner(*args):
        t0 = time.time()
        output = f(*args)
        elapsed = time.time() - t0
        print("Time Elapsed", elapsed)
        return output
    return inner

def my_ave(areas):
    my_sum = 0
    for a in areas:
        my_sum += a
    my_sum = my_sum / len(areas)
    #print("Myavg :",my_sum)
    return my_sum


def np_ave (areas):
    return np.mean(areas)

file = open('circles.txt')
list_str= file.read().splitlines()
radius = [ float(x) for x in list_str ]

areas = [0.0]*len(radius)
areas_np = np.zeros(len(radius))
for i in range(len(radius)):
    areas[i] = np.pi * radius[i]**2
    areas_np[i] = np.pi * radius[i]**2
  
# below the demos are adopted from the code in lecture5

# Time allocation with lists
my_func = timer(my_ave)
l1 = my_func(areas)

# Time allocation with numpy array
np_func = timer(np_ave)
l2 = np_func(areas_np)

file.close()