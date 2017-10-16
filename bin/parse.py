import csv

def csv_parse(location = 'data/csv/', i=43, b=61):
 for file in range(i, b):
  with open(location + str(file) + '.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      print(int(str(row['YEARMONTH'][:-2])), row['LOCATION'])




def csv_parse_row(year, location = 'data/csv/', i=43, b=62,row1 = 'YEARMONTH', row2 = 'LATITUDE', row3 = 'LONGITUDE'):
 for file in range(i, b):
     with open(location + str(file) + '.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
       int(str(row[row1][:-2])), row[row2], row[row3]
       if(int(str(row[row1][:-2])) == year):
         int(str(row[row1][:-2]))
         print (int(str(row[row1][:-2])), row[row2], row[row3])
     if(int(str(row[row1][:-2])) > year): break



csv_parse_row(1998)