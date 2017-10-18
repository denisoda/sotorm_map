
import cv2 as cv
import json
import csv
import parse


# Color
RED = 0, 0, 255

# json_loc
json_loc = "data/json/loc.json"

# location reading from json


def csv_parse_row(location = 'data/csv/', i=43, b=62,row1 = 'YEARMONTH', row2 = 'LATITUDE', row3 = 'LONGITUDE'):
 for file in range(i, b):
  with open(location + str(file) + '.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      return (int(str(row[row1][:-2])), row[row2], row[row3])



def location(Name_of_state):
   f = open(json_loc)
   s = f.read()
   location = json.loads(s, parse_int=1)
   return int(location[Name_of_state]['x']), int(location[Name_of_state]['y'])


##def convert_loc(x, y):
   ## return float(x) * 19.3, float(y) * -0.1469

##print(convert_loc(36.332, -967))

#def loc_by_year(year,loop):
# print(parse.csv_parse_row(year)[0][loop], parse.csv_parse_row(year)[1][loop], parse.csv_parse_row(year)[2][loop])





#for i in range(3):
 #print(parse.csv_parse_row(1999)[1][i], parse.csv_parse_row(1996)[2][i])

#file = open("json.js", "w")

#for i in range(10):
# file.write('{"x":'+'"'+str(parse.csv_parse_row(1998)[1][i])+'","y'+'":"'+str(parse.csv_parse_row(1998)[2][i])+'"}')

arr=[]

for i in range(50):
 arr.append(({i:(parse.csv_parse_row(1999)[1][i],parse.csv_parse_row(1999)[2][i])}))

with open('json.js', 'w') as f:
    f.write(json.dumps(arr))
# Map img ref
#map_img = 'data/map.jpg'



# loc of mark
x = 701
y = 660

loc = x, y

# Y - fist var; X - second var;
#parse.csv_parse()

#encode = json._default_encoder

#img = cv.imread(map_img)



#circle = cv.circle(img, loc, 13, RED, -1)

# Create a black image, a window and bind the function to window




#while 1:

#cv.imshow("Storm visualisation", circle)
#if cv.waitKey(0) & 0xFF == 27:
 #cv.destroyAllWindows()





