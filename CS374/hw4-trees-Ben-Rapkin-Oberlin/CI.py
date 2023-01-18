#Ben Rapkin

import math
#find CIs
a=0.9089
n=5620
temp=1.96*(math.sqrt((a*(1-a))/n))
b=[a-temp,a+temp]
print(b)