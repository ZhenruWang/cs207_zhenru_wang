
def decorator(f):
    def inner(*args):
        res = f(*args)
        if (res < 0 or res == 0) :
            raise ValueError("The result is negative.")
    return inner
    
def f_1(a,b,c):
    return b**2 - 4*a*c

def f_2(x):
    if (x > 0 or x == 0):
        return x
    else:
        return -1*x
    
def f_3(x,y):
    return x**2 + 4*y**2

print("Below are the function demos")
#demos are adopted from homework2 notebook
a = 1
b = 5
c = 2
print("Trying to compute the discriminant of {0:4.2f}x^2 + {1:4.2f}x + {2:4.2f}\n".format(a, b, c))
print(f_1(a, b, c)) # Positivity not violated

x = -1
print("Trying to calculate the absolute value of {0:8.6f}".format(x))
print(f_2(x)) # Positivity not violated

y = 3
z = -5
print("Trying to calculate the sum of ({0:4.3f})^2 + 4*({1:4.3f})^2".format(y,z))
print(f_3(y,z))


print("__________")
# Decoration test
dec_f1 = decorator(f_1)
dec_f2 = decorator(f_2)
dec_f3 = decorator(f_3)
def test(f,*args):
    try:
        f(*args)
        print("Didn't catch an error, the result is positive")
    except ValueError:
        print("Caught ValueError, the result is nonpositive") 

print("Below are the tests result when functions return positive value\n")
test(dec_f1,a,b,c)
test(dec_f2,x)
test(dec_f3,y,z)

print("__________")
print("Below are the tests result when functions return non-positive value\n")
a = 5
b = 1
c = 2
test(dec_f1,a,b,c)
x = 0
test(dec_f2,x)
y = 0
z = 0
test(dec_f3,y,z)