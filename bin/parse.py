import csv

def csv_parse(location = 'data/csv/', i=43, b=61):
 for file in range(i, b):
  with open(location + str(file) + '.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      print(int(str(row['YEARMONTH'][:-2])), row['LOCATION'])




csv_parse()