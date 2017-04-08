import csv
import sys

f = open('test.csv',"r")
reader = csv.reader(f)

for row in reader:
    for col in row:
        print('  ',col, end='')
    print()

f.close()