#Ben Rapkin
#make subset of data for testing pairs
import csv

with open("penguins.csv", "r") as source:
    reader = csv.reader(source)
      
    with open("output34.csv", "w",newline='') as result:
        writer = csv.writer(result, delimiter=',')
        for r in reader:          
            # Use CSV Index to remove a column from CSV
            #only write some cols
            writer.writerow((r[0], r[3], r[4]))