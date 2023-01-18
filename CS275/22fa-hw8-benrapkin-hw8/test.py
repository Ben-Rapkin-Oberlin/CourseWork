
import time

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def loop(n):
    sum=0
    for i in range(n):
        sum+=1
    return sum
        
n=100000000
st=time.time()
print(loop(n))
et=time.time()-st
print(et)