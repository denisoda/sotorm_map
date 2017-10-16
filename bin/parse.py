import csv

def csv_parse(location = 'data/csv/', i=43, b=61):
 for file in range(i, b):
  with open(location + str(file) + '.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      print(int(str(row['YEARMONTH'][:-2])), row['LOCATION'])


def csv_parse_row(year,location = 'data/csv/', i=43, b=62,row1 = 'YEARMONTH', row2 = 'LATITUDE', row3 = 'LONGITUDE',arr_date = [], arr_x = [], arr_y =[] ):
 for file in range(i, b):
     with open(location + str(file) + '.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
       int(str(row[row1][:-2])), row[row2], row[row3]
       if(int(str(row[row1][:-2])) == year):
        return int(str(row[row1][:-2])), row[row2], row[row3]
     if(int(str(row[row1][:-2])) > year):
         break

def csv_parse_row(year,location = 'data/csv/', i=43, b=62,row1 = 'YEARMONTH', row2 = 'LATITUDE', row3 = 'LONGITUDE',arr_date = [], arr_x = [], arr_y =[] ):
  for file in range(i, b):
    with open(location + str(file) + '.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
       int(str(row[row1][:-2])), row[row2], row[row3]
       if(int(str(row[row1][:-2])) == year and not str(row[row2])   == ""):
         int(str(row[row1][:-2]))
         arr_date.append (int((str(row[row1][:-2]))))
         arr_x.append(str(row[row2]))
         arr_y.append(str(row[row3]))
    if(int(str(row[row1][:-2])) > year):
        return   arr_date, arr_x, arr_y
        break



def loc_by_year(year,loop):
 print(csv_parse_row(year)[0][loop], csv_parse_row(year)[1][loop], csv_parse_row(year)[2][loop])


for i in range(90):
 print(loc_by_year (1998, i))

