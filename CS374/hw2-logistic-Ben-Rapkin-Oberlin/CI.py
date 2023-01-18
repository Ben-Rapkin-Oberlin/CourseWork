import math
a= .7674418604651163
n=432
temp=1.96*(math.sqrt((a*(1-a))/n))
b=[a-temp,a+temp]
print(b)