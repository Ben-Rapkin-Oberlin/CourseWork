# This was a utility script for runing the program 10 times with 10 diffrent seeds

import subprocess
import sys

a=[10,20,30,40,50,60,70,80,90,100]
b=[]
for i in a:
    #run hw1.py with the given arguments, read it's output (the accuracy)
    proc=subprocess.Popen([sys.executable,'./Hw1.py', "bonusData/output34.csv", "E", "1", "0.75", str(i)],stdout=subprocess.PIPE)
    temp=str(proc.stdout.read())
    word=""
    #strip the output to just the accuracy
    for letter in temp:
        if letter.isnumeric():
            word+=letter
    b.append("."+word[1:])
#find the average
f=[float(x) for x in b]
average=sum(f)/len(f)
print(average)
