import pandas as pd
import csv

yes = 'y'
classes = []
while(yes == 'y'):
    name, num, prof = input("Enter course, number, and professor name: ").split(",")
    classes.append((name, num, prof))
    yes = input("Enter 'y' if you want to add another class: ")

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #get average grade
            teacher = row[6]
            course = row[5]
            grade = []
            print(teacher)
            for i in range(7, 17):
                grade.append(row[i])
