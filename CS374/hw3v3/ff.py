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
trainData=df.iloc[:c,1:]
trainAnswers=df.iloc[:c,:1]
#print(trainAnswers.head())
#print(trainData.shape)
#print(c)

testData=df.iloc[c:,1:]

testAnswers=df.iloc[c:,:1]


model = tf.keras.Sequential()

#model.add(tf.keras.layers.Dense(ncol, inputt activation='sigmoid'))
#model.add(tf.keras.layers.Dense(num_hidden, input_shape=(c,ncol-1), activation='sigmoid'))
model.add(tf.keras.layers.Dense(num_hidden, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))


model.compile(loss = tf.keras.losses.BinaryCrossentropy(),
                optimizer = tf.keras.optimizers.SGD(),
                metrics = ['accuracy'])

model.fit(trainData, trainAnswers, epochs=500, verbose=1)
"""
#model.evaluate(testData, testAnswers)
a=model.predict(testData)
#print(a[1:5])
print(testAnswers[1:5])
a=[1 if i[0]>=round else 0 for i in a]
print(a[1:5])
correct=0
for i in range(len(a)):
    if a[i]==testAnswers.iloc[i,0]:
        correct+=1
#a=[1 if float(guess)==answer else 0 for guess,answer in zip(a,testAnswers)]
#print(a[1:5])
#print(sum(a)/len(a))
print(correct/len(a))
#model.summary()
#print(testAnswers.head())

"""