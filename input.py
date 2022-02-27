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
    