import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


import getData

tf.error_score='raise'
df=getData.readData("banknotes.csv")
ncol=df.shape[1]

df.shape[0]
trainData=df.iloc[:,1:]
testData=df.iloc[:,:1]

print(trainData.shape)
print(testData.shape)

layers=2
num_hidden=5
learning_rate=.1
round=.5
seed=1
trainpercent=.6

def create_model():
    model = tf.keras.Sequential()
    model.add(Dense(ncol-1, input_shape=(4,), activation='sigmoid'))
    for i in range(layers-1):
        model.add(tf.keras.layers.Dense(num_hidden, activation='sigmoid'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer= tf.keras.optimizers.SGD(), metrics=['accuracy'])

    return model

estimator = KerasClassifier(model=create_model, epochs=100,batch_size=1, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True)
results = cross_val_score(estimator, trainData, testData, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))


