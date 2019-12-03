import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

import sqlite3

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute("PRAGMA foreign_keys=1")

#PRIMARY KEY AUTOINCREMENT 
cursor.execute('''CREATE TABLE model_params (
               id INTEGER NOT NULL, 
               desc TEXT, 
               param_name TEXT, 
               value REAL)''')
db.commit()

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER NOT NULL, 
               desc TEXT, 
               feature_name TEXT, 
               value REAL)''')
db.commit()

cursor.execute('''CREATE TABLE model_results (
               id INTEGER NOT NULL, 
               desc TEXT, 
               train_score REAL, 
               test_score REAL)''')
db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
feature_names = data.feature_names
#print(feature_names)
# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

def save_to_database(model_id,model_desc,db,model,X_train, X_test, y_train, y_test):
# Assume model is an sklearn.linear_model.LogisticRegression. 
#
#Hint: Feature names can be extracted from data via the feature_names attribute.
#model_results: Train and validation accuracy obtained from the score method.
    
    #model_params: Values from the get_params method.
    for i in range(len(model.get_params().keys())):
        vals_to_insert = (model_id, model_desc, list(model.get_params().keys())[i], list(model.get_params().values())[i])
        cursor.execute('''INSERT INTO model_params 
                  (id, desc, param_name, value)
                  VALUES (?, ?, ?, ?)''', vals_to_insert)
    
    #model_coefs: Coefficient and intercept values of the fitted model (see coef_ and intercept_ attributes in the documentation).
    #fn = data.feature_names
    for i in range(len(X_train.columns)):
        vals_to_insert = (model_id, model_desc, X_train.columns[i], model.coef_[0][i])
        cursor.execute('''INSERT INTO model_coefs 
               (id, desc, feature_name, value)
               VALUES (?, ?, ?, ?)''', vals_to_insert)
    # intercept_
    vals_to_insert = (model_id, model_desc, 'intercept', model.intercept_[0])
    cursor.execute('''INSERT INTO model_coefs 
              (id, desc, feature_name, value)
              VALUES (?, ?, ?, ?)''', vals_to_insert)

    
    #model_results: Train and validation accuracy obtained from the score method.
    train_score = model.score(X_train,y_train)
    test_score = model.score(X_test,y_test)
    vals_to_insert = (model_id, model_desc, train_score, test_score)
    cursor.execute('''INSERT INTO model_results 
              (id, desc, train_score, test_score)
              VALUES (?, ?, ?, ?)''', vals_to_insert)

baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1,"Baseline model",db,baseline_model,X_train, X_test, y_train, y_test)

feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']
reduced_model = LogisticRegression(solver='newton-cg')
X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2,"Reduced model",db,reduced_model,X_train_reduced, X_test_reduced, y_train, y_test)

model3 = LogisticRegression(penalty = 'l1', max_iter = 1000, solver = 'liblinear')
model3.fit(X_train, y_train)
save_to_database(3,"L1 penalty model",db,model3,X_train, X_test, y_train, y_test)

max_test_score = cursor.execute('SELECT id, MAX(test_score) FROM model_results')
max_test_score = max_test_score.fetchall()[0]
max_id = max_test_score[0]
max_score = max_test_score[-1]
print('Best model id:', max_id)
print('Best validation score:', max_score)

lala = cursor.execute('''SELECT feature_name, value FROM model_coefs WHERE id = 3''')
lala = lala.fetchall()
for i in lala:
    print(i[0],':', i[1])
lala = np.array(lala)

model4 = LogisticRegression(solver = 'liblinear')
model4.fit(X_train,y_train)
model4.coef_ = lala[:-1,1].reshape(1,-1).astype('float64')
model4.intercept_ = lala[-1,1].astype('float64')

print('The reproduced score is',model4.score(X_test,y_test))
db.commit()
db.close()




