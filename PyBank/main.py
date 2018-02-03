import os
import csv


budget_csv = os.path.join("/Users/vinu/Documents/DA\ Bootcamp/My_Projects/python-challenge/PyBank/Resources/budget_data_1.csv")

with open("budget_csv") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter="-")
      csvfile.next()
      total = sum(int(r[1] for r in csv.reader(csvfile)))
      print(total)