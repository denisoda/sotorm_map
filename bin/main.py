import parse
import cv2 as cv
import json



# Color
RED = 0, 0, 255

# json_loc
json_loc = "data/json/loc.json"

# location reading from json

def location(Name_of_state):
   f = open(json_loc)
   s = f.read()
   location = json.loads(s, parse_int=1)
   return int(location[Name_of_state]['x']), int(location[Name_of_state]['y'])




# Map img ref
map_img = 'data/map.jpg'

read = cv.imread(map_img)

# loc of mark
#y = int(input("Y: "))
#x = int(input("X: "))

#loc = y, x
# Y - fist var; X - second var;
#parse.csv_parse()
read = cv.circle(read, location('Idaho'), 10, RED, -1)


screen = cv.imshow("Storm Map ", read)
cv.waitKey(0)
cv.destroyAllWindows()

