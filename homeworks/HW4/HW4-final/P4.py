class AutoDiffToy:
    def __init__(self, x, der = 1):
        self.val = x
        self.der = der
        
    def __add__(self,other):
        try:
            new_val = self.val + other.val
            new_der = self.der + other.der
        except AttributeError:
            new_val = self.val + other
            new_der = self.der
            
        return AutoDiffToy(new_val,new_der)
    
    def __radd__(self,other):
        return self.__add__(other)
        
    def __mul__(self, other):
        try:
            new_val = self.val * other.val
            new_der = self.val * other.der + other.val * self.der
        except AttributeError:
            new_val = self.val * other
            new_der = self.der * other
            
        return AutoDiffToy(new_val,new_der)
    
    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __neg__(self):
        return AutoDiffToy(-1 * self.val,-1 * self.der)
    
    def __sub__(self,other):
        return self.__add__(-other)
    
    def __rsub__(self,other):
        return (-self).__add__(other)


a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0
print('When f = 2 * x + 3, evaluated at x = 2:')
f = alpha * x + beta
print('f.val is',f.val,', f.der is', f.der)  
print()

alpha = -2.0
beta = -3.0
print('When f = x * -2 - 3, evaluated at x = 2:')
f = x * alpha + beta
print('f.val is',f.val,', f.der is', f.der)
print()

alpha = 2.0
beta = -3.0
print('When f = -3 + 2 * x, evaluated at x = 2:')
f = beta + alpha * x
print('f.val is',f.val,', f.der is', f.der)      
print()
 
alpha = -2.0
beta = 3.0
print('When f = 3 + x * -2, evaluated at x = 2:')
f = beta + x * alpha
print('f.val is',f.val,', f.der is', f.der)
    
         
    