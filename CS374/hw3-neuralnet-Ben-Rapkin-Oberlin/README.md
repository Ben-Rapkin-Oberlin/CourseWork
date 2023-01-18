Ben Rapkin
I have adhered to the honor code

Overall this assignment did not go as smoothly as I would have hoped. I started with the regular implementation that we had discussed in class, but I really wanted to implement the backpropagation via matrix multiplication, so I abandon that code. It was here I also began experimenting with writing code using Cython data types, this unfortunately would not make it into the final project However, trying this with matrices proved to be challenging as I couldn't find many sources related to the specific context of our assignment. Eventually I tried adapting two of them to our class, the first one I could not get to properly work, and the second one seemed to, without fail, overfit the model and achieve single digit accuracy on the test set. I was unfortunately really hopeful for the second model to work and by the time I realized it's flaw, there was very little time for me to rewrite the neural net class. However, I gave it my best shot. When I came to your office on Monday I had coded everything and was trying to trouble shoot the program. The error as you pointed out was in the order of operations of my backprop method. I fixed this, but that is when a typo with the signs rear it's head and stopped the code from obtaining any accuracy. At this point I tried to use a pre-built NN to solve the research questions (files ff.py and m.py), however, while they would get high accuracies on the training set, they scored abysmally on the training set, to the point where I didn't think they were correctly implemented and usable to answer the questions. Overall, I know my hw is very late, but I want you to know it wasn't just that I waited until the last day and have been putting in effort to get it working. I have likely spent 22+ hours between all the sperate versions working on this. 

Q1: Seed=123, Percent=.6  and Layers=1 (this does not include the output neuron)
    A. The test accuracy was 1 
    B. The test accuracy was 0.7674418604651163 
    C. The CI for the NN was [1.0, 1.0], whereas the CI for the LR was [0.7276033848369478, 0.8072803360932849]. The NN was more accurate in a significant manner. This means it is a better classifier for the monks1 dataset and can learn more important features.


Q2: Seed=123 n=.001
    A. A2=.6, A5=.85, A10=.5, A20=.5, and A50=.5

    B. The output for most tested nueron quantities was the same at 50%. I belive that, considering the output for the bonus question and that A2 and A5 change drastically when I alter the seed, they get better results due to random chance initializing those nodes with better wieghts/biases. Additionally when I run this with n=.0001, all nodes counts produce the same accuracy. Overall, this success This fades off when L>1 or N>=10 because this random and abnormal accuracy is much less likely over 50 nodes than 2. It's a regression to the mean. As to why A10==A50, this has occured becuase dispite having/combining n neurons, all of them move so little from their inital point that their improvements are inconsequential compared to the baseline random noise. I.e. practically it doesn't matter if you have 10 almost random neurons or 50, you still get random output becuase each nueron is still basically still random. 

    
Q3:
    C. Of the three charts, .1 and .01 have large steps in terms of accuracy. Both of them found the max or near max very quickly, whereas .001 meandered up and down for a while before ending up at ~.6 for both. This means that although higher learning rates step over more of the function, they can end up in the same place or better with much much less processing power than those with very low learning rates.

    D. The validation set was very similar to Training in that .1 preformed better than .01 which in turn preformed better than .001. One notably thing was that the larger learning rates mostly avoided the areas of lowered accuracy that the .001 rate got stuck in for most of training, this shows another potiental benifet to having larger learning rates in the correct context.

Q4. nodes=10, n=.01, percent=.6, Seed=123, round=.05, L=1
    A.05=0.3841698841698842, A.1=0.7702702702702703, A.5=0.9208494208494209, A.9=0.9208494208494209, and A.95=0.9208494208494209
    
    The Accuracies seem to increase as the threshold gets larger, up until a point, that point being classifying all instances as seismic events

    B. Following the formate (Recall Yes, Recall No)
    .05=(.519,.878)
    .1=(.790,.537)
    .5=(1,0)
    .9=(1,0)
    .95=(1,0)
    The recall shifted to more yes accuracy as the code started to guess yes more often but much less (none) accuracy for non seismic events

    I think that .5 is the best metric that we have. Everything below .5 is less accurate, and everything above has been trained to just say yes, which doesn't actually provide us any new information about the seismic event. Ideally, we might try somewhere between .5 and .9 even, but regardless, I think .5 is actually providing analysis of the data rather than gaming the data set makeup.


Q5.
    The hw says to do question 1 again but with different values of L, but it also mentions this in conjunction with changing nodes, which is not in question 1. I assume it wants us to do Q2. Sorry if this is wrong

    Using Seed=123 n=.001 Percent=.6, Threshold=.5
    L=1, A2=0.6, A5=0.85, A10=.5, A20=.5, and A50=.5
    L=2, A2=0.5, A5=0.5, A10=.5, A20=.5, and A50=.5
    L=3, A2=0.5, A5=0.5, A10=.5, A20=.5, and A50=.5

    It seems that the increased number of layers do not change the output of the program when n is very small. I think that if L was larger it might be able to improve very slightly as each layer's improvements might stack, however, I think this would be very subtle as still almost all neurons and their outputs are still random when the learning rate is so small. 



