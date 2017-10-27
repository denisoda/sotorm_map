import csv

location = 'data/csv/'


def csv_parse(year,arr_date = [], arr_x = [], arr_y =[],row1 = 'BEGIN_YEARMONTH', row2 = 'BEGIN_LAT', row3 = 'BEGIN_LON',counter=0):
    with open(location +"StormEvents_details-ftp_v1.0_d"+ str(year) + '.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            int(str(row[row1][:-2])), row[row2], row[row3]
            if (int(str(row[row1][:-2])) == year and not str(row[row2]) == ""):
                int(str(row[row1][:-2]))
                arr_date.append(int((str(row[row1][:-2]))))
                arr_x.append(str(row[row2]))
                arr_y.append(str(row[row3]))
                counter+=1
    return   arr_date, arr_x, arr_y

