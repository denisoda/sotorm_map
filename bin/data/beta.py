import cv2
import numpy as np

# mouse callback function


while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

def csv_parse_row(year,index,location = 'data/csv/', i=43, b=62,row1 = 'YEARMONTH', row2 = 'LATITUDE', row3 = 'LONGITUDE',arr_date = [], arr_x = [], arr_y =[] ):
 for file in range(i, b):
     with open(location + str(file) + '.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
       int(str(row[row1][:-2])), row[row2], row[row3]
       if(int(str(row[row1][:-2])) == year):
         int(str(row[row1][:-2]))
         arr_date.append (int((str(row[row1][:-2]))))
         arr_x.append(str(row[row2]))
         arr_y.append(str(row[row3]))

     if(int(str(row[row1][:-2])) > year):
         return arr_date[index], arr_x[index], arr_y[index]
         break