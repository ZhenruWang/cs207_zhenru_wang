import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,h):
    def inner(x):
        dev = f(x+h) - f(x)
        dev = dev/h
        return dev
    return inner

f = lambda x: np.log(x)
h_list = [1e-1, 1e-7, 1e-15]
x = np.arange(0.2,0.4,0.01)
derivative_mat = np.zeros((len(h_list),len(x)))
for i in range(len(h_list)):
    h = h_list[i]
    inner = numerical_diff(f,h)
    #print(inner(x).shape)
    derivative_mat[i,:] = inner(x)

#print(derivative_mat)
plt.plot(x,derivative_mat[0,:],c = 'blue',label = 'h = 1e-1')
plt.plot(x,derivative_mat[1,:],c = 'red',label = 'h = 1e-7',linewidth=5)
plt.plot(x,derivative_mat[2,:],c = 'green',label = 'h = 1e-15')

f_dev = lambda x: 1/x
plt.plot(x,f_dev(x),c = 'black',label = 'analytic',linestyle='dashed')
plt.legend()
plt.xlabel("value of x's")
plt.ylabel("derivative value")


print("Answer to Q-a: When h = 1e-7, the result is most closely to the true derivative.\n \
      When h is too small, there may be rounding error that cause the evaluation to be off and not smooth.\n \
      When h is too large, the evaluation was not accurate at all.")
print()
print("Answer to Q-b: AD would not encounter the errors addressed above since it avoids division by extremely small number.\n \
      And AD is guaruanteed to be accurate to machine precision since every step is analytical.")

plt.show()

        