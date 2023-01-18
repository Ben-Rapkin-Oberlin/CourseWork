


from tabnanny import verbose
import tensorflow as tf
import getData
import pandas as pd

layers=2
num_hidden=10
learning_rate=.1
round=.5
seed=12345
trainpercent=.6

tf.random.set_seed(seed)

df=getData.readData("monks1.csv")
#df=pd.read_csv("mnist_5v8.csv")
ncol=df.shape[1]

c=int(df.shape[0]*trainpercent)
X=df.iloc[:c,1:]
y=df.iloc[:c,:1]
#print(trainAnswers.head())
#print(trainData.shape)
#print(c)

T=df.iloc[c:,1:].to_numpy()

a=df.iloc[c:,:1].to_numpy()


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(10, activation='relu'))
#model.add(Dense(8, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer= tf.keras.optimizers.SGD(), metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=50, batch_size=1, verbose=2)
# make class predictions with the model
predictions = model.predict(T)

for i in range (len(predictions)):
    if predictions[i]>=round:
        predictions[i]=1
    else:
        predictions[i]=0
correct=0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        correct+=1
print(correct/len(predictions))

# summarize the first 5 cases% (X[i].tolist(), predictions[i], y[i]))