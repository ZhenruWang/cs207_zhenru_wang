import numpy as np
def circle_area(r):
    return np.pi*r**2

def my_ave(radii, func):
    my_sum = 0
    for r in radii:
        my_sum += func(r)
    my_sum = my_sum / len(radii)
    print("Myavg :",my_sum)
    return my_sum


file = open('circles.txt')
list_str= file.read().splitlines()
list_float = [ float(x) for x in list_str ]
my_ave(list_float,circle_area)

file.close() 
