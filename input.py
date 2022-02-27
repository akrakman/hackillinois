from numpy import average
import pandas as pd
import csv

yes = 'y'
classes = []
while(yes == 'y'):
    name, num, prof = input("Enter course, number, and professor name: ").split(".")
    classes.append((name, num, prof))
    yes = input("Enter 'y' if you want to add another class: ")

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        ##print(row[7])
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif row[7] == prof:
            #get average grade
            course = row[6]
            print(prof, course)
            #average = row[23]
            break
        #NOW WE HAVE AVERAGE GPA, PROF, COURSE!!
            
                


