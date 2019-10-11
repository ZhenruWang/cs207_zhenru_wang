import numpy as np
class Regression():
    params = dict()
    #The first key should be the coefficients (not including the intercept) 
    #and the second key should be the intercept. beta[-1]
    
    def __init__(self):
        self.params = dict()
    
    def get_params(self):
        '''
        for key in self.params.keys():
            print(type(key))
            print("The", key,"is",self.params[key])
        '''
        return self.params
    
    def set_params(self, **kwargs):
        return None
        
    def fit(self, X, y):
        return None
        
    def predict(self, X):
        #beta = np.array(self.params['coefficients']).transpose()
        coeff = self.params['coefficients']
        y_pred = np.dot(X,coeff)
        #y_pred = y_pred.reshape(1,89)
        y_pred += self.params['intercept']
        
        return y_pred
        
    def score(self, X, y):
        
        y_bar = np.mean(y)
        sst = np.sum([(y_i - y_bar)**2 for y_i in y])
        
        y_pred = self.predict(X)
        temp = y-y_pred
        sse = np.sum([i**2 for i in temp])
        return 1-sse/sst
    
class LinearRegression(Regression):
    def __init__(self):
        self.params = dict()
        
    def fit(self, X, y):
        ## add a column of ones to the front of X
        new_X = np.append(X,np.ones([X.shape[0],1]),1)
        beta = np.matmul(new_X.transpose(),new_X)
        beta = np.linalg.pinv(beta)
        beta = np.matmul(beta,new_X.transpose())
        beta = np.dot(beta,y)
        self.params['coefficients'] = beta[:-1]
        self.params['intercept'] = beta[-1]
        return None
    
class RidgeRegression(LinearRegression):
    def __init__(self,alpha):
        self.params = dict()
        self.params['alpha'] = alpha
        
    def fit(self, X, y):
        new_X = np.append(X,np.ones([X.shape[0],1]),1)
        beta = np.matmul(new_X.transpose(),new_X)
        gamma = self.params['alpha'] * np.eye(new_X.shape[1])
        beta += np.matmul(gamma.transpose(),gamma)
        #beta = np.linalg.pinv(beta)
        beta = np.linalg.inv(beta)
        beta = np.matmul(beta,new_X.transpose())
        beta = np.dot(beta,y)
        #beta = tuple(beta)
        self.params['coefficients'] = beta[:-1]
        self.params['intercept'] = beta[-1]
        return None
        
    def set_params(self, **kwargs):
        #print(kwargs)
        self.params['alpha'] = kwargs['alpha']
        return None