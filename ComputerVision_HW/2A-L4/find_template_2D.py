import cv2
import numpy as np
import scipy.signal as sp


# Find template 2D
def find_template_2D(template, img):
    # TODO: Find template in img and return [y x] location. Make sure this location is the top-left corner of the match.
    # Use scipy.signal.correlate2d
    pass

tablet = cv2.imread('images/tablet.png', 0)
cv2.imshow('Tablet', tablet)

glyph = tablet[74:165, 149:184]
cv2.imshow('Glyph', glyph)

tablet_2 = 1. * tablet - np.mean(tablet)
glyph_2 = 1. * glyph - np.mean(glyph)

y, x = find_template_2D(glyph_2, tablet_2)
print("Y: {}, X: {}".format(y, x))

