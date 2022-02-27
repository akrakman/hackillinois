from numpy import average, double
import pandas as pd
import csv

yes = 'y'
classes = []
while(yes == 'y'):
    name, num, prof = input("Enter course, number, and professor name: ").split(".")
    classes.append((name, num, prof))
    yes = input("Enter 'y' if you want to add another class: ")

with open('averagegpa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    average = 0
    total = 0
    list = []
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif row[6] == prof:
            total += 1
            course = row[5]
            average += double(row[21])
            list.append(prof)
            list.append(course)
    average = round(average / total, 2)
    list.append(average)
    print(list)

            
                


