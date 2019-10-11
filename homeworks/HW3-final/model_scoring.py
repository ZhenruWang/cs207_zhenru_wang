import Regression as reg
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

print(X_train.shape)
alpha= 0.1
#models = [reg.LinearRegression(), reg.RidgeRegression(alpha)]

print("For OLS Linear Regression model,")
model = reg.LinearRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
score = model.score(X_test,y_test)
print()
print("The parameters are:")
print(model.get_params())
print()
print("The R2 Score is:")
print(score)

print("____________________________")

print("For Ridge Regression model,")
model = reg.RidgeRegression(alpha)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
score = model.score(X_test,y_test)
print()
print("The parameters are:")
print(model.get_params())
print()
print("The R2 Score is:")
print(score)

'''
reg = Ridge(alpha = alpha)
reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)
score = reg.score(X_test,y_test)
print(r2_score(y_test,y_pred))
print(score)
#print(y_pred)
#print(reg.intercept_)
'''