import csv

file = 57

with open('data/csv/'+ str(file) +'.csv' ) as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['YEARMONTH'])





