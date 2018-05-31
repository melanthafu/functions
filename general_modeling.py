import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# read json file
file = 'data.json'
with open(file) as train_file:
    dict_train = json.load(train_file)

# converting json dataset from dictionary to dataframe
train = pd.DataFrame.from_dict(dict_train, orient='index')


train = pd.read_table('train.tsv')



# missing values
# outliers
# feature engineering 
# select features
#   variance analysis 
#   correlation analysis
#   lasso or stepwise model, feature importances to select features
# deal with high cardinal features, get dummy of categorical variables, remember to delete one
# correct the skewness and standadize normalize, dont touch categorical variables

# select model
# baseline
# imbalanced label
# random forest, select the target functions
# continuous: mse, categorica;: binary, roc auc, 
# confusion matrix and combined of the actual indicators, like the cost of benefits to select 
# split data

sns.boxplot(x = 'shipping', y = 'price', data = train)
plt.ylim(0, 100)
plt.show()

# feature importance

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=....)
clf.fit(X, y)
importance = clf.feature_importaces_

condi_dummy = pd.get_dummies(train.item_condition_id, prefix_sep='_', drop_first = True)