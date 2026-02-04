# Example code for training an ML model

#-----Importing libraries-------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# Alan
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
from scipy.stats import loguniform

#-----Importing data------------------------------------------------------------

names = np.loadtxt('names_selected.txt',dtype=str,delimiter='%')
fingerprints = np.loadtxt('fingerprints_selected.txt')
pkas = np.loadtxt('pkas_selected.txt')

accuracies = []

#-----Define the Machine Learning model-----------------------------------------

model = SVR(kernel='linear',C=0.16,epsilon=0.05)
#model = RandomForestRegressor()

#-----Train the model and assess its' prediction accuracy-----------------------

x = fingerprints
y = pkas

# Split the full dataset into a training set and a test set
x_train_full, x_test, y_train_full, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

#AlanAdd
param_grid = {
   'C' : loguniform(1e-2,1),
#   'gamma' : loguniform(1e-3,100),
   'epsilon' : loguniform(1e-2,1)
   }

# param_grid = {
     # 'max_depth' : [20,50],
     # 'n_estimators' : [10,25]
     # }
#search = GridSearchCV(model,param_grid,scoring='neg_root_mean_squared_error',cv=5,verbose=3)
#search = RandomizedSearchCV(model,param_grid,n_iter=10,scoring='neg_root_mean_squared_error',cv=3,verbose=3)
#search.fit(x_train_full,y_train_full)
#print(search.best_score_)
#print(search.best_params_)

#model = search.best_estimator_

n_train = [50,100,250,500,1000,2000]

for n in n_train:
  x_train_truncated = x_train_full[:n]
  y_train_truncated = y_train_full[:n]

  # Fit the model
#  model.fit(x_train_truncated, y_train_truncated.values.ravel())
  model.fit(x_train_truncated, y_train_truncated)

  y_predict_test = model.predict(x_test)

  # Test the accuracy of the model against the test set
  accuracy = root_mean_squared_error(y_test, y_predict_test)
  print(f'The root mean square error was {(accuracy)}!')

  accuracies.append(accuracy)

plt.plot(n_train,accuracies)
plt.xlabel('Training Structures')
plt.ylabel('RMSE')
plt.savefig('Learning Curve.png')
#plt.show()
plt.close()
plt.scatter(y_test,y_predict_test)
plt.plot(np.linspace(0,15,5),np.linspace(0,15,5),'k--')
plt.xlabel('True pKa')
plt.ylabel('Predicted pKa')
plt.savefig('Parity.png')
#plt.show()
plt.close()
