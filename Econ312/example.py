# Importing Required Library
import pandas as pd
import lightgbm as lgb
 
# Similarly LGBMRegressor can also be imported for a regression model.
from lightgbm import LGBMClassifier
 
# Reading the train and test dataset
data = pd.read_csv("cancer_prediction.csv)
 
# Removing Columns not Required
data = data.drop(columns = ['Unnamed: 32'], axis = 1)
data = data.drop(columns = ['id'], axis = 1)
 
# Skipping Data Exploration
# Dummification of Diagnosis Column (1-Benign, 0-Malignant Cancer)
data['diagnosis']= pd.get_dummies(data['diagnosis'])
 
# Splitting Dataset in two parts
train = data[0:400]
test = data[400:568]
 
# Separating the independent and target variable on both data set
x_train = train.drop(columns =['diagnosis'], axis = 1)
y_train = train_data['diagnosis']
x_test = test_data.drop(columns =['diagnosis'], axis = 1)
y_test = test_data['diagnosis']
 
# Creating an object for model and fitting it on training data set
model = LGBMClassifier()
model.fit(x_train, y_train)
 
# Predicting the Target variable
pred = model.predict(x_test)
print(pred)
accuracy = model.score(x_test, y_test)
print(accuracy)