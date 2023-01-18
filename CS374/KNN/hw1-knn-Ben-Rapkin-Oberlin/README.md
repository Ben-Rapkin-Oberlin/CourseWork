I have adhered to the honor code on this assignment.
Ben Rapkin

Research Questions:
1. Accuracy for each data set with seed=36 and k=1, and 75% split
Penguins:  0.872093023255814
monks1: 0.4444444444444444
mnist_100: 0.892
mnist_1000: 0.9448

2. Respective Confidence Intervals
Penguins:[0.836695608760846, 0.9074904377507819]
monks1:[0.39178024258460653, 0.4971086463042823]
mnist_100:[0.8727624227720848, 0.9112375772279152]
mnist_1000:[0.9403239435756907, 0.9492760564243092]

3. mnist_100 vs mnist_1000 
The larger data set had a higher accuracy likely due to more training data. Their confidence intervals did not overlap as such, larger data sets are generally more accurate

4. Penguins with 3 k values
k=1, accuracy= .872093023255814
k=3, accuracy= .813953488372093
k=5, accuracy=.8023255813953488
As k increased, accuracy went down. This is likely because the program overtrained and as such lost utility as a more general purpose classifier

5. Bonus
I used makeData.py to create the 6 pairs data set instead of playing with the read data function in Hw1.py
Additionally, I wrote run10.py to run Hw1.py with 10 different seeds and average the accuracies. It does use an external library (subprocess) but this is not functionally tied to kNN. All the below can be found without the run10.py script by repeatedly running Hw1.py with new seeds
For seeds [10,20,30,40,50,60,70,80,90,100] with split=.75 and k=1, the average accuracy is 0.8162790697674419
The command line arguments were the same in all of the below cases:
For attributes 1,2: a=0.9465116279069766
For attributes 1,3: a=0.9267441860465118
For attributes 1,4: a=0.805813953488372
For attributes 2,3: a=0.7546511627906977
For attributes 2,4: a=0.6988372093023256
For attributes 3,4: a=0.7279069767441859
bill length & bill depth did the best with bill length & flipper length coming in a close second. Attribute 4   lowered correlation and causing me to suspect that these 3 species are fairly similar in overall mass, meaning that small environmental factors has a significant impact on the value. Additionally I suspect that bill lengths are quiet different for the three penguin species.

This assignment overall went well and overall I enjoyed it as an introduction to the course. The actual coding went fairly smoothly with the hardest part being the CSV reader/writer. However, I was intimidated with time that mnist_1000 would take and I ended up spending a few hours re-writing the kNN algorithm to be faster, which in hindsight, took far longer than just waiting for the file to process. Additionally, I had some difficulties making the program deterministic due to mistakenly converting a list to a set when voting was preformed. 

I likely spent ~10 hours on this
