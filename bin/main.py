import cv2 as cv




# Color
RED = 0, 0, 255

#State loc

loc = {}

# Map img ref
map_img = 'data/map.jpg'

read = cv.imread(map_img)

# loc of mark
y = int(input("Y: "))
x = int(input("X: "))

loc = y, x
# Y - fist var; X - second var;
read = cv.circle(read, loc, 10, RED, -1)


screen = cv.imshow("ss", read)
cv.waitKey(0)
cv.destroyAllWindows()

