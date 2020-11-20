import cv2
import numpy as np


# For Your Eyes Only
frizzy = cv2.imread('images/frizzy.png')
froomer = cv2.imread('images/froomer.png')
cv2.imshow('Frizzy', frizzy)
cv2.imshow('Froomer', froomer)


# TODO: Find edges in frizzy and froomer images
frizzy_edge = cv2.Canny(frizzy, 0, 500)
froomer_edge = cv2.Canny(froomer, 0, 500)
cv2.imshow('Frizzy Edge', frizzy_edge)
cv2.imshow('Froomer Edge', froomer_edge)



# TODO: Display common edge pixels
cv2.imshow('Common', np.uint8(frizzy_edge & froomer_edge))
cv2.waitKey(0)
