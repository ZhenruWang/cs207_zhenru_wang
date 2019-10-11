import Regression as reg
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


alpha_list = np.arange(0.05,1,0.09)
score_list = []
for a in alpha_list:
    #model = reg.RidgeRegression(alpha)
    model = reg.RidgeRegression(0.1)
    model.set_params(alpha = a)
    
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    score = model.score(X_test,y_test)
    score_list.append(score)
    
plt.plot(alpha_list,score_list,label = 'Ridge Regression')

score_list_l = []
for alpha in alpha_list:
    model = reg.LinearRegression()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    score = model.score(X_test,y_test)
    #print(y_predict)
    score_list_l.append(score)
    
plt.plot(alpha_list,score_list_l,label = 'Linear Regression')
plt.legend()
plt.xlabel("alpha")
plt.ylabel("R^2 Error")