Ben Rapkin

I have adhered to the honor code

Overall I did like this assignment a good deal because it was pretty easy to debug (hopefully I haven't jinxed myself in saying that). Being able to see the trees and overall logic of the code was also really cool and a first for me. A large proportion of the time spent on this hw came from learning pandas and then, after a rewrite, numpy built in functions: their return type (why are there so many tuples), parameters, and issues like np.unique always sorting it's returned list leading to issues with mixed types. Overall while I certainly troubles here and there in the code, it never felt overwhelming like the NN and I always felt like I could figure out the issues in the code. I am a little curious about optimization however. As I mentioned I initially did this hw in pandas but that took ~8 minutes to process occupancy with numeric=False. With numpy it is much faster, however, my solution still takes 3x-5x the amount of time that yours does for occupancy with numeric=True. I wonder if there were better methods algorithmically to find entropy and build the tree, or if the slow down is mainly do to using slower built in methods and data structures. Maybe both. 

I likely spent 10-12 hours on this hw.

Q1.
    Seed=12, Train%=.75

    Accuracies:
    monks1=.9815, penguins=.9535, occupancy=.9899, opticalDigit=.9089, 

    CI:
    monks1=[0.9687929360925449, 0.9942070639074552]
    penguins=[0.9311833067751688, 0.9758166932248312]
    occupancy=[0.9885332129188159, 0.9912667870811841]
    opticalDigit=[0.9013767558903691, 0.9164232441096309]

Q2
    Please See the 4 PNGs starting with Q2 for images, labels means the tree is displaying the column used to split the data, attributes means the specific attribute chosen for each path

    To generate the attribute tree please uncomment lines 142 and 149 in treeClass.py and line 29 in tree.py. For labels just uncomment line 31 in tree.py

    The program learned that red jackets are always yes. Additionally it learned that if headshape matches bodyshape then the labe is also yes and the label is no for anything else. Albeit this rule was learned in a circuitus route where it needlessly looks at the robots's item before getting to this final rule. 

    These learned rules match the dataset's if you consider the end results (i.e. ignore that is diverts to looking at holdings before returning to body shape). 

Q3.
    The observed accuracy with Seed=12 and Train%=.75 was .5879

    CI=[0.575031114081075, 0.600768885918925]

    The span of the CI for numeric=False was much larger than that of the numeric=True trial (.02574 vs .01504). This seems to imply that the code was overall much more random than in the first trial and as such it had less of a grasp on rules and varies based on enviormental factors (seed). Also it should be explictly mentioned that there is a significant diffrence in accuracy between the two approaches

Q4. Seeds=[1,2,3,4,5,6,7,8,9]
        T, F
    1: 0.9117437722419929,0.5594306049822064
    2: 0.9209964412811388,0.5893238434163701
    3: 0.8918149466192171,0.5544483985765124
    4: 0.9117437722419929,0.594306049822064
    5: 0.9138790035587189,0.5879003558718862
    6: 0.9053380782918149,0.5444839857651246
    7: 0.9167259786476868,0.595729537366548
    8: 0.9074733096085409,0.5793594306049822
    9: 0.9110320284697508,0.6014234875444839

    Avg: 0.9100830367734284,0.5784895215500198


    The trend observed in Q3c where numeric values were much more accurate than categorical was again observed on every seed tried. This reinforces the idea that there is a significant statistical difference in whether instances are treated as numeric or categorical

    Both averages fell in their respective CIs, which is what we would expect for a 95% CI 



