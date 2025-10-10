import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.preprocessing import OneHotEncoder

show_plots = False
optimize = False

features = pd.read_excel('aap9112_data_file_s1.xlsx')

for j in features.keys():
    print(j,len(features[j].unique()))
    
features.replace(to_replace='2a, Boronic Acid',value='Boronic Acid',inplace=True)
features.replace(to_replace='2b, Boronic Ester',value='Boronic Ester',inplace=True)
features.replace(to_replace='2c, Trifluoroborate',value='Trifluoroborate',inplace=True)
features.replace(to_replace='2d, Bromide',value='Bromide',inplace=True)

# Values to drop based on box plot analysis below
features = features.loc[features['Ligand_Short_Hand'] != 'dppf']
features = features.loc[features['Ligand_Short_Hand'] != 'Xantphos']
features = features.loc[features['Reactant_1_Name'] != '6-chloroquinoline']
#features = features.loc[features['Reactant_2_Name'] != 'Trifluoroborate']
features = features.loc[features['Solvent_1_Short_Hand'] != 'THF_V2']
features = features.loc[features['Solvent_1_Short_Hand'] != 'MeOH/H2O_V2 9:1']
features = features.loc[features['Product_Yield_PCT_Area_UV'] != 0.0]

features = features.sample(2000,random_state=1)

yields = features['Product_Yield_PCT_Area_UV'].values
features = features[['Reactant_1_Name', 'Reactant_2_Name', 'Ligand_Short_Hand', 'Reagent_1_Short_Hand', 'Solvent_1_Short_Hand']]

print(yields.shape)

for j in features.keys():
    print(j,len(features[j].unique()))

    box_data = {}
    print(','.join(features[j].unique()))
    for i in features[j].unique():
        idx = np.argwhere(features[j].values == i)
        box_data[i] = yields[idx].reshape(-1)
        print(i,box_data[i].shape,sum(yields[idx].reshape(-1)==0))
    
    if show_plots:
        fig,ax = plt.subplots(1,1)
        ax.boxplot(box_data.values())
        ax.set_title(j)
        ax.set_xticklabels(box_data.keys())
        plt.show()

features.rename(columns={'Reactant_1_Name': 'Reactant 1', 'Reactant_2_Name': 'Reactant 2', 'Ligand_Short_Hand': 'Ligand', 'Reagent_1_Short_Hand': 'Base', 'Solvent_1_Short_Hand':'Solvent'},inplace=True)

features.to_csv('features.csv',index=False)
np.savetxt('yields.csv',yields,header='Yields (%)')

encoder = OneHotEncoder(sparse_output=False)

# Transform the features
x = encoder.fit_transform(features)
y = yields


#-----Define the Machine Learning model-----------------------------------------

model = SVR(C=95,epsilon=0.006,kernel='rbf')

#-----Train the model and assess its' prediction accuracy-----------------------

# Split the full dataset into a training set and a test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state = 1)

from scipy.stats import loguniform
from sklearn.model_selection import RandomizedSearchCV

# Here for testing purposes, remove before making available to students
if optimize:
    param_distributions = {
        'C': loguniform(0.1, 1000.0),
        'epsilon': loguniform(0.001, 10.0),
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
    }

    randomized_search = RandomizedSearchCV(
            estimator = model,
            param_distributions = param_distributions,
            n_iter = 100,
            random_state = 1,
            verbose = 2
        )

    randomized_search.fit(x_train, y_train)
    print(randomized_search.best_params_)
    y_predict_test = randomized_search.best_estimator_.predict(x_test)

else:
    # Fit the model
    model.fit(x_train, y_train)
    y_predict_test = model.predict(x_test)

# Test the accuracy of the model against the test set

accuracy = root_mean_squared_error(y_test, y_predict_test)
print(f'The root mean square error was {(accuracy)}%!')

errors = []

train_vals = [100,200,500,1000,2000]
for n_train in [100,200,500,1000,2000]:
    model.fit(x_train[:n_train], y_train[:n_train])
    y_predict_test = model.predict(x_test)
    errors.append(root_mean_squared_error(y_test, y_predict_test))

plt.close()

plt.rcParams.update({'font.size': 10})
plt.rcParams["figure.figsize"] = (4,2.5)
plt.rcParams["figure.dpi"] = 200

fig,ax = plt.subplots()
ax.plot(train_vals,errors,marker='o',ms=6,linewidth=3)
ax.set_xscale('log')
ax.set_xlabel('Training Set Size')
ax.set_ylabel('RMSE / %')

plt.tight_layout()
plt.savefig('lc.png')
