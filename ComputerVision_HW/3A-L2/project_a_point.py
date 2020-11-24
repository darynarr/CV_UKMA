import cv2
import numpy as np

# Project a point from 3D to 2D using a matrix operation

# Given: Point p in 3-space [x y z], and focal length f
# Return: Location of projected point on 2D image plane [u v]


def project_point(p, f):
    p = p[0]
    u = -f * (p[0] / p[2])
    v = -f * (p[1] / p[2])
    return np.array([[u, v]])


# Test: Given point and focal length (units: mm)
p = np.array([[200, 100, 120]])
f = 50

print (project_point(p, f))