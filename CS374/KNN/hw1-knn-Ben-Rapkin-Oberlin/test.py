
import math
a=0.7558139534883721
n=432
temp=1.96*(math.sqrt((a*(1-a))/n))
b=[a-temp,a+temp]
print(b)