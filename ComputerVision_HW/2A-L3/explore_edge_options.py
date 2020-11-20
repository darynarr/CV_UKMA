import cv2

# Explore edge options

# Load an image
img = cv2.imread('images/fall-leaves.png')
cv2.imshow('Image', img)


# TODO: Create a Gaussian filter. Use cv2.getGaussianKernel.


def get_gauss_2d(kernel_size, sigma):
    gauss = cv2.getGaussianKernel(ksize=kernel_size, sigma=sigma)
    return gauss @ gauss.T


gauss_filter = get_gauss_2d(5, 2.5)


# TODO: Apply it, specifying an edge parameter (try different parameters). Use cv2.filter2D.
def filter2d_edge(image, pad, kernel, border_type):
    new_img = cv2.copyMakeBorder(image, pad, pad, pad, pad, border_type)
    new_img = cv2.filter2D(new_img, -1, kernel)
    return new_img[pad:-pad, pad:-pad]


border_reflect_img = filter2d_edge(img, 50, gauss_filter, cv2.BORDER_REFLECT)
border_wrap_img = filter2d_edge(img, 50, gauss_filter, cv2.BORDER_WRAP)

cv2.imshow('Reflect border', border_reflect_img)
cv2.imshow('Wrap border', border_wrap_img)
cv2.waitKey(0)
