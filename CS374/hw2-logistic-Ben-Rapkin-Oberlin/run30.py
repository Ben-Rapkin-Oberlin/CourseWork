import subprocess
import sys
import time

#a=[x for x in range(0,5*30,5)]
#a=[12345, 12345, 12345, 12345,12345, 12345, 12345, 12345,12345, 12345, 12345, 12345]
#print(len(a))
a=[.5*x for x in range(8,90)]
b=[]
#ci=[0.9878904408983098, 0.9907035751561781]
d=0
start=time.process_time()
#print(start)
for i in a:
    #run hw1.py with the given arguments, read it's output (the accuracy)
    proc=subprocess.Popen([sys.executable,'./hw2.py', "occupancy.csv", str(i), ".6", "0.2", "1"],stdout=subprocess.PIPE)
    temp=str(proc.stdout.read())
    #print(temp)
    line1=temp.split(" ")
    line2=[]
    #word=""
    #strip the output to just the accuracy
    for word in line1:
        ttemp=""
        for letter in word:
            if letter.isdigit() or letter==".":
                ttemp=ttemp+letter
        line2.append(ttemp)
    #print(line2)
    b.append(((float(line2[0])), float(line2[1])))
    d+=1
    print("iter", d, "/", len(a))
    #elapsed=time.process_time()
    #print("elapsed time:", elapsed)
    #print("predicted time remaining:", ((elapsed/d)*(30-d))/60, "minutes")
#find the average
#f=[float(x) for x in b]
#bad=0
#for x in f:
   # if x<ci[0] or x>ci[1]:
     #   bad+=1
     #   print(x)
#print(bad)
#find the standard deviation
for i in range(0,len(b)):
    #print("learning rate: ", a[i], " accuracy: ",b[i][0]," efficenty: ",b[i][0]/b[i][1])
    #print(a[i], " accuracy: ",b[i][0]," efficenty: ",b[i][0]/b[i][1])
    print(a[i],b[i][0],b[i][0]/b[i][1])
#average=sum(f)/len(f)
#print(average)
