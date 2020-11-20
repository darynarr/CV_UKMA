import cv2
import numpy as np
import scipy.signal as sp


# Find template 2D
def find_template_2D(template, img):
    # TODO: Find template in img and return [y x] location. Make sure this location is the top-left corner of the match.
    corr = sp.correlate2d(img, template)
    y, x = np.unravel_index(np.argmax(corr), corr.shape)
    y += -template.shape[0]+1
    x += -template.shape[1]+1
    return y, x


tablet = cv2.imread('images/tablet.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Tablet', tablet)

glyph = tablet[74:165, 149:184]
cv2.imshow('Glyph', glyph)

tablet_2 = 1. * tablet - np.mean(tablet)
glyph_2 = 1. * glyph - np.mean(glyph)

y, x = find_template_2D(glyph_2, tablet_2)
print("Y: {}, X: {}".format(y, x))

tablet = cv2.cvtColor(tablet, code=cv2.COLOR_GRAY2BGR)
cv2.rectangle(tablet, (x, y), (x+glyph.shape[1], y+glyph.shape[0]),
              (0, 0, 255), thickness=2)
cv2.imshow('Rectangle', tablet)
cv2.waitKey(0)
