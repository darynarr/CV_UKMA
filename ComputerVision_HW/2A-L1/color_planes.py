import cv2
import numpy as np

# Color planes

img = cv2.imread('images/fruit.png')
cv2.imshow("Fruit image", img)

print(img.shape)

# TODO: Select a color plane, display it, inspect values from a row
b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]

cv2.imshow("Blue plane", b)
cv2.imshow("Green plane", g)
cv2.imshow("Red plane", r)

color = (0, 255, 0) 
row = 45
image_plane = cv2.line(np.array(b), (0, row), (img.shape[1], row), color, thickness=2)
print(b[:, 45])
cv2.imshow(f'Blue plane, the {row}th row', image_plane)
cv2.waitKey(0)
