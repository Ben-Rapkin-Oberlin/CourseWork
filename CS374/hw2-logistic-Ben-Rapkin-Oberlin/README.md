Files:
    hw2.py is the main file
    CI.py is to find confidence intervals
    run30.py runs hw2.py some number of times and collects output
    Hw2NData is all the data for the bonus
    Q4 and Q4.2 are also related to the bonus
    


Question 1: s=12345, n=.01, t=60% v=20%
    monks1: a=0.7558139534883721, CI=[0.7153021038225823, 0.7963258031541619]
    occupancy: a=0.989297008027244, CI=[0.9878904408983098, 0.9907035751561781]
    banknotes: a, CI=[0.9211923326935316, 0.9474208059925997]
    seismic: a=0.9187620889748549, CI=[0.9082281518061569, 0.9292960261435529]

Question 2: 
    Seeds=[x for x in range(0,5*30,5)]

    monks1: average=0.7383720930232556, which does fall in range of my CI, however, there were 8 instances that were out of the interval which is far higher than the 95% CI would predict

    occupancy: average=0.9886969918105895, which does fall in range of my CI, however, there were 10 instances that were out of the interval which is far higher than the 95% CI would predict

    banknotes: average=0.9566909975669099, which is above the CI, additionally, 25/30 tests were not in the CI and everyone was above. I think 12345 may have just been an abnormally poor seed. 

    seismic: average=0.9344294003868473, which is above the CI, additionally, 19/30 tests were not in the CI and everyone was above. I think 12345 may have just been an abnormally poor seed. 


Q.3: Seeds 1-10
    
    
    a. You can find the image as Graph.png and the data as 374Hw2Q3.xlsx

    b. They all follow a similar trend and all of them approch ~99-100% accuracy. The slow is contiously           decreasing after epoch 1

    c. This implies that training after Epoch ~100 is on a practical level largely insignificant and we could decrease the time to train this model by a factor of ~.2 and have very little change in accuracy 

Q.4 Bonus-Comparing learning rates, using s=1 and a 60%/20% split
    The lower n is, the more likely the program is to find generate a higher end accuracy, but it takes much more time. Like with Q.3 where we could largely cut out Epochs 200-500 and get the same end accuracy with far less computation, what is an optimal learning rate for occupancy? I ran the program from using values of .005 to 4 with a step of .005 for n. In Q4.png I graphed the outcomes. The first graph shows the accuracies which increased as n increased (although to an almost negligible degree). The second is the final accuracy vs the time taken to run the code, or the learning efficiency. 
    
    While we know that theoretically, there will be an N large enough that accuracy will eventually low and as such so to will learning efficiency, however, the data implies that this bounds is far off. 

    I continued to run this over the range 4-70 with a step of .5, and as you can see in Q4.2.png the time efficiency drastically decrease around n=45. However, when considering that the accuracy largely remains consistant, this is due to confounding factors

    One tempting soluntion for what is slowing down the algorithim is computational intesity increasing with large numbers, however, if this were the case then I would expect time to decrease in a linear fashion or at least in a manner that has very little deviation. 

    Additionally, I doubt the cause is being crowded out for cpu reasources as this trend remains over diffrent runs.  

    While the exact mechanism of this decline are not clear, it does provide an answer to the original question, even if an unexpected one. Objectivly speaking, the best seed I encountered from a accuracy to time ratio was  .895 with a ratio of 12.67. However, pratically speaking the diffrence between this and any seed over 1 is miniscle in our context. 
    
    Additionally, the best n for objective accuracy is shared between 9 values, ranging from 24.5-58 producing an accuracy of .9903

    Overall, the similarity between learning rates spaning multiple magnitudes is suprising as is the sudden and non-uniform increase in processing time realtive to accuracy. If you have any insights on why this may be happening, I would be very interested in hearing!

    