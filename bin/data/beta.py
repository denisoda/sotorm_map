import csv


for file in range(43, 61):
 with open('csv/'+ str(file) +'.csv' ) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      print(int(str(row['YEARMONTH'][:-2])), row['LOCATION'])





