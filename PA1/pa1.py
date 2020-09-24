from apyori import apriori
import csv
import pandas as pd

index = 0
temp = 0

# Determine the maximum row length.
with open("browsing-data.txt", "r") as csvfile:
    hw1reader = csv.reader(csvfile, delimiter=' ')
    for row in hw1reader:
        if index == 0:
            temp = len(row)
        elif len(row) > temp:
            temp = len(row)
        index += 1

maxLength = temp

index = 0
temp = 0

new_file = ''

# Generate new file with equal number of columns for all rows
with open("browsing-data.txt", 'r') as csvfile:
    hw1reader = csv.reader(csvfile, delimiter=' ')
    for row in hw1reader:
        new_str = ''
        index += 1

        for x in range(len(row)):
            if(row[x] != ''):
                new_str += row[x]
                new_str += ','
            
        if(len(row) < maxLength):
            diff = maxLength - len(row)
            for x in range(len(row), maxLength):
                new_str += ','
        
        new_file = new_file + new_str + '\n'

with open("hw1a.txt", "w+") as f:
    f.write(new_file)


