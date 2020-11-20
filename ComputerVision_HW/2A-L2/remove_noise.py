import cv2
import numpy as np

# Apply a Gaussian filter to remove noise
img = cv2.imread('images/saturn.png', cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imshow('Image', img)

# TODO: Add noise to the image
sigma_noise = 2.5
noised_img = img + sigma_noise * np.random.randn(*img.shape)
noised_img = noised_img.astype(np.uint8)
cv2.imshow('Noised image', noised_img)

# TODO: Now apply a Gaussian filter to smooth out the noise
kernel_size, sigma_smooth = 5, 2.5
gauss = cv2.getGaussianKernel(ksize=kernel_size, sigma=sigma_smooth)
gauss_filter = gauss @ gauss.T

smooth_img = cv2.filter2D(noised_img, -1, gauss_filter)
cv2.imshow('Smoothed image', smooth_img)

cv2.waitKey(0)
