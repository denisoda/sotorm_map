import parse
import cv2 as cv
import json
import numpy



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
img = map_img
encode = json._default_encoder


def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(read,(x,y),10,RED,-1)
        f = open("json.json", "w")
        f.write("{"+'"'+input("Name of the state : ")+'"'+":" +"{"+ '"x"'+":" +'"' + str(x) + '"' + "," +'"'+ "y" + '":' + '"' + str(y) + '"},')
        print("X: " + str(x) + " Y: " + str(y))


# Create a black image, a window and bind the function to window

cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', read)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()





