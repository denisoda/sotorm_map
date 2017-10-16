
import cv2 as cv
import json
import numpy
import csv


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


def convert_loc(x, y):
    x * 25.4
    y * 1.9255
    return x, y


# Map img ref
map_img = 'data/map.jpg'

read = cv.imread(map_img)

# loc of mark
#y = int(input("Y: "))
#x = int(input("X: "))

#loc = y, x
# Y - fist var; X - second var;
#parse.csv_parse()
img = map_img
encode = json._default_encoder





# Create a black image, a window and bind the function to window

cv.namedWindow('image')


while(1):
    cv.imshow('image', read)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()





