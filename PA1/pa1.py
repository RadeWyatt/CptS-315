from apyori import apriori
import pandas as pd
import csv

support = 100
baskets = []
with open("browsing-data.txt", "r") as a_file:
  for line in a_file:
      baskets.append(line.split(' ')[:-1])
#print(baskets)

index = 0
temp = 0

with open('browsing-data.txt', 'r') as csvfile:
    hw1reader = csv.reader(csvfile, delimiter = ' ')
    for row in hw1reader:
        new_str = ''
        #print('Length: ', len(row))
        if index == 0:
            temp = len(row)
        elif len(row) > temp:
            temp = len(row)
        index = index + 1
        #print('Index: ', index)
        
        for x in range(len(row)):
            if(row[x] != ''):
                new_str += row[x]
                new_str += ', '
        #print(new_str)
        #print("***************************")
        #print("***************************")

print('Maximum Length: ', temp)

maxLength = temp

index = 0
temp = 0

new_file = ''

with open('browsing-data.txt', 'r') as csvfile:
    hw1reader = csv.reader(csvfile, delimiter = ' ')
    for row in hw1reader:
        new_str = ''
        #print('Length: ', len(row))
        index += 1
        #print('Index: ', index)
        
        for x in range(len(row)):
            if(row[x] != ''):
                new_str += row[x]
                new_str += ', '
        
        #print(new_str)
        
        if(len(row) < maxLength):
            diff = maxLength - len(row)
            for x in range(len(row), maxLength):
                new_str += ', '
                
        #print(new_str)
        new_file = new_file + '\n' + new_str + '\n'
        
        #print("***************************")
        #print("***************************")
        
print(maxLength)
print(new_file)

with open("PA1a.txt", "w+") as f:
    f.write(new_file)
        
data = pd.read_csv('PA1a.txt', header = None)
data.head()

data.dropna()
data.head()
data.info()

records = []
rows = data.shape[0]
cols = data.shape[1]
print(rows)
print(cols)

for i in range(0, rows):
    records.append([str(data.values[i,j]) for j in range(0,cols)])
sup = 100 / rows
    
hw1rules = apriori(records, min_support=sup, min_confidence=0.4, min_lift=3, min_length=2)
hw1results = list(hw1rules)

print(len(hw1results))

with open("output.txt", 'w+') as f:
    for item in hw1results:
        
        pair = item[0]
        items = [x for x in pair]
        f.write("Rule: " + items[0] + " -> " + items[1] + "\n")
        
        f.write("Support: " + str(item[1]) + "\n")
        
        f.write("Confidence: " + str(item[2][0][2]) + "\n")
        f.write("Lift: " + str(item[2][0][3]) + "\n")
        f.write("=================================================\n")